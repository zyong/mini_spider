#/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_crawler_test.py.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 18:04
"""

import unittest
import sys

sys.path.append("..")
import webpage_crawler


class MockManager(object):
    """
    mock a test object
    """
    def run(self):
        pass

    def add_new_task(self):
        pass


class CrawlerTest(unittest.TestCase):
    """
    test crawler class
    """

    def setUp(self):
        manager = MockManager()
        self.crawler = webpage_crawler.Crawler(manager, 'testthread')

    def test_downloader(self):
        """

        :return:
        """
        result = self.crawler.downloader("http://www.baidu.com/", 1)
        if result[0] is True:
            assert result[1].find("http://www.baidu.com") != -1
        else:
            assert result[0] is True

if __name__ == "__main__":
    unittest.main()