import pytest
from Page.recommendPage import recommEnd


@pytest.mark.run(order=-1)
class Testmyhomesetting:
    def testmyhomesetting(self, app_start):
        self.driver = app_start
        try:
            agreementtext = recommEnd(self.driver).goto_myhome().click_myhome_setting().click_logout().get_agreement_text()
            assert "《用户协议》" == agreementtext
        except:
            self.driver.close_app()
