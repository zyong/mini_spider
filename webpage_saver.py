#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
网页内容保存模块，通过读取配置文件数据保存结果到磁盘

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/07/05 22:10
"""

import logging
import os
import re
import sys
import urllib


class Saver(object):
    """
    save web page content
    """

    def __init__(self, config):
        """

        :param config:
        """
        self._config = config
        target_url_pattern = self._config.get('target_url')
        self._pattern = re.compile(target_url_pattern)

    def save(self, url, document):
        """
        将网页保存到文件
        :param url: string
        :param document: string
        :return:
        """
        # check url whether match pattern
        if self._pattern.match(url) is None:
            return False

        filename = urllib.quote(url, safe="")
        path = self._config.get('output_directory')
        real_path = os.path.abspath(path)
        file_path = real_path + os.sep + filename
        if not os.path.exists(real_path):
            os.makedirs(real_path)

        try:
            with open(file_path, 'w') as f:
                f.write(document)
                return True
        except IOError as e:
            logging.error("I/O error({0}): {1}".format(e.errno, e.strerror))
        except Exception as e:
            logging.error('other error {0}'.format(sys.exc_info()[0]))

        return False
