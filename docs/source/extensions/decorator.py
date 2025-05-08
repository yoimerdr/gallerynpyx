from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx import addnodes


def arguments_option(arg):
    if arg in {None, True}:
        return ()
    elif arg is False:
        return None
    return [x.strip() for x in arg.split(',') if x.strip()]


def named_arguments_option(arg):
    if arg in {None, True}:
        return ()
    elif arg is False:
        return None
    results = []
    for x in arg.split(','):
        if not x.strip():
            continue
        name, value = x.split('=')
        name, value = name.strip(), value.strip()
        if not name or not value:
            raise ValueError("Invalid named argument: {}".format(x))
        results.append((name, value))
    return results


def get_string_value(arg):
    return arg.strip()[1:-1] if arg.startswith(("'", '"')) else None


def get_number_value(arg):
    try:
        return int(arg)
    except ValueError:
        try:
            return float(arg)
        except ValueError:
            return None


def get_boolean_value(arg):
    arg = arg.lower()
    return True if arg == "true" else False if arg == "false" else None


def get_element(arg):
    """
    :rtype: (nodes.inline, str)
    """
    value = get_boolean_value(arg)
    if value is not None:
        el = nodes.inline(text='', classes=["kc", ])
    else:
        value = get_number_value(arg)
        if value is not None:
            el = nodes.inline(text='', classes=["mf" if '.' in arg else "mi", ])
        else:
            value = get_string_value(arg)
            if value is not None:
                el = nodes.inline(text='', classes=["s1"])
                value = "'{}'".format(value)
            else:
                value = arg.split(".")[-1]
                el = addnodes.pending_xref('', refdomain='py', reftype='obj', reftarget=arg,
                                           modname=None, classname=None)
                el['refexplicit'] = True

    return el, value


class DecoratorRefDirective(Directive):
    has_content = True
    required_arguments = 1
    option_spec = {
        "parameters": arguments_option,
        "named-parameters": named_arguments_option
    }

    def run(self):
        target = self.arguments[0]
        display_name = target.split('.')[-1]

        ref_node = addnodes.pending_xref('', refdomain='py', reftype='obj', reftarget=target, modname=None,
                                         classname=None)
        ref_node['refexplicit'] = True
        ref_node += nodes.inline(text=display_name, classes=["pre"])

        dl = nodes.definition_list(classes=["py", "function", "applied-decorator", ])

        args = self.options.get("parameters", None)
        kwargs = self.options.get("named-parameters", None)
        if args or kwargs:
            dl["classes"].append("callable")

        dt = nodes.term(classes=["sig", "sig-object", "py", "notranslate", ])

        prename = nodes.inline(classes=["sig-prename", "descclassname"])
        prename += nodes.inline(text='@', classes=["pre"])
        name = nodes.inline('', '', classes=["sig-name", "descname"])
        name += nodes.inline('', '', ref_node, classes=["pre"])

        dt += prename
        dt += name

        if args or kwargs:
            dt += nodes.inline(text='(', classes=["sig-paren", ])
            em = nodes.emphasis(classes=["sig-param"])
            for arg in args or ():
                el, value = get_element(arg)

                if el and value:
                    el += nodes.inline(text=value, classes=["pre"])
                    em += el
                    em += nodes.Text(", ")
            for (name, arg) in kwargs or ():
                el, value = get_element(arg)
                if el and value is not None:
                    em += nodes.inline('', '', nodes.inline(text=name, classes=["pre"]), classes=['pn'])
                    em += nodes.inline('', '', nodes.inline(text="=", classes=["pre"]), classes=['o'])
                    el += nodes.inline(text=value, classes=["pre"])
                    em += el
                    em += nodes.Text(", ")
            dt += em
            dt += nodes.inline(text=")", classes=["sig-paren"])

        dd = nodes.definition()
        self.state.nested_parse(self.content, self.content_offset, dd)

        dl_item = nodes.definition_list_item('', dt, dd)
        dl += dl_item
        return [dl]


def setup(app):
    app.add_directive("applied-decorator", DecoratorRefDirective)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
