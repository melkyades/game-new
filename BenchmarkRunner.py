__author__ = 'javier'


import random
import sys

class BenchmarkRunner:

    def __init__(self, benchmarks):
        self.runs = 5
        self.benchmarks = benchmarks

    def run(self):

        results = {}

        #random.shuffle(self.benchmarks)

        for benchmark in self.benchmarks:
            results[benchmark] = []
            benchmark.globalSetUp()

            sys.stdout.write("running %d passes of %s. \n" % (self.runs, benchmark.version)),

            for i in range(self.runs):
                sys.stdout.write("%d... " % i)
                sys.stdout.flush()
                results[benchmark].append(benchmark.run())

            benchmark.globalTearDown()
            sys.stdout.write("\n")
        return results

