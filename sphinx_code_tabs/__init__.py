__version__ = '0.1.0'

from docutils.parsers.rst import directives, Directive
from docutils import nodes
from sphinx.directives.code import CodeBlock

import os


CSS_FILE = "code-tabs.css"
JS_FILE = "code-tabs.js"


class CodeTabs(Directive):

    """
    This directive is used to contain a group of code blocks which can be
    selected as tabs of a single notebook.
    """

    has_content = True

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)
        node = nodes.container(text)
        node["classes"].append("code-tabs")
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class CodeTab(CodeBlock):

    """Single code-block tab inside .. code-tabs."""

    option_spec = dict(
        CodeBlock.option_spec,
        title=directives.unchanged_required)

    def run(self):
        outer = Tab()
        outer['title'] = self.options.get('title')
        outer['classes'] += ['code-tab']
        outer += super().run()
        return [outer]


class Tab(nodes.Part, nodes.Element):
    pass


def visit_tab_html(self, node):
    self.body.append(self.starttag(node, 'div', **{
        'data-title': node.attributes['title'],
    }))


def depart_tab_html(self, node):
    self.body.append('</div>')


def add_assets(app):
    app.config.html_static_path.append(os.path.dirname(__file__))
    app.add_css_file(CSS_FILE)
    app.add_js_file(JS_FILE)


def setup(app):
    app.add_node(Tab, html=(visit_tab_html, depart_tab_html))
    app.add_directive("code-tabs", CodeTabs)
    app.add_directive("code-tab", CodeTab)
    app.connect("builder-inited", add_assets)
