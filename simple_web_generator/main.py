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
    config = yaml_template.get("config", {})
    windows = list(get_windows(yaml_template))
    if config.get("windows_same_width", False):
        max_width = max(window.width for window in windows)
        for window in windows:
            window.width = max_width
    output = []
    for window in windows:
        output.append(window.render())
    click.echo("\n".join(output))

def get_windows(template):
    windows_info = template.get("windows", [])
    for window_info in windows_info:
        if 'id' in window_info:
            yield Window(**window_info)
        else:
            raise TemplateException("Id for window must be set")

class TemplateException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    main()
