# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
import pytest


@pytest.fixture(scope="session")
def appstart():

    print("app只启动一次，后面case公用一个driver")
    _package = "com.intelcupid.shesay"
    _activity = "com.intelcupid.shesay.main.PosterActivity"
    Options = {
        "platformName": "Android",
        "appium:appPackage": _package,
        "appium:appActivity": _activity,
        "appium:deviceName": "858f8512",
        # "appium:noReset": "true",
        "appium:autoGrantPermissions": "true",
        "newCommandTimeout": "6000",
        "automationName": "uiautomator2",
        "appium:noSign": "true"
    }

    app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Options)
    app_driver.implicitly_wait(5)
    return app_driver

#
# @pytest.fixture(scope="session")
# def appquit():
#     print("最后关闭一次app")
#     driver = appstart()
#     yield driver
#     driver.close()


