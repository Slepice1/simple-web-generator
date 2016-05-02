#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Window class"""

class Window:

    DEFAULT_HORIZONTAL_BORDER = "-";
    DEFAULT_VERTICAL_BORDER = "|";
    DEFAULT_CORNER = "+";

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get("name", self.id)
        self.show_name = kwargs.get("show_name", False)

    def render(self):
        pass
