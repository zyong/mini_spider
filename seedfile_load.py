#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
抓取种子加载模块,处理种子数据的load

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/08/20 16:15
"""

class SeedFileLoad(object):
    """
    seed load class
    """

    def __init__(self, seed_file):
        self._seed_file = seed_file

    def get(self):
        """
        获取种子数据
        :return:
        """
        url_set = set()
        with open(self._seed_file, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if not line.strip():
                    continue
                url_set.add(line)

        return url_set
