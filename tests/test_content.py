import pytest

from simple_web_generator.content import Content

class TestContentClass:
    def test_constructor(self):
        #Content with empty text
        content_empty = vars(Content(""))
        assert content_empty['html'] == ""
        assert content_empty['_plain_text'] == ""
        assert content_empty['width'] == 0
        assert content_empty['height'] == 0
        #Content with text without markup
        content_text = Content("Vojtěch \"Slepice1\" Jelínek")
        content_text_vars = vars(content_text)
        assert content_text.render() == "Vojtěch \"Slepice1\" Jelínek"
        assert content_text_vars['_plain_text'] == "Vojtěch \"Slepice1\" Jelínek"
        assert content_text_vars['width'] == len("Vojtěch \"Slepice1\" Jelínek")
        assert content_text_vars['height'] == 1
        #Content with multiline text
        content_multiline_text = Content("test111\ntest2\ntest3")
        content_multiline_text_vars = vars(content_multiline_text)
        assert content_multiline_text_vars['_plain_text'] == "test111\ntest2\ntest3"
        assert content_multiline_text.render() == "test111\ntest2\ntest3"
        assert content_multiline_text_vars['width'] == 7
        assert content_multiline_text_vars['height'] == 3
        #Contnt with multiline text and empty lines
        content_multiline_empty = Content("test1\n\ntest3")
        content_multiline_empty_vars = vars(content_multiline_empty)
        assert content_multiline_empty_vars['_plain_text'] == "test1\n\xa0\ntest3"
        assert content_multiline_empty.render() == "test1\n\xa0\ntest3"
        assert content_multiline_empty_vars['width'] == 5
        assert content_multiline_empty_vars['height'] == 3
        #Content with links
        content_links = Content("[example1](http://example.com/)\n[example2](http://example2.com/)")
        content_links_vars = vars(content_links)
        assert content_links_vars['_plain_text'] == "example1\nexample2"
        html = '<a href="http://example.com/">example1</a>\n<a href="http://example2.com/">example2</a>'
        assert content_links.render() == html
        assert content_links_vars['width'] == 8
        assert content_links_vars['height'] == 2
