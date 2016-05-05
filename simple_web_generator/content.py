#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Window class"""

import markdown
from bs4 import BeautifulSoup, NavigableString

class Content:

    """Class for various content, content must be inside window"""

    def __init__(self, text):
        text = ''.join([line+'\n' if len(line) else "&nbsp;\n" for line in text.splitlines()])
        self.html = markdown.markdown(text)
        self.plain_text = self._get_plain_text(self.html)

        if self.plain_text:
            self.width = max((len(line) for line in self.plain_text.splitlines()))
            self.height = len(self.plain_text.splitlines())
        else:
            self.width = 0
            self.height = 0

    def _get_html(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        return str(self._strip_tags(soup, ['p']))

    def _get_plain_text(self, text):
        return ''.join(BeautifulSoup(text, 'html.parser').findAll(text=True))

    def _strip_tags(self, soup, invalid_tags):
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()
        return soup

    def render(self):
        return self._get_html(self.html)
