# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2022/9/7 12:15 AM

# File_name: 'testTvAlterServer_okx.py'

"""
Describe: this is a demo!
"""


import time
import unittest
import requests
import json

class TestTvAlterServer(unittest.TestCase):

    def testFLModelService(self):
        """
        测试 自动对接tv 警报服务
        :return:
        """
        t = time.time()
        url = "http://16.122:80/tvAlerServer/api/trade"
        input ={
  "exchange": "okx",
  "symbol": "SUSHI-USDT-SWAP",
  "comment": "long",
  "price": "{{strategy.order.price}}",
  "qty": "2",
  "batch_qty": "1",
  "qty_flag": "qty",
  "ai_code": "WXpoa01VhwQVFFQjZZVEExUVVaQ09EQk6TkVRek56WTRNekkzT1RRMFlYcEFRRUI2WVVoMVlXNW5NVEF4T0VBPQTVAlert",
  "diaccess_token": "【非必填，钉钉群机器人的token】",
  "keyword": "【非必填，钉钉群机器人的keyword】",
  "feishu_bot_id": "【非必填，如果你有飞书群机器人的bot id 就可以填】"
}

        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(input)
        print(type(data))

        res = requests.post(url, data, headers=headers)
        print(res)
        print(json.dumps(res.json(), indent=4, ensure_ascii=False,sort_keys=False))
        print(time.time() - t)

if __name__ == '__main__':
    unittest.main()
