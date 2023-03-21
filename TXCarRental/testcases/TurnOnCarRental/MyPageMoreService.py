#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/3/22.

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
retValue = os.popen('adb shell pm clear com.tiexing.carrental', 'r')
print(retValue)

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "64f2dece"
caps["appium:appPackage"] = "com.tiexing.carrental"
caps["appium:appActivity"] = "com.woyaou.weex.newsdk.WeexPageActivity"
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
    'appPackage': 'com.tiexing.carrental',
    'appActivity': 'com.woyaou.weex.newsdk.WeexPageActivity',
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
driver.find_element(AppiumBy.ID, "com.tiexing.carrental:id/tvAgree").click()
sleep(8)

# ID-首页点击“我的”
driver.tap([(862, 1788), (937, 1863)])
sleep(3)

# Accessibility-我的页面，点击“登录或注册”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "登录或注册").click()

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)

# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# Accessibility-我的页面，点击“全部订单”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "全部订单").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“待付款”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "待付款").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“已支付”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "已支付").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“已完成”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "已完成").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“待评价”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "待评价").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“建议反馈”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "建议反馈").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“在线客服”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "在线客服").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“隐私政策”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "隐私政策").click()
sleep(1)
driver.keyevent(4)

# Accessibility-我的页面，点击“关于我们”，并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "关于我们").click()
sleep(1)
driver.keyevent(4)

# driver.quit()