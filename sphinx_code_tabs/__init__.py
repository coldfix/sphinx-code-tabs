__version__ = '0.4.0'

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


class Tabs(SphinxDirective):

    """
    This directive is used to contain a group of code blocks which can be
    selected as tabs of a single notebook.
    """

    final_argument_whitespace = True
    required_arguments = 0
    optional_arguments = 1
    has_content = True

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)
        node = TabGroup(text)
        node["classes"].append("tabs")
        node["tabgroup"] = self.arguments[0] if self.arguments else None
        if self.env.app.builder.name in _compatible_builders:
            tabbar = TabBar()
            tabbar["classes"].append("tabbar")
            node.append(tabbar)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        selected = node.get("selected", 0)
        if self.env.app.builder.name in _compatible_builders:
            tabbar.children[selected]['classes'].append('selected')
            node.children[1 + selected]['classes'].append('selected')
        else:
            node.children[selected]['classes'].append('selected')

        return [node]


class Tab(SphinxDirective):

    option_spec = {
        'selected': directives.flag,
    }

    final_argument_whitespace = True
    required_arguments = 1
    optional_arguments = 0
    has_content = True

    def run(self):
        is_supported = self.env.app.builder.name in _compatible_builders
        title = self.options.get('title')
        index = len(self.state.parent.children) - is_supported
        if 'selected' in self.options:
            self.state.parent['selected'] = index
        if not title:
            title = self.options.pop('caption', None)
        if not title and self.arguments:
            title = self.arguments[0]
        if not title:
            title = "Tab {}".format(index + 1)
        if is_supported:
            # generate navbar button:
            tabbutton = TabButton()
            tabbutton['index'] = index
            tabbutton['classes'].append("tabbutton")
            tabbutton.append(nodes.Text(title))
            tabbar = self.state.parent.children[0]
            tabbar.append(tabbutton)
            # generate page:
            outer = TabNode()
            outer['index'] = index
            outer['classes'].append('tab')
        else:
            self.options.setdefault('caption', title)
            outer = nodes.container()

        self.make_page(outer)
        return [outer]

    def make_page(self, node):
        page = nodes.container("\n".join(self.content))
        page['classes'].append("nocode")
        node.append(page)
        self.state.nested_parse(self.content, self.content_offset, page)


class CodeTab(CodeBlock):

    """Single code-block tab inside .. code-tabs."""

    option_spec = CodeBlock.option_spec.copy()
    option_spec.update({
        'title': directives.unchanged,
        'selected': directives.flag,
    })

    run = Tab.run

    def make_page(self, node):
        node += super().run()


class TabGroup(nodes.container):
    pass


class TabBar(nodes.Part, nodes.Element):
    pass


class TabButton(nodes.Part, nodes.Element):
    pass


class TabNode(nodes.Part, nodes.Element):
    pass


def visit_tabgroup_html(self, node):
    self.body.append(self.starttag(node, 'div', **{
        'data-tabgroup': node.attributes['tabgroup'] or '',
        'class': 'docutils container',
    }))


def depart_tabgroup_html(self, node):
    self.body.append('</div>')


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
    app.add_node(TabGroup, html=(visit_tabgroup_html, depart_tabgroup_html))
    app.add_node(TabBar, html=(visit_tabbar_html, depart_tabbar_html))
    app.add_node(TabButton, html=(visit_tabbutton_html, depart_tabbutton_html))
    app.add_node(TabNode, html=(visit_tab_html, depart_tab_html))
    app.add_directive("tabs", Tabs)
    app.add_directive("tab", Tab)
    app.add_directive("code-tabs", Tabs)
    app.add_directive("code-tab", CodeTab)
    app.connect("builder-inited", add_assets)
