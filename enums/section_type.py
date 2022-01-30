from enum import Enum


class SectionType(Enum):
    TEXT = "text"
    EMOJI = "emoji"
    USER = "user"
    LINK = "link"

    @classmethod
    def get_value(cls, element: dict) -> str:
        element_type = element.get('type')
        if element_type == SectionType.TEXT:
            return element['text']
        elif element_type == SectionType.EMOJI:
            return element['name']
        elif element_type == SectionType.USER:
            return element['user_id']
        elif element_type == SectionType.LINK:
            return element['url']
        else:
            return ""
