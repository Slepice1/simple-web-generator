import pytest

from simple_web_generator.window import Window

class TestWindowClass:
    def test_basic_constructor(self):
        #Window with only id set
        window_only_id = vars(Window(**{'id': 'header'}))
        assert window_only_id['id'] == "header"
        assert window_only_id['name'] == "header"
        assert window_only_id['show_name'] == False
        #Window with id and name set
        window_id_name = vars(Window(**{'id': 'header', 'name': 'ABOUT'}))
        assert window_id_name['id'] == "header"
        assert window_id_name['name'] == "ABOUT"
        assert window_id_name['show_name'] == False
        assert window_id_name['width'] == 3
        assert window_id_name['height'] == 3
        #Window with id and name and show_name set
        window_all = vars(Window(**{'id': 'header', 'name': 'ABOUT', 'show_name': True}))
        assert window_all['id'] == "header"
        assert window_all['name'] == "ABOUT"
        assert window_all['show_name'] == True

    def test_content_constructor(self):
        window_sizes = vars(Window(**{'id': 'header', 'width': '5', 'height': 8}))
        assert window_sizes['id'] == "header"
        assert window_sizes['width'] == 7
        assert window_sizes['height'] == 10

        window_name_size = vars(Window(**{'id': 'header', 'show_name': True}))
        assert window_name_size['id'] == "header"
        assert window_name_size['width'] == 10
        assert window_name_size['height'] == 3

        window_content_size = vars(Window(**{'id': 'header', 'content': "Ahoj toto je okno", 'width': '8'}))
        assert window_content_size['id'] == "header"
        assert window_content_size['content'].render() == "Ahoj toto je okno"
        assert window_content_size['width'] == 19
        assert window_content_size['height'] == 3

    def test_no_content_render(self):
        window_only_id = Window(**{'id': 'header'})
        assert window_only_id.render() == ("+-+\n"
                                           "| |\n"
                                           "+-+")
        window_with_sizes = Window(**{'id': 'header', 'width': 5, 'height': 2})
        assert window_with_sizes.render() == ("+-----+\n"
                                              "|     |\n"
                                              "|     |\n"
                                              "+-----+")
        window_show_id = Window(**{'id': 'header', 'show_name': True})
        assert window_show_id.render() == ("+-header-+\n"
                                           "|        |\n"
                                           "+--------+")
        window_show_id_fixed_width = Window(**{'id': 'header', 'show_name': True, 'width': 10})
        assert window_show_id_fixed_width.render() == ("+-header---+\n"
                                                       "|          |\n"
                                                       "+----------+")

    def test_content_render(self):
        window_line_content = Window(**{'id': 'header', 'content': "Vojtěch \"Slepice1\" Jelínek"})
        assert window_line_content.render() == ("+--------------------------+\n"
                                                "|Vojtěch \"Slepice1\" Jelínek|\n"
                                                "+--------------------------+")
