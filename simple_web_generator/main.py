#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""



import click
import yaml

from simple_web_generator.window import Window

@click.command()
@click.argument('template', type=click.File('r'))
def main(template):
    yaml_template = yaml.load(template)
    click.echo(yaml_template)

def get_windows(template):
    windows_info = template.get("windows", [])
    windows = []
    for window_info in windows_info:
        if 'id' in window_info:
            windows.append(Window(**window_info))
        else:
            raise TemplateException("Id for window must be set")
    return windows

class TemplateException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    main()
