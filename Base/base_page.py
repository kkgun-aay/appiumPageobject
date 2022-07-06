# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from Utils.seed_message_to_lark import seed_message
from appium.webdriver.common.mobileby import AppiumBy
from Utils.install_apk import get_onactivity


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
            is_crash = get_onactivity()
            if is_crash is True:
                return self.driver.find_element(*locator)
            else:
                # seed_message.seedmessage("app在点击{}元素之前崩溃了".format(locator))
                print("app在点击{}元素之前崩溃了".format(locator))
                self.driver.quit()
        except Exception as e:
            print("{}--元素未找到,点击失败了".format(locator))
            return e

    def login_find_element(self, locator):
        try:
            self.login_handle_box()
            is_crash = get_onactivity()
            if is_crash is True:
                return self.driver.find_element(*locator)
            else:
                seed_message.seedmessage("app崩溃了")
                self.driver.quit()
        except Exception as e:

            print("{}--元素未找到".format(locator))
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


