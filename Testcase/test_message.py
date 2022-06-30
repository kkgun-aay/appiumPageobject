from Page.recommendPage import recommEnd


class Testmessage:
    def testmessage(self, appstart):
        self.driver = appstart
        messagetext = recommEnd(self.driver).goto_message().get_message_tab_text()
        # messagetext = MessagePage(self.driver).click_message_tab().get_message_tab_text()

        assert "消息" == messagetext
