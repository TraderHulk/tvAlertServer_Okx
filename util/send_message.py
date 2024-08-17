# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2021/4/8 1:48 PM

# File_name: 'send+_message.py'

"""
Describe: this is a demo!
"""


import requests
import json

class DingPushMessage(object):
    """钉钉推送 钉钉群消息"""

    @classmethod
    def ding_push_message(cls,msg,access_token,keywords):
        """
        推送消息
        :param msg: 推送的消息
        :param access_token: 权限token
        :param keywords: 权限设置的keyword,用于发送消息。
        :return:
        """
        web_url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(access_token)

        # 构建请求头部
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        # 构建请求数据
        message = {
            "msgtype": "text",
            "text": {
                "content": keywords+"："+msg
            },
            "at": {
                "isAtAll": True
            }
        }
        # 对请求的数据进行json封装
        message_json = json.dumps(message)
        # 发送请求
        info = requests.post(url=web_url, data=message_json, headers=header)
        # 打印返回的结果
        # print(info.text) #{"errcode":0,"errmsg":"ok"}
        return json.loads(info.text)



class FeiShuMessage(object):

    @classmethod
    def send_text(cls,Text, bot_id):
        """发送普通消息"""
        url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot_id}"
        headers = {"Content-Type": "text/plain"}
        data = {
            "msg_type": "text",
            "content": {
                "text": Text
            }
        }
        r = requests.post(url, headers=headers, json=data)
        return r.text


if __name__ == "__main__":
    FeiShuMessage.send_text(Text="test",bot_id="f5f3b5a4-e3a7-4a65-a61d-65842f6037de")





