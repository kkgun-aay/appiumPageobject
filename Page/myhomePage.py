from Base.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from Utils.install_apk import get_onactivity


class MyHome(BasePage):

        myhomesetting = (AppiumBy.ID, "com.intelcupid.shesay:id/ibSetting")

        def click_myhome_setting(self):

            self.find_app_element(self.myhomesetting).click()
            from Page.myhomesettingPage import MyhomeSetting
            return MyhomeSetting(self.driver)