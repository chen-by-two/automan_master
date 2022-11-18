# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class mqAfterDirectCleaned(httpHandler):
	def __init__(self):
		super(mqAfterDirectCleaned, self).__init__()
		self.host = "http://gs-fin-statement.uniondrug.net"
		self.path = "/mq/after/direct/cleaned"
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
		self.logger.info(self.path +"	done" + "MBS-直付订单入清算")
		return self.response


class mqAfterDirectGoodsReplaced(httpHandler):
	def __init__(self):
		super(mqAfterDirectGoodsReplaced, self).__init__()
		self.host = "http://gs-fin-statement.uniondrug.net"
		self.path = "/mq/after/direct/goods/replaced"
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
		self.logger.info(self.path +"	done" + "MBS-直付订单商品替换")
		return self.response



class directEquityClaimSync(httpHandler):
	def __init__(self):
		super(directEquityClaimSync, self).__init__()
		self.host = "http://gs-fin-statement.uniondrug.net"
		self.path = "/direct/equity/claim/sync"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = { "directPay": 1, "claimType": 0, "orderNo": "92061611603549650106", "claimGoodsList": [ { "unitPrice": 35.2, "itemId": 9909473, "claimType": 0, "totalAmount": 35.2, "reverseAmount": 0, "quantity": 1, "claimAmount": 30.98, "claimedAmount": 30.98 } ], "gmtCreatedStr": "2022-06-28 19:09:58", "policyNo": "YPB202201040001", "insurerId": 161205, "claimedAmount": 30.98 }

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "推送理赔流水到财务结算")
		return self.response