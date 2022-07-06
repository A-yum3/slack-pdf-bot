from app.models.message_content import MessageContent
from app.models.rich_text_basic import RichTextBasic


class RichTextList(MessageContent):
    def __init__(self, element: dict):
        self.type = element.get('type')
        self.list_style = element.get('style')
        self.indent = element.get('indent')
        elements = element.get('elements')
        self.elements = [RichTextBasic(element) for element in elements]
