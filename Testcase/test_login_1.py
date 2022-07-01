import pytest
from Page.loginPage import Login


@pytest.mark.run(order=1)
class TestLogin:
    def testlogin(self, appstart):
        self.driver = appstart
        get_toast = Login(self.driver).not_serach_wechat()
        assert "请先阅读并同意" in get_toast

        recommendText = Login(self.driver).app_login().get_recommed_text()
        assert "推荐" == recommendText


if __name__ == "__main__":
    # pytest.main(['-q', '-s'])
    pytest.main(['-q', '-s', "test_recommend.py", "test_discover.py"])