# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler

class partnerDetail(httpHandler):
	def __init__(self):
		super(partnerDetail, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/detail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId": "578"}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info("商户信息:"+self.host+self.path)
		return self.response


class partnerBillInfo(httpHandler):
	def __init__(self):
		super(partnerBillInfo, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/bill/info/detail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"unitId":"578"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	核算单位票据信息")
		return self.response


class merchantInfo(httpHandler):
	def __init__(self):
		super(merchantInfo, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/merchant/info"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId": "578"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	核算单位票据信息")
		return self.response


class partnerSetting(httpHandler):
	def __init__(self):
		super(partnerSetting, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/setting/detail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId": "578"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取核算单位的结算配置")
		return self.response


class vipDetail(httpHandler):
	def __init__(self):
		super(vipDetail, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/apply/vip/detail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"unitId":"578"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	VIP申请在线开票详情")
		return self.response


class partnerTodoList(httpHandler):
	def __init__(self):
		super(partnerTodoList, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partnerTodoList/paging"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"unitId":"578"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取商家的待办事项")
		return self.response


class insurerInfo(httpHandler):
	def __init__(self):
		super(insurerInfo, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/insurer/info"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId": "5"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取商家的待办事项")
		return self.response

class versionControl(httpHandler):
		def __init__(self):
			super(versionControl, self).__init__()
			self.host = "http://ps-finance-data.turboradio.cn"
			self.path = "/businessCenterVersion/detail"
			self.headers = {"Content-Type": "application/json;charset=UTF-8"}
			self.params = None
			self.data = {}

		def changeEnv(self, env):
			self.host = self.host.replace("turboradio.cn", env)

		def excute(self):
			if self.params != None:
				for k in self.params.keys():
					self.path = self.path + self.params[k]
			self.response = self.run(1)
			self.logger.info(self.path + "	done" + "	获取商家的版本控制信息")
			return self.response


class unitRelationship(httpHandler):
	def __init__(self):
		super(unitRelationship, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/relationship/unit/detail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId": "5"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取商家的待办事项")
		return self.response

class unitBillInfo(httpHandler):
	def __init__(self):
		super(unitBillInfo, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/bill/info/unit/detail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"unitId": "5"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	核算单位的基础信息和票据信息")
		return self.response

# testcase 0011
class workerExist(httpHandler):
	def __init__(self):
		super(workerExist, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/worker/exist"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId": "15961530","unitId": "578","type": 1}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info("用户信息:"+self.host+self.path)
		return self.response

# testcase 0012: 换新服务协议
class partnerRenewal(httpHandler):
	def __init__(self):
		super(partnerRenewal, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/renewal/listing"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId": "578"}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info("核算单位换新服务协议:"+self.host+self.path)
		return self.response

# testcase 0013: 商品税收分类编码信息
class taxClassification(httpHandler):
		def __init__(self):
			super(taxClassification, self).__init__()
			self.host = "http://ps-finance-data.turboradio.cn"
			self.path = "/tax/classification/encode/detail/by/match"
			self.headers = {"Content-Type": "application/json;charset=UTF-8"}
			self.params = None
			self.data = {"productName":"麝香壮骨膏","approvalNumber":"国药准字Z20063568（延）","skuNo":"134164-G013697"}

		def changeEnv(self, env):
			self.host = self.host.replace("turboradio.cn", env)
			return self.host

		def excute(self):
			if self.params != None:
				for k in self.params.keys():
					self.path = self.path + self.params[k]
			self.response = self.run(1)
			self.logger.info("商品税收分类编码信息:" + self.host + self.path)
			return self.response

# testcase 0014: 用户管理用户信息
class companyWorker(httpHandler):
		def __init__(self):
			super(companyWorker, self).__init__()
			self.host = "http://ps-finance-data.turboradio.cn"
			self.path = "/company/worker/paging"
			self.headers = {"Content-Type": "application/json;charset=UTF-8"}
			self.params = None
			self.data = {"memberId": "15961530","type": 4}

		def changeEnv(self, env):
			self.host = self.host.replace("turboradio.cn", env)
			return self.host

		def excute(self):
			if self.params != None:
				for k in self.params.keys():
					self.path = self.path + self.params[k]
			self.response = self.run(1)
			self.logger.info("用户管理用户信息:" + self.host + self.path)
			return self.response


class dictDetailByName(httpHandler):
	def __init__(self):
		super(dictDetailByName, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/dict/detailByName"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"dictKey":"自动生成金蝶凭证"}

	def changeEnv(self, env):
		self.host = self.host.replace("turboradio.cn", env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info("根据字典名称查询详情:" + self.host + self.path)
		return self.response

class partnerDiscountDetailByTime(httpHandler):
	def __init__(self):
		super(partnerDiscountDetailByTime, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/discount/detail/by/time"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"organizationId":578,"times":"2022-07-20 16:30:57","balanceType":1,"channel":1}

	def changeEnv(self, env):
		self.host = self.host.replace("turboradio.cn", env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info("指定连锁日期的协议扣率详情:" + self.host + self.path)
		return self.response

class partnerDirectorAuditListing(httpHandler):
	def __init__(self):
		super(partnerDirectorAuditListing, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/partner/director/audit/listing"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"directorId":"1113"}

	def changeEnv(self, env):
		self.host = self.host.replace("turboradio.cn", env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info("连锁审核列表:" + self.host + self.path)
		return self.response

class workerSystemPaging(httpHandler):
	def __init__(self):
		super(workerSystemPaging, self).__init__()
		self.host = "http://ps-finance-data.turboradio.cn"
		self.path = "/worker/system/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"16234369","systemId":"1211","type":4}

	def changeEnv(self, env):
		self.host = self.host.replace("turboradio.cn", env)
		return self.host

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info("分页列表:" + self.host + self.path)
		return self.response