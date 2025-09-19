from textnode import *
from enum import Enum

def main():
    test_node = TextNode("This is some anchor text", TextType.LINK)
    print(test_node)


main()