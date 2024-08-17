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
        测试 alert_message 发出的信息
        :return:
        """
        t = time.time()
        url = "http://10:80/tvAlerServer/api/trade"

        input = {
            "exchange": "okx",
            "symbol": "ORDI-USDT-SWAP",
            "comment": "订单buy@7.689",
            "prev_market_position": "sell",
            "price": "{{strategy.order.price}}",
            "qty": "10",
            "batch_qty": "5",
            "ai_code": "TVdVMk1ESmmpGaVltTmtOV1JtYcEFRRUI2WVVoMVlXNW5NVEF4T0VBPQTVAlert",
            "diaccess_token": "",
            "keyword": "",
            "feishu_bot_id": ""
        }

        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(input)
        print(type(data))

        res = requests.post(url, data, headers=headers)
        print(res)
        print(json.dumps(res.json(), indent=4, ensure_ascii=False))
        print(time.time() - t)

if __name__ == '__main__':
    unittest.main()
