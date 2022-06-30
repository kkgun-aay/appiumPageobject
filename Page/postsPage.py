from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from Base.base_page import BasePage
from Page.discoverPage import Discover
from Page.postnewsPage import PostNews
from Utils.install_apk import get_onactivity


class PostsPage(BasePage):

    addposttab = (AppiumBy.ID, "com.intelcupid.shesay:id/ivPostAdd")
    postlike = (AppiumBy.ID, "com.intelcupid.shesay:id/ivLike")
    postcomment = (AppiumBy.ID, "com.intelcupid.shesay:id/ivComment")
    friendlikeemoji = (AppiumBy.ID, "com.intelcupid.shesay:id/ivFriendLikeEmoji2")

    def click_addposttab(self):
        self.find_app_element(self.addposttab).click()
        return PostNews(self.driver)

    def click_postlike(self):
        self.find_app_element(self.postlike).click()
        self.find_app_element(self.friendlikeemoji).click()

