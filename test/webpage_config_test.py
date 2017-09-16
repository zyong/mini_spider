#/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_config_test.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 18:37
"""

import unittest
import sys

sys.path.append("..")
import webpage_config

class ConfigLoadTest(unittest.TestCase):
    """
    test manager class
    """
    def setUp(self):
        self.config = webpage_config.Config('./test.conf')
        self.config.load()

    def test_get(self):
        assert self.config.get('url_list_file') == './urls'
        assert self.config.get('output_directory') == './output'
        assert self.config.get('max_depth') == '1'
        assert self.config.get('crawl_interval') == '1'
        assert self.config.get('crawl_timeout') == '1'
        assert self.config.get('thread_count') == '1'
