import unittest
from markdown_to_html_node import markdown_to_html_node, extract_title
from htmlnode import *

class TestMartdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
        
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_markdown_to_html_complete(self):
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
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6><p>This is a paragraph of text.</p><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><blockquote>This is a quote.</blockquote><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li><li>Item 4</li><li>Item 5</li><li>Item 6</li><li>Item 7</li><li>Item 8</li><li>Item 9</li><li>Item 10</li><li>Item 11</li></ol><pre><code>This is code\n</code></pre></div>",
        )

    def test_extract_title(self):
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
        title = extract_title(md)
        self.assertEqual(title, "Heading 1")

    def test_extract_title_2(self):
        md = """
## Heading 2

#   Heading 1   

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
        title = extract_title(md)
        self.assertEqual(title, "Heading 1")
    
    def test_extract_title_3(self):
        md = """
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
        with self.assertRaises(ValueError):
            extract_title(md)
        

        
if __name__ == "__main__":
    unittest.main()