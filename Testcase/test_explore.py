from Page.recommendPage import recommEnd
from Utils.get_function_name import get__function_name
from Utils.get_log import Log


class Testexplroe:
    def testexplore(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info", "点击精选按钮，点击列表第一个人进入对方资料页，如果还没点喜欢，进行点喜欢操作并返回到精选页面，进行断言")
            explore_text = recommEnd(self.driver).goto_recommedtoday().click_explore().goto_user_profile_and_back().find_explore()
            assert "精选" == explore_text
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False