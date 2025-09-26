import re
from textnode import *

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    return text_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            textlist = node.text.split(delimiter)
            if len(textlist) % 2 != 1:
                raise Exception("Invalid Markdown syntax")
            for i in range(len(textlist)):
                if i % 2 == 0 and textlist[i] != "":
                    new_nodes.append(TextNode(textlist[i], TextType.TEXT))
                if i % 2 == 1 and textlist[i] != "":
                    new_nodes.append(TextNode(textlist[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_node(node, text_type):
    new_nodes = []
    if node.text_type != TextType.TEXT:
        return [node]
    if text_type == TextType.IMAGE:
        extracts = extract_markdown_images(node.text)
    else:
        extracts = extract_markdown_links(node.text)
    if not extracts:
        return [node]
    text = node.text
    for alt, link in extracts:
        pattern = (
            f"![{alt}]({link})"
            if text_type == TextType.IMAGE
            else f"[{alt}]({link})"
        )
        sections = text.split(pattern, 1)
        if len(sections) != 2:
            msg = "invalid markdown, image section not closed" if text_type == TextType.IMAGE else "invalid markdown, link section not closed"
            raise ValueError(msg)
        if sections[0]:
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
        new_nodes.append(TextNode(alt, text_type, link))
        text = sections[1]
    if text:
        new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node(node, TextType.IMAGE))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node(node, TextType.LINK))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)