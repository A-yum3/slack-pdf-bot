from models.element import Element
from models.message_content import MessageContent


class RichTextPreformatted(MessageContent):
    def __init__(self, element: dict):
        super().__init__()
        elements = element.get('elements')
        self.elements = [Element(element) for element in elements]
