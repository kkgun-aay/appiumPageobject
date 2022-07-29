from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from Base.base_page import BasePage
from Utils.install_apk import get_onactivity


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
    # #本地地理位置弹窗同意按钮
    allowloction = (AppiumBy.ID, "com.intelcupid.shesay:id/btnAllowLocation")
    strallowloction = "com.intelcupid.shesay:id/btnAllowLocation"
    likelist = (AppiumBy.ID, "com.intelcupid.shesay:id/tvOutOfLikeList")
    likelisttext = "com.intelcupid.shesay:id/tvOutOfLikeList"
    permission_allow1 = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    permission_allow2 = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    recommendlike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlLike")
    recommendliketext = "com.intelcupid.shesay:id/ibControlLike"
    recommendsuperlike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlSuper")
    recommenddislike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlPass")
    recommendpost = (AppiumBy.ID, "com.intelcupid.shesay:id/ivPostOne")
    superlikesure_id = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSure")
    superlikesure = (AppiumBy.XPATH, "//android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[5]")
    matchclose = (AppiumBy.ID, "com.intelcupid.shesay:id/ivClose")
    superhelp = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSuperHelp")
    superhelp_text = "com.intelcupid.shesay:id/tvSuperHelp"
    feedback = (AppiumBy.ID, "com.intelcupid.shesay:id/tvFeedback")
    report_index4 = (AppiumBy.XPATH, "//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[4]")
    feedbacktext = "com.intelcupid.shesay:id/tvFeedback"
    input = (AppiumBy.ID, "com.intelcupid.shesay:id/reportReasonInput")
    submit = (AppiumBy.ID, "com.intelcupid.shesay:id/reportSubmit")
    toppeople_close = "com.intelcupid.shesay:id/ivCancel"
    toppeople_close_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ivCancel")
    xpath_allow_loction = "//*[contains(@text,'允许') and @class='android.widget.Button']"

    def click_loction_allow(self):
        if self.is_element_exist(self.strallowloction) is True:
            print("发现带有允许字样的系统弹窗，进行处理中")
            self.find_app_element(self.allowloction).click()
            # 通过find_elements方法一直取返回对象的第一个元素去点击，适配Android手机带有多个允许字样的地理位置弹窗
            self.driver.find_elements(AppiumBy.XPATH, self.xpath_allow_loction)[0].click()
            self.find_app_element(self.allowloction).click()
            self.driver.find_elements(AppiumBy.XPATH, self.xpath_allow_loction)[0].click()
            return self

        else:
            print("未发现带有允许字样的系统弹窗，略过")
            return self

    def goto_discover(self):
        self.find_app_element(self.discover).click()
        from Page.discoverPage import Discover
        return Discover(self.driver)

    def click_recommend_like(self):

        if self.is_element_exist(self.recommendliketext):
            self.find_app_element(self.recommendlike).click()
            if self.is_element_exist(self.toppeople_close):
                self.find_app_element(self.toppeople_close_id).click()
            return self

        else:
            if self.is_element_exist(self.likelisttext):
                return self.find_app_element(self.likelist).text

    def click_recommend_superlike(self):
        if self.is_element_exist(self.recommendliketext):
            self.find_app_element(self.recommendsuperlike).click()
            if self.is_element_exist(self.superhelp_text):
                self.find_app_element(self.matchclose).click()
            else:
                self.find_app_element(self.superlikesure_id).click()
            # return self
        else:
            if self.is_element_exist(self.likelisttext):
                return self.find_app_element(self.likelist).text

    def click_recommend_pass(self):
        if self.is_element_exist(self.recommendliketext):
            self.find_app_element(self.recommenddislike).click()
            return self
        else:
            if self.is_element_exist(self.likelisttext):
                return self.find_app_element(self.likelist).text

    def click_feedback(self):
        reporttext = "举报或反馈"
        if self.is_element_exist(self.recommendliketext):
            self.scroll_find_element(reporttext)
            self.find_app_element(self.report_index4).click()
            self.find_app_element(self.input).send_keys("测试,请忽略")
            # el2.hide_keybord()
            self.find_app_element(self.submit).click()
            toast = self.get_toast()
            return toast

    def goto_message(self):
        self.find_app_element(self.sessiontab).click()
        get_onactivity()
        from Page.messagePage import MessagePage
        return MessagePage(self.driver)

    def goto_myhome(self):
        self.find_app_element(self.myhome).click()
        get_onactivity()
        from Page.myhomePage import MyHome
        return MyHome(self.driver)

    def goto_matchsetting(self):

        self.find_app_element(self.setting).click()
        get_onactivity()
        from Page.settingPage import Setting
        return Setting(self.driver)

    def get_recommed_text(self):

        text = self.find_app_element(self.recommend).text
        get_onactivity()
        return text

    def goto_recommedtoday(self):
        self.find_app_element(self.recommend).click()
        get_onactivity()
        return self

    def click_explore(self):
        if self.is_element_exist(self.explore_id) is True:
            self.find_app_element(self.explore).click()
            get_onactivity()
            return self
        else:
            self.click_explorecover()

    def click_explorecover(self):
        self.find_app_element(self.explorecover).click()
        get_onactivity()
        return self

    def find_explore(self):
        if self.is_element_exist(self.explore_id) is True:

            text = self.find_app_element(self.explore).text
            get_onactivity()
            return text
        else:
            return self.find_app_element(self.explorecover).text

    def find_explorecover(self):
        text = self.find_app_element(self.explorecover).text
        get_onactivity()
        return text

    def click_blackvip_button(self):
        self.find_app_element(self.blackvipbutton).click()
        get_onactivity()
        from Page.blackvipPage import Blackvip
        return Blackvip(self.driver)

    def goto_likelist(self):
        self.find_app_element(self.likelist).click()
        from Page.heartfootprint import Heartfootprint
        return Heartfootprint(self.driver)

    def goto_user_profile_and_back(self):
        self.find_app_element(self.user_profile).click()
        get_onactivity()

        likebutton = "com.intelcupid.shesay:id/ibControlLike"
        if self.is_element_exist(likebutton) is True:
            self.find_app_element(self.likebutton).click()
            return self
        else:
            self.find_app_element(self.userprofile_back).click()
            return self
