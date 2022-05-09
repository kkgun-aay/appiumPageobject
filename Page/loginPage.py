from time import sleep

from appium.webdriver.common.mobileby import AppiumBy
# from selenium.webdriver.remote.webdriver import WebDriver
# import pytest
from Base.base_page import BasePage
from Page.recommendPage import recommEnd


class Login(BasePage):

    remember = (AppiumBy.ID, "com.intelcupid.shesay:id/ivRemember")
    wechat = (AppiumBy.ID, "com.intelcupid.shesay:id/vWechat")
    wechat_agreement = (AppiumBy.ID, "com.intelcupid.shesay:id/tvAgreement")
    secret = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSecret")
    agreepopup = (AppiumBy.ID, "com.intelcupid.shesay:id/tvAgree")
    stragreepopup = "com.intelcupid.shesay:id/tvAgree"

    def app_login(self):
        self.find_app_element(self.remember).click()
        self.find_app_element(self.wechat).click()
        return recommEnd(self.driver)
        # if self.is_element_exist(self.agreepopup) is True:
        #     self.find_app_element(self.agreepopup).click()
        #     self.find_app_element(self.remember).click()
        #     self.find_app_element(self.wechat).click()
        #     return recommEnd(self.driver)
        # else:
        #     self.find_app_element(self.remember).click()
        #     self.find_app_element(self.wechat).click()
        #     return recommEnd(self.driver)

    def get_agreement_text(self):
        return self.find_app_element(self.wechat_agreement).text

    def not_serach_wechat(self):
        sleep(2)
        if self.is_element_exist(self.stragreepopup) is True:
            self.find_app_element(self.agreepopup).click()
            self.find_app_element(self.wechat).click()
            toast = self.get_toast()
            return toast
        else:
            self.find_app_element(self.wechat).click()
            toast = self.get_toast()
            return toast
        # self.find_app_element(self.wechat).click()
        # toast = self.get_toast()
        # return toast

