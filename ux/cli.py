#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import io, os, sys

import codecs
import gzip
import math

from clint.textui import progress

from ux.io import *

def line_reader(path, label='', width=32, hide=None, every=100, codec='utf-8',
                skip_empty=False):
    if label is None:
        label = path

    input_file = read_file(path)
    counter = CountIO(input_file)
    reader = codecs.iterdecode(counter, codec) \
        if codec is not None else counter

    with progress.Bar(label=label, width=width, hide=hide, every=every,
                      expected_size=counter.line_count) as bar:
        for i, line in enumerate(reader):
            bar.show(i + 1, counter.line_count)

            if skip_empty:
                if line.strip() == '':
                    continue

            yield line

    input_file.close()


def enumerate_progress(lst, label='', width=32, hide=None, every=100, codec='utf-8'):
    total = len(lst)

    with progress.Bar(label=label, width=width, hide=hide, every=every,
                      expected_size=total) as bar:
        for i, item in enumerate(lst):
            bar.show(i + 1, total)
            yield i, item
