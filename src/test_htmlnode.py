import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", "children")
        node2 = HTMLNode("tag", "value", "children")
        self.assertEqual(node, node2)

    def test_different_tag(self):
        node = HTMLNode("tag", "value", "children", {"key": "value"})
        node2 = HTMLNode("different tag", "value", "children", {"key": "value"})
        self.assertNotEqual(node, node2)

    def test_different_value(self):
        node = HTMLNode("tag", "value", "children", {"key": "value"})
        node2 = HTMLNode("tag", "different value", "children", {"key": "value"})
        self.assertNotEqual(node, node2)
    
    def test_different_children(self):
        node = HTMLNode("tag", "value", "children", {"key": "value"})
        node2 = HTMLNode("tag", "value", "different children", {"key": "value"})
        self.assertNotEqual(node, node2)

    def test_different_props(self):
        node = HTMLNode("tag", "value", "children", {"key": "value"})
        node2 = HTMLNode("tag", "value", "children", {"different_key": "different_value"})
        self.assertNotEqual(node, node2)

    def test_eq_all_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()