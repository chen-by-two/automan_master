# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import requests
import Common.ReadConfig as readConfig
from Common.LoggerHandler import MyLog as Log


localReadConfig = readConfig.readConfig()


class httpTools:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.json = None

    def set_url(self, url):
        self.url = url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, data = self.data,headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            self.logger.info(response.url)
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,timeout=float(timeout))
            self.logger.info(self.data)
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ == '__main__':
    http1 = httpTools()
    http1.set_url("http://java.goodscenter.mng.turboradio.cn/spu/save")
    http1.set_headers({"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"})
    #http1.set_json({"goodsType":"1","goodsSubType":"11","cateName":["12815"],"cateId":"12815","goodsName":"刘昊然测试1592314435","enName":None,"approvalNumber":"1592314435","dosage":None,"form":None,"manufacturer":None,"deleted":0,"id":None,"attrs":None})
    http1.set_data({"goodsType":"1","goodsSubType":"11","cateName":["12815"],"cateId":"12815","goodsName":"刘昊然测试1592314435","enName":None,"approvalNumber":"1592314435","dosage":None,"form":None,"manufacturer":None,"deleted":0,"id":None,"attrs":None})
    http1.logger.info("请求ulr地址" + http1.url)

    http1.logger.info("返回结果"+http1.get().text)
