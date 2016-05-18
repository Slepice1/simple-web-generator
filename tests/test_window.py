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
        window_id_name = vars(Window(**{'id': 'header',
                                        'name': 'ABOUT'}))
        assert window_id_name['id'] == "header"
        assert window_id_name['name'] == "ABOUT"
        assert window_id_name['show_name'] == False
        assert window_id_name['width'] == 2
        assert window_id_name['height'] == 2
        #Window with id and name and show_name set
        window_all = vars(Window(**{'id': 'header',
                                    'name': 'ABOUT',
                                    'show_name': True}))
        assert window_all['id'] == "header"
        assert window_all['name'] == "ABOUT"
        assert window_all['show_name'] == True

    def test_content_constructor(self):
        window_sizes = vars(Window(**{'id': 'header',
                                      'width': '5',
                                      'height': 8}))
        assert window_sizes['id'] == "header"
        assert window_sizes['width'] == 5
        assert window_sizes['height'] == 8

        window_name_size = vars(Window(**{'id': 'header', 'show_name': True}))
        assert window_name_size['id'] == "header"
        assert window_name_size['width'] == 10
        assert window_name_size['height'] == 2

        window_content_size = vars(Window(**{'id': 'header',
                                             'content': "Ahoj toto je okno",
                                             'width': '8'}))
        assert window_content_size['id'] == "header"
        assert window_content_size['content'].render() == "Ahoj toto je okno"
        assert window_content_size['width'] == 19
        assert window_content_size['height'] == 3

    def test_no_content_render(self):
        window_only_id = Window(**{'id': 'header'})
        assert window_only_id.render() == ("++\n"
                                           "++")
        window_with_sizes = Window(**{'id': 'header',
                                      'width': 5,
                                      'height': 4})
        assert window_with_sizes.render() == ("+---+\n"
                                              "|   |\n"
                                              "|   |\n"
                                              "+---+")
        window_show_id = Window(**{'id': 'header',
                                   'show_name': True})
        assert window_show_id.render() == ("+-header-+\n"
                                           "+--------+")
        window_show_id_fixed_width = Window(**{'id': 'header',
                                               'show_name': True,
                                               'width': 12,
                                               'height': 3})
        assert window_show_id_fixed_width.render() == ("+-header---+\n"
                                                       "|          |\n"
                                                       "+----------+")

    def test_content_render(self):
        window_line_content = Window(**{'id': 'header',
                                        'content': "Vojtěch \"Slepice1\" Jelínek"})
        assert window_line_content.render() == ("+--------------------------+\n"
                                                "|Vojtěch \"Slepice1\" Jelínek|\n"
                                                "+--------------------------+")

        window_line_content_header = Window(**{'id': 'header',
                                               'show_name': True,
                                               'content': "Vojtěch \"Slepice1\" Jelínek"})
        assert window_line_content_header.render() == ("+-header-------------------+\n"
                                                       "|Vojtěch \"Slepice1\" Jelínek|\n"
                                                       "+--------------------------+")

        window_multiline_content = Window(**{'id': 'header',
                                             'content': "test111\ntest2\ntest3"})
        assert window_multiline_content.render() == ("+-------+\n"
                                                     "|test111|\n"
                                                     "|test2  |\n"
                                                     "|test3  |\n"
                                                     "+-------+")
        window_multiline_empty = Window(**{'id': 'header',
                                           'content': "test1\n\ntest3"})
        assert window_multiline_empty.render() == ("+-----+\n"
                                                   "|test1|\n"
                                                   "|\xa0    |\n" #hardspace
                                                   "|test3|\n"
                                                   "+-----+")
        links = "[example1](http://example.com/)\n[example2](http://example2.com/)"
        window_links = Window(**{'id': 'header', 'content': links})
        assert window_links.render() == ('+--------+\n'
                                         '|<a href="http://example.com/">example1</a>|\n'
                                         '|<a href="http://example2.com/">example2</a>|\n'
                                         '+--------+')

    def test_no_content_basic_padding_render(self):
        window_one_padding_ver = Window(**{'id': 'header',
                                           'padding': '1 0 0 0'})
        assert window_one_padding_ver.render() == ("++\n"
                                                   "||\n"
                                                   "++")
        window_one_padding_hor = Window(**{'id': 'header',
                                           'padding': '0 0 0 1'})
        assert window_one_padding_hor.render() == ("+-+\n"
                                                   "+-+")
        window_two_paddings_ver = Window(**{'id': 'header',
                                            'padding': '1 0 1 0'})
        assert window_two_paddings_ver.render() == ("++\n"
                                                    "||\n"
                                                    "||\n"
                                                    "++")
        window_two_paddings_hor = Window(**{'id': 'header',
                                            'padding': '0 1 0 1'})
        assert window_two_paddings_hor.render() == ("+--+\n"
                                                    "+--+")
        window_two_paddings_diff = Window(**{'id': 'header',
                                             'padding': '1 1 0 0'})
        assert window_two_paddings_diff.render() == ("+-+\n"
                                                     "| |\n"
                                                     "+-+")
        window_three_paddings = Window(**{'id': 'header',
                                          'padding': '2 1 0 1'})
        assert window_three_paddings.render() == ("+--+\n"
                                                  "|  |\n"
                                                  "|  |\n"
                                                  "+--+")

    def test_heading_basic_padding_render(self):
        window_one_padding_ver = Window(**{'id': 'header',
                                           'show_name': True,
                                           'padding': '1 0 0 0'})
        assert window_one_padding_ver.render() == ("+-header-+\n"
                                                   "|        |\n"
                                                   "+--------+")
        window_one_padding_hor = Window(**{'id': 'header',
                                           'show_name': True,
                                           'padding': '0 0 0 1'})
        assert window_one_padding_hor.render() == ("+-header--+\n"
                                                   "+---------+")
        window_two_paddings_ver = Window(**{'id': 'header',
                                            'show_name': True,
                                            'padding': '1 0 1 0'})
        assert window_two_paddings_ver.render() == ("+-header-+\n"
                                                    "|        |\n"
                                                    "|        |\n"
                                                    "+--------+")
        window_two_paddings_hor = Window(**{'id': 'header',
                                            'show_name': True,
                                            'padding': '0 1 0 1'})
        assert window_two_paddings_hor.render() == ("+-header---+\n"
                                                    "+----------+")

    def test_set_sizes_basic_padding_render(self):
        window_one_padding_ver = Window(**{'id': 'header',
                                           'show_name': True,
                                           'padding': '1 0 0 0',
                                           'height': 5})
        assert window_one_padding_ver.render() == ("+-header-+\n"
                                                   "|        |\n"
                                                   "|        |\n"
                                                   "|        |\n"
                                                   "+--------+")
        window_one_padding_hor = Window(**{'id': 'header',
                                           'show_name': True,
                                           'padding': '0 0 0 1',
                                           'width': 12})
        assert window_one_padding_hor.render() == ("+-header---+\n"
                                                   "+----------+")
        window_three_paddings = Window(**{'id': 'header',
                                          'padding': '2 1 0 1',
                                          'width': 5,
                                          'height': 5})
        assert window_three_paddings.render() == ("+---+\n"
                                                  "|   |\n"
                                                  "|   |\n"
                                                  "|   |\n"
                                                  "+---+")
    def test_content_padding_render(self):
        window_line_content = Window(**{'id': 'header',
                                        'content': "Vojtěch \"Slepice1\" Jelínek",
                                        'padding': '1 1 0 1'})
        assert window_line_content.render() == ("+----------------------------+\n"
                                                "|                            |\n"
                                                "| Vojtěch \"Slepice1\" Jelínek |\n"
                                                "+----------------------------+")

        window_line_content_header = Window(**{'id': 'header',
                                               'show_name': True,
                                               'content': "Vojtěch \"Slepice1\" Jelínek",
                                               'padding': '1 2 1 1'})
        assert window_line_content_header.render() == ("+-header----------------------+\n"
                                                       "|                             |\n"
                                                       "| Vojtěch \"Slepice1\" Jelínek  |\n"
                                                       "|                             |\n"
                                                       "+-----------------------------+")

        window_multiline_content = Window(**{'id': 'header',
                                             'content': "test111\ntest2\ntest3",
                                             'padding': '0 2 0 3'})
        assert window_multiline_content.render() == ("+------------+\n"
                                                     "|   test111  |\n"
                                                     "|   test2    |\n"
                                                     "|   test3    |\n"
                                                     "+------------+")
        window_multiline_empty = Window(**{'id': 'header',
                                           'content': "test1\n\ntest3",
                                           'padding': '2 1 1 1'})
        assert window_multiline_empty.render() == ("+-------+\n"
                                                   "|       |\n"
                                                   "|       |\n"
                                                   "| test1 |\n"
                                                   "| \xa0     |\n" #hardspace
                                                   "| test3 |\n"
                                                   "|       |\n"
                                                   "+-------+")
        links = "[example1](http://example.com/)\n[example2](http://example2.com/)"
        window_links = Window(**{'id': 'header',
                                 'content': links,
                                 'padding': '0 2 0 3'})
        assert window_links.render() == ('+-------------+\n'
                                         '|   <a href="http://example.com/">example1</a>  |\n'
                                         '|   <a href="http://example2.com/">example2</a>  |\n'
                                         '+-------------+')
