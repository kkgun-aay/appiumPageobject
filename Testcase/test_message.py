from Page.recommendPage import recommEnd
from Utils.get_function_name import get__function_name
from Utils.get_log import Log


class Testmessage:
    def testmessage(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info","点击消息tab，进入到消息页，进行断言")
            messagetext = recommEnd(self.driver).goto_message().get_message_tab_text()
        # messagetext = MessagePage(self.driver).click_message_tab().get_message_tab_text()

            assert "消息" == messagetext
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False
