# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class Phone(httpHandler):
	def __init__(self):
		super(Phone, self).__init__()
		self.host = "https://api.vvhan.com"
		self.path = "/api/phone"
		self.headers = None
		self.params = {"tel":"15951652383"}
		self.data = None

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		# if self.params != None:
		# 	for k in self.params.keys():
		# 		self.path = self.path+self.params[k]
		self.response = self.run(0)
		self.logger.info(self.path +"	done" + "	手机号归属地查询API接口")
		return self.response