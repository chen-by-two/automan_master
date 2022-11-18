# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import Common.HttpTools as http
from Common.LoggerHandler import MyLog as Log
import json
import Common.JsonTools as jsonTools

class httpHandler:
    def __init__(self):
        self.log = Log.get_log()
        self.jsonTool = jsonTools
        self.logger = self.log.logger
        self.headers  = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
        self.host = "http://java.goodscenter.mng.turboradio.cn"
        self.path = ""
        self.params = {}
        self.data = {}
        self.response = None

    #修改参数 0修改bodydata，1修改url后parmas
    def modifyJson(self,i,key,value):
        if i == 0:
            self.jsonTool.modifyJson(self.data,key,value)
        elif i == 1:
            self.jsonTool.modifyJson(self.params,key,value)
        else:
            self.logger.error("修改参数失败")

    #执行接口调用，0是get，1是post
    def run(self,method):
        httpExcute = http.httpTools();
        httpExcute.set_url(self.host+self.path)
        httpExcute.set_headers(self.headers)
        httpExcute.set_data(json.dumps(self.data))
        httpExcute.set_params(self.params)
        if method == 0:
            res = httpExcute.get()
        if method == 1:
            res = httpExcute.post()
        self.logger.info(res.text)
        return res