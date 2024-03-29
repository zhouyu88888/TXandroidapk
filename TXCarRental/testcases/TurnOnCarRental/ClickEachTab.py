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

# Accessibility-首页，点击“送车上门”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "送车上门").click()
sleep(3)

# Accessibility-首页，点击“芝麻信用免押金”，落地页点击“立即免押租车”并返回
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "芝麻信用免押金").click()
sleep(3)
# 获取屏幕宽度
width = driver.get_window_size()['width']

# 获取屏幕高度
height = driver.get_window_size()['height']

# 利用 "swipe" 实现滑动, 屏幕从下向上滑动
driver.swipe(width*0.5, height*0.9, width*0.5, height*0.1, 1000)
sleep(1)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "立即免押租车").click()
sleep(1)

# 点击“安心租”
driver.tap([(279, 1443)])
sleep(3)

# 利用 "swipe" 实现滑动, 屏幕从下向上滑动
driver.swipe(width*0.5, height*0.9, width*0.5, height*0.1, 1000)
driver.swipe(width*0.5, height*0.9, width*0.5, height*0.1, 1000)
sleep(1)

driver.tap([(811, 1820)])
sleep(5)

# 点击“企业用车”
# driver.tap([(797, 1285)])
# sleep(5)

# 点击“新手指南”
driver.tap([(751, 1511)])
sleep(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "立即租车").click()
sleep(5)

# 点击底部优惠券tab
driver.tap([(535, 1825)])
sleep(5)

# 点击我的tab
driver.tap([(901, 1812)])
sleep(5)

# driver.quit()
