from enum import Enum


class TextStyle(Enum):
    BOLD = "bold"
    STRIKE = "strike"
    ITALIC = "italic"
    CODE = "code"

    @classmethod
    def get_style(cls, element: dict):
        style = element.get('style')
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
