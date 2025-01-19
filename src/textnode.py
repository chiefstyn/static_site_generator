from enum import Enum

class TextType(Enum)
	NORMAL_TEXT = "normal"
	BOLD_TEXT = "bold"
	ITALIC_TEXT = "italic"
	CODE_TEXT = "code"
	LINK = "link"
	IMAGE = "image"


class TextNode(Enum):
	self.text
	self.text_type
	self.url
