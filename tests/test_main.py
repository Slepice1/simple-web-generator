# -*- coding: utf-8 -*-
from pytest import raises

import pytest
parametrize = pytest.mark.parametrize

from simple_web_generator import metadata
from simple_web_generator.window import Window
from simple_web_generator.main import main, get_windows

import click
from click.testing import CliRunner

import yaml

class TestMain:
    @parametrize('helparg', ['--help'])
    def test_help(self, helparg, capsys):
        with raises(SystemExit) as exc_info:
            main(['progname', helparg])
        out, err = capsys.readouterr()
        # Should have printed some sort of usage message. We don't
        # need to explicitly test the content of the message.
        assert 'usage' in out.lower()
        # Should exit with zero return code.
        assert exc_info.value.code == 0

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
        #Window with id and name and show_name set
        window_all = vars(Window(**{'id': 'header', 'name': 'ABOUT', 'show_name': True}))
        assert window_all['id'] == "header"
        assert window_all['name'] == "ABOUT"
        assert window_all['show_name'] == True

    def  test_content_constructor(self):
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
        assert window_content_size['content'] == "Ahoj toto je okno"
        assert window_content_size['width'] == 19
        assert window_content_size['height'] == 3

    def test_no_content_render(self):
        window_only_id = Window(**{'id': 'header'})
        assert window_only_id.render() == "+-+\n| |\n+-+"
        window_with_sizes = Window(**{'id': 'header', 'width': 5, 'height': 2})
        assert window_with_sizes.render() == "+-----+\n|     |\n|     |\n+-----+"
        window_show_id = Window(**{'id': 'header', 'show_name': True})
        assert window_show_id.render() == "+-header-+\n|        |\n+--------+"

class TestYAMLParsing:
    def test_basic_windows(self):
        with click.open_file('tests/sample_files/test1.yaml', 'r') as f:
            template = yaml.load(f)
            result = get_windows(template)
        #Should return list of windows
        #assert result == [Window(**{'id': 'header', 'name': 'header'}), Window(**{'id': 'main', 'name': 'about'}), Window(**{'id': 'footer'})]
