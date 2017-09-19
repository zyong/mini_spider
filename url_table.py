#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
url_table.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/08/20 16:15
"""

import threading


class UrlTable(object):
    """
    保留下载过的链接，提供判断链接是否已经下载过的方法
    线程安全
    """

    def __init__(self):
        self._crawled_url_set = set()
        self._mutex = threading.Lock()

    def insert_url(self, url):
        """
        向集合中添加url，线程安全
        :param url: 需要插入的链接
        :return: False 重复插入，True 非重复插入
        """
        result = True
        self._mutex.acquire()
        if url in self._crawled_url_set:
            result = False
        else:
            self._crawled_url_set.add(url)
        self._mutex.release()
        return result


