from Page.recommendPage import recommEnd


class Testexplroe:

    def testexplore(self, appstart):

        self.driver = appstart
        explore_text = recommEnd(self.driver).goto_recommedtoday().click_explore().goto_user_profile_and_back().find_explore()
        assert "精选" == explore_text