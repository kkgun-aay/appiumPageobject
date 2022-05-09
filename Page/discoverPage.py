# -*- coding: utf-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from Base.base_page import BasePage


class Discover(BasePage):

    discover = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabDiscover")
    resonate = (AppiumBy.ID,"com.intelcupid.shesay:id/tvResonate")

    # def click_discover_tab(self):
    #     self.find_app_element(self.discover).click()
    #     return self

    def get_resonate_text(self):
        return self.find_app_element(self.resonate).text


