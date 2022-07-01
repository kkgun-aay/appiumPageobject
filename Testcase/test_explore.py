import sys
from Page.recommendPage import recommEnd


class Testexplroe:
    def testexplore(self, app_start):
        self.driver = app_start
        try:
            explore_text = recommEnd(self.driver).goto_recommedtoday().click_explore().goto_user_profile_and_back().find_explore()
            assert "精选" == explore_text
        except:
            self.driver.launch_app()