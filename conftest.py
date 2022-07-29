# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
import pytest
from Base.app import App
from Utils.install_apk import installapk


# path = "/Users/lvxs/Desktop/androidapk"
# print("先安装最新release包，然后在启动apk")
# installapk(path)

# driver = None


@pytest.fixture(scope="session")
def app_start():
    driver = App().app_start()
    return driver


