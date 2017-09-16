# /usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_config.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/08/20 16:15
"""

import ConfigParser
import logging

import webpage_exception


class Config(object):
    """
    config file load class
    """

    # conf key value dict
    conf_key = {}

    def __init__(self, config_file='spider.conf'):
        """
         :param file string 配置文件名
         :return: None
        """
        self._config = ConfigParser.ConfigParser()
        self._config_file = config_file

    def load(self, section='spider'):
        """

        :param section: config file section
        :return: None
        """
        with open(self._config_file, 'r') as f:
            self._config.readfp(f)

        for key, val in self._config.items(section):
            self.conf_key[key] = val

    def get(self, key):
        """

        :param key: conf file field
        :return: String |Exception
        """
        if key in self.conf_key:
            return self.conf_key[key]
        raise webpage_exception.ConfigException(u"{0} conf key not find".format(key))