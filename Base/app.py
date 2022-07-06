# # # -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
# from Base.base_page import BasePage


class App:
    _package = "com.intelcupid.shesay"
    _activity = "com.intelcupid.shesay.main.PosterActivity"
    driver: webdriver = None

    def app_start(self):

        if self.driver is None:
            Options = {
                "platformName": "Android",
                "appium:appPackage": self._package,
                "appium:appActivity": self._activity,
                "appium:deviceName": "858f8512",
                "appium:noReset": "true",
                # "appium:autoGrantPermissions": "true",
                "newCommandTimeout": "6000",
                "automationName": "uiautomator2",
                "appium:noSign": "true"
            }

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Options)
            self.driver.implicitly_wait(8)

        return self.driver