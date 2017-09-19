#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_parser.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/07/05 22:09
"""
import logging
from bs4 import BeautifulSoup
import urlparse


class Parser(object):
    """
    parse page content, and get url from content
    """

    def get_url(self, source_url, document):
        """
        获取所有页面的url
        :param source_url:string
        :param document:string
        :return:set
        """
        _url_set = set()

        try:
            soup = BeautifulSoup(document, 'html.parser')
        except Exception as e:
            logging.error("{0} page parser failed".format(source_url))
            return _url_set

        for link in soup.find_all('a'):
            _link = link.get('href')
            if not _link or _link == '#':
                continue
            parser = urlparse.urlparse(_link)
            if parser.hostname:
                if parser.scheme is None or not parser.scheme:
                    parser_source = urlparse.urlparse(source_url)
                    _link = u"{0}:{1}".format(parser_source.scheme, _link)
                _url_set.add(_link)
            else:
                return_url = self._add_http_header(source_url, _link)
                if return_url is not False:
                    _url_set.add(return_url)
        return _url_set

    @staticmethod
    def _add_http_header(source_url, new_link):
        """
        提取完整url，几种情况
        1 当前站点的url
            . url绝对地址
            . url相对地址
        :param source_url: source url
        :param new_link:
        :return:
        """
        parser = urlparse.urlparse(source_url)
        port = parser.port
        hostname = parser.hostname
        protocol = parser.scheme
        if new_link.startswith(u'http'):
            return new_link
        else:
            if new_link.startswith(u"javascript:"):
                return False

            if new_link.startswith(u"//"):
                return u"{0}:{1}".format(protocol, new_link)
            else:
                if port != 80 and port is not None:
                    new_link = u"{0}://{1}:{2}/{3}".format(protocol, hostname, port, new_link)
                else:
                    new_link = u"{0}://{1}/{2}".format(protocol, hostname, new_link)
                return new_link
