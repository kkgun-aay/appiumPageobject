import pytest
from Page.recommendPage import recommEnd
from Utils.get_function_name import get__function_name
from Utils.get_log import Log


@pytest.mark.run(order=-1)
class Testmyhomesetting:
    def testmyhomesetting(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info","点击我的按钮，，点击设置按钮，滑动到底部，点击退出登录，进行断言")
            agreementtext = recommEnd(self.driver).goto_myhome().click_myhome_setting().click_logout().get_agreement_text()
            assert "《用户协议》" == agreementtext
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.close_app()
            assert False
