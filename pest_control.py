#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pest_control - search a text file for bugs and print the number of occurrence
# Copyright (c) 2020 Paulo Vital <pvital@gmail.com>
#

import argparse
import sys


DEBUG = False


def printd(content):
    '''
    Prints DEBUG messages with given content.

    Args:
        content: str   string to print as DEBUG message

    Returns:
        None
    '''
    if DEBUG:
        print(f'---> \033[1;33;40mDEBUG\033[m - {content}')


def init_argparse():
    '''
    Initialize the argument parsing.

    Returns:
        argparse.ArgumentParser
    '''
    parser = argparse.ArgumentParser(
        prog='pest_control.py',
        usage='%(prog)s [OPTIONS]... BUG_FILE FILE',
        description='Search a text file for bugs and print the number of occurrences'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'{parser.prog} version 0.1'
    )

    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Print debug messages.'
    )

    parser.add_argument(
        'BUG_FILE',
        nargs='+',
        help='Path of text file containing the bugs to be searched.'
    )
    parser.add_argument(
        'FILE',
        nargs='+',
        help='Path of text file to search by bugs.'
    )

    return parser


def read_file(file):
    '''
    Read a give file and returns a list with it's lines content.

    Args:
        file: str   path of the file to be read

    Returns:
        list containing the lines of file
    '''
    file_content = []

    printd(f'Reading input file: {file}')
    with open(file) as f:
        for line in f:
            file_content.append(line.rstrip())

    return file_content


def main():
    '''
    Main function.
    '''
    global DEBUG

    # Parse the arguments
    parser = init_argparse()
    args = parser.parse_args()

    # Set DEBUG variable
    if args.debug:
        DEBUG = True

    # Read the input files
    try:
        bug = read_file(args.BUG_FILE[0])
        printd(f'Bug type loaded.')
        landscape = read_file(args.FILE[0])
        printd(f'Landscape loaded.')
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        print(f'{parser.prog}: {err.filename} - {err.strerror}')
        return sys.exit(err.errno)


if __name__ == "__main__":
    main()
    sys.exit(0)
