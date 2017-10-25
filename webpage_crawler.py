#!/usr/bin/env python
# -*- coding:utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
数据抓取模块,以多线程的方式抓取每条url，并下发保存处理

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/07/05 22:07
"""

import logging
import requests
import threading
import time

from requests import ReadTimeout
from requests.exceptions import InvalidURL
from requests.exceptions import ConnectionError

import webpage_parser
import webpage_saver


class Crawler(threading.Thread):
    """
    webpage crawler class

    Attributes:
        _manager: web page manager object
        _mutex: thread lock object
      
    """
    PC_UA = "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）"

    MOBILE_UA = "Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) \
AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 \
(compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）"

    def __init__(self, manager, thread_name):
        """
        init crawler class

        Args:
            manager: webpage_manager.Manager 任务管理程序
            thread_name: string 抓取线程名
        """
        self._manager = manager
        self._mutex = threading.Lock()

        super(Crawler, self).__init__(name=thread_name)

    def downloader(self, url, timeout):
        """
        执行实际的抓取操作

        Args:
            url: string
            timeout: int 抓取超时秒
        Returns: 
            返回两个值,(bool, string|int)
            true 抓取成功, 第二个结果为抓取返回的内容
            false 抓取失败, 第二个结果为具体失败的原因

        """
        if (not url.startswith("http://")) and \
                (not url.startswith("https://")):
            url = "http://" + url

        url = url.strip()

        # 默认PC-UA抓取
        headers = {
            "User-Agent": self.PC_UA
        }
        try:
            r = requests.get(url, timeout=timeout, headers=headers)
        except AttributeError as e:
            logging.error("attribute error %s with url".format(e.message, url))
            return False, 1
        except ReadTimeout as e:
            logging.error("read timeout {0}".format(url))
            return False, 2
        except InvalidURL as e:
            logging.error("Invalid url {0}".format(url))
            return False, 3
        except ConnectionError as e:
            logging.error("Connection Error url {0}".format(url))
            return False, 4
        except Exception as e:
            logging.error("other error {0}".format(e.message))
            return False, 99

        if r.status_code == 200:
            return True, r.content
        else:
            return False, r.status_code

    def run(self):
        """
        任务执行线程
        1 从任务队列提取任务
        2 抓取对应url
        3 如果抓取成功分析url内容
        4 写内容到文件
        """

        # 网页解析程序
        page_parser = webpage_parser.Parser()
        page_saver = webpage_saver.Saver(self._manager.get_config())

        timeout = int(self._manager.get_config().get('crawl_timeout'))

        while True:
            self._mutex.acquire()
            task = self._manager.get_task()
            task_url = task[0]
            task_level = task[1]
            self._mutex.release()

            # 过滤url
            if task_url.startswith("//"):
                logging.error(u"url {0} startswith //".format(task_url))
                continue

            logging.info("url:{0},level:{1} start to crawl".format(task_url, task_level))
            result = self.downloader(task_url, timeout)

            # 抓取成功
            if result[0]:
                url_set = page_parser.get_url(task_url, result[1])
                for url in url_set:
                    self._manager.add_new_task(url, int(task_level) + 1)

                # 保存抓取的结果
                page_saver.save(task_url, result[1])
            else:
                logging.error("crawl url %s failed, status code %d" % (task_url, result[1]))

            self._manager.task_done()

            # 抓取间隔设置
            time.sleep(int(self._manager.get_config().get('crawl_interval')))
