# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class AdvisorListRecommendAdv(httpHandler):
	def __init__(self):
		super(AdvisorListRecommendAdv, self).__init__()
		self.host = "http://data.recommend.turboradio.cn"
		self.path = "/advisor/listRecommendAdv"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":1,"pharmacyProvinceCode":"10000","pharmacyCityCode":"10001","pharmacyAreaCode":"10002","longitude":13.4,"latitude":23.5,"pageNum":1,"pageSize":10}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询推荐顾问")
		return self.response