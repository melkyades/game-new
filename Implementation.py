from subprocess import call # to launch benchs with their language implementations
import os


class Implementation(object):
    def __init__(self, name, executable, extension):
        self.name = name
        self.executable = executable
        self.extension = extension

    def __repr__(self):
        return self.name + " impl"

    def run(self, benchmark):
        params = benchmark.options
        #print (self.executable + " " + benchmark.execute_path() + " " + str(benchmark.value))
        output = open(os.devnull, 'w')
        if params["input"] == "stdin":
            input_file = open(benchmark.input_file_name())
            call(self.executable + " " + benchmark.execute_path(), stdin=input_file, stdout=output, shell=True)
        else:
            call(self.executable + " " + benchmark.execute_path() + " " + str(benchmark.value), stdout=output, shell=True)



__author__ = 'javier'
