import pytest
from Page.recommendPage import recommEnd


class Testsetting:
    @pytest.mark.run(order=1)
    def test_setting_back(self, app_start):
        self.driver = app_start
        try:
            settingtext = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_back()
            assert "推荐" == settingtext.get_recommed_text()
        except:
            self.driver.launch_app()

    @pytest.mark.run(order=3)
    def test_setting_finish(self, app_start):
        self.driver = app_start
        try:
            recommEndtext = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_finish()
            assert "推荐" == recommEndtext.get_recommed_text()
        except:
            self.driver.launch_app()

    @pytest.mark.run(order=2)
    def test_click_locationback(self, app_start):
        self.driver = app_start
        try:
            back_to_recommend = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_location().click_back().click_back()
            assert "推荐" == back_to_recommend.get_recommed_text()
        except:
            self.driver.launch_app()
