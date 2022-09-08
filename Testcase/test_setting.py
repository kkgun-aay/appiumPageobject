import pytest
from Page.recommendPage import recommEnd
from Utils.get_function_name import get__function_name
from Utils.get_log import Log


class Testsetting:
    # @pytest.mark.run(order=1)
    def test_setting_back(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info","点击匹配偏好按钮，直接返回，进行断言")
            settingtext = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_back()
            assert "推荐" == settingtext.get_recommed_text()
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    # @pytest.mark.run(order=3)
    def test_setting_finish(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info","点击匹配偏好按钮，点击右上角完成按钮，返回到推荐页进行断言")
            recommEndtext = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_finish()
            assert "推荐" == recommEndtext.get_recommed_text()
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    # @pytest.mark.run(order=2)
    def test_click_locationback(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info","点击匹配偏好，点击更改地理位置按钮，然后点击返回，再次点击返回到推荐页")
            back_to_recommend = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_location().click_back().click_back()
            assert "推荐" == back_to_recommend.get_recommed_text()
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False
