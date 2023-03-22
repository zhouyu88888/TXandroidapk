#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/3/13.

# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import appium
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import os
import sys

sys.path.append(r"D:\devTools\jenkins\workspace\TXAndroidApps-UiAutomationIntegration")
sys.path.append(r"C:\Users\铁行\AppData\Roaming\Python\Python311\site-packages")
sys.path.append(r"C:\Users\铁行\AppData\Local\Programs\Python\Python311\Lib\site-packages")

# For W3C actions
# cmd命令清缓存进app
# 'r' 消除转义符带来的影响,即'\'
retValue = os.popen('adb shell pm clear com.zhsl.air', 'r')
print(retValue)

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "64f2dece"
caps["appium:appPackage"] = "com.zhsl.air"
caps["appium:appActivity"] = "com.woyaou.mode.common.WelcomeActivity"
caps["appium:noReset"] = "true"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 6000
caps["appium:connectHardwareKeyboard"] = True

driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 或者用下面的配置参数
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': '',
    'appPackage': 'com.zhsl.air',
    'appActivity': 'com.woyaou.mode.common.WelcomeActivit',
    'noReset': True
}
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 设置缺省等待时间
driver.implicitly_wait(10)

# 如果有协议弹窗，点击
iknow = driver.find_elemen_by_id()
if iknow:
    iknow.button()

# ID-首次安装/清缓存进入弹窗协议，点击同意
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/tvAgree").click()
sleep(5)

# 点击免押租车tab
driver.tap([(188, 488)])
sleep(5)
# 点击送车上门、芝麻信用免押金
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "送车上门").click()
sleep(1)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "芝麻免押金说明").click()
sleep(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "立即免押租车").click()
sleep(3)
# 点击异地还车按钮
driver.tap([(866, 696), (995, 763)])
sleep(3)

# 点击机票tab
driver.tap([(458, 498)])
sleep(5)
# 点击带儿童、带婴儿、目的地置换
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/ckbChild").click()
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/ckbBaby").click()
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/btn_swapStation").click()
sleep(3)

# 点击火车票tab
driver.tap([(690, 495)])
sleep(5)
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/only_gd_zh").click()
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/only_student_zh").click()
driver.find_element(AppiumBy.ID, "com.zhsl.air:id/btn_swapStation").click()
sleep(3)

# 点击汽车票tab
driver.tap([(915, 501)])
sleep(5)

# 点击客服tab
driver.tap([(535, 1813)])
sleep(5)

# 点击我的tab
driver.tap([(898, 1813)])
sleep(5)
# 点击登录/注册账号
driver.tap([(333, 312)])
sleep(3)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)

# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# 点击立即提现入口
driver.tap([(857, 525)])
sleep(3)
# 点击立即提现按钮
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "立即提现").click()
# 提现弹窗点击确认提现按钮
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "确认提现").click()
sleep(3)
driver.keyevent(4)
# 提现页面返回我的页面
sleep(1)
driver.keyevent(4)

# 我的页面-点击租车订单入口
driver.tap([(150, 729)])
sleep(3)
driver.keyevent(4)
sleep(1)
# 我的页面-点击飞机票订单入口
driver.tap([(398, 736)])
sleep(3)
driver.keyevent(4)
sleep(1)
# 我的页面-点击火车票订单入口
driver.tap([(665, 717)])
sleep(3)
driver.keyevent(4)
sleep(1)
# 我的页面-点击汽车票订单入口
driver.tap([(930, 717)])
sleep(3)
driver.keyevent(4)
sleep(1)

# 我的页面-点击隐私政策
driver.tap([(188, 1017), (997, 1078)])
sleep(3)
driver.keyevent(4)
sleep(1)
# 我的页面-点击建议反馈
driver.tap([(188, 1207), (997, 1268)])
sleep(3)
driver.keyevent(4)
sleep(1)
# 我的页面-点击关于我们
driver.tap([(188, 1397), (997, 1458)])
sleep(3)
driver.keyevent(4)
sleep(1)

# driver.quit()

