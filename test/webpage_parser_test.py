#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
test webpage_parser class

Authors: zhaoyong(zhaoyong01@baidu.com)
Date:    2017/09/16 20:10
"""

import os
import sys
import unittest

sys.path.append("../")
import webpage_parser


class ParserTest(unittest.TestCase):
    """
    test parser web page class
    """

    def test_get_url(self):
        """
        test get url method
        """
        if os.path.exists('test.xhtml') is False:
            print "test.xhtml file not exists"
            return False

        with open('test.xhtml', 'r') as f:
            self.content = f.read()

        parser = webpage_parser.Parser()
        url_set = parser.get_url("http://pycm.baidu.com:8081/", self.content)
        assert "javascript:location.href=\"page4.html" not in url_set
        assert "http://pycm.baidu.com:8081/page1.html" in url_set
        assert "http://pycm.baidu.com:8081/page3.html" in url_set
