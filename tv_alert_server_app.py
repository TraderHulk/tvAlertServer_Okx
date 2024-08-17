# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2022/5/31 4:40 PM

# File_name: 'start_run.py'

"""
Describe: this is a demo!
"""
import uvicorn
import logging.config
from os import path
from fastapi import FastAPI
from pydantic import BaseModel
from src.manager import StratgyManger



class InputDataItem(BaseModel):
    """输入数据对象"""
    exchange:str = "okx"
    symbol:str = ""
    price:str = ""
    qty:str = ""
    batch_qty :str = "" #分批止盈止损的时候用的qty
    qty_flag :str = "" #是固定数量还是固定金额还是固定金额比例 取值：qty/money/moeny_rate
    strategyName:str = "" #策略名称
    ai_code :str = ""
    api_key :str = "" #加密的时候必须要填写
    secretKey:str = "" #加密的时候必须要填写
    passphrase:str = "" #加密的时候必须要填写
    diaccess_token:str = "" #支持钉钉发送交易信息
    keyword:str=""
    feishu_bot_id:str=""#支持飞书发送交易信息
    action:str=""
    comment:str = ""
    prev_market_position: str = "" #只在alert message 的时候使用 表示下单前的仓位状态


# 导入日志配置文件
log_file_path = path.join(path.dirname(path.abspath(__file__)), "configs/logging.conf")
logging.config.fileConfig(log_file_path)
# 创建日志对象
logger = logging.getLogger()
loggerInfo = logging.getLogger("TimeInfoLogger")
Consolelogger = logging.getLogger("ConsoleLogger")
app = FastAPI()
sm = StratgyManger()

@app.post("/tvAlerServer/api/trade")
async def tv_service(res_item:InputDataItem):
    """tv自动交易服务"""
    try:
        res= sm.parsingMsg(req_data=res_item)
    except Exception as e:
        logging.error("app 服务报错，报错信息："+str(e))

        res = {"msg":"报错"}
    logging.info(res)
    return res


if __name__ == '__main__':
    uvicorn.run(app='tv_alert_server_app:app', host="127.0.0.1", port=80, reload=True)











