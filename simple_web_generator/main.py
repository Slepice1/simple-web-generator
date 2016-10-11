#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

import click
import yaml
import os

from simple_web_generator.window import Window

@click.command()
@click.argument('template', type=click.File('r'))
@click.option('--directory', default=False)
@click.option('--template', default=False)
def main(template, directory):
    yaml_template = yaml.load(template)
    config = yaml_template.get("config", {})

    windows = list(get_windows(yaml_template))
    if config.get("windows_same_width", False):
        max_width = max(window.width for window in windows)
        for window in windows:
            window.width = max_width
    rendered_text = render(windows, config)
    if directory:
        if template:
            create_html_file(directory, rendered_text, template)
        else:
            create_html_file(directory, rendered_text)
    else:
        click.echo(rendered_text)

def create_html_file(directory_name, generated_text,
                     template="simple_web_generator/template.html"):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    with open("simple_web_generator/template.html", "r") as template:
        template_text = template.read();
        with open(os.path.join(directory_name, "index.html"), "w") as write_file:
            write_file.write(template_text.replace("<!--text-->", generated_text))

def render(windows, config):
    output = []
    spaces_between_windows = config.get("spaces_between_windows", 1)
    for window in windows:
        output.append(window.render())
        output.extend("" for _ in range(spaces_between_windows))
    return "\n".join(output)

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
