#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pest_control - search a text file for bugs and print the number of occurrence
# Copyright (c) 2020 Paulo Vital <pvital@gmail.com>
#

import argparse
import sys

import Levenshtein


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


def find_bug(bug, landscape, start = 0):
    '''
    Return the lowest index in the landscape string where bug string is found 
    within the slice landscape[start:]. 
    
    This implementation considers if the bug string contains space characters,
    not considering them on the landscape.

    Args:
        bug: string
        landscape: string
        start: int
    
    Returns:
        int
    '''
    pos = -1
    # Having spaces on bug (string to look for), we have to get the position in
    # a different way, so...
    if bug.count(' ') > 0:
        # Having spaces on it, let's use Levenshtein Distance to confirm the
        # hit of our search.
        #
        # First, get the position in the line of the first character of bug
        p_bug = landscape.find(bug[0], start)
        if p_bug >= 0:
            lev = Levenshtein.distance(bug, landscape[p_bug:p_bug+len(bug)])
            if lev <= bug.count(' '):
                # We have a camouflaged bug
                pos = p_bug
    else:
        # Don't have spaces in bug string, so it's easier
        pos = landscape.find(bug, start)
    return pos


def count_bug(bug, line, start = 0):
    '''
    Return the number of occurrences of bug string in the line string.

    Args:
        bug: string     string to search for.
        line: string    string line to search for the bug.
        start: int      position of start slice.
    
    Returns:
        int with the number of occurences found.
    '''
    count = 0

    while start < len(line):
        pos = find_bug(bug, line, start)
        if pos >= 0:
            count += 1
            start = pos + len(bug)
        else:
            break

    return count

def search_by_bugs(bug, landscape):
    '''
    Search a text file content by bugs.

    Args:
        bug: list            pattern of the bug to be searched
        landscape: list     text content to be searched

    Returns:
        int     number of bugs pattern found on text content.
    '''
    printd(f'Searching by bugs...')
    bugs_found = 0

    # Bug size can have several lines
    bug_size = len(bug)
    bug_line = 0

    # Let's find where in landscape, possible bugs be located.
    for line_i, line in enumerate(landscape):
        printd(f'Scanning landscape line {line_i}...')

        # How many possible bugs (p_bug) can we have in this landscape line?
        #
        # For that, we have to set the previous position on line (old_pos)
        # since we can have more than one bug in the same landscape line, but
        # first, we check if the bug[bug_line] has space (blank, \s) on it.
        old_pos = -1
        p_bug = count_bug(bug[bug_line], line, old_pos + 1)

        while p_bug > 0:
            # We have a possible bug here, let's investigate...
            pos = find_bug(bug[bug_line], line, old_pos + 1)
            printd(f'\t Found possible bug at position {pos}')

            # Bug line counter (b_l_count) to check bug_size with findings
            b_l_count = 1

            # Checking if the next lines of bug (bug_j) matches with the next
            # lines of the landscape (next_line) in the same position (pos)
            for bug_j in range(bug_line + 1, bug_size):
                next_line = line_i + bug_j
                if next_line < len(landscape):
                    # Check if the bug[bug_j] in landscape[next_line]
                    r_pos = find_bug(bug[bug_j], landscape[next_line], pos)
                    if r_pos == pos:
                    # if landscape[next_line].find(bug[bug_j][0], pos) == pos:
                        b_l_count += 1

            # If all calculations are equal to the bug_size, we have a bug!
            if b_l_count == bug_size:
                bugs_found += 1
                printd(f'\t >>> Bugs found so far: {bugs_found}')

            # Update control variables
            old_pos = pos + len(bug[bug_line])
            p_bug = count_bug(bug[bug_line], line, old_pos + 1)

    return bugs_found


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

    # Search for the bugs
    bugs_found = search_by_bugs(bug, landscape)
    print(f'Found {bugs_found} bugs in {args.FILE[0]}')


if __name__ == "__main__":
    main()
    sys.exit(0)
