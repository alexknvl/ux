#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

from clint.textui import progress

from ux.io import CountIO, read_file


def enumerate_lines_with_progressbar(path, label='', limit=None,
                                     width=32, hide=None, every=100,
                                     codec='utf-8', skip_empty=False):
    if label is None:
        label = path

    input_file = read_file(path)
    counter = CountIO(input_file)
    reader = codecs.iterdecode(counter, codec) \
        if codec is not None else counter

    with progress.Bar(label=label, width=width, hide=hide, every=every,
                      expected_size=counter.line_count) as bar:
        for i, line in enumerate(reader):
            if limit is None:
                cnt = counter.line_count
            else:
                cnt = min(limit, counter.line_count)

            bar.show(i + 1, cnt)

            if skip_empty:
                if line.strip() == '':
                    continue

            yield i, line

    input_file.close()


def enumerate_with_progressbar(lst, label='',
                               width=32, hide=None, every=100,
                               codec='utf-8'):
    total = len(lst)

    with progress.Bar(label=label, width=width, hide=hide, every=every,
                      expected_size=total) as bar:
        for i, item in enumerate(lst):
            bar.show(i + 1, total)
            yield i, item
