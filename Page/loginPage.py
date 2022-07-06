from time import sleep
from appium.webdriver.common.mobileby import AppiumBy
from Base.base_page import BasePage
from Page.recommendPage import recommEnd
from Utils.install_apk import get_onactivity


class Login(BasePage):

    remember = (AppiumBy.ID, "com.intelcupid.shesay:id/ivRemember")
    wechat = (AppiumBy.ID, "com.intelcupid.shesay:id/vWechat")
    wechat_agreement = (AppiumBy.ID, "com.intelcupid.shesay:id/tvAgreement")
    secret = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSecret")
    agreepopup = (AppiumBy.ID, "com.intelcupid.shesay:id/tvAgree")
    disagreepopup = "com.intelcupid.shesay:id/tvDisagree"
    osbutton = "android:id/button1"
    osbutton_id = (AppiumBy.ID, "android:id/button1")

    def app_login(self):
        self.login_find_element(self.remember).click()
        self.login_find_element(self.wechat).click()
        return recommEnd(self.driver)

    def click_agerrpopup(self):
        self.find_app_element(self.agreepopup).click()
        return self

    def click_wechat_icon(self):
        self.find_app_element(self.wechat).click()
        return self

    def get_agreement_text(self):
        return self.login_find_element(self.wechat_agreement).text

    def not_serach_wechat(self):
        sleep(2)
        if self.is_element_exist(self.disagreepopup) is True:
            # self.login_find_element(self.agreepopup).click()
            # self.login_find_element(self.wechat).click()
            self.click_agerrpopup().click_wechat_icon()
            toast = self.get_toast()
            return toast
        else:
            # self.login_find_element(self.wechat).click()
            self.click_wechat_icon()
            toast = self.get_toast()
            return toast


