from textnode import TextNode
from leafnode import LeafNode

text_type_text="text"
text_type_bold="bold"
text_type_italic="italic"
text_type_code="code"
text_type_link="link"
text_type_image="image"

def main():
    testing_text_to_html_node(should_test=False)
    node = TextNode("normal text /#italic text/# normal text", text_type_text)
    new_nodes = split_nodes_delimiter([node], "/#", text_type_italic)
    print(new_nodes)

    
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            nodes_text = node.text.split(delimiter)
            for i in range(len(nodes_text)):
                if i % 2 == 1:
                    list_of_nodes.append(TextNode(text=nodes_text[i], text_type=text_type))
                else:
                    list_of_nodes.append(TextNode(text=nodes_text[i], text_type=text_type_text))
        else:
            list_of_nodes.append(node)
    return list_of_nodes



def text_node_to_html_node(text_node):
    text_types = [
        "text",
        "bold",
        "italic",
        "code",
        "link",
        "image"
    ]
    
    if text_node.text_type not in text_types:
        raise Exception("unallowed text type")
    
    text_node_text_type = text_node.text_type
    if text_node_text_type == "text":
        return LeafNode(value=text_node.text)
    if text_node_text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    if text_node_text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    if text_node_text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    if text_node_text_type == "link":
        return LeafNode(tag="a", props={"href": text_node.url}, value=text_node.text)
    if text_node_text_type == "image":
        return LeafNode(tag="img", props={"src": text_node.url, "alt": text_node.text}, value="")
    


def testing_text_to_html_node(should_test):
    if should_test:
        text_textnode = TextNode("text_text_node", "text", None)
        print(text_textnode.__repr__())
        text_node_to_leaf = text_node_to_html_node(text_textnode)
        print(text_node_to_leaf.__repr__())

        link_textnode = TextNode("link_text_node", "link", "www.hahah.pl")
        print(link_textnode.__repr__())
        link_node_to_leaf = text_node_to_html_node(link_textnode)
        print(link_node_to_leaf.__repr__())

        image_textnode = TextNode("image_text_node", "image", "www.image.pl")
        print(image_textnode.__repr__())
        image_node_to_leaf = text_node_to_html_node(image_textnode)
        print(image_node_to_leaf.__repr__())
    


if __name__ == "__main__":
    main()