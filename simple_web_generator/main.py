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

def add_default(window_info, default):
    for key in default:
        if key not in window_info:
            window_info[key] = default[key]
    return window_info

def get_windows(template):
    default = template.get("window_default", {})
    windows_info = template.get("windows", [])
    for window_info in windows_info:
        if 'id' in window_info:
            yield Window(add_default(window_info, default))
        else:
            raise TemplateException("Id for window must be set")

class TemplateException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    main()
