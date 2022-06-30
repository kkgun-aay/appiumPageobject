from Base.base_page import BasePage
from appium.webdriver.common.mobileby import AppiumBy

from Utils.install_apk import get_onactivity


class Heartfootprint(BasePage):

    back_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ivBack")
    dislikeuserlike = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[2]")
    receive_id = (AppiumBy.ID, "com.intelcupid.shesay:id/tvExchange")
    buy_id = (AppiumBy.ID, "com.intelcupid.shesay:id/tvBuy")
    get_superlike_id = (AppiumBy.ID, "com.intelcupid.shesay:id/compared_one")
    close_superlike_popup = (AppiumBy.ID, "com.intelcupid.shesay:id/ivClose")

    def back_to_recommend(self):
        self.find_app_element(self.back_id).click()
        from Page.recommendPage import recommEnd
        return recommEnd(self.driver)

    def switch_tab(self):
        self.find_app_element(self.dislikeuserlike).click()
        return self
        # self.find_app_element(self.back_id).click()
        # from Page.recommendPage import recommEnd
        # return recommEnd(self.driver)

    def click_free_receive(self):
        self.find_app_element(self.receive_id).click()
        self.find_app_element(self.close_superlike_popup).click()
        return self

    def click_superlike_buy(self):
        # self.get_app_state()
        self.find_app_element(self.buy_id).click()
        # self.find_app_element(self.close_superlike_popup).click()
        return self

