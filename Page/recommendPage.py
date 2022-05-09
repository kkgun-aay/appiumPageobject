from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from Base.base_page import BasePage


class recommEnd(BasePage):

    recommend = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabRecommend")
    discover = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabDiscover")
    sessiontab = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabSession")
    myhome = (AppiumBy.ID, "com.intelcupid.shesay:id/tvTabHome")
    setting = (AppiumBy.ID, "com.intelcupid.shesay:id/ivMatchSetting")
    explore = (AppiumBy.ID, "com.intelcupid.shesay:id/tvExplore")
    explore_id = "com.intelcupid.shesay:id/tvExplore"
    explorecover = (AppiumBy.ID, "com.intelcupid.shesay:id/vExploreCover")
    blackvipbutton = (AppiumBy.ID, "com.intelcupid.shesay:id/tvCheck")
    user_profile = (AppiumBy.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView[1]")
    likebutton = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlLike")
    userprofile_back = (AppiumBy.ID, "com.intelcupid.shesay:id/ibBarLeft")
    allowloction = (AppiumBy.ID, "com.intelcupid.shesay:id/btnAllowLocation")
    strallowloction = "com.intelcupid.shesay:id/btnAllowLocation"
    likelist = (AppiumBy.ID, "com.intelcupid.shesay:id/tvOutOfLikeList")
    permission_allow1 = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    permission_allow2 = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    recommendlike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlLike")
    recommendsuperlike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlSuper")
    recommenddislike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlPass")
    recommendpost = (AppiumBy.ID, "com.intelcupid.shesay:id/ivPostOne")

    def goto_discover(self):
        self.find_app_element(self.discover).click()
        from Page.discoverPage import Discover
        return Discover(self.driver)

    def click_recommend_like(self):
        self.find_app_element(self.recommendlike).click()
        return self

    def click_recommend_superlike(self):
        self.find_app_element(self.recommenddislike).click()
        return self

    def click_recommend_pass(self):
        self.find_app_element(self.recommendsuperlike).click()
        return self

    def goto_message(self):
        self.find_app_element(self.sessiontab).click()
        from Page.messagePage import MessagePage
        return MessagePage(self.driver)

    def goto_myhome(self):
        self.find_app_element(self.myhome).click()
        from Page.myhomePage import MyHome
        return MyHome(self.driver)

    def goto_matchsetting(self):

        self.find_app_element(self.setting).click()
        from Page.settingPage import Setting
        return Setting(self.driver)

    def get_recommed_text(self):

        text = self.find_app_element(self.recommend).text
        return text

    def goto_recommedtoday(self):
        self.find_app_element(self.recommend).click()
        return self

    def click_explore(self):
        if self.is_element_exist(self.explore_id) is True:
            self.find_app_element(self.explore).click()
            return self
        else:
            self.click_explorecover()

    def click_explorecover(self):
        self.find_app_element(self.explorecover).click()
        return self

    def find_explore(self):
        if self.is_element_exist(self.explore_id) is True:
            return self.find_app_element(self.explore).text
        else:
            return self.find_app_element(self.explorecover).text

    def find_explorecover(self):
        return self.find_app_element(self.explorecover).text

    def click_blackvip_button(self):
        self.find_app_element(self.blackvipbutton).click()
        from Page.blackvipPage import Blackvip
        return Blackvip(self.driver)

    def goto_likelist(self):
        self.find_app_element(self.likelist).click()
        from Page.heartfootprint import Heartfootprint
        return Heartfootprint(self.driver)

    def goto_user_profile_and_back(self):
        self.find_app_element(self.user_profile).click()

        likebutton = "com.intelcupid.shesay:id/ibControlLike"
        if self.is_element_exist(likebutton) is True:
            self.find_app_element(self.likebutton).click()
            return self
        else:
            self.find_app_element(self.userprofile_back).click()

            return self
