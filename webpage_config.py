#!/usr/bin/env python
# -*- coding:utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
配置数据解析模块

Authors: zhaoyong(zhaoyong01@baidu.com)
Date:    2017/08/20 16:15
"""

import ConfigParser

import webpage_exception


class Config(object):
    """
    config file load class

    Attributes:
        _config: ConfigParser object
        _config_file: config file address

    """

    # conf key value dict
    conf_key = {}

    def __init__(self, config_file='spider.conf'):
        """
        init config class
        """
        self._config = ConfigParser.ConfigParser()
        self._config_file = config_file

    def load(self, section='spider'):
        """

        Args:
          section: config file section

        """
        with open(self._config_file, 'r') as f:
            self._config.readfp(f)

        for key, val in self._config.items(section):
            self.conf_key[key] = val

    def get(self, key):
        """

        Args: 
            key: conf file field
        Returns: 
            String if successful
        Raises:
            ConfigException: conf field not find
        """
        if key in self.conf_key:
            return self.conf_key[key]
        raise webpage_exception.ConfigException(u"{0} conf key not find".format(key))
