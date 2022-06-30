from appium.webdriver.common.appiumby import AppiumBy
from Base.base_page import BasePage
from Utils.install_apk import get_onactivity


class Setting(BasePage):

    settingtext = (AppiumBy.ID, "com.intelcupid.shesay:id/tvBarTitle")
    back = (AppiumBy.ID, "com.intelcupid.shesay:id/ibBarLeft")
    finish = (AppiumBy.ID, "com.intelcupid.shesay:id/tvBarRight")
    location = (AppiumBy.ID, "com.intelcupid.shesay:id/tvLocationEdit")

    def click_back(self):
        self.find_app_element(self.back).click()
        from Page.recommendPage import recommEnd
        return recommEnd(self.driver)

    def click_finish(self):
        self.find_app_element(self.finish).click()
        from Page.recommendPage import recommEnd
        return recommEnd(self.driver)

    def get_setting_text(self):
        print(self.find_app_element(self.settingtext).text())
        text = self.find_app_element(self.settingtext).text()
        return text

    def click_location(self):
        self.find_app_element(self.location).click()
        from Page.settingLocationPage import Location
        return Location(self.driver)