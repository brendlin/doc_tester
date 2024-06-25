Doc Tester
========

This repository is a testbed for documentation with Sphinx.

Progression of commands
========

 - Installed sphinx using git
 - run
```
mkdir doc
cd doc
sphinx-quickstart # "no" to question "separate source and build directories?"
```
This will make the following files:
 - Makefile
 - _build
 - _static
 - _templates
 - conf.py
 - index.rst
 - make.bat

Then:
 - run `sphinx-build -M html . _build`
