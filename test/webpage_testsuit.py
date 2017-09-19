#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_testsuit.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 20:25
"""

import unittest
import sys

sys.path.append('..')
import webpage_config_test
import webpage_crawler_test
import webpage_parser_test
import webpage_saver_test
import url_table_test


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(webpage_crawler_test.CrawlerTest("test_downloader"))
    suite.addTest(webpage_parser_test.ParserTest("test_get_url"))
    suite.addTest(webpage_config_test.ConfigLoadTest("test_get"))
    suite.addTest(webpage_saver_test.SaverTest("test_save"))
    suite.addTest(url_table_test.UrlTableTest("test_insert_url"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)