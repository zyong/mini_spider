#/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_saver.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/07/05 22:10
"""
import base64
import os
import urllib
import re

import logging

import sys


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

        filename = base64.urlsafe_b64encode(url)
        path = self._config.get('output_directory')
        real_path = os.path.abspath(path)
        file_path = real_path + os.sep + filename
        if os.path.exists(real_path) is False:
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
