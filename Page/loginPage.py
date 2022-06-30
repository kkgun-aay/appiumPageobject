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
    stragreepopup = "com.intelcupid.shesay:id/tvAgree"
    osbutton = "android:id/button1"
    osbutton_id = (AppiumBy.ID, "android:id/button1")

    def app_login(self):
        self.login_find_element(self.remember).click()
        self.login_find_element(self.wechat).click()
        return recommEnd(self.driver)

    def get_agreement_text(self):
        return self.login_find_element(self.wechat_agreement).text

    def not_serach_wechat(self):
        sleep(2)
        # if self.is_element_exist(self.stragreepopup) is True:
        self.login_find_element(self.agreepopup).click()
        self.login_find_element(self.wechat).click()
        toast = self.get_toast()
        return toast
        # else:
        #     self.login_find_element(self.wechat).click()
        #     toast = self.get_toast()
        #     return toast


