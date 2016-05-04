import pytest

from simple_web_generator.content import Content

class TestContentClass:
    def test_basic_constructor(self):
        #Content with empty text
        content_empty = vars(Content(""))
        assert content_empty['html'] == ""
        assert content_empty['plain_text'] == ""
        #Content with text without markup
        content_text = vars(Content("Vojtěch \"Slepice1\" Jelínek"))
        assert content_text['html'] == "Vojtěch \"Slepice1\" Jelínek"
        assert content_text['plain_text'] == "Vojtěch \"Slepice1\" Jelínek"
        #Content with multiline text
        content_multiline_text = vars(Content("test1\ntest2\ntest3"))
        assert content_multiline_text['plain_text'] == "test1\ntest2\ntest3"
        assert content_multiline_text['html'] == "test1<br/>\ntest2<br/>\ntest3"
        #Contnt with multiline text and empty lines
        content_multiline_text = vars(Content("test1\n\ntest3"))
        assert content_multiline_text['plain_text'] == "test1\n\xa0\ntest3"
        assert content_multiline_text['html'] == "test1<br/>\n\xa0<br/>\ntest3"
