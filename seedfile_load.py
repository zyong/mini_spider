#!/usr/bin/env python
# -*- coding:utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################

"""
抓取种子加载模块,处理种子数据的load

Authors: zhaoyong(zhaoyong01@baidu.com)
Date:    2017/08/20 16:15
"""


class SeedFileLoad(object):
    """
    加载种子文件提供给网页抓取的初始化
    
    Attributes:
      _seed_file: 种子文件地址

    """

    def __init__(self, seed_file):
        """
        init SeedFileLoad class
        """
        self._seed_file = seed_file

    def get(self):
        """
        获取种子数据
        Returns:
          set集合数据，包含全部url

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
