import unittest
from markdown_blocks import *


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """


        This is **bolded** paragraph   

        
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items   


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_block_to_block_type(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

This is a paragraph of text.


- Item 1
- Item 2
- Item 3

> This is a quote.

1. Item 1
2. Item 2
3. Item 3
4. Item 4
5. Item 5
6. Item 6
7. Item 7
8. Item 8
9. Item 9
10. Item 10
11. Item 11

```
This is code
```
"""
        blocks = markdown_to_blocks(md)
        blocktypes = []
        for block in blocks:
            blocktypes.append(block_to_block_type(block))
        self.assertListEqual(blocktypes, [
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST,
            BlockType.QUOTE,
            BlockType.ORDERED_LIST,
            BlockType.CODE,
        ])

    def test_invalid_heading_no_space(self):
        block = "#heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_wrong_start(self):
        block = "2. Second item\n3. Third item"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH) 

if __name__ == "__main__":
    unittest.main()