from Page.recommendPage import recommEnd
from Utils.get_function_name import get__function_name


class Testmessage:
    def testmessage(self, app_start):
        self.driver = app_start
        try:
            messagetext = recommEnd(self.driver).goto_message().get_message_tab_text()
        # messagetext = MessagePage(self.driver).click_message_tab().get_message_tab_text()

            assert "消息" == messagetext
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False
