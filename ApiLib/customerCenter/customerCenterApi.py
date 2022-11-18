# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class PromoteSendcard(httpHandler):
	def __init__(self):
		super(PromoteSendcard, self).__init__()
		self.host = "http://admincustomercenter.backend.turboradio.cn"
		self.path = "/promote/sendcard"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"memberId":"15961742","schemeId":"20201016141722932132","cardNum":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	客服中心发营销卡")
		return self.response


class VoucherCreate(httpHandler):
	def __init__(self):
		super(VoucherCreate, self).__init__()
		self.host = "http://admincustomercenter.backend.turboradio.cn"
		self.path = "/voucher/create"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"memberId":"15961742","schemeId":"20201016143030178249","requestNo":"2020-10-16T06:30:52.490Z"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	客服中心发抵扣券")
		return self.response


class VoucherListing(httpHandler):
	def __init__(self):
		super(VoucherListing, self).__init__()
		self.host = "http://admincustomercenter.backend.turboradio.cn"
		self.path = "/voucher/listing"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"page":1,"limit":10,"equityStatus":[],"memberId":"15961742"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	抵扣券列表")
		return self.response


class PromoteCardlist(httpHandler):
	def __init__(self):
		super(PromoteCardlist, self).__init__()
		self.host = "http://admincustomercenter.backend.turboradio.cn"
		self.path = "/promote/cardlist"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"page":1,"limit":10,"equityStatus":[],"status":"1","memberId":"15961742"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	营销卡列表")
		return self.response


class OrderRefundApplyPaging(httpHandler):
	def __init__(self):
		super(OrderRefundApplyPaging, self).__init__()
		self.host = "http://admincustomercenter.backend.turboradio.cn"
		self.path = "/orderRefundApply/paging"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"page":1,"limit":10,"equityStatus":[],"status":0}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	订单退款申请列表")
		return self.response


class RefundapplyInfo(httpHandler):
	def __init__(self):
		super(RefundapplyInfo, self).__init__()
		self.host = "http://admincustomercenter.backend.turboradio.cn"
		self.path = "/refundapply/info"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"applyNo":"92051952160346948341","orderNo":"92051911603469380142"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	订单退款申请详情")
		return self.response