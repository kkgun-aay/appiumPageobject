from appium.webdriver.common.appiumby import AppiumBy

from Base.base_page import BasePage
from Utils.install_apk import get_onactivity


class MyhomeSetting(BasePage):

    logoutbutton = (AppiumBy.ID, "com.intelcupid.shesay:id/tvLogout")
    logoutpop = (AppiumBy.XPATH, "//android.widget.LinearLayout/android.widget.TextView[2]")

    def click_logout(self):
        text = "退出登录"
        self.scroll_find_element(text)
        self.find_app_element(self.logoutpop)
        from Page.loginPage import Login
        return Login(self.driver)