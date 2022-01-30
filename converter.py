from reportlab.lib.pagesizes import mm, portrait, A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import cidfonts
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import BaseDocTemplate, PageTemplate
from reportlab.platypus import Paragraph, PageBreak
from reportlab.platypus.flowables import Spacer
from reportlab.platypus.frames import Frame


class Converter:
    # TODO Messageを受け取るように修正
    def __init__(self, value_lists):
        self.value_lists = value_lists

    # TODO 表示形式修正
    def to_pdf(self):
        pdfmetrics.registerFont(cidfonts.UnicodeCIDFont("HeiseiMin-W3"))

        file_name = 'output.pdf'  # ファイル名を設定

        doc = BaseDocTemplate(file_name, title="test", pagesize=portrait(A4))

        show = 1  # Frameの枠を表示
        frames = [
            Frame(10 * mm, 20 * mm, 190 * mm, 260 * mm, showBoundary=show),
        ]

        page_template = PageTemplate("frames", frames=frames)
        doc.addPageTemplates(page_template)
        style_dict = {
            "name": "nomarl",
            "fontName": "HeiseiMin-W3",
            "fontSize": 20,
            "leading": 20,
            "firstLineIndent": 20,
        }
        style = ParagraphStyle(**style_dict)

        flowables = []

        space = Spacer(10 * mm, 10 * mm)

        para = Paragraph("こんなものは、reportlabではない!!<br/><br/>", style)
        flowables.append(para)
        flowables.append(space)
        para = Paragraph("本当のreportlabをお見せします。", style)
        flowables.append(para)
        flowables.append(space)
        para = Paragraph("次のページに来てください", style)
        flowables.append(para)

        # 改ページ
        flowables.append(PageBreak())

        para = Paragraph("<span backcolor=yellow>フーレム1</span>", style)
        flowables.append(para)
        para = Paragraph("Paragraphを使うことで長い文章を自動で折り返してくれます。さらにはみ出せば次のページに進みます。", style)
        flowables.append(para)
        para = Paragraph("ちゃんと続きの高さから次のParagraphを描画してくれます。", style)
        flowables.append(para)
        para = Paragraph("Frameを使えば、はみ出した分は次のフレームまたはページへ自動で進みます。", style)
        flowables.append(para)
        para = Paragraph("Frameを使うことで、段組みのような複雑なレイアウトを表現できます。", style)
        flowables.append(para)

        doc.multiBuild(flowables)

        return file_name
