# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


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
		self.logger.info(self.path +"\tdone" + "	统一交易创建待确认单")
		return self.response
#新增
class UnifyorderConfirmCreateNew(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmCreateNew, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/confirm/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzMzMDYsInd4T3BlbmlkIjoib3lseWx1Q09pYXBaMzVfd0RQZFFiX2tuVnhwRSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTYyMzMzMDYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU1ZjIwXHU2MDAwXHU0ZmEwIiwibW9iaWxlIjoiMTMzNzIwMzg3MDEifSwiY2hhbm5lbCI6eyJvcGVuaWQiOiJveWx5bHVDT2lhcFozNV93RFBkUWJfa25WeHBFIiwidHlwZSI6IndlY2hhdCJ9fQ.qi8EruQyVCAOEdWcf2yySy47cZoAeObhFCAvvfoUBsafVC8KEvFRs2-3CePJfn9TFo07KNT4L8fceROhdFuzF7FTl7tYSdD6t16LyQggopvp_eiiTa1IfZlpzyHod2df7i1KIUdHh1TdM1riSDQZVTsruhvnLWQnHObgcty8LW3d7RTY4LoeuoeaVbo9TSIZOXXqPyEOjak_0c60wWM7VESsqm9dbOIBXxBhtj6FEAJoZNKSlB5A4ERRRkt4cdj5VWYc9Mc9LsSRWIbhmKiGBePaoWqhkwy-Qg8jMJkebQeSVAgloO2M9C8Ompm0SgB-Jkz9vKh9peM6VmIen9bBfA"}
		self.params = None
		self.data = {"skuNos": "578-892369609305358336",
                      "requestNo": "16462994027411",
                      "channel": 7,
                      "saleMerchantId": "539",
                      "saleStoreId": "74596",
                      "assistantId": 0,
                      "shareMemberId": 0,
                      "commissionNo": "",
                      "partnerMerchantId": 0,
                      "partnerOpenId": 0,
                      "channelId": "0",
                      "orderSource": 0,
                      "orderMethod": "3",
                      "tid": "",
                      "quantity": "1",
                      "showInsuredMember": None}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易创建预订单接口")
		return self.response

#新增查询UnifyorderqueryMulti
class UnifyorderqueryMulti(httpHandler):
    def __init__(self):
        super(UnifyorderqueryMulti, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/member/resource/query/multi"
        self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzMzMDYsInd4T3BlbmlkIjoib3lseWx1Q09pYXBaMzVfd0RQZFFiX2tuVnhwRSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTYyMzMzMDYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU1ZjIwXHU2MDAwXHU0ZmEwIiwibW9iaWxlIjoiMTMzNzIwMzg3MDEifSwiY2hhbm5lbCI6eyJvcGVuaWQiOiJveWx5bHVDT2lhcFozNV93RFBkUWJfa25WeHBFIiwidHlwZSI6IndlY2hhdCJ9fQ.qi8EruQyVCAOEdWcf2yySy47cZoAeObhFCAvvfoUBsafVC8KEvFRs2-3CePJfn9TFo07KNT4L8fceROhdFuzF7FTl7tYSdD6t16LyQggopvp_eiiTa1IfZlpzyHod2df7i1KIUdHh1TdM1riSDQZVTsruhvnLWQnHObgcty8LW3d7RTY4LoeuoeaVbo9TSIZOXXqPyEOjak_0c60wWM7VESsqm9dbOIBXxBhtj6FEAJoZNKSlB5A4ERRRkt4cdj5VWYc9Mc9LsSRWIbhmKiGBePaoWqhkwy-Qg8jMJkebQeSVAgloO2M9C8Ompm0SgB-Jkz9vKh9peM6VmIen9bBfA"}
        self.data = {
                "confirmNo": "059175a4e67d6530440e417add6cd73a"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易获取用户可用权益列表接口")
        return self.response
#查询UnifyorderqueryResourceId
class UnifyorderqueryResourceId(httpHandler):
		def __init__(self):
			super(UnifyorderqueryResourceId, self).__init__()
			self.host = "https://wx.uniondrug.net"
			self.path = "/unifyorder/confirm/resouce/change"
			self.headers = {"Content-Type": "application/json;charset=UTF-8",
							"Authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzMzMDYsInd4T3BlbmlkIjoib3lseWx1Q09pYXBaMzVfd0RQZFFiX2tuVnhwRSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTYyMzMzMDYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU1ZjIwXHU2MDAwXHU0ZmEwIiwibW9iaWxlIjoiMTMzNzIwMzg3MDEifSwiY2hhbm5lbCI6eyJvcGVuaWQiOiJveWx5bHVDT2lhcFozNV93RFBkUWJfa25WeHBFIiwidHlwZSI6IndlY2hhdCJ9fQ.qi8EruQyVCAOEdWcf2yySy47cZoAeObhFCAvvfoUBsafVC8KEvFRs2-3CePJfn9TFo07KNT4L8fceROhdFuzF7FTl7tYSdD6t16LyQggopvp_eiiTa1IfZlpzyHod2df7i1KIUdHh1TdM1riSDQZVTsruhvnLWQnHObgcty8LW3d7RTY4LoeuoeaVbo9TSIZOXXqPyEOjak_0c60wWM7VESsqm9dbOIBXxBhtj6FEAJoZNKSlB5A4ERRRkt4cdj5VWYc9Mc9LsSRWIbhmKiGBePaoWqhkwy-Qg8jMJkebQeSVAgloO2M9C8Ompm0SgB-Jkz9vKh9peM6VmIen9bBfA"}

			self.data = {
				"resourceIdList": ["23430110"],
				"resourceType": 1,
				"balanceTimes": None,
				"oneTimeValue": 0,
				"balanceValue": None,
				"rsourceName": "药联健康权益",
				"resourceDescription": 1,
				"resourceCutOffDate": "2026-04-30 23:59:59",
				"nominalValue": 0,
				"type": 3,
				"checked": 1,
				"confirmNo": "169efc9c5d613824bd357dd4acbb92d1"
			}

		def changeEnv(self, env):
			self.host = self.host.replace("uniondrug.net", env)

		def excute(self):
			if self.params != None:
				for k in self.params.keys():
					self.path = self.path + self.params[k]
			self.response = self.run(1)
			self.logger.info(self.path + "\tdone" + "	统一交易获取资源接口")
			return self.response
#rc 创建订单接口
class UnifyorderRCOrdercreate(httpHandler):
	def __init__(self):
		super(UnifyorderRCOrdercreate, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/order/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8",
						"Authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzMzMDYsInd4T3BlbmlkIjoib3lseWx1Q09pYXBaMzVfd0RQZFFiX2tuVnhwRSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTYyMzMzMDYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU1ZjIwXHU2MDAwXHU0ZmEwIiwibW9iaWxlIjoiMTMzNzIwMzg3MDEifSwiY2hhbm5lbCI6eyJvcGVuaWQiOiJveWx5bHVDT2lhcFozNV93RFBkUWJfa25WeHBFIiwidHlwZSI6IndlY2hhdCJ9fQ.qi8EruQyVCAOEdWcf2yySy47cZoAeObhFCAvvfoUBsafVC8KEvFRs2-3CePJfn9TFo07KNT4L8fceROhdFuzF7FTl7tYSdD6t16LyQggopvp_eiiTa1IfZlpzyHod2df7i1KIUdHh1TdM1riSDQZVTsruhvnLWQnHObgcty8LW3d7RTY4LoeuoeaVbo9TSIZOXXqPyEOjak_0c60wWM7VESsqm9dbOIBXxBhtj6FEAJoZNKSlB5A4ERRRkt4cdj5VWYc9Mc9LsSRWIbhmKiGBePaoWqhkwy-Qg8jMJkebQeSVAgloO2M9C8Ompm0SgB-Jkz9vKh9peM6VmIen9bBfA"}
		self.data = {"confirmNo": "734333451127250ecec913c59ae5e021"}

	def changeEnv(self, env):
		self.host = self.host.replace("uniondrug.net", env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path + "\tdone" + "	统一交易创建订单接口")
		return self.response

#rc支付
class UnifyorderPayModes(httpHandler):
	def __init__(self):
		super(UnifyorderPayModes, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/cashier/payModes"
		self.headers = {"Content-Type": "application/json;charset=UTF-8",
						"Authorization": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzMzMDYsInd4T3BlbmlkIjoib3lseWx1Q09pYXBaMzVfd0RQZFFiX2tuVnhwRSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTYyMzMzMDYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU1ZjIwXHU2MDAwXHU0ZmEwIiwibW9iaWxlIjoiMTMzNzIwMzg3MDEifSwiY2hhbm5lbCI6eyJvcGVuaWQiOiJveWx5bHVDT2lhcFozNV93RFBkUWJfa25WeHBFIiwidHlwZSI6IndlY2hhdCJ9fQ.qi8EruQyVCAOEdWcf2yySy47cZoAeObhFCAvvfoUBsafVC8KEvFRs2-3CePJfn9TFo07KNT4L8fceROhdFuzF7FTl7tYSdD6t16LyQggopvp_eiiTa1IfZlpzyHod2df7i1KIUdHh1TdM1riSDQZVTsruhvnLWQnHObgcty8LW3d7RTY4LoeuoeaVbo9TSIZOXXqPyEOjak_0c60wWM7VESsqm9dbOIBXxBhtj6FEAJoZNKSlB5A4ERRRkt4cdj5VWYc9Mc9LsSRWIbhmKiGBePaoWqhkwy-Qg8jMJkebQeSVAgloO2M9C8Ompm0SgB-Jkz9vKh9peM6VmIen9bBfA"}

		self.data = {
			"miniprogram": None,
			"orderNo": "92030301603287940777",
			"supportAppPay": None
		}

	def changeEnv(self, env):
		self.host = self.host.replace("uniondrug.net", env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path + self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path + "\tdone" + "	统一交易选择支付方式接口")
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

class UnifyorderRCOrderDetail(httpHandler):
	def __init__(self):
		super(UnifyorderRCOrderDetail, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/order/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"orderNo":"80072005158767125750"}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	RC统一交易订单详情")
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



	# RC支付流水接口--zhudenghu
class UnifyorderRcPaymentNo(httpHandler):
		def __init__(self):
			super(UnifyorderRcPaymentNo, self).__init__()
			self.host = "http://java.pmc.cashier.uniondrug.net"
			self.path = "/cashier/queryCashierAllByOutTradeNo"
			self.headers = {"Content-Type": "application/json;charset=UTF-8",
							"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
			self.params = None
			self.data = {"outTradeNo": "80090308158776935933", "status":1}

		def changeEnv(self, env):
			self.host = self.host.replace("uniondrug.net", env)

		def excute(self):
			if self.params != None:
				for k in self.params.keys():
					self.path = self.path + self.params[k]
			self.response = self.run(1)
			self.logger.info(self.path + "\tdone" + "	获取交易流水信息接口")
			return self.response

# RC创建支付接口--zhudenghu
class UnifyorderRcCashierCreate(httpHandler):
		def __init__(self):
			super(UnifyorderRcCashierCreate, self).__init__()
			self.host = "https://wx.uniondrug.net"
			self.path = "/unifyorder/cashier/create"
			self.headers = {"Content-Type": "application/json;charset=UTF-8",
							"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
			self.params = None
			self.data = {"orderNo": "80090308158776935933", "payMode": "CWXPAY"}

		def changeEnv(self, env):
			self.host = self.host.replace("uniondrug.net", env)

		def excute(self):
			if self.params != None:
				for k in self.params.keys():
					self.path = self.path + self.params[k]
			self.response = self.run(1)
			self.logger.info(self.path + "\tdone" + "	统一交易创建支付接口")
			return self.response

class UnifyorderRcFinishPayment(httpHandler):
	def __init__(self):
		super(UnifyorderRcFinishPayment, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/order/finishpay"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"first":False,"orderNo":"80072005158767125750"}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易支付结果确认")
		return self.response
# RC校验支付是否成功--zhudenghu
class UnifyorderRcCashierCheck(httpHandler):
	def __init__(self):
		super(UnifyorderRcCashierCheck, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/cashier/check"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"first":False,"orderNo":"80072005158767125750"}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易支付结果确认")
		return self.response


class UnifyorderMemberEquityQuery(httpHandler):
	def __init__(self):
		super(UnifyorderMemberEquityQuery, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/member/equity/query"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易订单详情页拉取可用权益列表")
		return self.response


class UnifyorderConfirmEquityChange(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmEquityChange, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/equity/change"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"id":24413516,"equityNo":"1000680724125568","equityName":"自付转权益","equityStyle":1,"equityStyleText":"面额","availableFrom":"2020-07-01 17:28:44","availableTo":"2120-07-01 23:59:59","balanceValue":1,"balanceTimes":0,"oneTimeValue":0,"equityType":1,"equityTypeText":"普通权益","equityStatus":1,"equityStatusText":"正常","memberId":15961742,"merchantId":7,"programId":108,"nominalValue":1,"usedValue":0,"lockedValue":0,"availableValue":1,"availableTimes":0,"nominalTimes":0,"usedTimes":0,"lockedTimes":0,"recycleMoney":"0.00","recycleTimes":0,"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易订单详情页选择权益")
		return self.response


class UnifyorderMemberIntegralUse(httpHandler):
	def __init__(self):
		super(UnifyorderMemberIntegralUse, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/member/integral/use"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易使用积分")
		return self.response


class UnifyorderMemberIntegralStop(httpHandler):
	def __init__(self):
		super(UnifyorderMemberIntegralStop, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/member/integral/stop"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易取消使用积分")
		return self.response


class UnifyorderMemberResourceQuery(httpHandler):
	def __init__(self):
		super(UnifyorderMemberResourceQuery, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/member/resource/query"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易订单详情页拉取可用资源列表")
		return self.response


class UnifyorderConfirmResouceChange(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmResouceChange, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/resouce/change"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"rsourceId":"ca15b9a0660d4ff880c5","resourceType":1,"balanceTimes":0,"oneTimeValue":0,"balanceValue":3,"rsourceName":"lhr满5-3营销卡","resourceDescription":"lhr满5-3营销卡","resourceCutOffDate":"2023-07-09 23:59:59","type":5,"checked":True,"confirmNo":"aa0c649fc56da7ecfd39f98371d05e0d"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易订单详情页选择资源")
		return self.response


class UnifyproductDetails(httpHandler):
	def __init__(self):
		super(UnifyproductDetails, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyproduct/details"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"skuNo":"53219-5062011","channel":"8","channelId":0}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易商品详情拉取")
		return self.response


class UnifyproductBuyLimit(httpHandler):
	def __init__(self):
		super(UnifyproductBuyLimit, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyproduct/buyLimit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"memberId":15961742,"skuNo":"53219-5062011"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易商品风控")
		return self.response
# rc统一交易风控接口
class UnifyRCproductBuyLimit(httpHandler):
	def __init__(self):
		super(UnifyRCproductBuyLimit, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyproduct/buyLimit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"memberId":15961742,"skuNoQries": [{
                      "skuNo": "578-847792818180063232",
                      "quantity": "1"
                    }]}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	rc环境统一交易商品风控")
		return self.response


class UnifyorderConfirmRemark(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmRemark, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/remark"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"aa0c649fc56da7ecfd39f98371d05e0d","remarks":[{"deliveryMerchantId":539,"remark":"SDK"}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易添加订单备注")
		return self.response


class UnifyorderAddressQueryInfos(httpHandler):
	def __init__(self):
		super(UnifyorderAddressQueryInfos, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/address/query/infos"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易拉取用户收货地址")
		return self.response


class UnifyorderConfirmShipmentChange(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmShipmentChange, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/shipment/change"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"aa0c649fc56da7ecfd39f98371d05e0d","id":28996,"consigneeName":"刘昊然","mobile":"15005150023","province":"新疆维吾尔自治区","city":"乌鲁木齐市","region":"沙依巴克区","street":"喀纳斯湖北路306号新疆卷烟厂","fullAddress":"新疆维吾尔自治区乌鲁木齐市沙依巴克区喀纳斯湖北路306号新疆卷烟厂","tag":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易切换收货地址")
		return self.response


class UnifyorderAddressAdd(httpHandler):
	def __init__(self):
		super(UnifyorderAddressAdd, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/address/add"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"id":"","confirmNo":"aa0c649fc56da7ecfd39f98371d05e0d","consigneeName":"测试","mobile":"15002123365","province":"北京市","provinceCode":"110000","city":"北京市","cityCode":"110100","region":"东城区","regionCode":"110101","street":"阿斯顿撒","fullAddress":"北京市北京市东城区阿斯顿撒","isDefault":"0","tag":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易新增收货地址")
		return self.response


class UnifyorderMemberCouponQuery(httpHandler):
	def __init__(self):
		super(UnifyorderMemberCouponQuery, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/member/coupon/query"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"a872759a27dad372f7ffd811e49a9efb","deliveryMerchantId":578}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易拉取优惠券")
		return self.response

#RC获取优惠券接口
class UnifyorderRCMemberCouponQuery(httpHandler):
	def __init__(self):
		super(UnifyorderRCMemberCouponQuery, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/member/coupon/query"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"a872759a27dad372f7ffd811e49a9efb"}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	RC统一交易拉取优惠券")
		return self.response
#rc 是否是联合会员接口
class UnifyorderRCUserRole(httpHandler):
	def __init__(self):
		super(UnifyorderRCUserRole, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/confirm/userRole/containsIdentity"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"identityCode": 60}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易查询联合会员接口")
		return self.response

#RC获取统一交易页用户规则查询接口
class UnifyorderRCUserRuleQuery(httpHandler):
	def __init__(self):
		super(UnifyorderRCUserRuleQuery, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/confirm/userRule/query"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {
	"ruleTypes": [2, 3],
	"resources": [{
		"resourceType": 3,
		"details": [{
			"resourceId": "",
			"resourceValue": "0"
		}]
	}, {
		"resourceType": 4,
		"details": [{
			"resourceId": "",
			"resourceValue": "1.9"
		}]
	}],
	"totalAmount": 2,
	"channel": 7,
	"goodsList": [{
		"merchantId": 578,
		"storeId": 4123,
		"goodsType": 1,
		"goodsAmount": 2,
		"goodsNumber": 1,
		"skuNo": "578-847792818180063232",
		"tradeCode": "",
		"childList": []
	}]
}
	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	RC统一交易用户规则查询")
		return self.response


class UnifyorderConfirmCouponChange(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmCouponChange, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyorder/confirm/coupon/change"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
		self.params = None
		self.data = {"confirmNo":"a872759a27dad372f7ffd811e49a9efb","deliveryMerchantId":578,"coupon":{"extraValues":{},"itemUuid":"578","goodsAmount":5555,"skuNo":None,"goodsBarCode":"12312312","goodsType":1,"couponId":"160308604737700015","couponAmount":5,"childList":None,"cardResult":{"cardId":"90f2da94246c4533a82f","cardName":"lhr减5块优惠券","cardDescription":"lhr减5块优惠券","cardBalance":5,"cardLimit":5,"gmtEffectedStart":"2020-10-19 00:00:00","gmtEffectedEnd":"2023-07-15 23:59:59","payType":None,"fullAmount":None},"key":"12312312","checked":True}}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易使用优惠券")
		return self.response