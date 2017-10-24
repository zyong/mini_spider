#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
test webpage_saver class

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/09/16 20:35
"""
import base64
import os
import sys
import unittest
import urllib

sys.path.append("..")
import webpage_saver


class MockConfig(object):
    """
    mock config class
    """
    def get(self, key):
        """

        Args:
          key: conf field
        Returns:
          return config string
        """
        if key == "target_url":
            return ".*.(htm|html)$"

        if key == "output_directory":
            return "./output"


class SaverTest(unittest.TestCase):
    """
    test save webpage class
    """
    def test_save(self):
        """
        test save file
        """
        config = MockConfig()
        self.saver = webpage_saver.Saver(config)

        content="""
<!DOCTYPE html>
<!-- test the HTML5 tree builder of user agent -->
<title>hello <a href=1/page1_4.html>page1_4</title>
<p><b><a href=1/page1_1.html style='font-style:italic'>page1_1</p>
<a target=_blank href=1/page1_2.html>page1_2<b>
<div style='display:none'><a href=1/page1_3.html>page1_3</div>
"""
        url = "http://pycm.baidu.com:8081/page1.html"
        self.saver.save(url, content)
        file = urllib.quote(url, safe="")
        path = "{0}/{1}".format(config.get('output_directory'), file)
        assert os.path.exists(path) is True

        with open(path, 'r') as f:
            file_content = f.read()
            assert file_content == content
