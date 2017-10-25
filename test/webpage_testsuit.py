#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
 webpage test suite, add test case to exec

Authors: zhaoyong(zhaoyong01@baidu.com)
Date:    2017/09/16 20:25
"""

import os
import sys
import unittest

#sys.path.append('./')
file_path = os.path.dirname(os.path.realpath(__file__))
# file_path  = 'test/'
parent_path = os.path.realpath('%s/../' % file_path)
sys.path.insert(0, parent_path)

import test.url_table_test as url_table_test
import test.webpage_config_test as webpage_config_test
import test.webpage_crawler_test as webpage_crawler_test
import test.webpage_parser_test as webpage_parser_test
import test.webpage_saver_test as webpage_saver_test


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(webpage_crawler_test.CrawlerTest("test_downloader"))
    suite.addTest(webpage_parser_test.ParserTest("test_get_url"))
    suite.addTest(webpage_config_test.ConfigLoadTest("test_get"))
    suite.addTest(webpage_saver_test.SaverTest("test_save"))
    suite.addTest(url_table_test.UrlTableTest("test_insert_url"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
