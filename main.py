import pytest
from multiprocessing import Process,Pool


def run_case(device_info):
    pytest.main(["--cmdopt={}".format(device_info),'-q', '-s', '/Users/lvxs/PycharmProjects/sheSayUiTest/Testcase/test_login_1.py'])


if __name__ == '__main__':
    devices_infos = [{"udid": "feee6ee6", "port": "4723"}, {"udid": "e6d4e140", "port": "4725"}]

    with Pool(len(devices_infos)) as pool:
        # device_infos:要处理的数据列表，main：处理device_infos列表中数据的函数
        pool.map(run_case, devices_infos)  # 并行
        pool.close()  # 关闭进程池，不再接受新的进程
        pool.join()  # 主进程阻塞等待子进程的退出
