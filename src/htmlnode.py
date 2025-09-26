


class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props


    def to_html(self):
      raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {k}="{v}"' for k, v in self.props.items())
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


    def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: no tag")   
        if self.children is None:
            raise ValueError("invalid ParentNode: children is None")
        if len(self.children) == 0:
            raise ValueError("invalid ParentNode: no children")
        HTMLstring = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError("invalid child: not a HTMLNode")
            HTMLstring += child.to_html()
        return HTMLstring + f"</{self.tag}>"


    def __repr__(self):
        return f"ParentNode({self.tag}, Children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")   
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"