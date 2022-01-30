from enums.rich_text_type import RichTextType


class MessageFactory:
    def __init__(self):
        pass

    def creates(self, message: dict) -> list:
        self.create_by_blocks(message.get('blocks'))

    def create_by_blocks(self, blocks):
        for block in blocks:
            for element in block.get('elements'):
                self.create_by_rich_text(element)

    def create_by_rich_text(self, element: dict):
        rich_text_type = element.get('type')
        if rich_text_type == RichTextType.SECTION:
            pass
        elif rich_text_type == RichTextType.LIST:
            pass
        elif rich_text_type == RichTextType.PREFORMATTED:
            pass
        else:
            pass
        for inner_element in element.get('elements'):
            pass
