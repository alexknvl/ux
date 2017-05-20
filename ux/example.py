#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys, time

from ux.profiling import profile_stage
from ux.cli import enumerate_with_progressbar, enumerate_lines_with_progressbar
from ux.io import (estimate_compression_ratio, estimate_file_size,
                   estimate_line_length, estimate_line_count, read_file)


def main(path):
    with profile_stage('Doing something'):
        a = list(range(100000))
        time.sleep(1)

    with profile_stage('doing stuff', detailed=True):
        with read_file(path) as f:
            print('Compression ratio: %.2f' % estimate_compression_ratio(f))
            print('File size        : %s'   % estimate_file_size(f))
            print('Line length      : %.1f' % estimate_line_length(f))
            print('Line count       : %.1f' % estimate_line_count(f))
            print()
            print('Reading the file... Press Ctrl-C to interrupt.')
        for line in enumerate_lines_with_progressbar(path):
            pass

        for i, line in enumerate_with_progressbar(range(1000000)):
            pass

if __name__ == '__main__':
    main(sys.argv[1])
