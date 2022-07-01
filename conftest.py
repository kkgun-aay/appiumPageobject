# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
import pytest
from Base.app import App
from Utils.install_apk import installapk


# path = "/Users/lvxs/Desktop/androidapk"
# print("先安装最新release包，然后在启动apk")
# installapk(path)

# driver = None


# @pytest.fixture(scope="session")
# def appstart():
#     global driver
#     print("app只启动一次，后面case公用一个driver")
#     _package = "com.intelcupid.shesay"
#     _activity = "com.intelcupid.shesay.main.PosterActivity"
#     Options = {
#         "platformName": "Android",
#         "appium:appPackage": _package,
#         "appium:appActivity": _activity,
#         "appium:deviceName": "858f8512",
#         "appium:noReset": "true",
#         # "appium:autoGrantPermissions": "true",
#         "newCommandTimeout": "6000",
#         "automationName": "uiautomator2",
#         "appium:noSign": "true"
#     }
#     if driver is None:
#         driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Options)
#         driver.implicitly_wait(6)
#         sleep(3)
#     return driver


@pytest.fixture(scope="session")
def app_start():
    driver = App().app_start()
    return driver


