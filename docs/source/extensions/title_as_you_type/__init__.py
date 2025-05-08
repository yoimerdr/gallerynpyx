"""
Package edited from https://github.com/rmcgibbo/sphinxcontrib-lunrsearch

It was edited to allow the search of titles present in the sphinx documentation,
but without disabling the default search.
"""
import argparse
import os
from os.path import dirname, join, exists
import json

import six
import sphinx.search
from sphinx.application import Sphinx
from sphinx.util.console import colorize
from sphinx.util.osutil import copyfile
from sphinx.util import logging
from sphinx.jinja2glue import SphinxFileSystemLoader

logger = logging.getLogger(__name__)

stored = []

cfg = argparse.Namespace(
    title_mode=None,
    max_results=7,
    relative_url=None,
    tokenizer_separator=None,
    navigation_mode=None,
    exclue_titles=False,
    with_wildcard=True,
    loaded=False
)


def info(msg):
    logger.info('{} {}'.format(
        colorize('bold', '[TitleAsYouType]'),
        msg
    ))

class IndexBuilder(sphinx.search.IndexBuilder):
    def freeze(self):
        """Create a usable data structure for serializing."""
        data = super(IndexBuilder, self).freeze()
        try:
            names = data['docnames']
        except KeyError:
            names = data['filenames']

        if not cfg.exclude_titles:
            for (title, content) in data['alltitles'].items():
                for (index, path) in content:
                    if not path:
                        continue
                    stored.append({
                        "anchor": path,
                        "root": names[index],
                        'title': title,
                    })

        for prefix, items in six.iteritems(data['objects']):
            for item in items:
                index, type_index, _, _, prop = item
                title = "{}.{}".format(prefix, prop)

                source = {
                    'title': title,
                    'root': names[index],
                    'anchor': title,
                }

                if cfg.title_mode != "full":
                    if cfg.title_mode == "parent":
                        prop = "{}.{}".format(prefix.split(".")[-1], prop)

                    source['label'] = prop

                stored.append(source)

        cfg.loaded = True

        return data


def builder_inited(app):
    # adding a new loader to the template system puts our searchbox.html
    # template in front of the others, it overrides whatever searchbox.html
    # the current theme is using.
    # it's still up to the theme to actually _use_ a file called searchbox.html
    # somewhere in its layout. but the base theme and pretty much everything
    # else that inherits from it uses this filename.
    app.builder.templates.loaders.insert(0, SphinxFileSystemLoader(dirname(__file__)))
    # adds the variable to the context used when rendering the searchbox.html
    # app.config.html_context.update({ })

def copy_static_files(app, _):
    # because we're using the extension system instead of the theme system,
    # it's our responsibility to copy over static files outselves.
    if not cfg.loaded:
        info('The index has not been loaded. Deletes the results docs or try other folder for sphinx out.')
        return

    info('Copying static files.')

    files = ['js/lunr-searchbox.js', 'css/lunr-searchbox.css']
    for f in files:
        src = join(dirname(__file__), f)
        dest = join(app.outdir, '_static', f)
        if not exists(dirname(dest)):
            os.makedirs(dirname(dest))
        copyfile(src, dest, force=True)

    if not stored:
        info('No search data found. Nothing to do. Checks your indexes or '
             'deletes the results docs or try other folder for sphinx out.')
        return

    info('Copying search data.')
    with open(join(app.outdir, "_static", "js", "lunr-search-data.js"), "w", encoding="utf-8") as fs:
        data = {
            "data": stored,
            "maxResults": cfg.max_results,
            "relativeUrl": cfg.relative_url,
            "tokenizerSeparator": cfg.tokenizer_separator,
            "navigationMode": cfg.navigation_mode,
            "withWildcard": cfg.with_wildcard,
        }

        fs.write("var LunrDataSearch = {}".format(json.dumps(data)))

    info('All done.')

def init_config(app: Sphinx):
    title_mode = app.config.tyasutype_title_mode
    if title_mode not in ('parent', 'full', 'short'):
        title_mode = 'full'

    navigation_mode = app.config.tyasutype_navigation_mode

    if navigation_mode not in ('simple', 'infinite'):
        navigation_mode = 'simple'

    relative_url = app.config.tyasutype_relative_url

    if relative_url and relative_url[0] != '/':
        relative_url = '/' + relative_url
    if relative_url[-1] != '/':
        relative_url += '/'

    cfg.relative_url = relative_url
    cfg.title_mode = title_mode
    cfg.max_results = int(app.config.tyasutype_max_results)
    cfg.tokenizer_separator = str(app.config.tyasutype_tokenizer_separator)
    cfg.navigation_mode = navigation_mode
    cfg.exclude_titles = bool(app.config.tyasutype_exclude_titles)
    cfg.with_wildcard = bool(app.config.tyasutype_with_wildcard)


def setup(app: Sphinx):
    # adds <script> and <link> to each of the generated pages to load these
    # files.
    app.add_js_file('https://unpkg.com/lunr/lunr.min.js')
    app.add_css_file('css/lunr-searchbox.css')
    app.add_js_file('js/lunr-searchbox.js')
    app.add_js_file('js/lunr-search-data.js')

    app.connect('builder-inited', builder_inited)
    app.connect('build-finished', copy_static_files)

    app.add_config_value('tyasutype_relative_url', None, 'env')
    app.add_config_value('tyasutype_exclude_titles', False, 'env')
    app.add_config_value('tyasutype_with_wildcard', True, 'env')
    app.add_config_value('tyasutype_max_results', 7, 'env')
    app.add_config_value('tyasutype_title_mode', 'full', 'env')
    app.add_config_value('tyasutype_navigation_mode', 'simple', 'env')
    app.add_config_value('tyasutype_tokenizer_separator', r'[\s.\-]+', 'env')
    init_config(app)
    sphinx.search.IndexBuilder = IndexBuilder
