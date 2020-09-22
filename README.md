# Trayport Technical Challenge - Software Developer

This respository contains a solution for the technical challenge for the role 
of Software Developer at Trayport Vienna.

## The problem – Find the bug

Your program shall search a text file for bugs and print the number of their 
occurrence. The bug is drawn ASCII – style and can be found within bug.txt.

For testing purposes, we provide a text file called landscape.txt. The contents
of this file is a lot simpler than the file that we will be testing the 
completed program. Each occurrence of the character pattern as specified in 
bug.txt is counted, except for the whitespaces contained therein.

## Requirements

The solution uses an external Python module that is necessary to be installed
before it's execution. Follow the next exection steps to setup the environment:

```
$ python3 -m venv .env
$ source .env/bin/activate
(.env) $ pip3 install -r requirements.txt
```

The following sections consider you still are in the virtual environment (venv).

## How to use it

The solution is made as a command line interpreter (CLI) application that 
parse arguments to know the necessary inputs. To execute the application,
provide the path of the file containing the "bug" pattern (BUG_FILE) and the 
path of the file to be analysed (FILE) the the tool.

```
$ python3 src/pest_control.py BUG_FILE FILE
```

The output will be presented in the STDOUT as a string informing how many of
the patterns from the first input argument were found in the second input
argument.

```
$ python3 src/pest_control.py samples/bug.txt samples/landscape.txt
Found 3 bugs in samples/landscape.txt
```

To see all the options available to interact with the tool, execute:

```
$ python3 src/pest_control.py -h
usage: pest_control.py [OPTIONS]... BUG_FILE FILE

Search a text file for bugs and print the number of occurrences

positional arguments:
  BUG_FILE       Path of text file containing the bugs to be searched.
  FILE           Path of text file to search by bugs.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -d, --debug    Print debug messages.
```

## Unittests

Tests to stress the search_by_bugs() methos with different cases of landscapes
were added to this solution:

* test case 01: test bug.txt and landscape.txt provided by Trayport
* test case 02: test bug.txt and landscape_02.txt with bugs in the horizontal line
* test case 03: test bug.txt and landscape_03.txt with bugs in a polluted environment
* test case 04: test bug.txt and landscape_04.txt with bugs in the vertical
* test case 05: test bug.txt and landscape_05.txt with mixed bugs

To execute the test cases, run:

```
$ python3 -m unittest tests/test_pest_control.py
```
