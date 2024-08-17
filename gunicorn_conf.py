# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: hxc
# CreatDate: 2020/3/17 10:30
# !/home/xx/.virtualenvs/xx/bin/python
# encoding: utf-8
# gunicorn 配置文件
"""
运行方式
gunicorn -c gunicorn_conf.py service:app
"""
import multiprocessing
import os

# import gevent.monkey
# gevent.monkey.patch_all()


# 监听端口
bind = '{}:{}'.format('0.0.0.0', 80)
# 工作模式  使用uvicorn模式 fastapi 使用以下工作模式
worker_class = 'uvicorn.workers.UvicornWorker'
# worker_class = "uvicorn.workers.UvicornH11Worker"

# 启动的进程数
# workers = multiprocessing.cpu_count() * 2 + 1
# 最少2个 这样可以保证一个挂掉的时候可以使用另一个
workers = 2
# 设置守护进程
daemon = True

# 设置日志记录水平
# loglevel = 'debug'
loglevel = 'info'
# 设置错误信息日志路径
errorlog = "log/fast_error.log"
# 设置访问日志路径
accesslog = "log/fast_access.log"
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 把print 写入到日志里
capture_output = True
# uvicorn 无效
# 代码更新时将重启工作，默认为False。此设置用于开发，每当应用程序发生更改时，都会导致工作重新启动。

# https时设置证书位置
# certfile='/etc/nginx/cert/1_wujie.rpaii.com_bundle.crt'
# keyfile='/etc/nginx/cert/2_wujie.rpaii.com.key'
# 设置超时时间
timeout = 600
