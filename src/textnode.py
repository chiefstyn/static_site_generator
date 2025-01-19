from enum import Enum

class TextType(Enum):
	NORMAL_TEXT = "normal"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK = "link"
	IMAGE = "image"


class TextNode:
	def __init__(self, text, text_type, url):	
		self.text = text ##actual content for this text node
		self.text_type = text_type ##required input that must be a valid member of enum, enfores valid types for the node
		self.url = url ##node contains a link or image or link

	def __eq__ (self, other):
		if isinstance(other, TextNode):
			return False
		return (
			self.text == other.text and 
			self.text_type == other.text_type and
			self.url == other.url
		)
	
	def __repr__ (self):
		return f"TextNode({self.text},{self.text_type.value},{self.url})"