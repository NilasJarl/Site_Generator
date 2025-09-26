from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(textblock):
    if textblock.startswith(("# ", "## ", "### ","#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if textblock.startswith("```") and textblock.endswith("```"):
        return BlockType.CODE
    blocks = textblock.split("\n")
    num_blocks = len(blocks)
    quotes = 0
    unorder = 0
    order = 0
    for block in blocks:
        if block == "":
            num_blocks -= 1
            continue
        if block.startswith(">"):
            quotes += 1
            continue
        if block.startswith("- "):
            unorder += 1
            continue
        if block.startswith(f"{order + 1}. "):
            order += 1
    if quotes == num_blocks:
        return BlockType.QUOTE
    if unorder == num_blocks:
        return BlockType.UNORDERED_LIST
    if order == num_blocks:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
            

    


def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        new_block = block.strip()
        if new_block != "":
            blocks.append(new_block)
    return blocks
