# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2022/9/6 11:39 PM

# File_name: 'config.py'

"""
Describe: this is a demo!
"""
import base64
from easydict import EasyDict as edict


__C = edict()
cfg = __C

#brokerTag
__C.BINANCEBROKERTAG = ""
__C.OKXROKERTAG = ""



# database config
__C.DBCONFIG = edict()
__C.DBCONFIG.MINCACHED = 5
__C.DBCONFIG.MAXCACHED = 10
__C.DBCONFIG.MAXCONNECTIONS = 50
__C.DBCONFIG.BLOCKING = True
__C.DBCONFIG.MAXSHARED = 51

#机器人配置
#做多 的comment 取值范围
longComment = ["buy","long","entry_long","entry_buy","B","b","BUY","LONG"]
#做空 的comment 取值范围
shortComment = ["sell","short","entry_short","entry_sell","S","s","SELL","SHORT"]
#平多 的comment 取值范围
tpLongComment =  ["tp_buy","tp_long","TP_BUY","TP_LONG","TP-BUY","TP-LONG","close_buy","close_long","CLOSE_BUY","exit_buy","exit_long","EXIT_BUY"]
#平空 的comment 取值范围
tpShortComment = ["tp_sell","tp_short","TP_SELL","TP_SHORT","TP-SELL","TP-SHORT","close_sell","close_short","CLOSE_SELL","exit_sell","exit_short","EXIT_SELL"]









