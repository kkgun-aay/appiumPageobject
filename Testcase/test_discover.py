# -*- coding: utf-8 -*-
import pytest
# from Base.app import App
from Page.loginPage import Login
from Page.recommendPage import recommEnd


class Testdiscover:

    def testdiscover(self,appstart):

        self.driver = appstart
        resonateText = recommEnd(self.driver).goto_discover().get_resonate_text()
        assert "共鸣" == resonateText


if __name__ == "__main__":
    pytest.main(['-q','-s'])