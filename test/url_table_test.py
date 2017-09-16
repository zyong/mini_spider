#/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
url_table_test.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 20:52
"""

import unittest
import sys

sys.path.append('../')
import url_table


class UrlTableTest(unittest.TestCase):

    def test_insert_url(self):
        url1 = "http://pycm.baidu.com:8081"

        urlTable = url_table.UrlTable()
        urlTable.insert_url(url1)
        result = urlTable.insert_url(url1)

        assert result == False
