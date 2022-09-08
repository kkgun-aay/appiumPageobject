import requests
import json


class seed_message:

    @classmethod
    def seedmessage(cls, str):
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/1458dac4-7e74-44ed-afa5-81e6a97c0b7d'

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            "msgtype": "text",
            "title": "AppUI自动化测试",
            "text": str
             }
        resq = requests.post(url, data=json.dumps(data), headers=headers)
        if resq.status_code == 200 and resq.json()['ok'] is not False:
            # print(resq.json())
            print('消息发送成功')
        else:
            print('发送失败errcode{}'.format(resq.json()) )