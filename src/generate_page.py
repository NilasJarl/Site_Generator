import os, shutil
from markdown_to_html_node import markdown_to_html_node, extract_title
from htmlnode import HTMLNode, ParentNode


def static_to_public(source, destination):
    path_destination = os.path.abspath(destination)
    path_source = os.path.abspath(source)
    if os.path.exists(path_destination):
        shutil.rmtree(path_destination)
    os.makedirs(path_destination, exist_ok=True)
    _copy_recursive(path_source, path_destination)

def _copy_recursive(path_source, path_destination):
    for content in os.listdir(path_source):
        content_path = os.path.join(path_source, content)
        destination_path = os.path.join(path_destination, content)
        if os.path.isdir(content_path):
            os.makedirs(destination_path, exist_ok=True)
            _copy_recursive(content_path, destination_path)
            continue
        else:
            shutil.copy(content_path, destination_path)



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
            template = f.read() 
    title = extract_title(markdown)
    html_string = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    dest_path_dir = os.path.dirname(dest_path)
    os.makedirs(dest_path_dir, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        if os.path.isdir(content_path):
            generate_page_recursive(content_path, template_path, os.path.join(dest_dir_path, content))
        elif os.path.isfile(content_path):
            filename, file_extension = os.path.splitext(content)
            if file_extension == ".md":
                generate_page(content_path, template_path, os.path.join(dest_dir_path, filename + ".html"))            





   