# -*- coding: utf-8 -*-
import pytest
from Page.recommendPage import recommEnd


class Testdiscover:

    @pytest.mark.run(order=1)
    def test_discover(self,appstart):
        self.driver = appstart
        resonateText = recommEnd(self.driver).goto_discover().get_resonate_text()
        assert "共鸣" == resonateText

    @pytest.mark.run(order=2)
    def test_discover_all_btn(self, appstart):
        self.driver = appstart
        text = recommEnd(self.driver).goto_discover().goto_signal_page().click_resonate_change().click_resonate_bell().click_flash()
        assert "轻触屏幕 马上开聊" == text

    @pytest.mark.run(order=3)
    def test_create_signal_success(self, appstart):
        self.driver = appstart
        text = recommEnd(self.driver).goto_discover().goto_signal_page().click_create_signal().get_resonate_text()
        assert "共鸣" == text



