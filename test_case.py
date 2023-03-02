#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/3/2.

import unittest, time
import os
from plugins import HTMLTestRunner
from plugins.HTMLTestRunner import HTMLTestRunner


class TestDemo(unittest.TestCase):

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")

    def test_03(self):
        print("test_03")

if __name__ == '__main__':
    # 获取路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # 测试报告路径
    report_path = os.path.join(cur_path, 'report')
    # 获取当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestDemo('test_01'))
    suite.addTest(TestDemo('test_02'))
    suite.addTest(TestDemo('test_03'))
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(title='自动化测试报告',
                                          description='用例执行情况：',
                                          stream=open(report_path + '\\' + now + ' HTMLReport.html', 'wb'),
                                          verbosity=2
                                          )

    # 运行测试用例
    runner.run(suite)

