from htmlnode import *
from markdown_blocks import *
from textnode import *
from split_nodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parents = []
    for block in blocks:
        parents.append(create_html_block(block))
    return ParentNode("div", parents)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No header 1 in markdown document")


def heading_tag(textblock):
    if textblock.startswith("# "):
        return "h1", 2
    if textblock.startswith( "## "):
        return "h2", 3
    if textblock.startswith("### "):
        return "h3", 4
    if textblock.startswith("#### "):
        return "h4", 5
    if textblock.startswith("##### "):
        return "h5", 6
    return "h6", 7


def create_html_block(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.CODE:
        block = block[3:-3]
        if block.startswith("\n"):
            block = block[1:]
        children = [text_node_to_html_node(TextNode(block, TextType.TEXT))]
        return ParentNode("pre", [ParentNode("code", children)])
    if block_type == BlockType.HEADING:
        tag, length = heading_tag(block)
        children = text_to_children(block[length:].strip())
        return ParentNode(tag, children)
    lines = block.split("\n")
    if block_type == BlockType.PARAGRAPH:
        children = text_to_children(" ".join(lines).strip())
        return ParentNode("p", children)
    new_lines = []
    if block_type == BlockType.QUOTE:
        for line in lines:
            new_lines.append(line[1:].strip())
        children = text_to_children("\n".join(new_lines))    
        return ParentNode("blockquote", children)
    if block_type == BlockType.UNORDERED_LIST:
        for line in lines:
            new_lines.append(ParentNode("li", text_to_children(line[2:].strip())))
        return ParentNode("ul", new_lines)
    if block_type == BlockType.ORDERED_LIST:
        for line in lines:
            new_lines.append(ParentNode("li", text_to_children(line[line.find(".") + 2:].strip())))
        return ParentNode("ol", new_lines)
    raise ValueError("Invalid Block Type")


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children
    
    