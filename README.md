# game-new
A set of python scripts to run language benchmarks game easily.

The benchmark code was taken from https://github.com/kragen/shootout

run with

    $ python BenchmarkGame.py

edit BenchmarkGame.py to configure the benchmarks to run

Requirements
------------

requirements beyond python are either for reports and statistics or either
for benchmarks themselves.
You need Texttable (http://foutaise.org/code/texttable/) to print the reports.

Some benchmarks may require special libraries depending on the implementation,
iirc examples are pidigits and meteor for python.


Things to do
------------

- Add computer information to report (min/max/current cpu speed, cpu brand, total/available memory, etc)
- Save results to a json file
- Create a static html file to show results in browser (using some js charts library)