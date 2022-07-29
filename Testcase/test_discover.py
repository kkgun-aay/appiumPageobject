# -*- coding: utf-8 -*-
from Page.recommendPage import recommEnd
import pytest
from Utils.get_function_name import get__function_name


class Testdiscover:

    # @pytest.mark.run(order=1)
    def test_discover(self,app_start):
        self.driver = app_start

        try:
            resonateText = recommEnd(self.driver).goto_discover().get_resonate_text()
            assert "共鸣" == resonateText
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    # @pytest.mark.run(order=2)
    def test_discover_all_btn(self, app_start):
        self.driver = app_start
        try:
            text = recommEnd(self.driver).goto_discover().goto_signal_page().click_resonate_change().click_resonate_bell().click_flash()
            assert "轻触屏幕 马上开聊" == text
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False

    # @pytest.mark.run(order=3)
    def test_create_signal_success(self, app_start):
        self.driver = app_start
        try:
            text = recommEnd(self.driver).goto_discover().goto_signal_page().click_create_signal().get_resonate_text()
            assert "共鸣" == text
        except:
            print("{}函数执行失败".format(get__function_name()))
            self.driver.launch_app()
            assert False



