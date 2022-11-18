# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


# class wechatSubscribeStatus(httpHandler):
# 	def __init__(self):
# 		super(wechatSubscribeStatus, self).__init__()
# 		self.host = "https://business-center-backend.uniondrug.net"
# 		self.path = "/wechat/subscribe/status"
# 		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer", "signature": "sign"}
# 		self.params = None
# 		self.data = {}
#
# 	def changeEnv(self,env):
# 		self.host = self.host.replace("uniondrug.net",env)
#
# 	def excute(self):
# 		if self.params != None:
# 			for k in self.params.keys():
# 				self.path = self.path+self.params[k]
# 		self.response = self.run(1)
# 		self.logger.info(self.path +"	done" + "	商家查询微信状态")
# 		return self.response

class subscribeStatus(httpHandler):
	def __init__(self):
		super(subscribeStatus, self).__init__()
		self.host = "http://gs-moss-wechat.uniondrug.net"
		self.path = "/subscribe/status"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer", "signature": "sign"}
		self.params = None
		self.data = {"mobile":"15952059901"}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	公众号关注状态")
		return self.response

class systemRoleWorkertree(httpHandler):
	def __init__(self):
		super(systemRoleWorkertree, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/systemRole/workertree"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer", "signature": "sign"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家查询菜单权限")
		return self.response

class organizeFinanceAccountUnitDetail(httpHandler):
	def __init__(self):
		super(organizeFinanceAccountUnitDetail, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/organizeFinanceAccount/unitDetail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer", "signature": "sign"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家查询连锁是否开通财税")
		return self.response


class announcementPartnerCountUnread(httpHandler):
	def __init__(self):
		super(announcementPartnerCountUnread, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/announcementPartner/countUnread"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer", "signature": "sign"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家查询连锁公共未读数量")
		return self.response


class directPayoutStatementPaging(httpHandler):
	def __init__(self):
		super(directPayoutStatementPaging, self).__init__()
		self.host = "https://business-center-backend.turboradio.cn"
		self.path = "/direct/payout/statement/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {"page": 1, "limit": 10, "pageData": "2022-05-01T08:51:35.739Z", "businessStatus": "", "statementCycle": [], "settleCycle": [], "blueText": 999, "nzSelectedIndex": 0, "statementType": 1, "statementNo": "DS20220429100001"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家查询直付结算单")
		return self.response


class payoutBillPaging(httpHandler):
	def __init__(self):
		super(payoutBillPaging, self).__init__()
		self.host = "https://business-center-backend.turboradio.cn"
		self.path = "/payout/bill/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {"page": 1, "limit": 10, "pageData": "2022-05-01T08:51:35.739Z", "businessStatus": "", "statementCycle": [], "settleCycle": [], "blueText": 999, "nzSelectedIndex": 0, "statementType": 1, "statementNo": "DS20220429100001"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家服务平台查询开票单")
		return self.response


class applyOnlineUnitDetail(httpHandler):
	def __init__(self):
		super(applyOnlineUnitDetail, self).__init__()
		self.host = "https://ps-finance-data.turboradio.cn" # 文档内接口为：business-center-backend.uniondrug.cn/apply/online/unit/detail
		self.path = "/apply/online/unit/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"unitId":"555"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家发票列表信息")
		return self.response


class applyVipDetail(httpHandler):
	def __init__(self):
		super(applyVipDetail, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/applyVip/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	在线开票vip详情")
		return self.response


class announcementPartnerAvailable(httpHandler):
	def __init__(self):
		super(announcementPartnerAvailable, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/announcementPartner/available"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = { "page": 1, "limit": 10, "billNo": "20220517100517", "billNos": [ "20220517100517" ], "invoiceNo":" ", "invoiceCode": " ", "expressNo": " ", "expressCode": " ", "expressType": 1, "invoiceStatus": 2 }

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询连锁未读公告")
		return self.response


class announcementPartnerPaging(httpHandler):
	def __init__(self):
		super(announcementPartnerPaging, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/announcementPartner/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = { "page": 1, "limit": 10, "billNo": "20220517100517", "billNos": [ "20220517100517" ], "invoiceNo":" ", "invoiceCode": " ", "expressNo": " ", "expressCode": " ", "expressType": 1, "invoiceStatus": 2 }

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询连锁公告列表")
		return self.response

class businessCenterVersionDetail(httpHandler):
	def __init__(self):
		super(businessCenterVersionDetail, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/businessCenterVersion/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家服务平台版本")
		return self.response


class userUuid(httpHandler):
	def __init__(self):
		super(userUuid, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/user/uuid"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取用户UUID")
		return self.response


class transactionOrdersPaging(httpHandler):
	def __init__(self):
		super(transactionOrdersPaging, self).__init__()
		self.host = "https://business-center-backend.uniondrug.net"
		self.path = "/transactionOrders/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"pageNo":1,"pageSize":10,"pageData":"2022-07-20T08:26:37.376Z","payTime":None,"nzSelectedIndex":0,"blueText":-30,"startDate":"2022-06-20 00:00:00","endDate":"2022-07-20 23:59:59"}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家服务平台交易订单页面")
		return self.response