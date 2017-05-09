#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys, time

from ux.profiling import profile_stage
from ux.cli import line_reader
from ux.io import (estimate_compression_ratio, estimate_file_size,
                   estimate_line_length, estimate_line_count, read_file)

def main(path):
    with profile_stage('Doing something'):
        a = list(range(100000))
        time.sleep(3)

    with profile_stage('doing stuff', detailed=True):
        with read_file(path) as f:
            print('Compression ratio: %s', estimate_compression_ratio(f))
            print('File size        : %s', estimate_file_size(f))
            print('Line length      : %s', estimate_line_length(f, max_error=0.1, probability=0.9))
            print('Line count       : %s', estimate_line_count(f, max_error=0.1, probability=0.9))
            print()
            print('Reading the file... Press Ctrl-C to interrupt.')
        for line in line_reader(path):
            pass

if __name__ == '__main__':
    main(sys.argv[1])
