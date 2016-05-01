#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

import argparse
import sys

import click
import yaml

@click.command()
@click.argument('input', type=click.File('r'))
def main():
    click.echo("lol xd")

if __name__ == '__main__':
    main()
