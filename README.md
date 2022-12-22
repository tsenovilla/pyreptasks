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

You may find examples of usage in the folder "examples".

Developing
==========

If you want to contribute, to ensure that you have all the needed dependencies installed in your local environment, install the requirements described in requirements.txt. To do so, you can download the file or just copy it into a "requirements.txt" file then do

% pip install -r requirements.txt

This project uses "black" to format code. We support "pre-commit" to ensure this formatting has been run. If you have installed the requirements, you should have these packages already installed.

"Codecov" is set up for this project, so for any push or pull request you may check the code coverage report at https://app.codecov.io/gh/tsenovilla/pyreptasks. 

Testing
=======

This project uses "pytest" to run the tests defined in the folder "tests". 

To run the tests localy, install the test requirements described in tests_requirements.txt. To do so, you can download the file or just copy it into a "tests_requirements.txt" then do

% pip install -r test_requirements.txt

To run all the tests, go to the repository where you have stored the folder "tests" and run:

% pytest

In the case that you would like to run only a specific test, select it with pytest:

% pytest tests/test_switch.py

Versions log
============

Version 1.0.0
-------------

- New module switch.py: Contains the class Switch, allowing the user to skip defining a switch structure.

Version 2.0.1
-------------

- Update of module switch.py: From this version, integer_switch is not a parameter anymore. This parameter was used in 
  a Switch object to indicate that the switch had to contain only integer keys. The parameter is deleted due to its
  functionality was not actually relevant. 

- Switch examples and tests updates to fit with the new version.

- Minor changes: Use of setuptools_scm (https://github.com/pypa/setuptools_scm/) package to manage version control instead of versioneer, used in the previous version. This also allows us to get rid of some configuration files in order to get a simpler package. 

NOTE: The use of version name 2.0.1 instead of 2.0.0 is due to setuptools_scm needs a non-zero last number.

Other
=====

Author: Tomás Senovilla Polo

Email : tspscgs@gmail.com

License: pyreptasks is available under the MIT license. See LICENSE.txt for more information.
