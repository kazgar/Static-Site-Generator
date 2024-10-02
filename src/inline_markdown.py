from textnode import TextNode
from leafnode import LeafNode
import re 

text_type_text="text"
text_type_bold="bold"
text_type_italic="italic"
text_type_code="code"
text_type_link="link"
text_type_image="image"

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


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
    return

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
