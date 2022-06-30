# -*- coding: utf-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from Base.base_page import BasePage
from Utils.install_apk import get_onactivity


class Discover(BasePage):

    discover = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabDiscover")
    resonate = (AppiumBy.ID,"com.intelcupid.shesay:id/tvResonate")
    flash = (AppiumBy.ID, "com.intelcupid.shesay:id/tvFlash")
    resonate_change = (AppiumBy.ID, "com.intelcupid.shesay:id/tvResonateChange")
    resonate_bell = (AppiumBy.ID, "com.intelcupid.shesay:id/ivResonateBell")
    plant_select_btn = (AppiumBy.ID, "com.intelcupid.shesay:id/tvPlanetSelectBtn")
    create_signal = (AppiumBy.ID, "com.intelcupid.shesay:id/vSignalCreate")
    bell_back = (AppiumBy.ID, "com.intelcupid.shesay:id/ibBarLeft")
    detail = (AppiumBy.ID, "com.intelcupid.shesay:id/tvButton")
    detail_text = "com.intelcupid.shesay:id/tvButton"
    question = (AppiumBy.XPATH, "//*[@text='问个问题男生来答']")
    edit_text = (AppiumBy.ID, "com.intelcupid.shesay:id/etText")
    submit_signal = (AppiumBy.ID, "com.intelcupid.shesay:id/tvComplete")
    flash_text_xpath = (AppiumBy.XPATH, "//*[@text='轻触屏幕 马上开聊']")

    # def click_discover_tab(self):
    #     self.find_app_element(self.discover).click()
    #     return self

    def get_resonate_text(self):
        text = self.find_app_element(self.resonate).text
        return text

    def click_resonate_change(self):
        self.find_app_element(self.resonate_change).click()
        self.find_app_element(self.plant_select_btn).click()
        return self

    def goto_signal_page(self):
        self.find_app_element(self.resonate).click()
        return self

    def click_flash(self):
        self.find_app_element(self.flash).click()
        flash_text = self.find_app_element(self.flash_text_xpath).text
        return flash_text

    def click_resonate_bell(self):
        self.find_app_element(self.resonate_bell).click()
        self.find_app_element(self.bell_back).click()
        return self

    def click_create_signal(self):
        self.find_app_element(self.create_signal).click()
        if self.is_element_exist(self.detail_text):
            self.find_app_element(self.detail).click()
            self.find_app_element(self.question).click()
            self.find_app_element(self.edit_text).send_keys("UI自动化测试，请忽略，UI自动化测试，请忽略")
            self.find_app_element(self.submit_signal).click()
            self.find_app_element(self.bell_back).click()
            return self
        else:
            self.find_app_element(self.question).click()
            self.find_app_element(self.edit_text).send_keys("UI自动化测试，请忽略，UI自动化测试，请忽略")
            self.find_app_element(self.submit_signal).click()
            self.find_app_element(self.bell_back).click()
            return self

