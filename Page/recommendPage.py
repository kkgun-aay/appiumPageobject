from time import sleep
from appium.webdriver.common.mobileby import AppiumBy
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
    # 精选页用户资料卡用elements方法定位
    user_profile_id = "com.intelcupid.shesay:id/ivAvatar"
    # likebutton = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlLike")
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
    # 超喜欢按钮id
    recommendsuperlike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlSuper")
    # 超喜欢按钮str_id
    recommend_super_like_str = "com.intelcupid.shesay:id/ibControlSuper"
    recommenddislike = (AppiumBy.ID, "com.intelcupid.shesay:id/ibControlPass")
    recommendpost = (AppiumBy.ID, "com.intelcupid.shesay:id/ivPostOne")
    # 超喜欢发送按钮以及女号匹配成功选择发送上次问题弹窗上的确认发送按钮id（发送上次问题弹窗上需要用底层find方法，因为有关闭按钮）
    superlikesure_id = (AppiumBy.ID, "com.intelcupid.shesay:id/tvSure")
    # 超喜欢发送按钮以及女号匹配成功选择发送上次问题弹窗上的确认发送按钮 id_str
    superlikesure_id_str = "com.intelcupid.shesay:id/tvSure"
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
    # 黑金超喜欢已送出弹窗中的跳过留言按钮以及女号匹配成功选择发送上次问题弹窗上的选择新问题
    black_vip_skip = (AppiumBy.ID, "com.intelcupid.shesay:id/tvCancel")
    # 黑金超喜欢已送出弹窗中的跳过留言str类型ID
    black_vip_skip_str = "com.intelcupid.shesay:id/tvCancel"
    # 黑金超喜欢已送出弹窗中的输入框
    black_vip_message_input = (AppiumBy.ID, "com.intelcupid.shesay:id/tvMessageInput")
    # 匹配成功弹窗发送上次的问题按钮
    match_success_last_time = (AppiumBy.ID, "com.intelcupid.shesay:id/tvLastQuestion")
    # 匹配成功弹窗选择新问题按钮
    match_success_new = (AppiumBy.ID, "com.intelcupid.shesay:id/tvNewQuestion")
    # 点击选择新问题按钮跳转的出题页面发送题目按钮
    send_answer_quest = (AppiumBy.ID, "com.intelcupid.shesay:id/questAnswerQuestionSend")
    # 点击选择新问题跳转到出题页输入框
    send_answer_input = (AppiumBy.ID, "com.intelcupid.shesay:id/shadowQuestInput")
    # 点击选择新问题跳转到出题页面不提问，直接打招呼按钮
    skip_answer = (AppiumBy.ID, "com.intelcupid.shesay:id/questAnswerQuestionSkip")
    # 匹配成功弹窗选择问题按钮str
    match_success_new_str = "com.intelcupid.shesay:id/tvNewQuestion"
    # 匹配成功弹窗继续匹配按钮
    match_success_continue = (AppiumBy.ID, "com.intelcupid.shesay:id/tvBottomGoOn")
    # 匹配成功弹窗（未出过题的）---去出题
    match_success_not_send = (AppiumBy.ID, "com.intelcupid.shesay:id/tvFemaleQuest")
    # 男生匹配成功弹窗右上角关闭按钮
    boy_match_success_close = "com.intelcupid.shesay:id/ivClose"
    # 男生匹配成功弹窗右上角关闭按钮id
    boy_match_success_close_id = (AppiumBy.ID, "com.intelcupid.shesay:id/ivClose")
    # 匹配成功页面继续匹配按钮
    boy_match_success_continue_id = "com.intelcupid.shesay:id/btnMaleGoOn"
    # 同性匹配确认发送按钮
    sex_match_success_send_id = "com.intelcupid.shesay:id/tvSendBtn"
    # 同性匹配成功确认按钮字符串id
    sex_match_success_send_str_id = "com.intelcupid.shesay:id/tvSendBtn"
    # 同性匹配更换打招呼语按钮
    sex_match_success_change_hello_id = "com.intelcupid.shesay:id/ivChangeHello"
    # 出题页用户头像id
    user_profile = (AppiumBy.ID, "com.intelcupid.shesay:id/ivTargetPhoto")
    # 出题页再出一题按钮
    question_add = (AppiumBy.ID, "com.intelcupid.shesay:id/tvQuestionAdd")
    # 出题页再出一题按钮str
    question_add_str = "com.intelcupid.shesay:id/tvQuestionAdd"
    # 参考题库
    question_bank = (AppiumBy.ID, "com.intelcupid.shesay:id/tvQuestBankBottom")
    # 题库列表
    question_list = (AppiumBy.ID, "com.intelcupid.shesay:id/tvQAQuest")
    # 题库列表str
    question_list_str = "com.intelcupid.shesay:id/tvQAQuest"
    # 出题页删除题目按钮
    question_delect = (AppiumBy.ID, "com.intelcupid.shesay:id/ivQuestionOneDelete")
    # 跳转到私聊页点击左上角返回按钮
    profile_back = (AppiumBy.ID, "com.intelcupid.shesay:id/ibBack")

    def click_loction_allow(self):
        if self.is_element_exist(self.strallowloction) is True:
            Log.print_console("info", "发现带有允许字样的系统弹窗，进行处理中")
            self.find_app_element(self.allowloction)
            # 通过find_elements方法一直取返回对象的第一个元素去点击，适配Android手机带有多个允许字样的地理位置弹窗
            self.driver.find_elements(AppiumBy.XPATH, self.xpath_allow_loction)[0]
            self.find_app_element(self.allowloction)
            self.driver.find_elements(AppiumBy.XPATH, self.xpath_allow_loction)[0]
            return self

        else:
            # print("未发现带有允许字样的系统弹窗，略过")
            Log.print_console("info", "未发现带有允许字样的系统弹窗,直接return,去跑case")
            return self

    def goto_discover(self):
        self.find_app_element(self.discover)
        from Page.discoverPage import Discover
        return Discover(self.driver)

    def boy_click_recommend_like_match_success(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "开始点击推荐页喜欢按钮")
            self.find_app_element(self.recommendlike)
            Log.print_console("info", "点喜欢匹配成功，点击右上角关闭按钮")
            # 由于app内所有关闭按钮ID都一样，所以当遇到弹窗关闭按钮时采用appium底层find方法
            self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
            # self.find_app_element(self.send_answer_input).send_keys("今天吃的啥好吃的")
            # self.find_app_element(self.send_answer_quest)
            # 这里还没处理完,需要加从未出过题的逻辑,以及同性匹配逻辑
            # else:
            #     self.find_app_element(self.match_success_continue)
            return self
        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def boy_click_recommend_like_match_success_click_continue(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "开始点击推荐页喜欢按钮并关闭页面")
            self.find_app_element(self.recommendlike)
            # if self.is_element_exist(self.boy_match_success_close):
            Log.print_console("info", "点喜欢匹配成功，点击继续匹配按钮并关闭页面")
            self.driver.find_element(AppiumBy.ID, self.boy_match_success_continue_id)
            return self
        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def boy_click_recommend_superlike_match_success(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "开始点击推荐页超喜欢按钮")
            self.find_app_element(self.recommendsuperlike)
            if self.is_element_exist(self.superhelp_text):
                Log.print_console("info", "判断如果没有超喜欢个数，直接关闭购买弹窗")
                self.find_app_element(self.matchclose)
                return self
            else:
                Log.print_console("info", "开始点击超喜欢弹窗上的确定按钮，送出超喜欢")
                self.find_app_element(self.superlikesure_id)
                # 判断超喜欢匹配成功是否是同性匹配
                if self.is_element_exist(self.sex_match_success_send_str_id):
                    Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
                else:
                    Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                    self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
            return self
        else:
            Log.print_console("info", "没有找到推荐页超喜欢按钮的ID，直接return，进行下一条case")
            return self

    def click_recommend_pass(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "开始点击推荐页无感按钮")
            self.find_app_element(self.recommenddislike)
            return self
        else:
            Log.print_console("info", "没有找到推荐页无感按钮的ID，直接return，进行下一条case")
            return self

    def click_recommend_feedback(self):
        Log.print_console("info", "开始滑动查找举报反馈按钮，并点击")
        if self.is_element_exist(self.recommendliketext):
            reporttext = "举报或反馈"
            self.scroll_find_element(reporttext)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("其他")')
            # self.find_app_element(self.report_index4)
            self.find_app_element(self.input).send_keys("测试,请忽略")
            # el2.hide_keybord()
            self.find_app_element(self.submit)
            Log.print_console("info", "自定义举报成功，并返回toast")
            toast = self.get_toast()
            return toast
        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def goto_message(self):
        self.find_app_element(self.sessiontab)
        from Page.messagePage import MessagePage
        return MessagePage(self.driver)

    def goto_myhome(self):
        self.find_app_element(self.myhome)
        from Page.myhomePage import MyHome
        return MyHome(self.driver)

    def goto_matchsetting(self):

        self.find_app_element(self.setting)
        from Page.settingPage import Setting
        return Setting(self.driver)

    def get_recommed_text(self):

        text = self.find_app_element(self.recommend).text
        return text

    def goto_recommedtoday(self):
        self.find_app_element(self.recommend)
        return self

    def click_explore(self):
        Log.print_console("info", "点击精选tab，进去精选页面")
        if self.is_element_exist(self.explore_id) is True:
            self.find_app_element(self.explore)
            return self
        else:
            self.click_explorecover()
            return self

    def click_explorecover(self):
        self.find_app_element(self.explorecover)
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
        self.find_app_element(self.blackvipbutton)
        from Page.blackvipPage import Blackvip
        return Blackvip(self.driver)

    def goto_likelist(self):
        self.find_app_element(self.likelist)
        from Page.heartfootprint import Heartfootprint
        return Heartfootprint(self.driver)

    def boy_explore_swipe(self, element):
        sleep(3)
        self.swipe_up()
        # 由于是imageview组建，用底层find_elements方法查找多个通过元素，通过列表长度来决定用那个元素去点击
        elements_list = self.driver.find_elements(AppiumBy.ID, self.user_profile_id)
        # 当列表长度大于1时，用最后一个元素去点击
        if len(elements_list) > 1:
            # self.find_app_element(self.user_profile_index_2)
            Log.print_console("info", "列表长度大于1，用第二个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[1]
            # super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
            # 判断传入的元素是超喜欢/喜欢/无感 然后在进行对应的操作
            if element == self.recommendsuperlike:
                Log.print_console("info", "进入对方资料页点击超喜欢按钮，并匹配成功")
                self.find_app_element(element)
                self.find_app_element(self.superlikesure_id)
                if self.is_element_exist(self.black_vip_skip_str) is True:
                    self.find_app_element(self.black_vip_skip)
                else:
                    Log.print_console("info", "超喜欢统一都是弹同性匹配成功弹窗")
                    if self.is_element_exist(self.sex_match_success_send_str_id):
                        Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                        self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                        self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
                    else:
                        Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                        self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
            elif element == self.recommendlike:
                self.find_app_element(element)
                Log.print_console("info", "点喜欢匹配成功，点击继续匹配按钮并关闭页面")
                self.driver.find_element(AppiumBy.ID, self.boy_match_success_continue_id)

            else:
                self.find_app_element(element)

        else:
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[0]
            # super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
            Log.print_console("info", "进入对方资料页点击超喜欢按钮，并匹配成功")
            if element == self.recommendsuperlike:
                self.find_app_element(element)
                self.find_app_element(self.superlikesure_id)
                if self.is_element_exist(self.black_vip_skip_str) is True:
                    self.find_app_element(self.black_vip_skip)
                else:
                    Log.print_console("info", "超喜欢统一都是弹同性匹配成功弹窗")
                    if self.is_element_exist(self.sex_match_success_send_str_id):
                        Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                        self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                        self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
                    else:
                        Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                        self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
            elif element == self.recommendlike:
                self.find_app_element(element)
                Log.print_console("info", "点喜欢匹配成功，点击继续匹配按钮并关闭页面")
                self.driver.find_element(AppiumBy.ID, self.boy_match_success_continue_id)

            else:
                Log.print_console("info", "点击对方资料页无感按钮")
                self.find_app_element(element)

    #女号的精选匹配成功需要再完善几种case！！！！
    def girl_explore_swipe(self):
        sleep(3)
        self.swipe_up()
        # 由于是imageview组建，用底层find_elements方法查找多个通过元素，通过列表长度来决定用那个元素去点击
        elements_list = self.driver.find_elements(AppiumBy.ID, self.user_profile_id)
        # 当列表长度大于1时，用最后一个元素去点击
        if len(elements_list) > 1:
            # self.find_app_element(self.user_profile_index_2)
            Log.print_console("info", "列表长度大于1，用第二个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[1]
            # super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
            # 判断传入的元素是超喜欢/喜欢/无感 然后在进行对应的操作
            # if element == self.recommendsuperlike:
            Log.print_console("info", "进入对方资料页点击超喜欢按钮，并匹配成功")
            self.find_app_element(self.recommendsuperlike)
            self.find_app_element(self.superlikesure_id)
            if self.is_element_exist(self.black_vip_skip_str) is True:
                self.find_app_element(self.black_vip_skip)
            else:
                Log.print_console("info", "超喜欢统一都是弹同性匹配成功弹窗")
                if self.is_element_exist(self.sex_match_success_send_str_id):
                    Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
                else:
                    Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                    self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
            # elif element == self.recommendlike:
        else:
            Log.print_console("info", "列表长度小于1，用第一个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[0]
            # super_like_button = "com.intelcupid.shesay:id/ibControlSuper"
            # 判断传入的元素是超喜欢/喜欢/无感 然后在进行对应的操作
            # if element == self.recommendsuperlike:
            Log.print_console("info", "进入对方资料页点击超喜欢按钮，并匹配成功")
            self.find_app_element(self.recommendsuperlike)
            self.find_app_element(self.superlikesure_id)
            if self.is_element_exist(self.black_vip_skip_str) is True:
                self.find_app_element(self.black_vip_skip)
            else:
                Log.print_console("info", "超喜欢统一都是弹同性匹配成功弹窗")
                if self.is_element_exist(self.sex_match_success_send_str_id):
                    Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
                else:
                    Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                    self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)

        sleep(1)
        self.swipe_up()
        elements_list = self.driver.find_elements(AppiumBy.ID, self.user_profile_id)
        if len(elements_list) > 1:
            Log.print_console("info", "超喜欢完成后，滑动页面，进行点击喜欢操作")
            # 由于是imageview组建，用底层find_elements方法查找多个通过元素，通过列表长度来决定用那个元素去点击
            Log.print_console("info", "列表长度大于1，用第二个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[1]
            self.find_app_element(self.recommendlike)
            Log.print_console("info", "女号匹配成功，点击匹配成功弹窗上的选择新问题按钮跳转到出题页")
            self.find_app_element(self.match_success_new)
            Log.print_console("info", "选择直接打招呼并点击")
            self.find_app_element(self.skip_answer)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("直接打招呼")')
            Log.print_console("info", "跳转到与对方的私聊页，然后返回")
            self.find_app_element(self.profile_back)
        else:
            Log.print_console("info", "超喜欢完成后，滑动页面，进行点击喜欢操作")
            Log.print_console("info", "列表长度小于1，用第一个元素去点击")
            # 由于是imageview组建，用底层find_elements方法查找多个通过元素，通过列表长度来决定用那个元素去点击
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[0]
            self.find_app_element(self.recommendlike)
            Log.print_console("info", "女号匹配成功，点击匹配成功弹窗上的选择新问题按钮跳转到出题页")
            self.find_app_element(self.match_success_new)
            Log.print_console("info", "选择直接打招呼并点击")
            self.find_app_element(self.skip_answer)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("直接打招呼")')
            Log.print_console("info", "跳转到与对方的私聊页，然后返回")
            self.find_app_element(self.profile_back)

        sleep(1)
        self.swipe_up()
        elements_list = self.driver.find_elements(AppiumBy.ID, self.user_profile_id)
        if len(elements_list) > 1:
            Log.print_console("info", "列表长度大于1，用第二个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[1]
            Log.print_console("info", "滑动页面后，女号开始点击精选页面用户资料页喜欢按钮")
            self.find_app_element(self.recommendlike)
            # if self.is_element_exist(self.boy_match_success_close):
            Log.print_console("info", "女号点喜欢匹配成功，点击继续匹配按钮并关闭页面")
            self.find_app_element(self.match_success_continue)
        else:
            Log.print_console("info", "列表长度小于1，用第一个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[0]
            Log.print_console("info", "滑动页面后，女号开始点击精选页面用户资料页喜欢按钮")
            self.find_app_element(self.recommendlike)
            # if self.is_element_exist(self.boy_match_success_close):
            Log.print_console("info", "女号点喜欢匹配成功，点击继续匹配按钮并关闭页面")
            self.find_app_element(self.match_success_continue)
        sleep(1)
        self.swipe_up()
        elements_list = self.driver.find_elements(AppiumBy.ID, self.user_profile_id)
        if len(elements_list) > 1:
            Log.print_console("info", "列表长度大于1，用第二个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[1]
            Log.print_console("info", "女号精选页点喜欢匹配成功后点击发送上次问题")
            self.find_app_element(self.recommendlike)
            self.find_app_element(self.match_success_last_time)
            Log.print_console("info", "点击确认发送按钮发送问题")
            self.driver.find_element(AppiumBy.ID, self.superlikesure_id_str)
        else:
            Log.print_console("info", "列表长度小于1，用第一个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[0]
            Log.print_console("info", "女号精选页点喜欢匹配成功后点击发送上次问题")
            self.find_app_element(self.recommendlike)
            self.find_app_element(self.match_success_last_time)
            Log.print_console("info", "点击确认发送按钮发送问题")
            self.driver.find_element(AppiumBy.ID, self.superlikesure_id_str)

        sleep(1)
        self.swipe_up()
        elements_list = self.driver.find_elements(AppiumBy.ID, self.user_profile_id)
        if len(elements_list) > 1:
            Log.print_console("info", "列表长度大于1，用第二个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[1]
            Log.print_console("info", "女号精选页点喜欢匹配成功后点击发送上次问题")
            self.find_app_element(self.recommendlike)
            self.find_app_element(self.match_success_last_time)
            Log.print_console("info", "点击选择新问题")
            self.driver.find_element(AppiumBy.ID, self.black_vip_skip_str)
            Log.print_console("info", "跳转到出题页，先点击一下用户头像进入对方资料页在返回，在出题发送")
            self.find_app_element(self.user_profile)
            self.find_app_element(self.userprofile_back)
            # 判断有没有再出一题按钮
            if self.is_element_exist(self.question_add_str) is True:
                Log.print_console("info", "点击再出一题，选择题库，选完题目并发送")
                self.find_app_element(self.question_add)
                self.find_app_element(self.question_bank)
                # 弹窗右上角有关闭按钮，所以用底层find方法
                self.driver.find_elements(AppiumBy.ID, self.question_list_str)[0]
                self.find_app_element(self.send_answer_quest)
                Log.print_console("info", "获取发送题目成功toast进行断言")
                toast_text = self.get_toast()
                return toast_text
        else:
            Log.print_console("info", "列表长度小于1，用第一个元素去点击")
            self.driver.find_elements(AppiumBy.ID, self.user_profile_id)[0]
            Log.print_console("info", "女号精选页点喜欢匹配成功后点击发送上次问题")
            self.find_app_element(self.recommendlike)
            self.find_app_element(self.match_success_last_time)
            Log.print_console("info", "点击选择新问题")
            self.driver.find_element(AppiumBy.ID, self.black_vip_skip_str)
            Log.print_console("info", "跳转到出题页，先点击一下用户头像进入对方资料页在返回，在出题发送")
            self.find_app_element(self.user_profile)
            self.find_app_element(self.userprofile_back)
            # 判断有没有再出一题按钮
            if self.is_element_exist(self.question_add_str) is True:
                Log.print_console("info", "点击再出一题，选择题库，选完题目并发送")
                self.find_app_element(self.question_add)
                self.find_app_element(self.question_bank)
                # 弹窗右上角有关闭按钮，所以用底层find方法
                self.driver.find_elements(AppiumBy.ID, self.question_list_str)[0]
                self.find_app_element(self.send_answer_quest)
                Log.print_console("info", "获取发送题目成功toast进行断言")
                toast_text = self.get_toast()
                return toast_text

    def boy_goto_user_profile_and_back(self):
        Log.print_console("info", "切到精选页，点击精选页列表第一个用户的超喜欢按钮，并匹配成功")
        self.find_app_element(self.super_like_id)
        self.find_app_element(self.superlikesure_id)
        if self.is_element_exist(self.black_vip_skip_str) is True:
            self.find_app_element(self.black_vip_skip)
        else:
            if self.is_element_exist(self.sex_match_success_send_str_id):
                Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
            else:
                Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)

        Log.print_console("info", "开始滑动页面，并进入下一个用户资料页点击喜欢按钮匹配成功")
        self.boy_explore_swipe(self.recommendlike)
        Log.print_console("info", "开始滑动页面，并进入下一个用户资料页点击超喜欢按钮匹配成功")
        self.boy_explore_swipe(self.profile_super_like_id)
        Log.print_console("info", "开始滑动页面，并进入下一个用户资料页点击无感按钮")
        self.boy_explore_swipe(self.profile_pass_id)
        return self

    def girl_click_recommend_like_match_success_and_send_question(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "女号，开始点击推荐页喜欢按钮")
            self.find_app_element(self.recommendlike)
            Log.print_console("info", "女号匹配成功，点击发送上次问题按钮")
            self.find_app_element(self.match_success_last_time)
            Log.print_console("info", "点击确认发送按钮发送问题")
            self.driver.find_element(AppiumBy.ID, self.superlikesure_id_str)
            # self.find_app_element(self.send_answer_input).send_keys("今天吃的啥好吃的")
            # self.find_app_element(self.send_answer_quest)
            # 这里还没处理完,需要加从未出过题的逻辑,以及同性匹配逻辑
            # else:
            #     self.find_app_element(self.match_success_continue)
            return self
        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def girl_click_recommend_like_match_success_and_click_select_new_question(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "女号，开始点击推荐页喜欢按钮")
            self.find_app_element(self.recommendlike)
            Log.print_console("info", "女号匹配成功，点击匹配成功弹窗上的选择新问题按钮跳转到出题页")
            self.find_app_element(self.match_success_new)
            Log.print_console("info", "选择直接打招呼并点击")
            self.find_app_element(self.skip_answer)
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("直接打招呼")')
            Log.print_console("info", "跳转到与对方的私聊页，然后返回")
            self.find_app_element(self.profile_back)
            return self
        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def girl_click_recommend_like_match_success_click_continue(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "女号开始点击推荐页喜欢按钮")
            self.find_app_element(self.recommendlike)
            # if self.is_element_exist(self.boy_match_success_close):
            Log.print_console("info", "女号点喜欢匹配成功，点击继续匹配按钮并关闭页面")
            self.find_app_element(self.match_success_continue)
            return self
        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def girl_click_recommend_like_match_success_and_add_question_send(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "女号，开始点击推荐页喜欢按钮")
            self.find_app_element(self.recommendlike)
            Log.print_console("info", "女号匹配成功，点击发送上次问题按钮")
            self.find_app_element(self.match_success_last_time)
            Log.print_console("info", "点击选择新问题")
            self.driver.find_element(AppiumBy.ID, self.black_vip_skip_str)
            Log.print_console("info", "跳转到出题页，先点击一下用户头像进入对方资料页在返回，在出题发送")
            self.find_app_element(self.user_profile)
            self.find_app_element(self.userprofile_back)
            # 判断有没有再出一题按钮
            if self.is_element_exist(self.question_add_str) is True:
                Log.print_console("info", "点击再出一题，选择题库，选完题目并发送")
                self.find_app_element(self.question_add)
                self.find_app_element(self.question_bank)
                # 弹窗右上角有关闭按钮，所以用底层find方法
                self.driver.find_elements(AppiumBy.ID, self.question_list_str)[0]
                self.find_app_element(self.send_answer_quest)
                Log.print_console("info", "获取发送题目成功toast进行断言")
                toast_text = self.get_toast()
                return toast_text
            else:
                Log.print_console("info", "没有再出一题按钮证明是三个问题，先删除一个再添加")
                self.find_app_element(self.question_delect)
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("删除问题")')
                self.find_app_element(self.question_add)
                self.find_app_element(self.question_bank)
                # 弹窗右上角有关闭按钮，所以用底层find方法
                self.driver.find_elements(AppiumBy.ID, self.question_list_str)[0]
                self.find_app_element(self.send_answer_quest)
                Log.print_console("info", "获取发送题目成功toast进行断言")
                toast_text = self.get_toast()
                return toast_text

        else:
            Log.print_console("info", "没有找到推荐页喜欢按钮的ID，直接return，进行下一条case")
            return self

    def girl_click_recommend_super_like_and_sex_match_success(self):
        if self.is_element_exist(self.recommendliketext):
            Log.print_console("info", "女号开始点击推荐页超喜欢按钮")
            self.find_app_element(self.recommendsuperlike)
            if self.is_element_exist(self.superhelp_text):
                Log.print_console("info", "判断如果没有超喜欢个数，直接关闭购买弹窗")
                self.find_app_element(self.matchclose)
                return self
            else:
                Log.print_console("info", "开始点击超喜欢弹窗上的确定按钮，送出超喜欢")
                self.find_app_element(self.superlikesure_id)
                # 判断超喜欢匹配成功是否是同性匹配
                if self.is_element_exist(self.sex_match_success_send_str_id):
                    Log.print_console("info", "女号同性匹配成功点击随机打招呼语并发送")
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                    self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
                else:
                    Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                    self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
            return self
        else:
            Log.print_console("info", "没有找到推荐页超喜欢按钮的ID，直接return，进行下一条case")
            return self

    def girl_goto_user_profile_and_back(self):
        Log.print_console("info", "切到精选页，点击精选页列表第一个用户的超喜欢按钮，并匹配成功")
        self.find_app_element(self.super_like_id)
        self.find_app_element(self.superlikesure_id)
        if self.is_element_exist(self.black_vip_skip_str) is True:
            self.find_app_element(self.black_vip_skip)
        else:
            if self.is_element_exist(self.sex_match_success_send_str_id):
                Log.print_console("info", "同性匹配成功点击随机打招呼语并发送")
                self.driver.find_element(AppiumBy.ID, self.sex_match_success_change_hello_id)
                self.driver.find_element(AppiumBy.ID, self.sex_match_success_send_id)
            else:
                Log.print_console("info", "送出超喜欢并且匹配成功，点击匹配成功弹窗右上角关闭按钮")
                self.driver.find_element(AppiumBy.ID, self.boy_match_success_close)
        self.girl_explore_swipe()
        return self

