#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:周宇 time:2023/2/20.

from time import sleep
import appium

# For W3C actions

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

# 车辆选择页/下单页不操作、悬停15mins不操作页面，出价格变化提示弹窗
# Accessibility-点击重新加载，刷新数据
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "重新加载").click()
# sleep(3)
driver.tap([(191, 1175), (886, 1304)])
sleep(5)

# driver.quit()