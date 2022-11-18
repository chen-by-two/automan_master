# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class paymentCreate(httpHandler):
	def __init__(self):
		super(paymentCreate, self).__init__()
		self.host = "http://finance.backend.turboradio.cn"
		self.path = "/capitalPayment/create" #
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"id":None,"paymentCode":None,"operator":{"workerId":"395","workerName":"方倩玲"},"serialId":"1650873465025307691","businessNo":"SS1122334455","payer":None,"payerId":"7","payerName":"上海聚音信息科技有限公司","payerAccount":"1001101719100022593","payerAccountName":"上海聚音信息科技有限公司","payerBank":"中国工商银行股份有限公司","payerBankHouse":"中国工商银行股份有限公司上海市大连路支行","payerCnaps":"102290010174","payeeType":"0","recipientId":None,"recipientType":"1","recipientName":"FZS公司","recipientAccount":"666688889999","recipientAccountName":"FZS公司","recipientBankObject":{"bankId":"308","name":"招商银行股份有限公司","code":"308"},"recipientBank":"招商银行股份有限公司","recipientBankHouseObject":{"name":"招商银行股份有限公司石河子分行","cnaps":"308902839018"},"recipientBankHouse":"招商银行股份有限公司石河子分行","recipientCnaps":"308902839018","confirmDate":None,"planPayDate":"2022-06-25","paidAmount":"188.00","payDate":None,"payAmount":188,"deductAmount":"0","payMethod":"电汇（T/T）","channel":"1","status":0,"businessType":"直付结算","openRechargeFund":0,"annexs":[],"removeAnnexIds":None,"createAnnexs":None,"outSerialId":None,"taxServiceDeductAmount":None,"payComment":None,"coinCode":"1122334455","remark":"测试","payableCompanyName":None,"payableCompanyId":None,"sourceMode":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新建付款单")
		return self.response

class bankChaimPageByPayer(httpHandler):
	def __init__(self):
		super(bankChaimPageByPayer, self).__init__()
		self.host = "https://pm-fin-shares.turboradio.cn"
		self.path = "/insure/policy/refund/confirm/paging" # 后端接口 /bankChaim/pageByPayer
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"page":1,"limit":10,"pageData":"2022-06-17T05:24:05.510Z","chaim":"3","payerOrganizationId":"161136"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	分页查询向药联付款的组织已认领交易记录")
		return self.response

class fundAccountGetByHolder(httpHandler):
	def __init__(self):
		super(fundAccountGetByHolder, self).__init__()
		self.host = "http://java.coin.service.turboradio.cn"
		self.path = "/fundAccount/getByHolder"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"holderId":"90026","holderType":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据组织 id 查询资金账户")
		return self.response

class connectTransferCallBack(httpHandler):
	def __init__(self):
		super(connectTransferCallBack, self).__init__()
		self.host = "http://java.coin.service.turboradio.cn"
		self.path = "/connect/transferCallBack"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"voucherNo":"FM20220104311523","waterNo":"20220104134358831768035","status":1,"message":"转账成功","reptImage":"","callback":"java.coin.service.uniondrug.net\/connect\/transferCallBack"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据组织 id 查询资金账户")
		return self.response

class mbsAuditCenter(httpHandler):
	def __init__(self):
		super(mbsAuditCenter, self).__init__()
		self.host = "http://java.coin.service.turboradio.cn"
		self.path = "/mbs/auditCenter"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"reason":None,"orderNo":"92070411603677670150","productId":"8","capitalPool":"5.00","channel":"1","auditNo":"92070468160367768711","capitalStatus":1,"type":"1","guaranteeId":"0","supplierMerchantId":"555","supplierStoreId":"60016","merchantId":"555","auditStatus":1,"mainOrderNo":"92070401603677660176","equityId":"0","status":2}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据组织 id 查询资金账户")
		return self.response