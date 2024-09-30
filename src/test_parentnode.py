import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("tag", [LeafNode("leaf_tag", "leaf_text")], "props")
        node2 = ParentNode("tag", [LeafNode("leaf_tag", "leaf_text")], "props")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = ParentNode("tag", [LeafNode("leaf_tag", "leaf_text")], "props")
        repr_string = node.__repr__()
        if repr_string == "ParentNode(tag, [LeafNode(leaf_tag, leaf_text, None)], props)":
            return True
        raise Exception("repr not working as intended")
    
    def test_to_html(self):
        node = ParentNode("tag", [LeafNode(tag="leaf_tag", value="leaf_value")], "props")
        to_html = node.to_html()
        if to_html == "<tag><leaf_tag>leaf_value</leaf_tag></tag>":
            return True
        raise Exception("to_html not working as intended")
    
    def test_skip_tag(self):
        try:
            node = ParentNode(children="children", props=None)
        except:
            return True
        raise Exception("\n!!!\nParentNode has been created without tag parameter\n!!!\n")
        
    def test_different(self):
        node = ParentNode("tag", "children1", props=None)
        node2 = ParentNode("tag", children="children1")
        self.assertEqual(node, node2)

    def test_skip_children(self):
        try:
            node = ParentNode("tag")
        except:
            return True
        raise Exception("\n!!!\nParentNode has been created without children parameter\n!!!\n")
    
    def test_nested_parent_nodes(self):
        try:
            node = ParentNode("tag", children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
                ], props=None)
            node2 = ParentNode("tag_parent", children=node, props=None)
        except:
            raise Exception("Something wrong with nesting ParentNodes")
        return True