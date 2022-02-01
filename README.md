# `fixup`: Automatically add and remove python import statements

The goal is that running `fixup my_file.py` will automatically add or remove
import statements to or from `my_file.py`. This project is inspired by
[autoimport](https://github.com/lyz-code/autoimport), with the key difference
that manipulation of source code will be done using abstract syntax trees
instead of regular expressions.

Currently this tool pre-alpha.
