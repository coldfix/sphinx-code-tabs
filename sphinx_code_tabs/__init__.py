__version__ = '0.3.0'

from docutils.parsers.rst import directives
from docutils import nodes
from sphinx.directives.code import CodeBlock
from sphinx.util.docutils import SphinxDirective

import os


CSS_FILE = "code-tabs.css"
JS_FILE = "code-tabs.js"

_compatible_builders = [
    "html",
    "singlehtml",
    "dirhtml",
    "readthedocs",
    "readthedocsdirhtml",
    "readthedocssinglehtml",
    "readthedocssinglehtmllocalmedia",
    "spelling",
]


class CodeTabs(SphinxDirective):

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
        if self.env.app.builder.name in _compatible_builders:
            tabbar = TabBar()
            tabbar["classes"].append("tabbar")
            node.append(tabbar)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class CodeTab(CodeBlock):

    """Single code-block tab inside .. code-tabs."""

    option_spec = dict(
        CodeBlock.option_spec,
        title=directives.unchanged_required)

    def run(self):
        is_supported = self.env.app.builder.name in _compatible_builders
        title = self.options.get('title')
        index = len(self.state.parent.children) - is_supported
        selected = index == 0
        if not title and self.arguments:
            title = self.arguments[0]
        if not title:
            title = "Tab {}".format(index + 1)
        if is_supported:
            # generate navbar button:
            tabbutton = TabButton()
            tabbutton['index'] = index
            tabbutton['classes'].append("tabbutton")
            if selected:
                tabbutton['classes'].append('selected')
            tabbutton.append(nodes.Text(title))
            tabbar = self.state.parent.children[0]
            tabbar.append(tabbutton)
            # generate page:
            outer = Tab()
            outer['index'] = index
            outer['classes'].append('code-tab')
            if not selected:
                outer['classes'].append('hidden')
            outer += super().run()
            return [outer]
        else:
            self.options.setdefault('caption', title)
            return super().run()


class TabBar(nodes.Part, nodes.Element):
    pass


class TabButton(nodes.Part, nodes.Element):
    pass


class Tab(nodes.Part, nodes.Element):
    pass


def visit_tabbar_html(self, node):
    self.body.append(self.starttag(node, 'ul'))


def depart_tabbar_html(self, node):
    self.body.append('</ul>')


def visit_tabbutton_html(self, node):
    self.body.append(self.starttag(node, 'li', **{
        'data-id': node.attributes['index'],
        'onclick': "sphinx_code_tabs_onclick(this)",
    }))


def depart_tabbutton_html(self, node):
    self.body.append('</li>')


def visit_tab_html(self, node):
    self.body.append(self.starttag(node, 'div', **{
        'data-id': node.attributes['index'],
    }))


def depart_tab_html(self, node):
    self.body.append('</div>')


def add_assets(app):
    app.config.html_static_path.append(os.path.dirname(__file__))
    app.add_css_file(CSS_FILE)
    app.add_js_file(JS_FILE)


def setup(app):
    app.add_node(TabBar, html=(visit_tabbar_html, depart_tabbar_html))
    app.add_node(TabButton, html=(visit_tabbutton_html, depart_tabbutton_html))
    app.add_node(Tab, html=(visit_tab_html, depart_tab_html))
    app.add_directive("code-tabs", CodeTabs)
    app.add_directive("code-tab", CodeTab)
    app.connect("builder-inited", add_assets)
