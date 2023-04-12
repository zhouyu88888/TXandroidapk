#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/4/13.

import appium
from appium.webdriver.common.appiumby import AppiumBy
import os
from time import sleep
import sys

sys.path.append(r"D:\devTools\jenkins\workspace\TXAndroidApps-UiAutomationIntegration")
sys.path.append(r"C:\Users\铁行\AppData\Roaming\Python\Python311\site-packages")
sys.path.append(r"C:\Users\铁行\AppData\Local\Programs\Python\Python311\Lib\site-packages")

# For W3C actions
# cmd命令清缓存进app
# 'r' 消除转义符带来的影响,即'\'
retValue = os.popen('adb shell pm clear com.woyaou', 'r')
print(retValue)

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "64f2dece"
caps["appium:appPackage"] = "com.woyaou"
caps["appium:appActivity"] = "com.woyaou.mode.common.WelcomeActivity"
caps["appium:noReset"] = "true"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 6000
caps["appium:connectHardwareKeyboard"] = True

driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 设置缺省等待时间
driver.implicitly_wait(10)

# 如果有协议弹窗，点击
iknow = driver.find_elemen_by_id()
if iknow:
    iknow.button()

# ID-首次安装/清缓存进入弹窗协议，点击同意
driver.find_element(AppiumBy.ID, "com.woyaou:id/tvAgree").click()
sleep(7)

# 火车票tab，点击外显日期，进选择日期页
driver.tap([(471, 478)])
sleep(1)
driver.find_element(AppiumBy.ID, "com.woyaou:id/tvDate").click()
sleep(2)
driver.keyevent(4)

# 火车票tab,点击查询
driver.find_element(AppiumBy.ID, "com.woyaou:id/tv_query").click()
sleep(3)

# 火车票列表，点击火车票信息
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '二等座')]").click()
sleep(3)

# 火车票列表，点击火车票信息预订
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '预订')]").click()
sleep(1)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)
# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# 火车票列表，点击火车票信息再次预订
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '预订')]").click()
sleep(1)

# 点击免登录预订
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '免登录预订')]").click()
sleep(1)

# 下单页，点击添加乘客入口
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '添加乘客')]").click()
sleep(1)

# 点击某一个乘客，确定
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '港澳居民')]").click()
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '确定')]").click()
sleep(1)

# 下单页，点击立即预定
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '立即预订')]").click()
sleep(1)
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '我知道了')]").click()
sleep(1)

# driver.quit()
