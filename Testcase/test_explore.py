import sys
from Page.recommendPage import recommEnd
from Utils.get_function_name import get__function_name


class Testexplroe:
    def testexplore(self, app_start):
        self.driver = app_start
        try:
            explore_text = recommEnd(self.driver).goto_recommedtoday().click_explore().goto_user_profile_and_back().find_explore()
            assert "精选" == explore_text
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False