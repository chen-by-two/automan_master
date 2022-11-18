# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class paging(httpHandler):
	def __init__(self):
		super(paging, self).__init__()
		self.host = "http://adminordercenter.backend.turboradio.cn"
		self.path = "/neworder/paging"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":10}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	订单管理后台")
		return self.response


class UnifyorderConfirmCreate(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmCreate, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"skuNos":["53219-5062011"],"requestNo":1594976313000,"channel":"8","saleMerchantId":"539","saleStoreId":"74596","assistantId":0,"shareMemberId":0,"commissionNo":"","partnerMerchantId":0,"partnerOpenId":0,"channelId":"0","orderSource":0}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		print("222222",self.headers)
		self.logger.info(self.path +"\tdone" + "	统一交易创建待确认单")
		return self.response


class UnifyorderConfirmInvoiceChange(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmInvoiceChange, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/invoice/change"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264","invoiceTitleNo":3,"title":"","titleType":"","content":"","taxNo":"","registerAddress":"","registerphone":"","openingBank":"","bankNo":"","mailbox":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易确认页更改发票信息")
		return self.response


class UnifyorderOrderCreate(httpHandler):
	def __init__(self):
		super(UnifyorderOrderCreate, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/order/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"confirmNo":"734333451127250ecec913c59ae5e021"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易创建订单")
		return self.response


class UnifyorderCashierPayModes(httpHandler):
	def __init__(self):
		super(UnifyorderCashierPayModes, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/cashier/payModes"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"orderNo":"80072005158767125750"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易支付方式")
		return self.response


class UnifyorderOrderDetail(httpHandler):
	def __init__(self):
		super(UnifyorderOrderDetail, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/order/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"orderNo":"80072005158767125750"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易订单详情")
		return self.response


class UnifyorderCashierCheck(httpHandler):
	def __init__(self):
		super(UnifyorderCashierCheck, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/cashier/check"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"first":False,"orderNo":"80072005158767125750"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易支付结果确认")
		return self.response


class NeworderOrdercancelsub(httpHandler):
	def __init__(self):
		super(NeworderOrdercancelsub, self).__init__()
		self.host = "http://adminordercenter.backend.turboradio.cn"
		self.path = "/neworder/ordercancelsub"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"orderNo": "80082617158776250778"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	仅退款")
		return self.response


class UnifyorderCashierCreate(httpHandler):
	def __init__(self):
		super(UnifyorderCashierCreate, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/cashier/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"orderNo":"80090308158776935933","payMode":"CWXPAY"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易支付")
		return self.response


class OrderCacheDel(httpHandler):
	def __init__(self):
		super(OrderCacheDel, self).__init__()
		self.host = "http://java.order.turboradio.cn"
		self.path = "/order/cache/del"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"orderNo": "80102401602963620281"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	订单删除缓存")
		return self.response


class LogisticsDeliverNotify(httpHandler):
	def __init__(self):
		super(LogisticsDeliverNotify, self).__init__()
		self.host = "http://java.order.turboradio.cn"
		self.path = "/logistics/deliver/notify"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"orderNo":"80101411600913910748","logistics":{"logisticsNo":"23111123131","company":"顺丰1哈22222","remark":""}}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	子订单发货")
		return self.response


class NeworderRefundcashier(httpHandler):
	def __init__(self):
		super(NeworderRefundcashier, self).__init__()
		self.host = "http://adminordercenter.backend.turboradio.cn"
		self.path = "/neworder/refundcashier"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"refundNo":"20111922338040570285","orderNo":"20111912337848450221"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	收银台整单退款")
		return self.response


class MngOrderOrderMngPaging(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngPaging, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/paging"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"page":1,"limit":10,"mobile":"15005150023"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台查询")
		return self.response


class MngOrderOrderMngDetail(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngDetail, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/detail"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"orderNo":"81012101604981171645","subOrderNo":"81012111604981181669"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台订单详情")
		return self.response


class MngOrderOrderMngOrderallequity(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngOrderallequity, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/orderallequity"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"equityIds":["28829064"],"mainOrderNo":"81012401605000730750"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台权益使用查询")
		return self.response


class MngOrderOrderMngExpresslist(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngExpresslist, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/expresslist"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = None

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台物流公司查询")
		return self.response


class MngOrderOrderMngOrdercancelsub(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngOrdercancelsub, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/ordercancelsub"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"orderNo":"81012411605000740734","refundReasonType":"6","refundReason":"123123"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台仅退款")
		return self.response


class MngOrderOrderMngRefundlist(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngRefundlist, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/refundlist"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"orderNo":"81012201604987820605","subOrderNo":"81012211604987840611"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台查询退款状态")
		return self.response


class MngOrderOrderMngDeliver(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngDeliver, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/deliver"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"orderNo":"81012511605001560719","erpSn":"81012511605001560719","merchantId":578,"logistics":{"logisticsNo":"123123","expressCode":"youzhengguoji","orderNo":"81012511605001560719","erpSn":"81012511605001560719","company":"邮政小包（国际），邮政包裹（国际）、邮政国内给据（国际)","remark":""}}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单后台发货")
		return self.response


class MngOrderOrderMngRefundgoods(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngRefundgoods, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/refundgoods"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"operatorId":"465","operatorName":"刘昊然","orderNo":"81012511605001560719"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单整单退货")
		return self.response


class MngOrderOrderMngRefundcashier(httpHandler):
	def __init__(self):
		super(MngOrderOrderMngRefundcashier, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-order/order/mng/refundcashier"
		self.headers = {"Content-Type": "application/json", "Authorization": "Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"refundNo":"81012521605004050779","orderNo":"81012511605001560719","refundReasonType":"8","refundReason":"12"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新订单整单退货收银台")
		return self.response