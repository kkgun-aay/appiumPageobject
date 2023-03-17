from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from Base.base_page import BasePage
from Page.discoverPage import Discover
from Page.postsPage import PostsPage


class MessagePage(BasePage):

    sessiontab = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabSession")
    messagetab = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSession")
    posttab = (AppiumBy.ID, "com.intelcupid.shesay:id/tvPosts")

    def click_message_tab(self):
        self.find_app_element(self.sessiontab)
        return self

    def click_post_tab(self):
        self.find_app_element(self.posttab)
        return PostsPage(self.driver)

    def get_message_tab_text(self):
        text = self.find_app_element(self.messagetab).text
        return text