# -*- coding: utf-8 -*-
from appium.webdriver.common.appiumby import AppiumBy
from Base.base_page import BasePage


class Discover(BasePage):

    discover = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabDiscover")
    resonate = (AppiumBy.ID,"com.intelcupid.shesay:id/tvResonate")
    flash = (AppiumBy.ID, "com.intelcupid.shesay:id/tvFlash")
    #筛选ID
    resonate_change = (AppiumBy.ID, "com.intelcupid.shesay:id/tvResonateChange")
    #收件箱
    resonate_bell = (AppiumBy.ID, "com.intelcupid.shesay:id/ivResonateBell")
    #星球确定按钮
    plant_select_btn = (AppiumBy.ID, "com.intelcupid.shesay:id/tvPlanetSelectBtn")
    create_signal = (AppiumBy.ID, "com.intelcupid.shesay:id/vSignalCreate")
    bell_back = (AppiumBy.ID, "com.intelcupid.shesay:id/ibBarLeft")
    #？号页的好的按钮
    detail = (AppiumBy.ID, "com.intelcupid.shesay:id/tvButton")
    detail_text = "com.intelcupid.shesay:id/tvButton"
    question = (AppiumBy.XPATH, "//*[@text='问个问题男生来答']")
    edit_text = (AppiumBy.ID, "com.intelcupid.shesay:id/etText")
    submit_signal = (AppiumBy.ID, "com.intelcupid.shesay:id/tvComplete")
    flash_text_xpath = (AppiumBy.XPATH, "//*[@text='轻触屏幕 马上开聊']")
    signal_sure_button = (AppiumBy.ID, "com.intelcupid.shesay:id/tvPositive")
    signal_sure_button_text = "com.intelcupid.shesay:id/tvPositive"

    # def click_discover_tab(self):
    #     self.find_app_element(self.discover)
    #     return self

    def get_resonate_text(self):
        text = self.find_app_element(self.resonate).text
        return text

    def click_resonate_change(self):
        self.find_app_element(self.resonate_change)
        self.find_app_element(self.plant_select_btn)
        return self

    def goto_signal_page(self):
        self.find_app_element(self.resonate)
        return self

    def click_page_button(self):
        self.find_app_element(self.detail)
        return self

    def click_signal_problem_and_send(self):
        self.find_app_element(self.question)
        self.find_app_element(self.edit_text).send_keys("UI自动化测试，请忽略，UI自动化测试，请忽略")
        self.find_app_element(self.submit_signal)
        self.find_app_element(self.bell_back)
        return self

    def click_signal_sure_button(self):
        self.find_app_element(self.signal_sure_button)
        return self

    def click_flash(self):
        self.find_app_element(self.flash)
        flash_text = self.find_app_element(self.flash_text_xpath).text
        return flash_text

    def click_resonate_bell(self):
        self.find_app_element(self.resonate_bell)
        self.find_app_element(self.bell_back)
        return self

    def click_create_signal(self):
        self.find_app_element(self.create_signal)
        if self.is_element_exist(self.detail_text):
            self.click_page_button().click_signal_problem_and_send()
            if self.is_element_exist(self.signal_sure_button_text):
                self.click_signal_sure_button()
            return self

        else:
            self.click_signal_problem_and_send()
            self.click_signal_sure_button()
            return self

