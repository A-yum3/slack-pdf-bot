from enum import Enum
from typing import Union

from app.models.message_content import MessageContent
from app.models.rich_text_basic import RichTextBasic
from app.models.rich_text_list import RichTextList


class RichTextType(Enum):
    SECTION = "rich_text_section"
    LIST = "rich_text_list"
    PREFORMATTED = "rich_text_preformatted"
    QUOTE = "rich_text_quote"

    @classmethod
    def make_content(cls, element: dict) -> Union[MessageContent, None]:
        section_type = element.get('type')
        if section_type == RichTextType.LIST.value:
            return RichTextList(element)
        else:
            return RichTextBasic(element)
