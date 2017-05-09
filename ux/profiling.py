#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import io, os, sys

import cProfile
import resource
import pstats

import easytime

class profile_stage(object):
    def __init__(self, name, detailed=False):
        self.name = name
        self.detailed = detailed

    def report(self, message):
        print("PROFILE[%s]: %s" % (message, self.name), file=sys.stderr)

    @property
    def memusage(self):
        usage = resource.getrusage(resource.RUSAGE_SELF)
        return usage[2] * resource.getpagesize() / 1024.0 / 1024.0

    def __enter__(self):
        self.start = easytime.now()
        self.start_memory = self.memusage

        if self.detailed:
            self.profiler = cProfile.Profile()
            self.profiler.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_memory = self.memusage

        self.end = easytime.now()
        duration = int(self.end - self.start)

        seconds = duration % 60
        duration = (duration - seconds) // 60
        minutes = duration % 60
        hours = (duration - minutes) // 60

        if hours != 0:
            time_str = '%sh%sm%ss' %\
                (hours, minutes, seconds)
        elif minutes != 0:
            time_str = '%sm%ss' %\
                (minutes, seconds)
        else:
            time_str = '%.2fs' % (self.end - self.start,)

        self.report("%s %.2fMB(%+.2fMB)" %
                    (time_str, self.end_memory,
                     self.end_memory - self.start_memory))

        if self.detailed:
            self.profiler.disable()
            s = io.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(self.profiler, stream=s).sort_stats(sortby)
            ps.print_stats()
            self.report(s.getvalue())
            self.profiler = None
