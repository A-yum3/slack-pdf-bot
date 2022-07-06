from enum import Enum
from typing import Union


class TextStyle(Enum):
    BOLD = "bold"
    STRIKE = "strike"
    ITALIC = "italic"
    CODE = "code"

    @classmethod
    def get_style(cls, style: dict) -> Union['TextStyle', None]:
        if style is None:
            return None

        if style.get(TextStyle.BOLD.value):
            return TextStyle.BOLD
        elif style.get(TextStyle.STRIKE.value):
            return TextStyle.STRIKE
        elif style.get(TextStyle.ITALIC.value):
            return TextStyle.ITALIC
        elif style.get(TextStyle.CODE.value):
            return TextStyle.CODE
        else:
            return None

    @classmethod
    def get_tag(cls, style: 'TextStyle') -> tuple:

        if style is None:
            return None

        if style == TextStyle.BOLD:
            return "<b>", "</b>"
        elif style == TextStyle.STRIKE:
            return "<strike>", "</strike>"
        elif style == TextStyle.ITALIC:
            return "<i>", "</i>"
        elif style == TextStyle.CODE:
            return "", ""  # TODO 考える
        else:
            return "", ""
