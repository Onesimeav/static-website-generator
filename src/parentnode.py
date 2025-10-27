from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag")
        
        if self.children == None:
            raise ValueError("Missing children")
        
        props_html = super().props_to_html()
        parent_html = f"<{self.tag}{props_html}>"
        for child in self.children:
            if child.children == None:
                parent_html += f"<{child.tag}{child.props_to_html()}>{child.value}</{child.tag}>"
            else:
                parent_html += f"{child.to_html()}"
        
        return parent_html+f"</{self.tag}>"