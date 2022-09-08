import re
from time import sleep

from ppadb.client import Client as AdbClient
import os

client = AdbClient(host="127.0.0.1", port=5037)
# client.device("feee6ee6")
devices = client.devices()


def installapk(path):
    apkpath = file_name(path)
    for device in devices:
        # print(device.is_installed("com.intelcupid.shesay"))
        bool = device.is_installed("com.intelcupid.shesay")
        if bool is True:
            device.uninstall("com.intelcupid.shesay")
            device.install(apkpath)
        else:
            device.install(apkpath)


def get_onactivity():
    sleep(2)
    # patter_text = "\s.*u0.(.+)\s\w+"
    patter_text = "\s.*u0.(.+)/.[a-z]\w+"
    for device in devices:
        activity = device.shell("dumpsys activity | grep mResumedActivity")
        text = re.search(patter_text, activity)
        if "com.intelcupid.shesay" in text.group(1):
            # print("app正常")
            return True
        else:
            return False


def get_mobi_devices():
    for device in devices:
        mobi_devices = device.shell("getprop ro.product.model")
        print(mobi_devices)
        return mobi_devices


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.apk':
                L.append(os.path.join(root, file))
    print(L[0])
    return L[0]


if __name__ == "__main__":
    path = "/Users/lvxs/Desktop/androidapk"
    # file_name(path)
    # installapk(path)
    # get_onactivity()
    get_mobi_devices()