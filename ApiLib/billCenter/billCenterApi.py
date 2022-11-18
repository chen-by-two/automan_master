# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler



class mbsBillSaleSave(httpHandler):
	def __init__(self):
		super(mbsBillSaleSave, self).__init__()
		self.host = "https://js-fin-bill.uniondrug.net"
		self.path = "/mbs/billSale/save"
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
		self.logger.info(self.path +"	done" + "MBS-推送销售清单到票据")
		return self.response


class invoicePage(httpHandler):
	def __init__(self):
		super(invoicePage, self).__init__()
		self.host = "https://js-fin-bill.uniondrug.net"
		self.path = "/invoice/page"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = { "page": 1, "limit": 10, "billNo": "20220517100517", "billNos": [ "20220517100517" ], "invoiceNo":" ", "invoiceCode": " ", "expressNo": " ", "expressCode": " ", "expressType": 1, "invoiceStatus": 2 }

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商家发票列表信息")
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

class financePayoutBillPaging(httpHandler):
	def __init__(self):
		super(financePayoutBillPaging, self).__init__()
		self.host = "https://pm-fin-shares.turboradio.cn"
		self.path = "/finance/payout/bill/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = { "page": 1, "limit": 10, "pageData": "2022-04-24T08:46:14.583Z", "selectIndex": 0, "billStatus": 1, "expressStatus": "" }

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	财务共享平台-票据中心查询应付开票单")
		return self.response


class directStatementCreate(httpHandler):
	def __init__(self):
		super(directStatementCreate, self).__init__()
		self.host = "http://gs-fin-statement.turboradio.cn"
		self.path = "/direct/statement/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = { "partnerId": 635, "partnerName": "国药控股国大药房上海连锁有限公司", "organizationId": 635, "organizationName": "国药控股国大药房上海连锁有限公司", "statementBeginDate": "2022-04-18", "statementEndDate": "2022-04-18", "businessType": 1, "statementLevel": 1, "subsidyAmount": "0", "workerId": 847, "workerName": "梁琪" }

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	创建直付结算单")
		return self.response


class directStatementAuditAccept(httpHandler):
	def __init__(self):
		super(directStatementAuditAccept, self).__init__()
		self.host = "http://gs-fin-statement.turboradio.cn"
		self.path = "/direct/statement/auto/audit/accept"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = { "statementNo": "${payoutStatementNo}" }

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	审核通过直付结算单")
		return self.response