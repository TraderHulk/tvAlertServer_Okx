# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2022/9/6 10:31 PM

# File_name: 'parsingStrategy.py'

"""
Describe: this is a demo!
"""
import base64
import logging
from configs.config import longComment,shortComment,tpLongComment,tpShortComment
from src.autoTraderBot import AutoTraderBotGroup



class StratgyManger(object):
    """策略管理器"""

    def __init__(self):
        # 下单方向
        self.longComment = longComment
        self.shortComment = shortComment
        # 出局方向
        self.tpLongComment = tpLongComment
        self.tpShortComment = tpShortComment

    def __parsingSide_comment(self,comment):
        """解析方向"""
        signal = "无"

        if comment in self.longComment:
            signal = "long"
        elif comment in self.shortComment:
            signal = "short"
        elif comment in self.tpLongComment:
            signal = "tp_long"
        elif comment in self.tpShortComment:
            signal = "tp_short"
        elif "tp_long_" in comment:
            #平一份多单
            signal = "tp_long_batch"
        elif "tp_short_" in comment:
            # 平一份空单
            signal =  "tp_short_batch"

        return signal

    def jiemi(self, api_code):
        """进行解密"""
        apiinfo_base642 = api_code.replace("TVAlert", "==")
        api_info1 = base64.b64decode(apiinfo_base642).decode()
        api_info = base64.b64decode(api_info1).decode()
        api_info_list = api_info.split("az@@@za")
        api_key, secretKey, passphrase = api_info_list[0], api_info_list[1], api_info_list[2]
        return api_key, secretKey, passphrase

    def parsingMsg(self,req_data):
        """进行解析tv给的消息"""
        result = {"symbol":"","side":"","status":"-1","msg": ""}

        # 解析信息
        strategyName = req_data.strategyName
        exchange = req_data.exchange
        symbol = req_data.symbol
        price = req_data.price

        #判断是固定数量还是固定金额还是固定金额比例
        #默认是数量
        qty = req_data.qty
        batch_qty = req_data.batch_qty
        qty_flag = req_data.qty_flag
        diaccess_token = req_data.diaccess_token
        keyword = req_data.keyword
        feishu_bot_id = req_data.feishu_bot_id
        comment = req_data.comment
        #处理非策略的信号（比如指标型的警报）只在alert message 的时候使用 表示下单前的仓位状态
        prev_market_position = req_data.prev_market_position
        logging.info("先前的仓位状态:{}".format(prev_market_position))
        api_key = req_data.api_key
        secretKey = req_data.secretKey
        passphrase = req_data.passphrase
        ai_code = req_data.ai_code
        # api 信息的解密
        if (api_key == "" or secretKey == ""  or  passphrase == "") and ai_code:
            api_key, secretKey, passphrase = self.jiemi(ai_code)
            api_key = api_key
            secretKey = secretKey
            passphrase = passphrase
        else:
            result['msg'] = "请填写api信息或者加密您的api信息"
            return result

        if "buy" in comment and prev_market_position == "flat":
            comment = "buy"
        elif "sell" in comment and prev_market_position == "flat":
            comment = "sell"
        elif "buy" in comment and prev_market_position in ["sell", "short"]:
            comment = "tp_short"
        elif "sell" in comment and prev_market_position in ["buy", "long"]:
            comment = "tp_long"

        signal = self.__parsingSide_comment(comment=comment)

        # 初始化一个自动交易机器人组
        autoTraderBot = AutoTraderBotGroup(exchange=exchange, api_key=api_key, secretKey=secretKey,
                                           passphrase=passphrase, diaccess_token=diaccess_token,
                                           keyword=keyword,feishu_bot_id=feishu_bot_id)

        if qty_flag == "money":
            #固定金额
            qty_s = autoTraderBot.standard_qty(qty=float(qty) / float(price),symbol=symbol)
            batch_qty_s = autoTraderBot.standard_qty(qty=float(batch_qty) / float(price),symbol=symbol)

        elif qty_flag == "money_rate":
            #固定金额比例
            usdt = autoTraderBot.get_usdt()
            qty_s = autoTraderBot.standard_qty(qty=float(usdt)*float(qty) / float(price),symbol=symbol)
            batch_qty_s = autoTraderBot.standard_qty(qty=float(usdt)*float(batch_qty) / float(price),symbol=symbol)
        else:
            #固定数量（张数）
            qty_s = qty
            batch_qty_s = batch_qty


        if "batch" in signal:
            logging.info("batch_qty:{}".format(batch_qty_s))
            autoTraderBot.onTick(symbol=symbol, price=price, signal=signal, qty=batch_qty_s, strategyName=strategyName)
        else:
            logging.info("qty:{}".format(qty_s))
            autoTraderBot.onTick(symbol=symbol, price=price, signal=signal, qty=qty_s, strategyName=strategyName)

        result["symbol"] = symbol
        result['side'] = signal
        result['status'] = 200
        result['msg'] = '交易执行完毕！！！'

        return result




















