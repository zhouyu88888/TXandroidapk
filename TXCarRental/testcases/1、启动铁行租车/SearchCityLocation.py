#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/2/23.

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
import os
from time import sleep

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

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

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

# Accessibility-取车城市点击“上海”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "上海").click()

# ID-选择城市页“温馨提示”弹窗，点击“确定”
driver.find_element(AppiumBy.ID, "com.tiexing.carrental:id/btn_right").click()

# ID-获取定位系统弹窗，点击“始终允许”
driver.find_element(AppiumBy.ID, "android:id/button1").click()

# className-定位搜索框
CLASS_NAME = "android.widget.EditText"
driver.find_element(AppiumBy.CLASS_NAME).click()
sleep(1)

