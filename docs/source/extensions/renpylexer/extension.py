# @PydevCodeAnalysisIgnore
from __future__ import print_function

import sys

from sphinx.directives.code import CodeBlock
from sphinx.roles import code_role
from pygments.lexers.agile import PythonLexer
from pygments.token import Token, Name, Operator
import re
import sphinx.addnodes
import docutils.nodes
import sphinx.domains

from . import keywords

KEYWORDS = set(keywords.keywords)
PROPERTIES = set(keywords.properties)

DECLARATIONS_CLASS_LIKE = {
    "image", "screen", "init python in", "class", "style"
}

PUNCTUATION_END_DECLARATION = ("(", ":")
PUNCTUATION_METHOD = (".",)
OPERATORS = ("=",",", "(",)

BUILTIN_FUNCTIONS = set(keywords.functions)

ROLE_OPTIONS = {
    'language': 'renpy'
}


class RenPyLexer(PythonLexer):
    name = "Ren'Py"
    aliases = ["renpy", "rpy"]
    filenames = ["*.rpy", "*.rpym"]

    def get_tokens_unprocessed(self, text):
        statement = ""
        class_like = False
        tokens = tuple(PythonLexer.get_tokens_unprocessed(self, text))
        for i, (index, token, value) in enumerate(tokens):
            if value.startswith("###"):
                continue

            statement += value
            nxt = tokens[i + 1] if i + 1 < len(tokens) else None
            prev = tokens[i - 1] if i - 1 >= 0 else None

            if value == 'gallerynpyx' and nxt and nxt[2] == ".":
                yield index, Name.Attribute, value
                continue

            if token == Token.Error and value == "$":
                yield index, Token.Keyword, value

            elif token in [Name, Operator.Word] and value in KEYWORDS:
                if class_like:
                    yield index, Name.Class, value
                elif nxt and nxt[2] in OPERATORS:
                    tkn = Token.Word
                    if prev and prev[2] == ".":
                        tkn = Name.Function
                    yield index, tkn, value
                else:
                    class_like = statement in DECLARATIONS_CLASS_LIKE

                    yield index, Token.Keyword, value

            elif token in Name and value in PROPERTIES:
                yield index, Name.Attribute, value
            elif class_like:
                if token == Operator or (token == Token.Punctuation and value in PUNCTUATION_END_DECLARATION):
                    class_like = False
                    yield index, token, value
                else:
                    yield index, Name.Class, value
            elif statement.startswith(PUNCTUATION_METHOD) and token == Name and nxt:
                tkn = Token.Word
                if nxt[2] == "(":
                    tkn = Name.Function
                yield index, tkn, value
            elif token in Name and value in BUILTIN_FUNCTIONS and nxt and nxt[2] == "(":
                yield index, Name.Function, value
            else:
                if not token == Token.Text:
                    statement = "" if value not in PUNCTUATION_METHOD else value

                class_like = False
                yield index, token, value


class RenpyDirective(CodeBlock):
    option_spec = CodeBlock.option_spec.copy()

    def __init__(self, name, arguments, options, content, lineno,
                 content_offset, block_text, state, state_machine):
        super(RenpyDirective, self).__init__(name, ['renpy'], options, content, lineno,
                 content_offset, block_text, state, state_machine)


def parse_var_node(env, sig, signode):
    m = re.match(r'(\S+)(.*)', sig)

    if m.group(1).split('.')[0] in ["config", "gui"]:
        signode += docutils.nodes.Text("define ", "define")

    signode += sphinx.addnodes.desc_name(m.group(1), m.group(1))
    signode += docutils.nodes.Text(m.group(2))

    ref = m.group(1)
    return ref


style_seen_ids = set()


def parse_style_node(env, sig, signode):
    m = re.match(r'(\S+)(.*)', sig)

    name = m.group(1)
    desc = m.group(2)
    desc = " - " + desc

    signode += sphinx.addnodes.desc_name(name, name)
    signode += docutils.nodes.Text(desc, desc)

    ref = m.group(1)

    while ref in style_seen_ids:
        print("duplicate id:", ref)
        ref = ref + "_alt"

    style_seen_ids.add(ref)

    return ref


scpref_seen_ids = set()


def parse_scpref_node(env, sig, signode):
    m = re.match(r'(\S+)(.*)', sig)

    signode += sphinx.addnodes.desc_name(m.group(1), m.group(1))
    signode += docutils.nodes.Text(m.group(2), m.group(2))

    ref = m.group(1)

    while ref in scpref_seen_ids:
        print("duplicate id:", ref)
        ref = ref + "_alt"

    scpref_seen_ids.add(ref)

    return ref


def renpy_role(role, rawtext, text, lineno, inliner, options=None, content=()):
    return code_role(role, rawtext, text, lineno, inliner, ROLE_OPTIONS, content)


def setup(app):
    if sys.version_info[0] == 2:
        app.add_lexer("renpy", RenPyLexer())
    else:
        app.add_lexer('renpy', RenPyLexer)

    app.add_object_type("var", "var", "single: %s (variable)", parse_node=parse_var_node)
    app.add_object_type("style-property", "propref", "single: %s (style property)", parse_node=parse_style_node)
    app.add_object_type("transform-property", "tpref", "single: %s (transform property)")
    app.add_object_type("screen-property", "scpref", "single: %s (screen property)", parse_node=parse_scpref_node)
    app.add_object_type("text-tag", "tt", "single: %s (text tag)")
    app.add_role('renpy', renpy_role)
    app.add_directive('renpy', RenpyDirective)
