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

# 机票tab，点击外显日期，进选择日期页
driver.find_element(AppiumBy.ID, "com.woyaou:id/flightGoDate").click()
sleep(3)

# 选择日期
driver.tap([(536, 1821)])
sleep(3)

# 机票tab,点击查询
driver.find_element(AppiumBy.ID, "com.woyaou:id/btn_query").click()
sleep(3)

# 航班列表，点击航班信息
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '航')]").click()
sleep(3)

# 机票列表，点击机票信息预订-出行优选机票
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '更多')]").click()
sleep(1)
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '立即预订')]").click()
sleep(1)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)
# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# 下单页，点击立即预定，提示“请添加乘机人”
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '立即预订')]").click()
sleep(1)

# 下单页，点击某一乘机人
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '祝一男')]").click()
sleep(1)

# 下单页，点击立即预定
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '立即预订')]").click()
sleep(1)

# driver.quit()
