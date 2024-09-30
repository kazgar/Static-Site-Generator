from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, props=props)
        self.children = children

    def to_html(self):
        if self.tag:
            if self.children:
                string_to_return = f"<{self.tag}>"
                for child in self.children:
                    string_to_return += child.to_html()
                string_to_return += f"</{self.tag}>"
                return string_to_return
            raise ValueError("node has no children")
        raise ValueError("tag parameter is required")
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if self.tag == other.tag:
            if self.children == other.children:
                if self.props == other.props:
                    return True 
        return False
        