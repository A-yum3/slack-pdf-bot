from app.models.message_content import MessageContent
from app.models.rich_text_section import RichTextSection


class RichTextList(MessageContent):
    def __init__(self, element: dict):
        self.list_style = element.get('style')
        self.indent = element.get('indent')
        elements = element.get('elements')
        self.elements = [RichTextSection(element) for element in elements]
