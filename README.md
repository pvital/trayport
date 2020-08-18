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

## How to use it.

The solution is made as a command line interpreter (CLI) application that 
parse arguments to know the necessary inputs. To execute the application,
provide the path of the file containing the "bug" pattern (BUG_FILE) and the 
path of the file to be analysed (FILE) the the tool.

```
$ python3 pest_control.py BUG_FILE FILE
```

To see all the options available to interact with the tool, execute:

```
$ python3 pest_control.py -h
usage: pest_control.py [OPTIONS]... BUG_FILE FILE

Search a text file for bugs and print the number of occurrences

positional arguments:
  BUG_FILE       Path of text file containing the bugs to be searched.
  FILE           Path of text file to search by bugs.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

