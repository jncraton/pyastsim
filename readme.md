pyastsim
========

[![Build Status](https://travis-ci.org/jncraton/pyastsim.svg?branch=master)](https://travis-ci.org/jncraton/pyastsim)
[![PyPI version](https://badge.fury.io/py/pyastsim.svg)](https://badge.fury.io/py/pyastsim)

Calculates the similarity between a batch of source files.

Installation
------------

The program can be installed using pip:

```
pip3 install pyastsim
```

Usage
-----

```
usage: pyastsim [-h] [--threshold THRESHOLD] [--show-diff]
                [--function FUNCTION]
                files [files ...]

Check source files for similarity

positional arguments:
  files                 List of files to compare

optional arguments:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
                        Similarity threshold. Values below this are not
                        reported.
  --show-diff           Show entire diff when reporting results.
  --function FUNCTION   Specific function to compare (Python source only)
```

Examples
--------

Show check for similarity of a group of files using default settings:

```
pyastsim *.py
```

Set a custom threshold to be more or less sensative (default threshold is 80% similarity):

```
pyastsim --threshold 90 *.py
```

Show full diffs when reporting similar files:

```
pyastsim --show-diff *.py
```

Remove all but one function from the AST before performing comparison:

```
pyastsim --function my_func *.py
```

Language Support
----------------

- Python (using internal AST for comparison)
- C/C++ (using GCC assembly output for comparison)

Difference Calculation
----------------------

The difference is calculated by first converting each supplied file to an abstract syntax tree (AST). The AST is then normalized to remove comments, docstrings, and standardize identifier names. We then convert the AST back to Python source code and calculate the Damerau–Levenshtein distance between each pair of source files. We further normalize this number by dividing it by the mean of the number of unicode code points in the files being compared. This gives us a rough percentage similarity between our files. To summarize:

1. Convert to AST
2. Remove comments and docstrings
3. Normalize identifiers
4. Convert back to source
5. Calculate Damerau–Levenshtein distance
6. Covert the edit distance to a percentage
