from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value,props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag ==None:
            return self.value
        if self.props:
            props_html = super().props_to_html()
            return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
