from autoapi.documenters import AutoapiClassDocumenter
from docutils.statemachine import StringList
from sphinx.ext import autodoc
from sphinx.ext.autodoc import bool_option

class ClassDocumenter(AutoapiClassDocumenter):
    priority = AutoapiClassDocumenter.priority + 100
    option_spec = AutoapiClassDocumenter.option_spec.copy()
    option_spec["autoapi-inheritance-simple"] = bool_option

    def add_directive_header(self, sig):
        if self.options.autoapi_inheritance_simple:
            autodoc.Documenter.add_directive_header(self, sig)
            if self.options.show_inheritance:
                sourcename = self.get_sourcename()
                self.add_line("", sourcename)

                if self.object.bases:
                    bases = ", ".join(":class:`~{}`".format(base) for base in self.object.bases)
                    self.add_line(f"   Bases: {bases}", sourcename)
        else:
            super(ClassDocumenter, self).add_directive_header(sig)

    def generate(
        self,
        more_content: StringList | None = None,
        real_modname: str | None = None,
        check_module: bool = False,
        all_members: bool = False,
    ) -> None:
        super().generate(more_content, real_modname, check_module, all_members)
        # print("\n".join(self.directive.result))

def setup(app):
    """
    :type app: sphinx.application.Sphinx
    """
    app.add_autodocumenter(ClassDocumenter, override=True)
