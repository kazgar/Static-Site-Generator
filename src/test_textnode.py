import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a node", "bold", "url")
        node2 = TextNode("This is also a node", "bold", "url")
        self.assertNotEqual(node, node2)

    def test_different_text_types(self):
        node = TextNode("This is a node", "bold", "url")
        node2 = TextNode("This is a node", "italic", "url")
        self.assertNotEqual(node, node2)

    def test_different_urls(self):
        node = TextNode("This is a node", "bold", "url")
        node2 = TextNode("This is a node", "bold", "different-url")
        self.assertNotEqual(node, node2)
        
    def test_same_urls(self):
        node = TextNode("This is a node", "bold", None)
        node2 = TextNode("This is a node", "bold")
        self.assertEqual(node, node2)
        

    

if __name__ == "__main__":
    unittest.main()