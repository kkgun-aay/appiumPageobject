import pytest
from Page.recommendPage import recommEnd


@pytest.mark.run(order=-1)
class Testmyhomesetting:
    def testmyhomesetting(self, appstart):
        self.driver = appstart
        agreementtext = recommEnd(self.driver).goto_myhome().click_myhome_setting().click_logout().get_agreement_text()
        assert "《用户协议》" == agreementtext
        self.driver.close_app()
