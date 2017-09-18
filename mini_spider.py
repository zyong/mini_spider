# /usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
"""
mini_spider.py

Authors: zhaoyong (zhaoyong01@baidu.com)
Date:    2017/07/02 17:16

设计思路：
1 链接抓取
2 网页编码转换
3 网页分析 & 新链接发现
4 新连接的入库
5 网页存储

一个Url的抓取就是一个线程，线程处理完成或失败都自动结束当前任务不影响其他逻辑
1 负责抓取和编码解析模块
2 负责链接的解析
3 多线程抓取
4 网页存储为文件
"""
import argparse
import logging
import os

import webpage_config
import webpage_manager

__version__ = 1.0


def create_logger_handler(error_log='test.log'):
    """
    创建logger
    :return:
    """
    # get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create a log handler for writing into file
    fh = logging.FileHandler(error_log)
    fh.setLevel(logging.DEBUG)

    # create a log handler for
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # define handler format
    formatter = logging.Formatter(
        '%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(fh)
    logger.addHandler(ch)


def main():
    """
    主程序
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="version info",
                        action="store_true")
    parser.add_argument("-c", help="config file",
                        default='spider.conf')
    args = parser.parse_args()

    # 默认配置文件
    conf_file = './spider.conf'
    if args.v:
        print "version:{0}".format(__version__)
        return

    if len(args.c) > 0 and os.path.exists(args.c):
        conf_file = args.c

    if not os.path.isfile(conf_file):
        logging.error("conf file not exists {0}".format(conf_file))
        os._exit(1)

    # 任务队列
    try:
        config = webpage_config.Config(conf_file)
        config.load('spider')
    except Exception as e:
        logging.error("load conf failed message {0}".format(e.message))
        os._exit(2)

    try:
        error_log = config.get('error_log')
    except Exception as e:
        logging.error(u"{0}".format(e.message))
        os._exists(3)

    try:
        # 设置日志
        create_logger_handler(error_log)
        logging.info("Starting mini spider")
        manager = webpage_manager.Manager(config)
        manager.run()
    except Exception as e:
        logging.error(u"{0}".format(e.message))
        os._exit(99)


if __name__ == "__main__":
    main()
