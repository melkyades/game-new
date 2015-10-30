
import glob
import os.path

from subprocess import call

from BenchmarkReporter import report
from BenchmarkRunner import BenchmarkRunner
from LanguageBenchmark import *
from Implementation import Implementation



#implementations = {'python3': Implementation("python3", "python3", "python3")}
implementations = {'python3': Implementation("ruby", "ruby", "yarv")}

# remember to have dependencies setup:
# mandlebrot numpy
# pydigits gmpy

configurations = {
    #"regexdna":     {"input": "stdin", "values": []},
    "binarytrees":       {"input": "command-line", "values": [9]},
    "chameleons":        {"input": "command-line", "values": [10000]},
    "chameneosredux":    {"input": "command-line", "values": [6000]},
    "fannkuchredux":     {"input": "command-line", "values": [4]},
    "fasta":             {"input": "command-line", "values": [1000]},
    "knucleotide":       {"input": "stdin", "values": [1000]},
    "mandelbrot":        {"input": "command-line", "values": [200]},
    "meteor":            {"input": "command-line", "values": [2098]},
    "nbody":             {"input": "command-line", "values": [10000]}, # 20000, 30000, 40000, 50000]},
    "pidigits":          {"input": "command-line", "values": [27]},
    "regexdna":          {"input": "stdin", "values": [10000]},
    "reversecomplement": {"input": "command-line", "values": [1000]},
    "spectralnorm":      {"input": "command-line", "values": [100]},
    "threadring":        {"input": "command-line", "values": [1000]}


}


class BenchmarkGame:
    def __init__(self):

        self.root_dir   = "."
        self.benchs_dir = self.root_dir + "/bench"
        self.temp_dir   = self.root_dir + "/tmp"

        benchmarks = self.make_benchmarks_fixture()
        assure_dir(self.temp_dir)

        self.generate_input_files()

        self.runner = BenchmarkRunner(benchmarks)

    def benchmarks(self):
        return os.walk(self.benchs_dir).next()[1]

    def make_benchmarks_fixture(self):

        fixture = []
        languages  = [implementations['python3']]

        for language in languages:
            benchmarks = self.make_benchmarks_fixture_for(language)
            fixture.extend(benchmarks)

        return fixture

    def make_benchmarks_fixture_for(self, language):
        benchmarks = []
        for bench_name, options in sorted(configurations.iteritems()):
            for version in self.versions_of(bench_name, language):
                new = [LanguageBenchmark(bench_name, language, version, self, options, value) for value in options["values"]]
                benchmarks.extend(new)

        return benchmarks

    def versions_of(self, bench_name, language):
        return [os.path.basename(path) for path in glob.glob(self.benchs_dir + "/" + bench_name + "/*." + language.extension)]

    def run(self):
        return self.runner.run()

    def start(self):
        results = self.run()
        report(results)

    #for regexdna and knucleotide
    def generate_input_files(self):
        for value in configurations["regexdna"]["values"]:
            out_file = open('%s/regexdna_input_%d.txt' % (self.temp_dir, value), 'w')
            call('python3 %s/fasta/fasta.python3 %d' % (self.benchs_dir, value), stdout=out_file, shell=True)

        for value in configurations["knucleotide"]["values"]:
            out_file = open('%s/knucleotide_input_%d.txt' % (self.temp_dir, value), 'w')
            call('python3 %s/fasta/fasta.python3 %d' % (self.benchs_dir, value), stdout=out_file, shell=True)


    # def checkToolsAreInstalled():
    #
    #    def check(cmd):
    #       try:
    #          with open( nullName, 'w') as df:
    #             call(cmd,stdout=df,stderr=STDOUT)
    #             exes.add(cmd[0])
    #       except OSError, (e,err):
    #          if e == ENOENT: # No such file or directory
    #             if logger: logger.debug('%s program not found', cmd[0])
    #
    #    check([makeExeName])
    #    check([ndiffExeName])
    #    check([cmpExeName])
    #    check([diffExeName])
    #    check([highlightExeName,' -h'])
    #def isexe(exename):
    #   return exename in exes


def assure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == '__main__':
    BenchmarkGame().start()
