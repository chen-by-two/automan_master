# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class MyCustomers(httpHandler):
	def __init__(self):
		super(MyCustomers, self).__init__()
		self.host = "https://advfront.turboradio.cn"
		self.path = "/advisor/myCustomers"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询我的顾客")
		return self.response


class GetRecommendAdvisor1(httpHandler):
	def __init__(self):
		super(GetRecommendAdvisor1, self).__init__()
		self.host = "https://advfront.turboradio.cn"
		self.path = "/advCustomer/getRecommendAdvisor"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	推荐列表查询")
		return self.response


class GetRecommendAdvisor2(httpHandler):
	def __init__(self):
		super(GetRecommendAdvisor2, self).__init__()
		self.host = "https://advfront.turboradio.cn"
		self.path = "/advCustomer/getRecommendAdvisor"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	推荐列表距离最近查询")
		return self.response


class GetAdvisorInfo(httpHandler):
	def __init__(self):
		super(GetAdvisorInfo, self).__init__()
		self.host = "https://advfront.turboradio.cn"
		self.path = "/advisor/getAdvisorInfo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"200341","latitude":"","longitude":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	顾问端-顾问详情")
		return self.response


class GetBindAdvisorInfo(httpHandler):
	def __init__(self):
		super(GetBindAdvisorInfo, self).__init__()
		self.host = "https://advfront.turboradio.cn"
		self.path = "/advAdvisor/getBindAdvisorInfo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15961031"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	顾客端-绑定顾问信息")
		return self.response