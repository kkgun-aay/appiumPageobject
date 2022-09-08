# -*- coding: utf-8 -*-
from Page.recommendPage import recommEnd
import pytest
from Utils.get_function_name import get__function_name
from Utils.get_log import Log


class Testdiscover:

    # @pytest.mark.run(order=1)
    def test_discover(self,app_start):
        self.driver = app_start

        try:
            Log.print_console("info", "点击发现按钮，进到发现页")
            resonateText = recommEnd(self.driver).goto_discover().get_resonate_text()
            assert "共鸣" == resonateText
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    # @pytest.mark.run(order=2)
    def test_discover_all_btn(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info", "进到发现页，点击选星球按钮，点击确定，点击收件箱然后返回，点击飞行按钮进入飞行页面,断言飞行按钮文案")
            text = recommEnd(self.driver).goto_discover().goto_signal_page().click_resonate_change().click_resonate_bell().click_flash()
            assert "轻触屏幕 马上开聊" == text
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    # @pytest.mark.run(order=3)
    def test_create_signal_success(self, app_start):
        self.driver = app_start
        try:
            Log.print_console("info", "点击发布底部发布信号按钮，选第一个话题，写文字，然后发布信号并返回，断言返回后是否在共鸣页面")
            text = recommEnd(self.driver).goto_discover().goto_signal_page().click_create_signal().get_resonate_text()
            assert "共鸣" == text
        except:
            Log.print_console("info","{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False



