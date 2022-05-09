# # -*- coding: utf-8 -*-
# from time import sleep
# from appium import webdriver
#
#
# class App:
#     _app_driver = None
#     _package = "com.intelcupid.shesay"
#     _activity = "com.intelcupid.shesay.main.PosterActivity"
#
#     @classmethod
#     def appstart(cls):
#         if cls._app_driver is None:
#             Options = {
#                 "platformName": "Android",
#                 "appium:appPackage": cls._package,
#                 "appium:appActivity": cls._activity,
#                 "appium:deviceName": "858f8512",
#                 "appium:noReset": "true",
#                 "appium:autoGrantPermissions": "true",
#                 "newCommandTimeout": "6000",
#                 "automationName": "uiautomator2",
#                 "appium:noSign": "true"
#             }
#
#             cls._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", Options)
#             cls._driver.implicitly_wait(5)
#         return cls._driver
#
#     @classmethod
#     def appclose(cls):
#         sleep(5)
#         cls._driver.quit()
