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

        self.padding = tuple(int(pad) for pad in kwargs.get("padding", "0 0 0 0").split(' '))

        self._set_sizes(kwargs.get("width", 2), kwargs.get("height", 2)) #must be at least 3

    def _set_border(self, border):
        self.horizontal_border = border.get("horizontal", Window.DEFAULT_HORIZONTAL_BORDER)
        self.vertical_border = border.get("vertical", Window.DEFAULT_VERTICAL_BORDER)
        self.corner = border.get("corner", Window.DEFAULT_CORNER)

    def _set_sizes(self, width, height):
        horizontal_padding = self.padding[1] + self.padding[3]
        computed_width = self.content.width + horizontal_padding + 2 #border size
        if self.show_name:
            computed_width = max(computed_width, len(self.name) + horizontal_padding + 4) #border size

        self.width = max(int(width), computed_width)
        self.inside_width = self.width - horizontal_padding - 2 #border size

        vertical_padding = self.padding[0] + self.padding[2]
        computed_height = self.content.height + vertical_padding + 2  #border size
        self.height = max(int(height), computed_height)
        self.inside_height = self.height - vertical_padding - 2 #border size

    def render(self):
        lines = []
        spaces_width = self.inside_width + self.padding[1] + self.padding[3]
        print(self.padding)
        horizontal_template = "{0}" + "{1}"*spaces_width + "{0}"
        #Top Border
        if self.show_name:
            template = "{0}{1}{2}" + "{1}"*(spaces_width-len(self.name)-1) + "{0}"
            lines.append(template.format(self.corner,
                                         self.horizontal_border,
                                         self.name))
        else:
            lines.append(horizontal_template.format(self.corner,
                                                    self.horizontal_border))
        #Top padding
        for i in range(self.padding[0]):
            lines.append(horizontal_template.format(self.vertical_border," "))
        #Content
        content_lines = self.content.render().splitlines()
        for i in range(self.inside_height):
            if i < len(content_lines):
                line_template = ("{0}" + "{1}"*self.padding[3] + "{2}" +
                                 "{1}"*(self.inside_width + self.padding[1] - len(content_lines[i])) + "{0}")
                lines.append(line_template.format(self.vertical_border,
                                                  " ",
                                                  content_lines[i]))
            else:
                lines.append(horizontal_template.format(self.vertical_border," "))
        #Bottom padding
        for i in range(self.padding[2]):
            lines.append(horizontal_template.format(self.vertical_border," "))
        #Bottom border
        lines.append(horizontal_template.format(self.corner,
                                                self.horizontal_border))
        return '\n'.join(lines)
