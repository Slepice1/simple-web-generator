#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Content class"""

import markdown
from bs4 import BeautifulSoup, NavigableString

class Content:

    """Class for various content, content must be inside window"""

    def __init__(self, text):
        assert isinstance(text, type("a")) # text is string

        text = ''.join([line+'\n' if len(line) else "&nbsp;\n" for line in text.splitlines()])
        self.html = markdown.markdown(text)
        self._plain_text = self._generate_plain_text(self.html)

        if self.plain_text:
            self.width = max((len(line) for line in self.plain_text.splitlines()))
            self.height = len(self.plain_text.splitlines())
        else:
            self.width = 0
            self.height = 0
            
        assert self.height >= 0 # sizes are positive or zero
        assert self.width >= 0

    def _generate_plain_text(self, text):
        return ''.join(BeautifulSoup(text, 'html.parser').findAll(text=True))

    def _get_html(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        return str(self._strip_tags(soup, ['p']))

    def _strip_tags(self, soup, invalid_tags):
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()
        return soup

    @property
    def plain_text(self):
        return self._plain_text

    def render(self):
        return self._get_html(self.html)
