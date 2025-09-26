import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_one(self):
        node = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_eq_two(self):
        node = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="this is a HTML node2", props={"href": "https://www.google.com", "target": "_blank2"})
        self.assertNotEqual(node, node2)

    def test_eq_three(self):
        testnode = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        testnode2 = HTMLNode(tag="a", value="this is a HTML node2", props={"href": "https://www.google.com", "target": "_blank2"})
        testnode3 = HTMLNode("a", "this is a HTML node3", [testnode, testnode2], {"href": "https://www.google.com", "target": "_blank3"})
        node = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "this is a HTML node", [testnode, testnode3], {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_four(self):
        testnode = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        testnode2 = HTMLNode(tag="a", value="this is a HTML node2", props={"href": "https://www.google.com", "target": "_blank2"})
        props = testnode.props_to_html()
        props2 = testnode2.props_to_html()
        self.assertNotEqual(props, props2)

    def test_eq_five(self):
        testnode = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        testnode2 = HTMLNode(tag="a", value="this is a HTML node2", props={"href": "https://www.google.com", "target": "_blank"})
        props = testnode.props_to_html()
        props2 = testnode2.props_to_html()
        self.assertEqual(props, props2)

    def test_eq_six(self):
        testnode = HTMLNode(tag="p", value="this is a HTML node", props={"href": "https://www.google.com", "target": "_blank"})
        testnode2 = HTMLNode(tag="a", value="this is a HTML node2", props={"href": "https://www.google.com", "target": "_blank2"})
        testnode3 = HTMLNode("a", "this is a HTML node3", [testnode, testnode2], {"href": "https://www.google.com", "target": "_blank3"})
        node = HTMLNode("a", "this is a HTML node3", [testnode, testnode2], {"href": "https://www.google.com", "target": "_blank3"})
        node2 = HTMLNode("a", "this is a HTML node3", [testnode, testnode2], {"href": "https://www.google.com", "target": "_blank3"})
        self.assertEqual(node, node2)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>") 

    def  test_leaf_to_html_i(self): 
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")
    
    def  test_leaf_to_html_a(self): 
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_leaf_plain(self):
        self.assertEqual(LeafNode("p", "Hello").to_html(), "<p>Hello</p>")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Click", {"href": "https://x.com", "target": "_blank"})
        html = node.to_html()
        self.assertTrue(html.startswith('<a '))
        self.assertIn('href="https://x.com"', html)
        self.assertIn('target="_blank"', html)
        self.assertTrue(html.endswith('>Click</a>'))

    def test_leaf_no_tag_raw(self):
        self.assertEqual(LeafNode(None, "Just text").to_html(), "Just text")

if __name__ == "__main__":
    unittest.main()