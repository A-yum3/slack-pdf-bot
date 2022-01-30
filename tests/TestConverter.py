from converter import Converter


class TestConverter(object):
    def test_output_pdf(self):
        Converter([]).to_pdf()
