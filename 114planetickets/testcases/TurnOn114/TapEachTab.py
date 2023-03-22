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
    'appPackage': 'com.woyaou',
    'appActivity': 'com.woyaou.mode.common.WelcomeActivity',
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
driver.find_element(AppiumBy.ID, "com.woyaou:id/tvAgree").click()
sleep(5)

# 跳过红包,点击返回键
driver.keyevent(4)
sleep(3)

# 首页机票tab，国内-点击携带儿童、携带婴儿
driver.find_element(AppiumBy.ID, "com.woyaou:id/ckbChild").click()
driver.find_element(AppiumBy.ID, "com.woyaou:id/ckbBaby").click()
sleep(5)

# 首页机票tab，点击国际/港澳台
driver.find_element(AppiumBy.ID, "com.woyaou:id/tvGuojiFlight").click()
sleep(5)

# 点击火车票tab
driver.tap([(400, 380)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)
# 点击学生票、高铁动车
driver.find_element(AppiumBy.ID, "com.woyaou:id/only_student").click()
driver.find_element(AppiumBy.ID, "com.woyaou:id/only_gd").click()
sleep(5)

# 点击汽车票tab
driver.tap([(680, 380)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)

# 点击酒店tab
driver.tap([(939, 367)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)

# 点击底部-目的地tab
driver.tap([(400, 1818)])
# ID-“温馨提示”弹窗，点击“确定”
driver.find_element(AppiumBy.ID, "com.woyaou:id/btn_right").click()
# ID-获取定位系统弹窗，点击“始终允许”
driver.find_element(AppiumBy.ID, "android:id/button1").click()

# ID-点击“去哪儿玩”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "去哪儿玩").click()
sleep(5)

# 点击底部-订单中心tab
driver.tap([(668, 1823)])
sleep(5)
# 订单中心点击飞机票
driver.tap([(72, 389), (198, 446)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击火车票
driver.tap([(342, 389), (468, 446)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击汽车票
driver.tap([(612, 389), (738, 446)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击酒店
driver.tap([(903, 389), (987, 446)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击专车订单
driver.tap([(150, 699), (672, 760)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击租车订单
driver.tap([(150, 850), (996, 911)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击门票订单
driver.tap([(150, 1002), (996, 1063)])
sleep(1)
driver.keyevent(4)
sleep(1)

# 点击“客服”图标
driver.find_element(AppiumBy.ID, "com.woyaou:id/ivKefu").click()
sleep(1)
driver.keyevent(4)
sleep(1)

# 点击底部-我的tab
driver.tap([(945, 1810)])
sleep(5)

# 点击“登录/注册账号”
driver.find_element(AppiumBy.ID, "com.woyaou:id/tv_account").click()
sleep(1)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)

# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# driver.quit()
