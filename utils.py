# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@IDE--Env : PyCharm--
@Project  :  ChatGPT_api
@File     :  utils.py
@Time     :  2023/2/10 17:31
@Author   :  gpc
@Contact  :  phone@163.com
@License  :  (C)Copyright 2021
@Desc     :  None
"""


class Logger(object):

    def __init__(self, filename, is_write=True, is_print=True):
        self.file = open(filename, 'a+', encoding="utf8")
        self.is_write = is_write
        self.is_print = is_print

    def __call__(self, log_text):
        # 记录日志信息
        # log_text = current_time() + "\t" + log_text
        if self.is_print:
            print(log_text)
        if self.is_write:
            self.file.write(log_text + "\n")
            self.file.flush()