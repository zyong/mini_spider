#!/usr/bin/env python
# -*- coding:utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
test webpage_config  class

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 18:37
"""

import os
import sys
import unittest

sys.path.append("../")
import webpage_config


class ConfigLoadTest(unittest.TestCase):
    """
    test manager class
    Attributes:
        config: webpage config object
    """

    def setUp(self):
        """init ConfigLoadTest"""
        abs_path = os.path.dirname(os.path.abspath(__file__))
        test_file_path = abs_path + os.path.sep + 'test.conf'
        self.config = webpage_config.Config(test_file_path)
        self.config.load()

    def test_get(self):
        """
        test get conf field method
        """
        assert self.config.get('url_list_file') == './urls'
        assert self.config.get('output_directory') == './output'
        assert self.config.get('max_depth') == '1'
        assert self.config.get('crawl_interval') == '1'
        assert self.config.get('crawl_timeout') == '1'
        assert self.config.get('thread_count') == '1'
