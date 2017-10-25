#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
test webpage_crawler

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 18:04
"""

import sys
import unittest

sys.path.append("..")
import webpage_crawler


class MockManager(object):
    """
    mock a test object
    """

    def run(self):
        """
        mock run method
        """
        pass

    def add_new_task(self):
        """
        mock add method
        """
        pass


class CrawlerTest(unittest.TestCase):
    """
    test crawler class
    Attributes:
        crawler: Crawler object
    """

    def setUp(self):
        manager = MockManager()
        self.crawler = webpage_crawler.Crawler(manager, 'testthread')

    def test_downloader(self):
        """
        test downloader method
        """
        result = self.crawler.downloader("http://www.baidu.com/", 1)
        if result[0] is True:
            assert result[1].find("http://www.baidu.com") != -1
        else:
            assert result[1] > 0


if __name__ == "__main__":
    unittest.main()
