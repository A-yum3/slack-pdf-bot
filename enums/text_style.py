from enum import Enum
from typing import Union


class TextStyle(Enum):
    BOLD = "bold"
    STRIKE = "strike"
    ITALIC = "italic"
    CODE = "code"

    @classmethod
    def get_style(cls, style: dict) -> Union['TextStyle', None]:
        if style.get(cls.BOLD):
            return cls.BOLD
        elif style.get(cls.STRIKE):
            return cls.STRIKE
        elif style.get(cls.ITALIC):
            return cls.STRIKE
        elif style.get(cls.CODE):
            return cls.CODE
        else:
            return None

    @classmethod
    def get_tag(cls, style: 'TextStyle') -> Union[tuple, None]:
        if style == cls.BOLD:
            return "<b>", "</b>"
        elif style == cls.STRIKE:
            return "<strike>", "</strike>"
        elif style == cls.ITALIC:
            return "<i>", "</i>"
        elif style == cls.CODE:
            return "", ""  # TODO 考える
        else:
            return None
