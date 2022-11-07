![PyPI](https://img.shields.io/pypi/v/pyreptasks)
[![CI](https://github.com/tsenovilla/pyreptasks/actions/workflows/ci.yaml/badge.svg)](https://github.com/tsenovilla/pyreptasks/actions/workflows/ci.yaml)
[![pre-commit](https://github.com/tsenovilla/pyreptasks/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/tsenovilla/pyreptasks/actions/workflows/pre-commit.yaml)
![Codecov](https://img.shields.io/codecov/c/gh/tsenovilla/pyreptasks)


Description
===========

This Python library provides the user with some tools useful to automate coding of repetitive tasks.

Installation and usage
======================

To install this package use : pip install pyreptasks

To import all the classes and methods of the package in your Python projects: from pyreptasks import *

Developing
==========

To ensure that you have all the needed dependencies installed in your local environment, install the requirements:

% pip install -r requirements.txt

This project uses "black" to format code. We support "pre-commit" to ensure this formatting has been run. If you have installed the requirements, you should have these packages already installed. Please, set up the commit hooks in your local environment:

% pre-commit install

Testing
=======

This project uses "pytest" to run the tests defined in the folder "tests". 

To run the tests, install the test dependencies (this includes pytest, if you do not have it yet):

% pip install -r requirements_test.txt

To run all the tests, go to the repository where you have stored the folder "tests" and run:

% pytest

   === 10 passed in 0.03s ===

In the case that you would like to run only a specific test, select it with pytest:

% pytest tests/test_switch.py

Versions log
============

Version 1.0.0
-------------

- New module switch.py: Contains the class Switch, allowing the user to skip defining a switch structure.


Other
=====

Author: Tomás Senovilla Polo

Email : tspscgs@gmail.com

License: pyreptasks is available under the MIT license. See LICENSE.txt for more information.
