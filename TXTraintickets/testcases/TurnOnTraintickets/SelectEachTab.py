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
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 设置缺省等待时间
driver.implicitly_wait(10)

# 如果有协议弹窗，点击
iknow = driver.find_elemen_by_id()
if iknow:
    iknow.button()

# ID-首次安装/清缓存进入弹窗协议，点击同意
driver.find_element(AppiumBy.ID, "com.tiexing:id/tvAgree").click()
sleep(10)

# 首页，火车票tab点击学生票、高铁动车、目的地置换
driver.keyevent(4)
driver.find_element(AppiumBy.ID, "com.tiexing:id/only_student").click()
driver.find_element(AppiumBy.ID, "com.tiexing:id/only_gd").click()
driver.find_element(AppiumBy.ID, "com.tiexing:id/btn_swapStation").click()
sleep(3)

# 点击机票tab
driver.tap([(421, 515)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)
# 点击目的地置换
driver.find_element(AppiumBy.ID, "com.tiexing:id/btn_swapStation").click()
sleep(3)
# 点击“往返”
driver.find_element(AppiumBy.ID, "com.tiexing:id/tv_two").click()
sleep(1)
# 点击携带儿童、携带婴儿
driver.find_element(AppiumBy.ID, "com.tiexing:id/ckbChild").click()
driver.find_element(AppiumBy.ID, "com.tiexing:id/ckbBaby").click()
sleep(1)

# 点击租车tab
driver.tap([(670, 495)])
sleep(5)
# 跳过优惠券
driver.keyevent(4)
sleep(5)
# 点击送车上门、芝麻信用免押金
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "送车上门").click()
sleep(1)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "芝麻信用免押金").click()
sleep(1)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "立即免押租车").click()
sleep(1)
# 点击异地还车按钮
driver.tap([(855, 910), (984, 977)])
sleep(3)

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
# 点击登录/注册账号
driver.tap([(335, 290)])
sleep(3)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)

# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# 点击我的钱包-钱包
driver.tap([(213, 633)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的钱包-积分
driver.tap([(539, 618)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的钱包-红包
driver.tap([(876, 651)])
sleep(1)
driver.keyevent(4)
sleep(1)

# 点击我的订单-飞机票
driver.tap([(104, 903), (209, 1008)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的订单-火车票
driver.tap([(359, 903), (464, 1008)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的订单-汽车票
driver.tap([(613, 1011), (721, 1060)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的订单-酒店
driver.tap([(886, 1011), (958, 1060)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的订单-专车
driver.tap([(121, 1228), (193, 1277)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的订单-租车
driver.tap([(376, 1228), (448, 1277)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击我的订单-门票
driver.tap([(631, 1228), (703, 1277)])
sleep(1)
driver.keyevent(4)
sleep(1)

# 点击更多服务-在线客服
driver.tap([(85, 1551), (229, 1600)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击更多服务-产品建议
driver.tap([(340, 1551), (484, 1600)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击更多服务-企业差旅
driver.tap([(595, 1551), (739, 1600)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击更多服务-推荐有奖
driver.tap([(827, 1551), (971, 1600)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击更多服务-关于我们
driver.tap([(85, 1746), (229, 1770)])
sleep(1)
driver.keyevent(4)
sleep(1)
# 点击更多服务-点评收藏
driver.tap([(340, 1746), (484, 1770)])
sleep(1)
driver.keyevent(4)
sleep(1)

# driver.quit()
