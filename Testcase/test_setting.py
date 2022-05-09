import pytest
from Page.recommendPage import recommEnd


class Testsetting:

    @pytest.mark.run(order=1)
    def test_setting_back(self, appstart):
        self.driver = appstart
        settingtext = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_back()
        assert "推荐" == settingtext.get_recommed_text()

    @pytest.mark.run(order=3)
    def test_setting_finish(self, appstart):
        self.driver = appstart
        recommEndtext = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_finish()
        assert "推荐" == recommEndtext.get_recommed_text()

    @pytest.mark.run(order=2)
    def test_click_locationback(self, appstart):
        self.driver = appstart
        back_to_recommend = recommEnd(self.driver).goto_recommedtoday().goto_matchsetting().click_location().click_back().click_back()
        assert "推荐" == back_to_recommend.get_recommed_text()
