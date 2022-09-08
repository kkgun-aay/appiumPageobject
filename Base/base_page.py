# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver

from Utils.get_log import Log
from Utils.seed_message_to_lark import seed_message
from appium.webdriver.common.mobileby import AppiumBy
from Utils.install_apk import get_onactivity
from Base.more_devices_app import App


# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    popup_id = [(AppiumBy.ID, "com.intelcupid.shesay:id/ivClose")]
    login_sys_popup_id = [(AppiumBy.ID, "android:id/button1")]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_app_element(self, locator):

        try:
            self.handle_box()

            return self.driver.find_element(*locator)

        except Exception as e:
            str_element = self.element_in_page_source("com.intelcupid.shesay")
            if str_element is False:
                Log.print_console("info", "app可能崩溃了")
            return e

    def login_find_element(self, locator):
        try:
            self.login_handle_box()
            return self.driver.find_element(*locator)
        except Exception as e:
            str_element = self.element_in_page_source("com.intelcupid.shesay")
            if str_element is False:
                Log.print_console("info", "app可能崩溃了")
            return e

    def scroll_find_element(self, text):

        try:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{}").instance(0));'.format(
                                         text)).click()

        except Exception as e:
            return e

    # 获取toast内容是否出现
    def get_toast(self):
        toast_loc = (AppiumBy.XPATH, "//*[@class=\"android.widget.Toast\"]")
        try:
            # 获取文本内容
            toast_text = self.driver.find_element(*toast_loc).text
            print(toast_text)
            return toast_text
        except:
            return False

    def is_element_exist(self, element):

        sleep(2)
        source = self.driver.page_source
        # print(source)
        if element in source:
            return True
        else:
            return False

    def handle_box(self):

        for locator in self.popup_id:
            # source_page = self.driver.page_source
            elements = self.driver.find_elements(*locator)
            # print(elements)
            if len(elements) >= 1:
                elements[0].click()
            else:
                # print("{} not found".format(str(locator)))
                return

    def login_handle_box(self):
        for locator in self.login_sys_popup_id:
            elements = self.driver.find_elements(*locator)
            if len(elements) >= 1:
                elements[0].click()
            else:
                # print("{} not found".format(str(locator)))
                return

    def element_in_page_source(self, str_element):
        sleep(2)
        source = self.driver.page_source
        # print(source)
        if str_element in source:
            return True
        else:
            return False

    def get_windows_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return x, y

    def swipe_up(self):
        l = self.get_windows_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.85)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2,500)

