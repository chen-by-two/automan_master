# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class projectList(httpHandler):
	def __init__(self):
		super(projectList, self).__init__()
		self.host = "http://compensate.module.turboradio.cn"
		self.path = "/project/paging"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	权益中心项目列表")
		return self.response

class guaranteesActive(httpHandler):
	def __init__(self):
		super(guaranteesActive, self).__init__()
		self.host = "http://compensate.module.turboradio.cn"
		self.path = "/ie/guarantees/active"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = { "guaranteeId": "","orderNo":"92080101603753652181"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.data["orderNo"] +"	done" + "	该订单中的保障是否已激活")
		return self.response

class groupSum(httpHandler):
	def __init__(self):
		super(groupSum, self).__init__()
		self.host = "http://compensate.module.turboradio.cn"
		self.path = "/project/statistic/groupSum"
		self.headers = {"Content-Type": "application/json",
							"Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = { "groupIds": [ "3960"]}

	def changeEnv(self, env):
		self.host = self.host.replace("turboradio.cn", env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path + "	done" + "	项目分组统计")
		return self.response

