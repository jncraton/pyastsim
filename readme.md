pyastsim
========

Calculates the similarity between a batch of Python files.

Difference Calculation
----------------------

The difference is calculated by first converting each supplied file to an abstract syntax tree (AST). The AST is then normalized to remove comments, docstrings, and standardize identifier names. We then convert the AST back to Python source code and calculate the Damerau–Levenshtein distance between each pair of source files. We further normalize this number by dividing it by the mean of the number of unicode code points in the files being compared. This gives us a rough percentage similarity between our files. To summarize:

1. Convert to AST
2. Remove comments and docstrings
3. Normalize identifiers
4. Convert back to source
5. Calculate Damerau–Levenshtein distance
6. Covert the edit distance to a percentage