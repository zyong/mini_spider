#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
webpage_manager.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/08/20 19:24
"""
import Queue

import seedfile_load
import url_table
import webpage_crawler


class Manager(object):
    """
    manager crawler task
    """
    def __init__(self, config):
        self._config = config
        self._crawl_task_queue = Queue.Queue()
        self._crawl_threads = []
        self.url_table = url_table.UrlTable()

    def run(self):
        """
        需要完成的工作
        1 设置抓取任务队列
        2 初始化任务线程
        3 等待任务队列执行结束
        :return:
        """

        # 添加种子链接
        seed_file = seedfile_load.SeedFileLoad(self._config.get('url_list_file'))
        for url in seed_file.get():
            self.add_new_task(url, 0)

        for i in range(0, int(self._config.get('thread_count'))):
            self._crawl_threads.append(webpage_crawler.Crawler(self, str(i)))

        for thread in self._crawl_threads:
            thread.setDaemon(True)
            thread.start()

        self._join()

    def add_new_task(self, url, level):
        # type: (object, object) -> object
        """
        add a new url to queue if url is new

        :param url:  url
        :param level: link depth
        :return:
        """

        # use url_table check whether new url
        if not self.url_table.insert_url(url):
            return False
        max_depth = int(self._config.get('max_depth'))
        if level > max_depth:
            return True
        self._crawl_task_queue.put((url, level))

    def get_task(self):
        """
        get new task
        :return:
        """
        return self._crawl_task_queue.get()

    def task_done(self):
        """
        task done
        :return:
        """
        self._crawl_task_queue.task_done()

    def get_config(self):
        """
        get config object
        :return:
        """
        return self._config

    def _join(self):
        """
        join queue
        :return:
        """
        self._crawl_task_queue.join()
