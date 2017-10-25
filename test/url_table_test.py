#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
test url_table class

Authors: zhaoyong(zhaoyong01@baidu.com)
Date:    2017/09/16 20:52
"""

import sys
import unittest

sys.path.append('../')
import url_table


class UrlTableTest(unittest.TestCase):
    """
    url table class test
    """

    def test_insert_url(self):
        """
        test insert url method
        """
        url1 = "http://pycm.baidu.com:8081"

        url_table_obj = url_table.UrlTable()
        url_table_obj.insert_url(url1)
        result = url_table_obj.insert_url(url1)

        assert result is False
