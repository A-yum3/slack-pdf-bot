from infra.pdf_converter import PdfConverter


class TestConverter(object):
    def test_output_pdf(self):
        PdfConverter([]).execute()
