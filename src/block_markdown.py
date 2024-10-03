from htmlnode import HTMLNode
from inline_markdown import *

text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

block_types_to_html_tags = {
    "paragraph": "p",
    "heading": "h",
    "unordered_list": "ul",
    "ordered_list": "ol",
    "quote": "blockquote",
    "code": ["pre", "code"]
}


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    list_of_nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if not block_type == "code":
            children = text_to_children(block)
            list_of_nodes.append(HTMLNode(tag=block_types_to_html_tags[block_type], value=None, children=children))
        else:
            child = HTMLNode(tag=block_types_to_html_tags[block_type][1], value=block, children=None)
            list_of_nodes.append(HTMLNode(tag=block_types_to_html_tags[block_type][0], value=None, children=[child]))

    return HTMLNode(tag="div", value=None, children=list_of_nodes)
    
def text_to_children(block):
    nodes = text_to_textnodes(block)
    html_nodes = []
    for node in nodes:
        if node.text_type == text_type_text:
            html_nodes.append(HTMLNode(tag=None, value=node.text))
        if node.text_type == text_type_bold:
            html_nodes.append(HTMLNode(tag="strong", value=node.text))
        if node.text_type == text_type_italic:
            html_nodes.append(HTMLNode(tag="em", value=node.text))
        if node.text_type == text_type_link:
            html_nodes.append(HTMLNode(tag="a", value=node.text, children=None, props={"href": node.url}))
        if node.text_type == text_type_image:
            html_nodes.append(HTMLNode(tag="img", value=None, children=None, props={"src": node.url, "alt": node.text}))
    return html_nodes



def markdown_to_blocks(markdown):
    blocks = list(filter(lambda x: x != "", markdown.split("\n\n")))
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    if block[0:2] == "# " or block[0:3] == "## " or block[0:4] == "### " or block[0:5] == "#### " or block[0:6] == "##### " or block[0:7] == "###### ":
        return "heading"
    
    lines = block.split("\n")

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"   

    if list(filter(lambda x: x[0] == ">", lines)) == lines:
        return "quote"
                
    if list(filter(lambda x: x[0:2] == "* " or x[0:2] == "- ", lines)) == lines:
        return "unordered_list"

    is_ordered_list = True
    for i in range(len(lines)):
        if lines[i][0:3] != f"{i+1}. ": 
            is_ordered_list = False
    if is_ordered_list == True:
        return "ordered_list"
    
    return "paragraph"


