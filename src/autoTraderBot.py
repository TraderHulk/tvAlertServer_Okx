# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2022/10/14 6:01 PM

# File_name: 'autoTraderBot.py'

"""
Describe: this is a demo!
"""
import logging
import datetime
from util.send_message import DingPushMessage,FeiShuMessage
from exchange.okk_swap import OkkSwap


class AutoTraderBotGroup():
    """自动交易机器人组"""

    def __init__(self,exchange,api_key,secretKey,passphrase,diaccess_token="",keyword="",feishu_bot_id=""):

        self.exchange = exchange
        self.diaccess_token=diaccess_token
        self.keyword =keyword
        self.feishu_bot_id = feishu_bot_id

        #更新交易所进行初始化不同机器人
        try:
            #初始化okk交易组机器人
            self.okk_bot = OkkSwap(api_key=api_key,secret_key=secretKey,passphrase=passphrase)
        except Exception as e:
            logging.error("初始化失败,需要查看交易所的名称是否填写正确！！！",e)


    def send_message(self, msg):
        if self.diaccess_token and self.keyword:
            DingPushMessage.ding_push_message(msg=msg, access_token=self.diaccess_token,
                                              keywords=self.keyword)
        elif self.feishu_bot_id :
            FeiShuMessage.send_text(Text=msg,bot_id=self.feishu_bot_id)


    def standard_qty(self,qty,symbol):
        """标准化 数量"""
        qty = qty
        qty = self.okk_bot.get_standard_qty(qty=qty, symbol=symbol)
        return qty

    def get_usdt(self):
        """获取总usdt"""
        usdt = self.okk_bot.updatebalance()
        logging.info("交易所：{}".format(self.exchange))
        logging.info("账户余额：{}".format(usdt))

        return usdt

    def onTick(self,symbol,signal,price,qty,strategyName):
        """根据signal执行交易"""
        #调用okk机器人进行执行
        self.okk_bot.do_market(signal, symbol, qty)

        logging.info( "交易所：{}".format(self.exchange))
        logging.info("下单币种：{}".format(symbol))
        logging.info("下单价格：{}".format(price))
        logging.info("下单数量：{} \n".format(str(qty)))
        logging.info("下单方向：{}".format(signal))
        logging.info("下单时间：{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        logging.info("-------------" * 10)
        msg = "【{}策略】\n".format(strategyName) + "交易所：{} \n".format(self.exchange) +\
              "下单币种：{} \n".format(symbol) + "下单价格：{} \n".format(price) +\
              "下单方向：{} \n".format(signal) + "下单数量：{} \n".format(str(qty)) +\
              "下单时间：{} \n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.send_message(msg)


