from time import sleep

from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from Base.base_page import BasePage
from Utils.get_log import Log


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
    user_profile_index_1 = (AppiumBy.XPATH, "//android.view.ViewGroup[1]/android.widget.ImageView[1]")
    user_profile_index_2 = (AppiumBy.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView[1]")
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
    report_index4 = (
        AppiumBy.XPATH, "//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[4]")
    feedbacktext = "com.intelcupid.shesay:id/tvFeedback"
    input = (AppiumBy.ID, "com.intelcupid.shesay:id/reportReasonInput")
    submit = (AppiumBy.ID, "com.intelcupid.shesay:id/reportSubmit")
    toppeople_close = "com.intelcupid.shesay:id/ivCancel"
    toppeople_close_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ivCancel")
    xpath_allow_loction = "//*[contains(@text,'允许') and @class='android.widget.Button']"
    super_like_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ivSuper")
    str_super_like = "com.intelcupid.shesay:id/ivSuper"
    # 精选用户资料页超喜欢id
    profile_super_like_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlSuper")
    # 精选用户资料页pass
    profile_pass_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlPass")
    # 黑金超喜欢已送出弹窗中的输入框发送按钮
    black_vip_send = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSend")
    # 黑金超喜欢已送出弹窗中的跳过留言按钮
    black_vip_skip = (AppiumBy.ID, "com.intelcupid.shesay:id/tvCancel")
    # 黑金超喜欢已送出弹窗中的跳过留言str类型ID
    black_vip_skip_str = "com.intelcupid.shesay:id/tvCancel"
    # 黑金超喜欢已送出弹窗中的输入框
    black_vip_message_input = (AppiumBy.ID, "com.intelcupid.shesay:id/tvMessageInput")
    #匹配成功弹窗发送上次的问题按钮
    match_success_last_time = (AppiumBy.ID, "com.intelcupid.shesay:id/tvLastQuestion")
    #匹配成功弹窗选择新问题按钮
    match_success_new = (AppiumBy.ID, "com.intelcupid.shesay:id/tvNewQuestion")
    #点击选择新问题按钮跳转的出题页面发送题目按钮
    send_answer_quest = (AppiumBy.ID, "com.intelcupid.shesay:id/questAnswerQuest")
    #点击选择新问题跳转到出题页输入框
    send_answer_input = (AppiumBy.ID, "com.intelcupid.shesay:id/shadowQuestInput")
    #点击选择新问题跳转到出题页面不提问，直接打招呼按钮
    skip_answer = (AppiumBy.ID, "com.intelcupid.shesay:id/questAnswerQuestionSkip")
    #匹配成功弹窗选择问题按钮str
    match_success_new_str = "com.intelcupid.shesay:id/tvNewQuestion"
    #匹配成功弹窗继续匹配按钮
    match_success_continue = (AppiumBy.ID, "com.intelcupid.shesay:id/tvBottomGoOn")
    #匹配成功弹窗（未出过题的）---去出题
    match_success_not_send = (AppiumBy.ID, "com.intelcupid.shesay:id/tvFemaleQuest")

    def click_loction_allow(self):
        if self.is_element_exist(self.strallowloction) is True:
            Log.print_console("info", "发现带有允许字样的系统弹窗，进行处理中")
            self.find_app_element(self.allowloction).click()
            # 通过find_elements方法一直取返回对象的第一个元素去点击，适配Android手机带有多个允许字样的地理位置弹窗
            self.driver.find_elements(AppiumBy.XPATH, self.xpath_allow_loction)[0].click()
            self.find_app_element(self.allowloction).click()
            self.driver.find_elements(AppiumBy.XPATH, self.xpath_allow_loction)[0].click()
            return self

        else:
            # print("未发现带有允许字样的系统弹窗，略过")
            Log.print_console("info", "未发现带有允许字样的系统弹窗")
            return self

    def goto_discover(self):
        self.find_app_element(self.discover).click()
        from Page.discoverPage import Discover
        return Discover(self.driver)

    def click_recommend_like_click_success_new(self):

        if self.is_element_exist(self.recommendliketext):
            self.find_app_element(self.recommendlike).click()
            if self.is_element_exist(self.match_success_new_str):
                self.find_app_element(self.match_success_new).click()
                self.find_app_element(self.send_answer_input).send_keys("今天吃的啥好吃的")
                self.find_app_element(self.send_answer_quest).click()
                #这里还没处理完,需要加从未出过题的逻辑
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

            text = self.find_app_element(self.explore).text
            return text
        else:
            return self.find_app_element(self.explorecover).text

    def find_explorecover(self):
        text = self.find_app_element(self.explorecover).text
        return text

    def click_blackvip_button(self):
        self.find_app_element(self.blackvipbutton).click()
        from Page.blackvipPage import Blackvip
        return Blackvip(self.driver)

    def goto_likelist(self):
        self.find_app_element(self.likelist).click()
        from Page.heartfootprint import Heartfootprint
        return Heartfootprint(self.driver)

    def explore_swipe(self, element):
        sleep(3)
        self.swipe_up()
        elements_list = self.driver.find_elements(AppiumBy.ID, self.str_super_like)

        if len(elements_list) > 1:
            self.find_app_element(self.user_profile_index_2).click()
            super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
            if self.is_element_exist(super_like_button) is True:
                if element == self.profile_super_like_id:
                    self.find_app_element(element).click()
                    self.find_app_element(self.superlikesure_id).click()
                    if self.is_element_exist(self.black_vip_skip_str) is True:
                        self.find_app_element(self.black_vip_skip).click()
                else:
                    self.find_app_element(element).click()

            else:
                self.find_app_element(self.userprofile_back).click()

        else:
            self.find_app_element(self.user_profile_index_1).click()
            super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
            if self.is_element_exist(super_like_button) is True:
                if element == self.profile_super_like_id:
                    self.find_app_element(element).click()
                    self.find_app_element(self.superlikesure_id).click()
                    if self.is_element_exist(self.black_vip_skip_str) is True:
                        self.find_app_element(self.black_vip_skip).click()
                else:
                    self.find_app_element(element).click()
            else:
                self.find_app_element(self.userprofile_back).click()

    # def goto_user_profile_and_back(self):
    #     self.find_app_element(self.user_profile).click()
    #
    #     likebutton = "com.intelcupid.shesay:id/ibControlLike"
    #     if self.is_element_exist(likebutton) is True:
    #         self.find_app_element(self.likebutton).click()
    #         return self
    #     else:
    #         self.find_app_element(self.userprofile_back).click()
    #         return self

    # def goto_user_profile_and_back(self):
    #
    #     self.find_app_element(self.user_profile_index_2).click()
    #     like_button = "com.intelcupid.shesay:id/ibControlLike"
    #     if self.is_element_exist(like_button) is True:
    #         self.find_app_element(self.likebutton).click()
    #
    #     else:
    #         self.find_app_element(self.userprofile_back).click()
    #
    #     # for i in range(3):
    #     self.swipe_up()
    #     sleep(2)
    #     elements_list = self.driver.find_elements(AppiumBy.ID, self.str_super_like)
    #
    #     if len(elements_list) > 1:
    #         self.find_app_element(self.user_profile_index_2).click()
    #         super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
    #         if self.is_element_exist(super_like_button) is True:
    #             self.find_app_element(self.profile_super_like_id).click()
    #             self.find_app_element(self.superlikesure_id).click()
    #             if self.is_element_exist(self.black_vip_skip_str) is True:
    #                 self.find_app_element(self.black_vip_skip)
    #
    #         else:
    #             self.find_app_element(self.userprofile_back).click()
    #
    #     else:
    #         self.find_app_element(self.user_profile_index_1).click()
    #         super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
    #         if self.is_element_exist(super_like_button) is True:
    #             self.find_app_element(self.profile_super_like_id).click()
    #             self.find_app_element(self.superlikesure_id).click()
    #             if self.is_element_exist(self.black_vip_skip_str) is True:
    #                 self.find_app_element(self.black_vip_skip)
    #         else:
    #             self.find_app_element(self.userprofile_back).click()
    #
    #     self.swipe_up()
    #     sleep(2)
    #     elements_list = self.driver.find_elements(AppiumBy.ID, self.str_super_like)
    #     if len(elements_list) > 1:
    #         self.find_app_element(self.user_profile_index_2).click()
    #         profile_pass = "com.intelcupid.shesay:id/ibControlPass"
    #         if self.is_element_exist(profile_pass) is True:
    #             self.find_app_element(self.profile_pass_id).click()
    #
    #         else:
    #             self.find_app_element(self.userprofile_back).click()
    #
    #     else:
    #         self.find_app_element(self.user_profile_index_1).click()
    #         profile_pass = "com.intelcupid.shesay:id/ibControlPass"
    #         if self.is_element_exist(profile_pass) is True:
    #             self.find_app_element(self.profile_pass_id).click()
    #         else:
    #             self.find_app_element(self.userprofile_back).click()

    def goto_user_profile_and_back(self):
        self.find_app_element(self.user_profile_index_2).click()
        like_button = "com.intelcupid.shesay:id/ibControlLike"
        if self.is_element_exist(like_button) is True:
            self.find_app_element(self.likebutton).click()

        else:
            self.find_app_element(self.userprofile_back).click()

        self.explore_swipe(self.profile_super_like_id)
        self.explore_swipe(self.profile_pass_id)
        return self
