#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Window class"""

class Window:

    DEFAULT_HORIZONTAL_BORDER = "-";
    DEFAULT_VERTICAL_BORDER = "|";
    DEFAULT_CORNER = "+";

    TEMPLATE = "{0}\n{1}{2}"

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name", self.id)
        self.show_name = kwargs.get("show_name", False)

        self.content = kwargs.get("content", "")

        self._set_border(kwargs.get("border", {}))

        self.width = self._get_width(kwargs.get("width", 1))
        self.height = self._get_height(kwargs.get("height", 1))

    def _set_border(self, border):
        self.horizontal_border = border.get("horizontal", Window.DEFAULT_HORIZONTAL_BORDER)
        self.vertical_border = border.get("vertical", Window.DEFAULT_VERTICAL_BORDER)
        self.corner = border.get("corner", Window.DEFAULT_CORNER)

    def _get_width(self, width):
        if self.show_name:
            width = max((int(width), len(self.content), len(self.name) + 2))
        else:
            width = max(int(width), len(self.content))
        return width + 2 #size of border

    def _get_height(self, height):
        height = max(int(height), len(self.content.splitlines()))
        return height + 2 #size of border

    def render(self):
        horizontal_template = "{0}" + "{1}"*(self.width-2) + "{0}"
        if self.show_name:
            template = "{0}{1}{2}" + "{1}"*(self.width-2-len(self.name)-1) + "{0}"
            top_border = template.format(self.corner,
                                         self.horizontal_border,
                                         self.name)
        else:
            top_border = horizontal_template.format(self.corner,
                                                    self.horizontal_border)

        bottom_border = horizontal_template.format(self.corner,
                                                   self.horizontal_border)

        content = ""
        for i in range(self.height-2):
            content_line_template = "{0}" + "{1}"*(self.width-2) + "{0}\n"
            content += content_line_template.format(self.vertical_border, " ")

        return Window.TEMPLATE.format(top_border, content, bottom_border)
