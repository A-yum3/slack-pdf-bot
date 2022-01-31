from typing import Union

from app.enums.element_type import ElementType
from app.enums.text_style import TextStyle


class Element:
    def __init__(self, element: dict):
        self.element_type: ElementType = element.get('type')
        self.text: str = element.get('text')
        self.user_id: str = element.get('user_id')
        self.name: str = element.get('name')
        self.url: str = element.get('url')
        self.style: Union[TextStyle, None] = TextStyle.get_style(element.get('style'))

        self.convert_br_tag()

    def get_with_tag(self) -> str:
        if self.text is None:
            return ""

        if self.style is None:
            return self.text
        else:
            # TODO とりあえずElementType.TEXTのみ考慮
            start, end = TextStyle.get_tag(self.style)
            return start + self.text + end

    def convert_br_tag(self) -> None:
        if self.text is None:
            return
        self.text = self.text.replace("\n", "<br/>")
