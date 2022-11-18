# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class CreditAccountTradeAdd(httpHandler):
	def __init__(self):
		super(CreditAccountTradeAdd, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditAccountTrade/add"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
		self.params = None
		self.data = {"account":"13310160002","nickName":"用户昵称","memberName":None,"gender":"01","birthdayPrefix":1,"birthday":None,"email":None,"mobile":None,"id":None}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分添加")
		return self.response


class CreditAccountTradeBatchAdd(httpHandler):
	def __init__(self):
		super(CreditAccountTradeBatchAdd, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditAccountTrade/batch/add"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
		self.params = None
		self.data = {"account":"13310160001","nickName":"2222","memberName":"","gender":"01","birthdayPrefix":1,"birthday":None,"email":"","mobile":"","id":15965146}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分批量添加")
		return self.response


class CreditGoodsTradeTransfer(httpHandler):
	def __init__(self):
		super(CreditGoodsTradeTransfer, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditGoodsTrade/transfer"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
		self.params = None
		self.data = {"id":"15965146","staCode":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分转移")
		return self.response


class CreditPayTradeTrialCalculation(httpHandler):
	def __init__(self):
		super(CreditPayTradeTrialCalculation, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPayTrade/trialCalculation"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分试算")
		return self.response


class CreditPayTradeLock(httpHandler):
	def __init__(self):
		super(CreditPayTradeLock, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPayTrade/lock"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分锁定")
		return self.response


class CreditPayTradeRelease(httpHandler):
	def __init__(self):
		super(CreditPayTradeRelease, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPayTrade/release"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分释放")
		return self.response


class CreditPayTradeConsume(httpHandler):
	def __init__(self):
		super(CreditPayTradeConsume, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPayTrade/consume"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分消费")
		return self.response


class CreditPreAccountTradePreAdd(httpHandler):
	def __init__(self):
		super(CreditPreAccountTradePreAdd, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPreAccountTrade/preAdd"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	预发积分添加")
		return self.response


class CreditPreAccountTradeEdit(httpHandler):
	def __init__(self):
		super(CreditPreAccountTradeEdit, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPreAccountTrade/edit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	预发放修改")
		return self.response


class CreditPreAccountTradeEditBatch(httpHandler):
	def __init__(self):
		super(CreditPreAccountTradeEditBatch, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPreAccountTrade/edit/batch"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	预发放批量修改")
		return self.response


class CreditIntegralTradeWithdraw(httpHandler):
	def __init__(self):
		super(CreditIntegralTradeWithdraw, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditIntegralTrade/withdraw"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	提现申请")
		return self.response


class CreditIntegralTradeConfirmWithdraw(httpHandler):
	def __init__(self):
		super(CreditIntegralTradeConfirmWithdraw, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditIntegralTrade/confirm/withdraw"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965146,
	"typeId":5,
	"cardNo":"香港123456",
	"cardName":"许戈子",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":0
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	权益提现确认")
		return self.response


class CreditCompanySettleTradeCheckCompanyCredit(httpHandler):
	def __init__(self):
		super(CreditCompanySettleTradeCheckCompanyCredit, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditCompanySettleTrade/checkCompanyCredit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "merchantId": "578",
    "startDate": "2021-01-25 00:00:00",
    "endDate": "2021-01-25 23:59:59",
    "checkType": 2,
    "amount": 202
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	流水积分校验接口")
		return self.response


class CreditCompanySettleTradePullCompanyRecords(httpHandler):
	def __init__(self):
		super(CreditCompanySettleTradePullCompanyRecords, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditCompanySettleTrade/pullCompanyRecords"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"orderNo":"81012511605002010159"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	连锁流水拉取接口")
		return self.response


class CreditCompanySettleTradeSettleApply(httpHandler):
	def __init__(self):
		super(CreditCompanySettleTradeSettleApply, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditCompanySettleTrade/settleApply"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "merchantId": 578,
    "statementNo": "JF20210125105878",
    "amount": 2
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	企业积分结算申请接口")
		return self.response


class CreditCompanySettleTradeSettleConfirm(httpHandler):
	def __init__(self):
		super(CreditCompanySettleTradeSettleConfirm, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditCompanySettleTrade/settleConfirm"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "statementNo": "11111",
    "status": 1,
    "completeDate": "2021-01-19 14:00:00"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	企业积分结算结果接口")
		return self.response


class CreditAccountQueryPreCount(httpHandler):
	def __init__(self):
		super(CreditAccountQueryPreCount, self).__init__()
		self.host = "http://credit-query-js.turboradio.cn"
		self.path = "/creditAccountQuery/preCount"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "accountNo": "",
    "memberName": "",
    "status": "1",
    "identity": "1",
    "partnerId": "1",
    "storeId": "1",
    "reason":1,
    "productName": "1",
    "orderNo": "1",
    "channel": 1,
    "partnerId": "1"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分统计列表")
		return self.response


class CreditAccountQueryCountHistory(httpHandler):
	def __init__(self):
		super(CreditAccountQueryCountHistory, self).__init__()
		self.host = "http://credit-query-js.turboradio.cn"
		self.path = "/creditAccountQuery/count/history"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "accountNo": "13303030001",
    "year": 2021,
    "month":3
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询历史积分历史")
		return self.response


class CreditPreAccountTradeEditInfo(httpHandler):
	def __init__(self):
		super(CreditPreAccountTradeEditInfo, self).__init__()
		self.host = "http://credit-srv-js.turboradio.cn"
		self.path = "/creditPreAccountTrade/edit/info"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "id": "2754",
    "auditId": "19041732128",
    "equityId": 1,
    "guaranteeId":1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	更新积分记录edit/info")
		return self.response


class CreditAccountAdminExport(httpHandler):
	def __init__(self):
		super(CreditAccountAdminExport, self).__init__()
		self.host = "http://credit-mng-jm.turboradio.cn"
		self.path = "/creditAccountAdmin/export"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "accountNo": "",
    "memberName": "",
    "status": "1",
    "identity": "1",
    "partnerId": "1",
    "storeId": "1",
    "reason":1,
    "productName": "1",
    "orderNo": "1",
    "channel": 1,
    "partnerId": "1",
    "exportKey":""
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分列表导出")
		return self.response


class CreditAccountQueryMemberAccountQuery(httpHandler):
	def __init__(self):
		super(CreditAccountQueryMemberAccountQuery, self).__init__()
		self.host = "http://credit-query-js.turboradio.cn"
		self.path = "/creditAccountQuery/memberAccount/query"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "memberId": "15964339",
    "identify":"consumer"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户积分账户金额查询")
		return self.response


class CreditAccountQueryPrePaging(httpHandler):
	def __init__(self):
		super(CreditAccountQueryPrePaging, self).__init__()
		self.host = "http://credit-query-js.turboradio.cn"
		self.path = "/creditAccountQuery/prePaging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "accountNo": "",
    "memberName": "",
    "memberId":15964339,
    "status": "",
    "identity": "consumer",
    "partnerId": "",
    "reason": "",
    "storeId": "",
    "productName": "",
    "orderNo": "",
    "channel": 1,
    "startDate":"",
    "endDate":"",
    "page": "1",
    "limit": "1"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	积分记录列表")
		return self.response