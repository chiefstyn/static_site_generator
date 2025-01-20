import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        props = {"href": "https://boot.dev", "target": "_blank"}
        node = HTMLNode(props=props)
        html_props = node.props_to_html()
        self.assertEqual(html_props, ' href="https://boot.dev" target="_blank"')


    def test_node_with_children(self):
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        parent = HTMLNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.children, [child1, child2])

if __name__ == "__main__":
    unittest.main()