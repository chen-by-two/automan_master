# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class MrchantStoreClerkCount(httpHandler):
	def __init__(self):
		super(MrchantStoreClerkCount, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/merchant/storeClerkCount"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "merchantId": "556"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-门店和店员数据")
		return self.response


class HomePageOperateData(httpHandler):
	def __init__(self):
		super(HomePageOperateData, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/homePage/operateData"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "type": "d",
    "merchantId": "556"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-经营数据（销售额）")
		return self.response


class HomePageMonthStoreTop(httpHandler):
	def __init__(self):
		super(HomePageMonthStoreTop, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/homePage/monthStoreTop"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "page": 1,
    "limit": 5,
    "merchantId": "556",
    "month": "2022-04"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-月度门店Top5")
		return self.response


class HomePageMonthClerkTop(httpHandler):
	def __init__(self):
		super(HomePageMonthClerkTop, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/homePage/monthClerkTop"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "page": 1,
    "limit": 5,
    "merchantId": "556",
    "month": "2022-04"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-月度店员Top5")
		return self.response


class HomePageMerchantDataQuality(httpHandler):
	def __init__(self):
		super(HomePageMerchantDataQuality, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/homePage/merchantDataQuality"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "merchantId": "556"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-连锁数据质量")
		return self.response


class HomePageGetBusinessInfo(httpHandler):
	def __init__(self):
		super(HomePageGetBusinessInfo, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/homePage/getBusinessInfo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "organizationId": "159798"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-商务经理")
		return self.response


class HomePageTodayData(httpHandler):
	def __init__(self):
		super(HomePageTodayData, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/homePage/todayData"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "merchantId": "556",
    "statisDate": "2022-04-21"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	首页-今日数据")
		return self.response


class MerchantInfo(httpHandler):
	def __init__(self):
		super(MerchantInfo, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/merchant/info"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "merchantId": "578"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	企业信息-企业信息")
		return self.response


class InclusiveCheckApply(httpHandler):
	def __init__(self):
		super(InclusiveCheckApply, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/inclusive/checkApply"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "merchantId": "578"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	是否已开通普惠3.0")
		return self.response


class UserLogin(httpHandler):
	def __init__(self):
		super(UserLogin, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/user/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "mobile": "15380905486",
    "password": "111111",
    "remember": "true"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	密码登录")
		return self.response