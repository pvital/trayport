#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_pest_control - unit tests for pest_control tool.
# Copyright (c) 2020 Paulo Vital <pvital@gmail.com>
#

import os
import unittest

import src.pest_control as pc


class TestPestControl(unittest.TestCase):
    '''
    Test Cases for pest_control tool.
    '''

    def setUp(self):
        self.bug_content = pc.read_file('samples/bug.txt')
        self.landscape_content = pc.read_file('samples/landscape.txt')

    def test_search_by_bugs_01(self):
        '''
        Test search_by_bugs() method, using samples provide by Trayport.
        '''
        result = pc.search_by_bugs(self.bug_content, self.landscape_content)
        self.assertEqual(result, 3)

    def test_search_by_bugs_02(self):
        '''
        Test search_by_bugs() method, using landscape with bugs side-by-side
        '''
        self.landscape_content = pc.read_file('samples/landscape_02.txt')
        result = pc.search_by_bugs(self.bug_content, self.landscape_content)
        self.assertEqual(result, 6)

    def test_search_by_bugs_03(self):
        '''
        Test search_by_bugs() method, using landscape with polluted bugs 
        '''
        self.landscape_content = pc.read_file('samples/landscape_03.txt')
        result = pc.search_by_bugs(self.bug_content, self.landscape_content)
        self.assertEqual(result, 3)

    def test_search_by_bugs_04(self):
        '''
        Test search_by_bugs() method, using landscape with vertical bugs
        '''
        self.landscape_content = pc.read_file('samples/landscape_04.txt')
        result = pc.search_by_bugs(self.bug_content, self.landscape_content)
        self.assertEqual(result, 10)

    def test_search_by_bugs_05(self):
        '''
        Test search_by_bugs() method, using landscape with mixed bugs
        '''
        self.landscape_content = pc.read_file('samples/landscape_05.txt')
        result = pc.search_by_bugs(self.bug_content, self.landscape_content)
        self.assertEqual(result, 7)

    def test_search_by_bugs_06(self):
        '''
        Test search_by_bugs() method, using landscape with camouflaged bugs
        '''
        self.landscape_content = pc.read_file('samples/landscape_06.txt')
        result = pc.search_by_bugs(self.bug_content, self.landscape_content)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
