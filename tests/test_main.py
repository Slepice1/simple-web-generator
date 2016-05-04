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

class TestYAMLParsing:
    def test_basic_windows(self):
        with click.open_file('tests/sample_files/test1.yaml', 'r') as f:
            template = yaml.load(f)
            result = get_windows(template)
        #Should return list of windows
        #assert result == [Window(**{'id': 'header', 'name': 'header'}), Window(**{'id': 'main', 'name': 'about'}), Window(**{'id': 'footer'})]
