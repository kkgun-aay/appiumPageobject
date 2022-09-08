import pytest
from Page.loginPage import Login
from Utils.get_function_name import get__function_name
from Utils.get_log import Log


@pytest.mark.run(order=1)
class TestLogin:

    # def test_get_activity(self, app_start):
    #     self.driver = app_start
    #     try:
    #         get_toast = Login(self.driver).get_now_activity()
    #         print(get_toast)
    #         # assert "请先阅读并同意" in get_toast
    #     except:
    #         print("{}函数执行失败".format(get__function_name()))
    #         self.driver.launch_app()
    #         assert False

    def test_gettoast_login(self, app_start):
        self.driver = app_start

        try:
            Log.print_console("info","未勾选用户协议时点击微信icon")
            get_toast = Login(self.driver).not_serach_wechat()
            assert "请先阅读并同意" in get_toast
        except:
            Log.print_console("info", "{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    def test_login_to_recommend(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info", "勾选用户协议后，点击微信icon登录")
            recommendText = Login(self.driver).app_login().get_recommed_text()
            assert "推荐" == recommendText
        except:
            Log.print_console("info", "{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False


if __name__ == "__main__":
    # pytest.main(['-q', '-s'])
    pytest.main(['-q', '-s', '--reruns=2', 'test_login_1.py'])