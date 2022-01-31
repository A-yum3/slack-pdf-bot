from enums.rich_text_type import RichTextType


class Message:
    def __init__(self, message: dict):
        self.blocks = message.get('blocks')
        self.files = message.get('files')
        self.message_contents = self.create_contents()

    def create_contents(self):
        return [RichTextType.make_content(content) for block in self.blocks for content in block.get('elements')]
