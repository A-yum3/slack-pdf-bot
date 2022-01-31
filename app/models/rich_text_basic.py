from app.models.element import Element
from app.models.message_content import MessageContent


class RichTextBasic(MessageContent):
    def __init__(self, element: dict):
        super().__init__()
        elements = element.get('elements')
        self.type = element.get('type')
        self.elements = [Element(element) for element in elements]
