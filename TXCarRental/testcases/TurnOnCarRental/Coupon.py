#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/3/21.

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

# ID-首页点击“优惠券”
driver.tap([(502, 1788), (577, 1863)])
sleep(3)

# ID-优惠券落地页，点击“立即使用”
driver.tap([(796, 403), (988, 462)])
sleep(3)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)

# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# ID-优惠券落地页，继续点击第一个“立即使用”
driver.tap([(796, 403), (988, 462)])
sleep(3)

# driver.quit()