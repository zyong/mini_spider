#/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
seedfile_load.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/08/20 16:15
"""

class SeedFileLoad(object):
    """

    """

    def __init__(self, seed_file):
        self._seed_file = seed_file

    def get(self):
        url_set = set()
        with open(self._seed_file, 'r') as f:
            url_set.add(f.readline())

        return url_set