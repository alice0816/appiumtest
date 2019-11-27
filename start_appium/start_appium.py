#!/usr/bin/python3
# -*- coding:utf-8 -*-
from appium import webdriver
import time


def get_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "App": "D:\\alice\\work\\Appium_Text\\imooc7.2.710102001android.apk"
        # "appPackage":"cn.com.open.mooc",
        # "appActivity":"com.imooc.component.imoocmain.splash.MCSplashActivity",
        # "noReset":"true"
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", capabilities)


# 取屏幕的宽高决定
def get_window_size():
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]
    return width, height


# 向左滑动屏幕
def swipe_left():
    x1 = get_window_size()[0] / 10 * 9
    y1 = get_window_size()[1] / 2
    x = get_window_size()[0] / 10
    driver.swipe(x1, y1, x, y1)


# 向右滑动屏幕
def swipe_right():
    x1 = get_window_size()[0] / 10 * 9
    y1 = get_window_size()[1] / 2
    x = get_window_size()[0] / 10
    driver.swipe(x, y1, x1, y1)


# 向上滑动屏幕
def swipe_up():
    x1 = get_window_size()[0] / 2
    y1 = get_window_size()[1] / 10 * 9
    y = get_window_size()[1] / 10
    driver.swipe(x1, y1, x1, y)


# 向下滑动屏幕
def swipe_down():
    x1 = get_window_size()[0] / 2
    y1 = get_window_size()[1] / 10 * 9
    y = get_window_size()[1] / 10
    driver.swipe(x1, y, x1, y1)


def swipe_direction(direction):
    if direction == "left":
        swipe_left()
    elif direction == "up":
        swipe_up()
    elif direction == "down":
        swipe_down()
    else:
        swipe_right()


def go_login():
    print(driver.find_element_by_id("cn.com.open.mooc:id/right_text"))
    driver.find_element_by_id("cn.com.open.mooc:id/right_text").click()


def login():
    driver.find_element_by_id("cn.com.open.mooc:id/accountEdit").send_keys(
        "18566058609"
    )
    driver.find_element_by_id("cn.com.open.mooc:id/passwordEdit").send_keys("537214")
    driver.find_element_by_id("cn.com.open.mooc:id/loginLabel").click()


def go_login_by_class():
    element = driver.find_element_by_class_name("android.widget.TextView")
    print(element)
    elements = driver.find_elements_by_class_name("android.widget.TextView")
    print(len(elements))
    elements[0].click()


def login_by_node():
    element = driver.find_element_by_id("cn.com.open.mooc:id/fl_content")
    elements = element.find_elements_by_class_name("android.widget.EditText")
    elements[0].clear()
    elements[0].send_keys("18566058609")
    elements[1].send_keys("537214")
    driver.find_element_by_id("cn.com.open.mooc:id/loginLabel").click()


def login_by_uiautomator():
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("18566058609")'
    ).clear()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("手机号/邮箱")'
    ).send_keys("18566058609")
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("cn.com.open.mooc:id/passwordEdit")'
    ).send_keys("537214")
    time.sleep(2)
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("cn.com.open.mooc:id/login")'
    ).click()


def login_by_xpath():
    # driver.find_element_by_xpath('//*[contains(@text,18566058609)]').clear()
    # class_text = '//android.widget.EditText[@text="手机号/邮箱"]'
    # driver.find_element_by_xpath(class_text).send_keys('18566058609')
    # driver.find_element_by_xpath('//*[contains(@resource-id,"cn.com.open.mooc:id/passwordEdit")]').send_keys('537214')
    # driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/loginLabel"]').click()

    # 找到父元素，再找父元素的兄弟元素
    class_text2 = '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/loginLabel"]/../preceding-sibling::android.widget.LinearLayout'
    class_text3 = '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/loginLabel"]/../preceding-sibling::android.widget.LinearLayout/android.widget.EditText'
    driver.find_element_by_xpath(class_text2).click()
    driver.find_element_by_xpath(class_text3).clear()
    driver.find_element_by_xpath(class_text3).send_keys("18566058609")
    class_text4 = '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/loginLabel"]/../preceding-sibling::*[@index="4"]'
    class_text5 = '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/loginLabel"]/../preceding-sibling::*[@index="4"]/android.widget.EditText'
    # driver.find_element_by_xpath(class_text4).click()
    driver.find_element_by_xpath(class_text4).send_keys("537214")
    driver.find_element_by_xpath(
        '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/loginLabel"]'
    ).click()


driver = get_driver()
# for i in range(3):
#     swipe_direction("left")
# go_login_by_class()
# time.sleep(3)
login_by_uiautomator()


# driver.d(resourceId='com.google.android.googlequicksearchbox:id/icon').click()
# if not driver.find_element_by_id("com.android.camera2:id/shutter_button").exists(timeout=120):
#     if driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").exists(timeout=10):
# driver.find_element_by_id("com.google.android.googlequicksearchbox:id/icon").click()

# if driver.find_element_by_id("com.android.camera2:id/confirm_button").exists(timeout=10):
# driver.find_element_by_id("com.android.camera2:id/confirm_button").click()
# if driver.find_element_by_id("com.android.camera2:id/confirm_button").exists(timeout=10):
# driver.find_element_by_id("com.android.camera2:id/confirm_button").click()
# driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
