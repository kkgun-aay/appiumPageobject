# -*- coding: utf-8 -*-
from time import sleep
from appium import webdriver
import pytest
# from Base.app import App
from Base.more_devices_app import App
from Page.loginPage import Login
from Utils.install_apk import installapk
import multiprocessing


# path = "/Users/lvxs/Desktop/androidapk"
# print("先安装最新release包，然后在启动apk")
# installapk(path)

# driver = None

# 注册自定义参数cmdopt到配置对象
def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


# 从配置对象获取cmdopt的值
@pytest.fixture(scope="session")
def cmd_opt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope="session")
def app_start(cmd_opt):
    cmd_opt = eval(cmd_opt)
    driver = App().app_start(cmd_opt)
    yield driver
    driver.quit()

    # return driver


# @pytest.fixture(scope="session")
# def app_start():
#     uid_list = ['feee6ee6', 'e6d4e140']
#     for i in range(len(uid_list)):
#         port = 4723 + 2 * i
#         driver = App().app_start(uid_list[i], port)
#         # yield driver
#
#     return driver





