from appium.webdriver.common.appiumby import AppiumBy
from Base.base_page import BasePage


class Location(BasePage):

    location_back = (AppiumBy.ID, "com.intelcupid.shesay:id/ibBarLeft")

    def click_back(self):
        self.find_app_element(self.location_back).click()
        from Page.settingPage import Setting
        return Setting(self.driver)