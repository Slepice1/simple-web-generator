#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Window class"""

from simple_web_generator.content import Content

class Window:

    """Basic window class"""

    DEFAULT_HORIZONTAL_BORDER = "-";
    DEFAULT_VERTICAL_BORDER = "|";
    DEFAULT_CORNER = "+";

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name", self.id)
        self.show_name = kwargs.get("show_name", False)

        self.content = Content(kwargs.get("content", ""))

        self._set_border(kwargs.get("border", {}))

        self.width = self._get_width(kwargs.get("width", 1))
        self.height = self._get_height(kwargs.get("height", 1))

    def _set_border(self, border):
        self.horizontal_border = border.get("horizontal", Window.DEFAULT_HORIZONTAL_BORDER)
        self.vertical_border = border.get("vertical", Window.DEFAULT_VERTICAL_BORDER)
        self.corner = border.get("corner", Window.DEFAULT_CORNER)

    def _get_width(self, width):
        if self.show_name:
            width = max((int(width), self.content.width, len(self.name) + 2))
        else:
            width = max(int(width), self.content.width)
        return width + 2 #size of border

    def _get_height(self, height):
        height = max(int(height), self.content.height)
        return height + 2 #size of border

    def render(self):
        lines = []
        horizontal_template = "{0}" + "{1}"*(self.width-2) + "{0}"
        if self.show_name:
            template = "{0}{1}{2}" + "{1}"*(self.width-2-len(self.name)-1) + "{0}"
            lines.append(template.format(self.corner,
                                         self.horizontal_border,
                                         self.name))
        else:
            lines.append(horizontal_template.format(self.corner,
                                                    self.horizontal_border))

        content_lines = self.content.render().splitlines()
        for i in range(self.height-2):
            if i < len(content_lines):
                line_template = "{0}{2}" + "{1}"*(self.width-2-len(content_lines[i])) + "{0}"
                lines.append(line_template.format(self.vertical_border,
                                                  " ",
                                                  content_lines[i]))
            else:
                line_template = "{0}" + "{1}"*(self.width-2) + "{0}"
                lines.append(line_template.format(self.vertical_border," ",))

        lines.append(horizontal_template.format(self.corner,
                                                self.horizontal_border))
        return '\n'.join(lines)
