#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/2/16.

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

# Accessibility-取车城市点击“上海”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "上海").click()

# ID-选择城市页“温馨提示”弹窗，点击“确定”
driver.find_element(AppiumBy.ID, "com.tiexing.carrental:id/btn_right").click()

# ID-获取定位系统弹窗，点击“始终允许”
driver.find_element(AppiumBy.ID, "android:id/button1").click()

# Accessibility-点击当前城市“南京”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "南京").click()

# Accessibility-进选择地址页，点击重新定位
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "重新定位").click()

# Xpath-点击实时定位
driver.find_element(AppiumBy.XPATH, "//android.view.View[contains(@content-desc, '江苏省南京市')]").click()

# Xpath-返回首页，点击时间选择器取车时间(模糊匹配)，进用车时间页
driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '月')]").click()

# 获取设备的宽度
# x = driver.get_window_size()['width']
# 获取设备的长度
# y = driver.get_window_size()['height']
# print(x)
# print(y)

# 屏幕向上滑动, x轴不变，y轴向上移动
# def swipeup(driver, n=1, t=500):
#    L = driver.get_window_size()
#    x1 = L['width'] * 0.83
#    y1 = L['height'] * 0.38
#    y2 = L['height'] * 0.03
#    for i in range(1):
        #driver.swipe(878, 569, 878, 90, 500)

# Accessibility/Xpath-选取日历具体取车/还车日期
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "取车时间").click()
sleep(3)
# 坐标点击日期1
driver.tap([(811, 1209), (863, 1259)])
sleep(5)
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "取车时间").click()
# 坐标点击日期2
driver.tap([(962, 1242), (1014, 1292)])
sleep(5)
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "重置").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "确定时间").click()
sleep(3)
# Accessibility-首页点击立即选车
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "立即选车").click()

# 10秒等待
sleep(10)

# Accessibility-检查页面元素：选择车辆页点击“修改”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "修改").click()
sleep(3)

# 收起修改页
driver.tap([(710, 1132)])
sleep(3)

# Accessibility-检查页面元素：选择车辆页点击“价格低到高”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "价格低到高").click()

# Accessibility-检查页面元素：选择车辆页点击“车型品牌”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "车型品牌").click()

# Accessibility-检查页面元素：选择车辆页点击“租车门店”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "租车门店").click()

# Accessibility-检查页面元素：选择车辆页点击“筛选”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "筛选").click()

# Accessibility-检查页面元素：筛选页签点击“确定”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "确定").click()

# Accessibility-检查页面元素：车辆选择页点击“SUV”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "SUV").click()
sleep(3)

# 车辆列表坐标点击资源1
driver.tap([(1067, 579)])
sleep(3)

# 车辆详情坐标点击资源1
# driver.tap([(992, 712)])
# sleep(3)

# Accessibility-检查页面元素：登录页勾选协议
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_privacy_checkbox").click()
driver.tap([(105, 1561), (156, 1612)])
sleep(3)
# Accessibility-检查页面元素：本机号码一键登录
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.tiexing.carrental:id/shanyan_view_bt_one_key_login").click()
driver.tap([(508, 1390)])
sleep(3)

# 车辆列表坐标点击资源1
driver.tap([(1067, 579)])
sleep(3)

# Accessibility-下单页，用车人信息，点击“添加驾驶员信息”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "添加驾驶员信息").click()
sleep(3)

# 选择驾驶员页，点击选择某一个驾驶员
driver.tap([(57, 514), (111, 708)])
sleep(3)

# 屏幕宽
# width = driver.get_window_size()['width']
# 屏幕高
# height = driver.get_window_size()['heigth']

# 屏幕从下向上滑动
# driver.swipe(width*0.5, height*0.9, width*0.5, height*0.1, 1000)

# 滑动到底部，点击门店政策详情
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "门店政策详情").click()
# driver.keyevent(4)

# 滑动到底部，点击《用车服务协议》
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "《用车服务协议》").click()
# driver.keyevent(4)

# Accessibility-下单页点击“明细”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "明细").click()

# Accessibility-下单页点击“提交订单”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "提交订单").click()
sleep(3)

# Accessibility-选择保险页点击“放弃优惠”
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "放弃优惠").click()

# 等待跳转支付页
sleep(10)

# driver.quit()

