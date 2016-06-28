#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Window class"""

from simple_web_generator.content import Content

class Window:

    """Basic window class"""

    HORIZONTAL_BORDER = "-";
    VERTICAL_BORDER = "|";
    CORNER = "+";

    def __init__(self, attributes):
        self.id = attributes.get("id")
        self.name = attributes.get("name", self.id)
        self.show_name = attributes.get("show_name", False)
        self.h2_name = attributes.get("h2_name", False)

        self.content = Content(attributes.get("content", ""))

        self._set_border(attributes.get("border", {}))
        self.padding = tuple(int(pad) for pad in attributes.get("padding", "0 0 0 0").split(' '))
        self._set_sizes(attributes.get("width", 2), attributes.get("height", 2)) #must be at least 3

    def _set_border(self, border):
        b = border
        self.top_border = b.get("top", b.get("horizontal", b.get("all", Window.HORIZONTAL_BORDER)))
        self.bottom_border = b.get("bottom", b.get("horizontal", b.get("all", Window.HORIZONTAL_BORDER)))
        self.left_border = b.get("left", b.get("vertical", b.get("all", Window.VERTICAL_BORDER)))
        self.right_border = b.get("right", b.get("vertical", b.get("all", Window.VERTICAL_BORDER)))
        self.corner = b.get("corner", b.get("all", Window.CORNER))

    def _set_sizes(self, width, height):
        horizontal_padding = self.padding[1] + self.padding[3]
        computed_width = self.content.width + horizontal_padding + 2 #border size
        if self.show_name:
            computed_width = max(computed_width, len(self.name) + horizontal_padding + 4) #border size

        self._width = max(int(width), computed_width)
        self.inside_width = self._width - horizontal_padding - 2 #border size

        vertical_padding = self.padding[0] + self.padding[2]
        computed_height = self.content.height + vertical_padding + 2  #border size
        self._height = max(int(height), computed_height)
        self.inside_height = self._height - vertical_padding - 2 #border size

        assert self.inside_height >= 0
        assert self.inside_width >= 0
        assert self._height >= self.inside_height
        assert self._width >= self.inside_width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._set_sizes(width, self._height)

    def render(self):
        lines = []
        spaces_width = self.inside_width + self.padding[1] + self.padding[3]
        horizontal_template = "{0}" + "{1}"*spaces_width + "{2}"
        #Top Border
        if self.show_name:
            template = "{0}{1}{2}" + "{1}"*(spaces_width-len(self.name)-1) + "{0}"
            if self.h2_name:
                name = "<h2>" + self.name + "</h2>"
            else:
                name = self.name
            lines.append(template.format(self.corner,
                                         self.top_border,
                                         name))
        else:
            lines.append(horizontal_template.format(self.corner,
                                                    self.top_border,
                                                    self.corner,))
        #Top padding
        for i in range(self.padding[0]):
            lines.append(horizontal_template.format(self.left_border,
                                                    " ",
                                                    self.right_border))
        #Content
        content_lines = self.content.render().splitlines()
        plain_content_lines = self.content.plain_text.splitlines()
        for i in range(self.inside_height):
            if i < len(content_lines):
                line_template = ("{0}" + "{1}"*self.padding[3] + "{2}" +
                                 "{1}"*(self.inside_width + self.padding[1] - len(plain_content_lines[i])) + "{3}")
                lines.append(line_template.format(self.left_border,
                                                  " ",
                                                  content_lines[i],
                                                  self.right_border))
            else:
                lines.append(horizontal_template.format(self.left_border,
                                                        " ",
                                                        self.right_border))
        #Bottom padding
        for i in range(self.padding[2]):
            lines.append(horizontal_template.format(self.left_border,
                                                    " ",
                                                    self.right_border))
        #Bottom border
        lines.append(horizontal_template.format(self.corner,
                                                self.bottom_border,
                                                self.corner))
        return '\n'.join(lines)
