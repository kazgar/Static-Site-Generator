import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("this is value", "<h1>", {"href": "https://www.google.com"})
        node2 = LeafNode("this is value", "<h1>", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_repr(self):
        node = LeafNode("value", "h", {"href": "https://www.google.com"})
        if node.__repr__() != f"LeafNode({node.value}, {node.tag}, {node.props})":
            raise Exception("__repr__ not working properly")

    def test_to_html(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        if node.to_html() != "<a href=\"https://www.google.com\">Click me!</a>":
            raise Exception("to_html not working properly")
        
    def test_skip_value(self):
        node = LeafNode(value=None, tag="tag", props=None)
        if not node:
            raise Exception("value argument has been skipped")
    
    def test_different_tags(self):
        node = LeafNode("value", None)
        node2 = LeafNode("value", props=None)
        self.assertEqual(node, node2)


