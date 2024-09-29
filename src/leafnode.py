from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, props=props)
        self.value = value
        
    def to_html(self):
        if self.value:
            if self.tag:
                if self.props != None:
                    props_string = ""
                    for key, value in self.props.items():
                        props_string += f" {key}=\"{value}\""
                    return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
                    
                return f"<{self.tag}>{self.value}</{self.tag}>"

        raise ValueError("LeafNode requires value")
    
    def __repr__(self):
        return f"LeafNode({self.value}, {self.tag}, {self.props})"
    
    def __eq__(self, other):
        if self.value == other.value:
            if self.tag == other.tag:
                if self.props == other.props:
                    return True
        return False
            