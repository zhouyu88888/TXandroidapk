#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/2/17.

# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import os
import sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("/usr/local/lib/python3.6/site-packages")
import appium
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

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

# 或者用下面的配置参数
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': '',
    'appPackage': 'com.tiexing.carrental',
    'appActivity': 'com.woyaou.weex.newsdk.WeexPageActivity',
    'noReset': True
}
#driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

#设置缺省等待时间
driver.implicitly_wait(10)

#如果有协议弹窗，点击
iknow = driver.find_elemen_by_id()
if iknow:
    iknow.button()

# ID-首次安装/清缓存进入弹窗协议，点击同意
driver.find_element(AppiumBy.ID, "com.woyaou:id/tvAgree").click()
sleep(5)

#driver.quit()

# find_element(by=AppiumBy.ID, value="et_account") , 点击 find_element方法查看源码，by=AppiumBy.ID，value是元素的 id名称
# 搜索完后调用driver.quit()会直接退出app
# input('**********')
# 30秒钟之后退出程序
#time.sleep(30)
#搜索完后不会退出app
# driver.quit()