from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import cidfonts
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


class Converter:
    def __init__(self, value_lists):
        self.value_lists = value_lists

    def to_pdf(self):
        pdfmetrics.registerFont(cidfonts.UnicodeCIDFont("HeiseiMin-W3"))

        file_name = 'output.pdf'  # ファイル名を設定
        pdf = canvas.Canvas(file_name, pagesize=portrait(A4))
        width, height = A4
        pdf.setFont('HeiseiMin-W3', 16)

        # insert text
        for index, text in enumerate(self.value_lists):
            pdf.drawString(x=50, y=(height - 50) - (index * 50), text=text)

        pdf.save()
        return file_name

# Converter(['こんにちは', '世界']).to_pdf()
