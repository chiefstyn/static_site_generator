


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value 
        self.children = children 
        self.props = props 


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
#                  <start tag : add props >            # value     # </closing tag>
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
            
                


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
    
        if self.props is None:
            return ""
        
        
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'

        print(f"Debug result: {props_html}")
        return props_html
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
