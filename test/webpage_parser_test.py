#/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_parser_test.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 20:10
"""

import unittest
import sys
import os

sys.path.append("..")
import webpage_parser


class ParserTest(unittest.TestCase):
    """
    test parser web page class
    """
    def test_get_url(self):
        """
        test get url method
        :return:
        """
        if os.path.exists('./test.html') is False:
            return False

        with open('./test.html', 'r') as f:
            self.content = f.read()
        parser = webpage_parser.Parser()
        url_set = parser.get_url("http://pycm.baidu.com:8081/", self.content)
        assert "http://pycm.baidu.com:8081/page1.html" in url_set
        assert "http://pycm.baidu.com:8081/page3.html" in url_set
