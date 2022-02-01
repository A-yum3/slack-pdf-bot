from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import mm, portrait, A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, PageTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus.flowables import Spacer
from reportlab.platypus.frames import Frame

from app.enums.rich_text_type import RichTextType


class PdfConverter:
    def __init__(self, messages: list, user_table: dict):
        self.messages = messages
        self.user_table = user_table

    # TODO 表示形式修正
    def execute(self):
        SOURCE_HAN_SANS_PATH = '../../fonts/SourceHanSansHW-VF.ttf'
        pdfmetrics.registerFont(TTFont('SourceHanSans', SOURCE_HAN_SANS_PATH))

        file_name = 'output.pdf'

        doc = BaseDocTemplate(file_name, title="test", pagesize=portrait(A4))

        frames = [
            Frame(10 * mm, 20 * mm, 190 * mm, 260 * mm, showBoundary=1),
        ]

        page_template = PageTemplate("frames", frames=frames)
        doc.addPageTemplates(page_template)
        style_text = {
            "name": "normal",
            "fontName": "SourceHanSans",
            "fontSize": 16,
            "leading": 20,
            "firstLineIndent": 0,
            "alignment": TA_RIGHT,
        }
        style = ParagraphStyle(**style_text)

        style_name = {
            "name": "normal",
            "fontName": "SourceHanSans",
            "fontSize": 10,
            "leading": 20,
            "firstLineIndent": 0,
        }
        name_style = ParagraphStyle(**style_name)

        flowables = []

        space = Spacer(3 * mm, 3 * mm)

        for message in self.messages:
            image_text = f'<img src="{self.user_table[message.user]["image"]}" valign="top"/>'

            flowables.append(Paragraph(image_text))
            flowables.append(Spacer(5 * mm, 5 * mm))
            flowables.append(Paragraph(self.user_table[message.user]['name'], name_style))

            for content in message.message_contents:
                if content is None:
                    continue

                if content.type == RichTextType.LIST.value:
                    for inner_content in content.elements:
                        for element in inner_content.elements:
                            p = Paragraph(element.get_with_tag(), style)
                            flowables.append(p)
                            flowables.append(space)
                else:
                    for element in content.elements:
                        p = Paragraph(element.get_with_tag(), style)
                        flowables.append(p)
                        flowables.append(space)

        doc.multiBuild(flowables)

        return file_name
