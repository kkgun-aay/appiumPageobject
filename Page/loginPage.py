from time import sleep
from appium.webdriver.common.mobileby import AppiumBy
from Base.base_page import BasePage
from Page.recommendPage import recommEnd


class Login(BasePage):

    remember = (AppiumBy.ID, "com.intelcupid.shesay:id/ivRemember")
    wechat = (AppiumBy.ID, "com.intelcupid.shesay:id/vWechat")
    wechat_agreement = (AppiumBy.ID, "com.intelcupid.shesay:id/tvAgreement")
    secret = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSecret")
    agreepopup = (AppiumBy.ID, "com.intelcupid.shesay:id/tvAgree")
    disagreepopup = "com.intelcupid.shesay:id/tvDisagree"
    osbutton = "android:id/button1"
    osbutton_id = (AppiumBy.ID, "android:id/button1")
    # 本地地理位置弹窗同意按钮
    allowloction = (AppiumBy.ID, "com.intelcupid.shesay:id/btnAllowLocation")
    strallowloction = "com.intelcupid.shesay:id/btnAllowLocation"

    def app_login(self):
        self.login_find_element(self.remember)
        self.login_find_element(self.wechat)
        return recommEnd(self.driver)

    def click_agerrpopup(self):
        self.find_app_element(self.agreepopup)
        return self

    def click_wechat_icon(self):
        self.find_app_element(self.wechat)
        return self

    def get_agreement_text(self):

        return self.login_find_element(self.wechat_agreement).text

    def not_serach_wechat(self):
        sleep(2)
        if self.is_element_exist(self.disagreepopup) is True:
            self.click_agerrpopup()
            if self.is_element_exist(self.osbutton) is True:
                #这里用底层的find方法，因为自己封装的检查了当前Activity，弹出系统弹窗时Activity不是app的
                self.driver.find_element(AppiumBy.ID, self.osbutton)
                self.click_wechat_icon()
                toast = self.get_toast()
                return toast
            else:
                self.click_wechat_icon()
                toast = self.get_toast()
                return toast
        else:
            # self.login_find_element(self.wechat)
            self.click_wechat_icon()
            toast = self.get_toast()
            return toast


