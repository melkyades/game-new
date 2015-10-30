# -*- coding: utf-8 -*-

import time
import sys

__author__ = 'Javier Pimás'


class Benchmark(object):

    def __init__(self, name, implementation, version, paths, options, value):
        self.name           = name
        self.implementation = implementation
        self.version        = version
        self.options        = options
        self.value          = value
        self.paths          = paths

        if sys.platform == "win32":
            # On Windows, the best timer is time.clock()
            self.timer = time.clock
        else:
            # On most other platforms the best timer is time.time()
            self.timer = time.time

    def __repr__(self):
        return self.name + " bench with " + str(self.value)

    def run(self):
        self.setUp()
        result = self.runMeasuring()
        self.tearDown()

        return result

    def runMeasuring(self):

        prev_tick = self.timer()
        self.implementation.run(self)
        elapsed = self.timer() - prev_tick
        return elapsed

    def execute_path(self):
        return self.paths.benchs_dir + "/" + self.name + "/" + self.version

    def input_file_name(self):
        input_file_path = self.paths.temp_dir
        input_file_name = self.name + "_input_" + str(self.value) + ".txt"
        return input_file_path + "/" + input_file_name


    def globalSetUp(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def globalTearDown(self):
        pass

#    def globalSetUp(self):

