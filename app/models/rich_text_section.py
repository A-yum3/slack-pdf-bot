from app.models.element import Element
from app.models.message_content import MessageContent


class RichTextSection(MessageContent):
    def __init__(self, element: dict):
        super().__init__()
        elements = element.get('elements')
        self.elements = [Element(element) for element in elements]
