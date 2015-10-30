
import texttable as tt
from math import sqrt
from scipy import stats

__author__ = 'javier'


def report(results):
    tab = tt.Texttable()
    tab.header(['Benchmark', 'Input', 'Average', 'std dev %', 'std dev', 'runs', 'discarded'])

    tab.set_cols_align(['r','r', 'r','r', 'r', 'r', 'r'])
    tab.set_deco(tab.HEADER | tab.VLINES)

    for benchmark, measures in sorted(results.items()):
        reportBenchmark(tab, benchmark, measures)

    table = tab.draw()
    print (table)

def reportBenchmark(tab, benchmark, measures):

    trimmed = stats.trimboth(sorted(measures), 0.1)
    runs = len(trimmed)
    average = sum(trimmed) / runs
    stddev  = sqrt(sum([(measure - average)**2 for measure in trimmed]))
    stddev_relative = stddev / average * 100
    tab.add_row([benchmark.version, benchmark.value, average, "%2.2f %%" % stddev_relative, stddev, len(measures), len(measures) - runs])

    tab.set_cols_width([35, 10, 10, 10, 10, 10, 10])
