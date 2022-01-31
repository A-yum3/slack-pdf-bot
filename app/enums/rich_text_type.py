from enum import Enum
from typing import Union

from app.models.message_content import MessageContent
from app.models.rich_text_list import RichTextList
from app.models.rich_text_preformatted import RichTextPreformatted
from app.models.rich_text_section import RichTextSection


class RichTextType(Enum):
    SECTION = "rich_text_section"
    LIST = "rich_text_list"
    PREFORMATTED = "rich_text_preformatted"

    @classmethod
    def make_content(cls, element: dict) -> Union[MessageContent, None]:
        section_type = element.get('type')
        if section_type == cls.SECTION:
            return RichTextSection(element)
        elif section_type == cls.LIST:
            return RichTextList(element)
        elif section_type == cls.PREFORMATTED:
            return RichTextPreformatted(element)
        else:
            return None
