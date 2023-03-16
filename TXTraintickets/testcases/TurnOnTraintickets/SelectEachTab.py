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

# For W3C actions
# cmd命令清缓存进app
# 'r' 消除转义符带来的影响,即'\'
retValue = os.popen('adb shell pm clear com.tiexing', 'r')
print(retValue)

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "64f2dece"
caps["appium:appPackage"] = "com.tiexing"
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
    'appPackage': 'com.tiexing',
    'appActivity': 'com.woyaou.mode.common.WelcomeActivity',
    'noReset': True
}
#driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 设置缺省等待时间
driver.implicitly_wait(10)

# 如果有协议弹窗，点击
iknow = driver.find_elemen_by_id()
if iknow:
    iknow.button()

# ID-首次安装/清缓存进入弹窗协议，点击同意
driver.find_element(AppiumBy.ID, "com.tiexing:id/tvAgree").click()
sleep(5)
driver.keyevent(4)

# 点击机票tab
driver.tap([(421, 515)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)
# 点击“往返”
driver.find_element(AppiumBy.ID, "com.tiexing:id/tv_two").click()

# 点击租车tab
driver.tap([(670, 495)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)

# 点击汽车票tab
driver.tap([(932, 508)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)

# 点击底部-优惠券tab
driver.tap([(407, 1827)])

# 点击底部-客服tab
driver.tap([(670, 1813)])
sleep(5)

# 点击底部-我的tab
driver.tap([(939, 1824)])
sleep(5)

# driver.quit()
