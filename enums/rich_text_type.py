from enum import Enum


class RichTextType(Enum):
    SECTION = "rich_text_section"
    LIST = "rich_text_list"
    PREFORMATTED = "rich_text_preformatted"

    @classmethod
    def get_value(cls, element: dict):
        element_type = element.get('type')
        if element_type == cls.SECTION:
            pass
        elif element_type == cls.LIST:
            pass
        elif element_type == cls.PREFORMATTED:
            pass
