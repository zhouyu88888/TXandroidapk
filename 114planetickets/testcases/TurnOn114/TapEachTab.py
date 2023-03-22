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
sleep(3)

# 首页机票tab，国内-点击往返
driver.find_element(AppiumBy.ID, "com.woyaou:id/tv_two").click()
sleep(3)
# 首页机票tab，国内-点击单程
driver.find_element(AppiumBy.ID, "com.woyaou:id/tv_one").click()
sleep(3)
# 点击置换往返地
driver.find_element(AppiumBy.ID, "com.woyaou:id/btn_swapStation").click()
sleep(3)

# 点击火车票tab
driver.tap([(471, 478)])
sleep(3)
# 跳过优惠券
driver.keyevent(4)
sleep(3)
# 点击学生票、高铁动车
driver.find_element(AppiumBy.ID, "com.woyaou:id/only_student").click()
driver.find_element(AppiumBy.ID, "com.woyaou:id/only_gd").click()
sleep(3)
# 点击置换往返地
driver.find_element(AppiumBy.ID, "com.woyaou:id/btn_swapStation").click()
sleep(3)

# 点击汽车票tab
driver.tap([(691, 483)])
sleep(3)
# 跳过优惠券
driver.keyevent(4)
sleep(3)
# 点击置换往返地
driver.find_element(AppiumBy.ID, "com.woyaou:id/btn_swapStation").click()
sleep(3)

# 点击租车tab
driver.tap([(928, 476)])
sleep(3)
# 跳过优惠券
driver.keyevent(4)
sleep(3)
# 点击异地还车
driver.tap([(866, 696), (995, 763)])
sleep(3)
# 点击送车上门
driver.tap([(954, 1340), (994, 1380)])
sleep(3)

# 点击底部-优惠券tab
driver.tap([(367, 1788), (442, 1863)])
sleep(3)
# 点击火车票
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "火车票").click()
sleep(1)
# 点击汽车票
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "汽车票").click()
sleep(1)
# 点击租车
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "租车").click()
sleep(1)
# 点击酒店/景点
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "酒店/景点").click()
sleep(1)

# 点击底部-订单中心tab
driver.tap([(668, 1823)])
sleep(3)
# 订单中心点击飞机票
driver.tap([(116, 499), (221, 604)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击火车票
driver.tap([(363, 499), (468, 604)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击汽车票
driver.tap([(610, 499), (715, 604)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击租车
driver.tap([(858, 499), (963, 604)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击酒店民宿
driver.tap([(252, 840), (444, 905)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击景点门票
driver.tap([(252, 1052), (444, 1117)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击专车
driver.tap([(252, 1264), (348, 1329)])
sleep(1)
driver.keyevent(4)
sleep(1)

# 点击底部-我的tab
driver.tap([(945, 1810)])
sleep(3)

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

# 我的tab，点击在线客服
driver.tap([(237, 1003)])
sleep(1)
driver.keyevent(4)

# 我的tab，点击建议反馈
driver.tap([(232, 1192)])
sleep(1)
driver.keyevent(4)

# 我的tab，点击企业差旅
driver.tap([(290, 1392)])
sleep(1)
driver.keyevent(4)

# 我的tab，点击关于我们
driver.tap([(171, 1584)])
sleep(1)
driver.keyevent(4)

# driver.quit()

