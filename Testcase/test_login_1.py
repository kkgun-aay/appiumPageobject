import pytest
from Page.loginPage import Login
from Utils.get_function_name import get__function_name


@pytest.mark.run(order=1)
class TestLogin:

    def test_gettoast_login(self, app_start):
        self.driver = app_start
        try:
            get_toast = Login(self.driver).not_serach_wechat()
            assert "请先阅读并同意" in get_toast
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    def test_login_to_recommend(self, app_start):
        self.driver = app_start
        try:
            recommendText = Login(self.driver).app_login().get_recommed_text()
            assert "推荐" == recommendText
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False


if __name__ == "__main__":
    # pytest.main(['-q', '-s'])
    pytest.main(['-q', '-s', 'test_login_1.py', 'test_recommend.py'])