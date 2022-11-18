# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class AssistantCreate(httpHandler):
	def __init__(self):
		super(AssistantCreate, self).__init__()
		self.host = "http://drugstore.backend.turboradio.cn"
		self.path = "/assistant/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"id":"","partnerShortName":"","mobile":"15005150003","fullName":"问问","role":"1","merchantType":-1,"partnerOrganId":"578","storeOrganId":"4123","storeShortName":"产品测试门店1-2","jobNumber":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	创建药店宝店员")
		return self.response


class V4CodePicture(httpHandler):
	def __init__(self):
		super(V4CodePicture, self).__init__()
		self.host = "http://app.turboradio.cn"
		self.path = "/v4/code/picture"
		self.headers = None
		self.params = {"key":"askjjiql1234"}
		self.data = None

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(0)
		self.logger.info(self.path +"\tdone" + "	接收药店宝图形验证码")
		return self.response


class V4CodeVerify(httpHandler):
	def __init__(self):
		super(V4CodeVerify, self).__init__()
		self.host = "http://app.turboradio.cn"
		self.path = "/v4/code/verify"
		self.headers = None
		self.params = None
		self.data = {"phrase":"angp","mobile":"15005150023","usage":"login","key":"ksdjjklk123","sendMethod":"yunpian"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	发送药店宝登录验证码")
		return self.response


class V4UsersSmslogin(httpHandler):
	def __init__(self):
		super(V4UsersSmslogin, self).__init__()
		self.host = "http://app.turboradio.cn"
		self.path = "/v4/users/smslogin"
		self.headers = None
		self.params = None
		self.data = {"appPackageName":"com.xun-ao.udsa","deviceSerial":"iPhone","deviceUuid":"3f109386f899c5c980a820ce118e787f4f890215b5af9832b43372884b01e416","deviceVersion":"13.5.1","mobile":"${mobile}","devicePlatform":"iOS","appVersionRelease":"3.21.0","CFBundleDisplayName":"药联药店宝","deviceModel":"iPhoneX","code":"1112","appName":"药联药店宝","appVersionVode":"3.21.0","appVersionNumber":"1.0"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	")
		return self.response


class PrivilegeList(httpHandler):
	def __init__(self):
		super(PrivilegeList, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/privilege/list"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"assistantId":"20083722","status":"2"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户特权列表")
		return self.response


class PrivilegeV2ProgressList(httpHandler):
	def __init__(self):
		super(PrivilegeV2ProgressList, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/privilege/v2/progress/list"
		self.headers = {"Content-Type": "application/json;charset=utf-8", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户特权列表")
		return self.response


class CiMemberPage(httpHandler):
	def __init__(self):
		super(CiMemberPage, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/page"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"limit":"10","name":"","type":"1","page":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	分页列表")
		return self.response


class CodeSend(httpHandler):
	def __init__(self):
		super(CodeSend, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/v4/code/send"
		self.headers = {"Content-Type": "application/json"}
		self.params = None
		self.data = {"mobile":"18354299687","usage":"login","sendMethod":"sms","isNew":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	发送药店宝登录验证码")
		return self.response


class V4UsersSmslogin1(httpHandler):
	def __init__(self):
		super(V4UsersSmslogin1, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/v4/users/smslogin"
		self.headers = {"Content-Type": "application/json"}
		self.params = None
		self.data = {"appVersionNumber":"1.0","deviceSerial":"iPhone","deviceUuid":"3ab3747c5ef1d6602fe523a1e39d6ebdd8733eb63c49032d63005e7b586745fe","deviceVersion":"13.6.1","mobile":"18354299687","devicePlatform":"iOS","appVersionRelease":"5.2.0.2","CFBundleDisplayName":"药联药店宝","deviceModel":"iPhone 8","code":"7062","appName":"药联药店宝","appVersionVode":"5.2.0.2","isNew":"1","appPackageName":"com.xun-ao.udsa"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	药店宝验证码登录")
		return self.response


class CiMemberChatList(httpHandler):
	def __init__(self):
		super(CiMemberChatList, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/chat/list"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"memberId":"111"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	会话列表")
		return self.response


class CiMemberStartChat(httpHandler):
	def __init__(self):
		super(CiMemberStartChat, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/start/chat"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"customerMemberId":"16236586","isYdbProgram":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	单人/群组发起聊天")
		return self.response


class CiMemberDetail(httpHandler):
	def __init__(self):
		super(CiMemberDetail, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/detail"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"memberId":16236586,"isYdbProgram":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	会员详情")
		return self.response


class CiMemberAdvisorDetail(httpHandler):
	def __init__(self):
		super(CiMemberAdvisorDetail, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/advisor/detail"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"memberIds":"123"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	顾问详情")
		return self.response


class PrivilegeRuleDetail(httpHandler):
	def __init__(self):
		super(PrivilegeRuleDetail, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/privilege/ruleDetail"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	特权规则详情")
		return self.response


class CiMemberEvaluateList(httpHandler):
	def __init__(self):
		super(CiMemberEvaluateList, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/evaluateList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"page":1,"limit":10,"type":0}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	评价列表")
		return self.response


class ResourceBannerList(httpHandler):
	def __init__(self):
		super(ResourceBannerList, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/resource/bannerList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	banner列表")
		return self.response


class ResourceServiceList(httpHandler):
	def __init__(self):
		super(ResourceServiceList, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/resource/serviceList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"partnerOrganId":"635"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	服务列表")
		return self.response


class CiMemberDeleteChat(httpHandler):
	def __init__(self):
		super(CiMemberDeleteChat, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/ci/member/deleteChat"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"isGroup":"0","memberId":"16236586"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	删除某个会话")
		return self.response


class DrugstoreuserGroupCreate(httpHandler):
	def __init__(self):
		super(DrugstoreuserGroupCreate, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/group/create"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"name":"Weee","members":[{"memberId":"16236586"}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	群组新建")
		return self.response


class GroupDetail(httpHandler):
	def __init__(self):
		super(GroupDetail, self).__init__()
		self.host = "https://app.uniondrug.net"
		self.path = "/drugstoreuser/group/detail"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"}
		self.params = None
		self.data = {"groupId":"28","isYdbProgram":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	群组详情")
		return self.response


class OrderCanUseList(httpHandler):
	def __init__(self):
		super(OrderCanUseList, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/canUseList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-9FGzuShNsYwdwA"}
		self.params = None
		self.data = {"resource":"2","items":[{"itemUuid":"d2e95199-aaf2-4c04-a26b-b2336c088c7c","goodsNo":"","internalId":"137","internalIdList":"","selectFlag":"1","goodsType":"1","goodsSubType":"11","rxFlag":"1","infusionFlag":"0","unitPrice":"84.00","afterActivityUnitPrice":"0","quantity":"1","merchantId":"159798","storeId":"159932","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"优普洛","realName":"罗替高汀贴片","tradeCode":"10690100000016","image":"https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1596779043602.jpg","approvalNumber":"H20180028","manufacturer":"LTS Lohmann Therapie-Systeme AG","form":"4.5mg:10cm²*7贴","pack":"盒","batchNumber":"","memberPrice":"84.00","originalPrice":"84.00","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"1","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"1","insuranceCode":"","totalAmount":"84.00","directAmount":"0","activityAmount":"42","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":{"activityId":"","requestNo":"","activityAmount":"0","activityType":"0","activityName":""},"activityName":"","itemAttr":{"id":"0","attrs":"0,1,3,31027,30003,31061,31080,31064,31083,31227,31055","cates":"0,44017,44018,2"},"giftDrug":{"itemUuid":"","goodsNo":"","internalId":"","internalIdList":"","selectFlag":"1","goodsType":"","goodsSubType":"0","rxFlag":"0","infusionFlag":"0","unitPrice":"0","afterActivityUnitPrice":"0","quantity":"0","merchantId":"0","storeId":"0","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"","realName":"","tradeCode":"","image":"","approvalNumber":"","manufacturer":"","form":"","pack":"","batchNumber":"0","memberPrice":"0","originalPrice":"0","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"0","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"0","insuranceCode":"","totalAmount":"0","directAmount":"0","activityAmount":"0","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":"","activityName":"","itemAttr":"","giftDrug":"","isHasActivity":"0","weight":"0"},"isHasActivity":"0","weight":"0"}],"serviceItems":[],"eshop":[{"expressType":"5","expressTypeSelect":"0","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊大大","receiveMobile":"18354299687","wayBillNo":"","address":"江苏省南京市雨花台区风信路6号金证橙风里测试","storeName":"","merchantName":"","longitude":"118.779047","latitude":"31.972011","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]},{"expressType":"3","expressTypeSelect":"1","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊战岗","receiveMobile":"18354299687","wayBillNo":"","address":"清水塘街道芙蓉中路一段319号绿地中心裙房103房","storeName":"长沙邻客智慧大药房有限公司","merchantName":"邻客智慧药房DTP","longitude":"112.987239","latitude":"28.210957","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]}],"sign":{"needSign":"0","needCard":"0","agreements":[],"frontCardImage":"","backendCardImage":"","signImageUrl":"","projectId":"","schemeId":""},"temperature":{"isNeed":"0","name":"","idCard":"","mobile":"","symptom":"","temperature":"","isRisk":"0"},"rx":{"isNeedRx":True,"isHasRx":False,"chooseRxType":"0","rxWaterNo":"","rxId":"","type":"0","rxImage":"","reason":"","status":"0","userName":"","userMobile":"","rxText":"","mode":"","supplierId":"0"},"merchantName":"邻客智慧药房DTP","storeName":"长沙邻客智慧大药房有限公司","drugs":[{"itemUuid":"d2e95199-aaf2-4c04-a26b-b2336c088c7c","goodsNo":"","internalId":"137","internalIdList":"","selectFlag":"1","goodsType":"1","goodsSubType":"11","rxFlag":"1","infusionFlag":"0","unitPrice":"84.00","afterActivityUnitPrice":"0","quantity":"1","merchantId":"159798","storeId":"159932","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"优普洛","realName":"罗替高汀贴片","tradeCode":"10690100000016","image":"https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1596779043602.jpg","approvalNumber":"H20180028","manufacturer":"LTS Lohmann Therapie-Systeme AG","form":"4.5mg:10cm²*7贴","pack":"盒","batchNumber":"","memberPrice":"84.00","originalPrice":"84.00","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"1","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"1","insuranceCode":"","totalAmount":"84.00","directAmount":"0","activityAmount":"42","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":{"activityId":"","requestNo":"","activityAmount":"0","activityType":"0","activityName":""},"activityName":"","itemAttr":{"id":"0","attrs":"0,1,3,31027,30003,31061,31080,31064,31083,31227,31055","cates":"0,44017,44018,2"},"giftDrug":{"itemUuid":"","goodsNo":"","internalId":"","internalIdList":"","selectFlag":"1","goodsType":"","goodsSubType":"0","rxFlag":"0","infusionFlag":"0","unitPrice":"0","afterActivityUnitPrice":"0","quantity":"0","merchantId":"0","storeId":"0","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"","realName":"","tradeCode":"","image":"","approvalNumber":"","manufacturer":"","form":"","pack":"","batchNumber":"0","memberPrice":"0","originalPrice":"0","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"0","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"0","insuranceCode":"","totalAmount":"0","directAmount":"0","activityAmount":"0","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":"","activityName":"","itemAttr":"","giftDrug":"","isHasActivity":"0","weight":"0"},"isHasActivity":"0","weight":"0"}],"amounts":[{"type":"2","name":"权益抵扣","resourceName":"","originAmount":"0.00","amount":"0.00"},{"type":"3","name":"平台活动","resourceName":"tq平台活动111","originAmount":"42.00","amount":"42.00"}],"allDiscountAmount":"42.00","saleAmount":"42.00","allDrugDiscountAmount":"42.00","allDrugSaleAmount":"42.00","isHasDtp":"1","services":[],"drugUser":{"drugUserId":"101","name":"樊战岗","idCard":"610523199201086936","mobile":"18354299687"},"businessStartTime":"08:30","businessEndTime":"17:30","storeStatus":"0","storeTimeStatus":"2","storeOpenTime":"0","storeTime":"0","merchantId":"159798","storeId":"159932","channel":"2","orderMethod":"14","assistantMemberId":"0","assistantId":"0","cardId":"","outActivityId":"","feeCardId":"","feeAmount":"0.00","equityUuid":"","equityIds":[],"equityName":"","coupon":{"couponId":"","cardId":"","couponAmount":"0","couponType":"0","schemeId":""},"eshopConfig":{"isUseEquity":"1","isUsePromoteCoupon":"1","isUseCoupon":"1","isUseActivity":"1","isUseFeeCoupon":"1","isUseOutActivity":"1"},"isShowUnionMember":"-1","orderNo":"","mainOrderNo":"","remark":"","isNeedIdentify":"0","isNeedTimelyDistribution":"1","orderAreaLimit":"0","requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","isUpdateRemark":"0"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页1")
		return self.response


class UserWxConfig(httpHandler):
	def __init__(self):
		super(UserWxConfig, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/user/wxConfig"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-10FGzuShNsYwdwA"}
		self.params = None
		self.data = {"url":"https://wx.uniondrug.net/otoDeal/confirm-order?requestNo=3f714ab0b0e0021794b6dcead79ca0b4"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页2")
		return self.response


class UserAddressList(httpHandler):
	def __init__(self):
		super(UserAddressList, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/user/addressList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-11FGzuShNsYwdwA"}
		self.params = None
		self.data = {"limit":20,"page":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页3")
		return self.response


class OrderUpdatePreOrder(httpHandler):
	def __init__(self):
		super(OrderUpdatePreOrder, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/updatePreOrder"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-12FGzuShNsYwdwA"}
		self.params = None
		self.data = {"eshop":[{"expressType":"5","expressTypeSelect":"1","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊大大","receiveMobile":"18354299687","wayBillNo":"","address":"江苏省南京市雨花台区风信路6号金证橙风里测试","storeName":"","merchantName":"","longitude":"118.779047","latitude":"31.972011","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]},{"expressType":"3","expressTypeSelect":"0","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊战岗","receiveMobile":"18354299687","wayBillNo":"","address":"清水塘街道芙蓉中路一段319号绿地中心裙房103房","storeName":"长沙邻客智慧大药房有限公司","merchantName":"邻客智慧药房DTP","longitude":"112.987239","latitude":"28.210957","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]}],"sign":{"needSign":"0","needCard":"0","agreements":[],"frontCardImage":"","backendCardImage":"","signImageUrl":"","projectId":"","schemeId":""},"temperature":{"isNeed":"0","name":"","idCard":"","mobile":"","symptom":"","temperature":"","isRisk":"0"},"rx":{"isNeedRx":True,"isHasRx":False,"chooseRxType":"0","rxWaterNo":"","rxId":"","type":"0","rxImage":"","reason":"","status":"0","userName":"","userMobile":"","rxText":"","mode":"","supplierId":"0"},"merchantName":"邻客智慧药房DTP","storeName":"长沙邻客智慧大药房有限公司","drugs":[{"itemUuid":"d2e95199-aaf2-4c04-a26b-b2336c088c7c","goodsNo":"","internalId":"137","internalIdList":"","selectFlag":"1","goodsType":"1","goodsSubType":"11","rxFlag":"1","infusionFlag":"0","unitPrice":"84.00","afterActivityUnitPrice":"0","quantity":"1","merchantId":"159798","storeId":"159932","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"优普洛","realName":"罗替高汀贴片","tradeCode":"10690100000016","image":"https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1596779043602.jpg","approvalNumber":"H20180028","manufacturer":"LTS Lohmann Therapie-Systeme AG","form":"4.5mg:10cm²*7贴","pack":"盒","batchNumber":"","memberPrice":"84.00","originalPrice":"84.00","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"1","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"1","insuranceCode":"","totalAmount":"84.00","directAmount":"0","activityAmount":"42","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":{"activityId":"","requestNo":"","activityAmount":"0","activityType":"0","activityName":""},"activityName":"","itemAttr":{"id":"0","attrs":"0,1,3,31027,30003,31061,31080,31064,31083,31227,31055","cates":"0,44017,44018,2"},"giftDrug":{"itemUuid":"","goodsNo":"","internalId":"","internalIdList":"","selectFlag":"1","goodsType":"","goodsSubType":"0","rxFlag":"0","infusionFlag":"0","unitPrice":"0","afterActivityUnitPrice":"0","quantity":"0","merchantId":"0","storeId":"0","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"","realName":"","tradeCode":"","image":"","approvalNumber":"","manufacturer":"","form":"","pack":"","batchNumber":"0","memberPrice":"0","originalPrice":"0","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"0","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"0","insuranceCode":"","totalAmount":"0","directAmount":"0","activityAmount":"0","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":"","activityName":"","itemAttr":"","giftDrug":"","isHasActivity":"0","weight":"0"},"isHasActivity":"0","weight":"0"}],"amounts":[{"type":"2","name":"权益抵扣","resourceName":"","originAmount":"0.00","amount":"0.00"},{"type":"3","name":"平台活动","resourceName":"tq平台活动111","originAmount":"42.00","amount":"42.00"}],"allDiscountAmount":"42.00","saleAmount":"42.00","allDrugDiscountAmount":"42.00","allDrugSaleAmount":"42.00","isHasDtp":"1","services":[],"drugUser":{"drugUserId":"101","name":"樊战岗","idCard":"610523199201086936","mobile":"18354299687"},"businessStartTime":"08:30","businessEndTime":"17:30","storeStatus":"0","storeTimeStatus":"2","storeOpenTime":"0","storeTime":"0","merchantId":"159798","storeId":"159932","channel":"2","orderMethod":"14","assistantMemberId":"0","assistantId":"0","cardId":"","outActivityId":"","feeCardId":"","feeAmount":"0.00","equityUuid":"","equityIds":[],"equityName":"","coupon":{"couponId":"","cardId":"","couponAmount":"0","couponType":"0","schemeId":""},"eshopConfig":{"isUseEquity":"1","isUsePromoteCoupon":"1","isUseCoupon":"1","isUseActivity":"1","isUseFeeCoupon":"1","isUseOutActivity":"1"},"isShowUnionMember":"-1","orderNo":"","mainOrderNo":"","remark":"","isNeedIdentify":"0","isNeedTimelyDistribution":"1","orderAreaLimit":"0","requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","isUpdateRemark":"0","longitude":"","latitude":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页4")
		return self.response


class RxRxTabList(httpHandler):
	def __init__(self):
		super(RxRxTabList, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/rx/rxTabList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-13FGzuShNsYwdwA"}
		self.params = None
		self.data = {"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页5")
		return self.response


class OrderInit(httpHandler):
	def __init__(self):
		super(OrderInit, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/init"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-14FGzuShNsYwdwA"}
		self.params = None
		self.data = {"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页6")
		return self.response


class DrugUserList(httpHandler):
	def __init__(self):
		super(DrugUserList, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/drugUser/list"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-15FGzuShNsYwdwA"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页7")
		return self.response


class DrugUserDetail(httpHandler):
	def __init__(self):
		super(DrugUserDetail, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/drugUser/detail"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-16FGzuShNsYwdwA"}
		self.params = None
		self.data = {"drugUserId":"101"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页8")
		return self.response


class DrugUserAdd(httpHandler):
	def __init__(self):
		super(DrugUserAdd, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/drugUser/add"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-17FGzuShNsYwdwA"}
		self.params = None
		self.data = {"name":"樊","idCard":"123","mobile":13211111111,"relation":"朋友","actionType":"1","id":"","requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","kidney":"正常","liver":"正常","allergic":"无","anamnesis":"无","gestational":"无"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页9")
		return self.response


class RxApplyRx(httpHandler):
	def __init__(self):
		super(RxApplyRx, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/rx/applyRx"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-18FGzuShNsYwdwA"}
		self.params = None
		self.data = {"prescriptionPhoto":["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/bi0vu5ves9fv732i1fnmmck654.png"],"offLineApply":{"userName":"樊战岗","userMobile":"18354299687","prescriptionPhoto":["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/bi0vu5ves9fv732i1fnmmck654.png"]},"type":2,"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","orderNo":"","drugUserId":"101"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页10")
		return self.response


class OrderCreateOrder(httpHandler):
	def __init__(self):
		super(OrderCreateOrder, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/createOrder"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-19FGzuShNsYwdwA"}
		self.params = None
		self.data = {"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页11")
		return self.response


class OrderPreDetail(httpHandler):
	def __init__(self):
		super(OrderPreDetail, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/preDetail"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-20FGzuShNsYwdwA"}
		self.params = None
		self.data = {"mainOrderNo":"92050601603437460218"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页12")
		return self.response


class OrderRxUrl(httpHandler):
	def __init__(self):
		super(OrderRxUrl, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/rxUrl"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-21FGzuShNsYwdwA"}
		self.params = None
		self.data = {"orderNo":"92050611603437470215","mainOrderNo":"92050601603437460218"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	好药交易页13")
		return self.response


class ApiDrugCategory(httpHandler):
	def __init__(self):
		super(ApiDrugCategory, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/drug/category"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-22FGzuShNsYwdwA"}
		self.params = None
		self.data = {"page":1,"searchSource":1,"title":"","sortField":2,"sortType":2,"searchContent":"","addHistory":"0","isAccurate":"0","location":"116.397309,39.909473","storeId":"","specializeSearch":"","nearbyStores":True,"supplyEshop":"1","isGather":"1","showDrugName":"0"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商1")
		return self.response


class ApiCartAddCart(httpHandler):
	def __init__(self):
		super(ApiCartAddCart, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/cart/addCart"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-23FGzuShNsYwdwA"}
		self.params = None
		self.data = {"products":[{"scene":"1","isPreTime":"","sourceTradeCode":"312a4cb705b3d2dc71b275d4dfb90ef3","showName":"百康药房抽取式面巾纸","shops":[{"isColdChain":"0","isDtp":"0","tradeCode":"TANv%2B%2BcudXzsDTz9Y%2BgH8wlxWOY8","drugName":"","commonName":"百康药房抽取式面巾纸","brand":"","price":"9.00","img":[],"manufacturer":"河北满城县诚信纸业有限公司","approvalNumber":"冀卫消证字（2011）第0015号","description":"","isPrescription":False,"projectId":"2","merchantId":"36668","merchantStatus":"1","merchantIsPrescription":"1","storeId":"39827","shopStatus":"1","storeDomestic":"1","storeRider":"1","expressType":"0","storeOnlySelf":"1","storeDistance":"3.0","storeStartTime":"00:00:00","storeEndTime":"23:59:59","goodsInternalId":"9294","realTradeCode":"TANv%2B%2BcudXzsDTz9Y%2BgH8wlxWOY8","realCommonName":"百康药房抽取式面巾纸","form":"400张*3包","pack":"袋","sales":"175.0","channel":"2","distance":"1.1584331851680167","scene":"1","goodsSignType":"","goodsSubType":"19","goodsType":"1","isOffShelf":False,"attrs":[],"cates":[]}],"isColdChain":"0","isDtp":"0","tradeCode":"TANv%2B%2BcudXzsDTz9Y%2BgH8wlxWOY8","drugName":"","commonName":"百康药房抽取式面巾纸","brand":"","price":"9.00","img":[],"manufacturer":"河北满城县诚信纸业有限公司","approvalNumber":"冀卫消证字（2011）第0015号","description":"","isPrescription":False,"projectId":"2","merchantId":"0","merchantStatus":"1","merchantIsPrescription":"1","storeId":"0","shopStatus":"1","storeDomestic":"1","storeRider":"1","expressType":"0","storeOnlySelf":"1","storeDistance":"3.0","storeStartTime":"","storeEndTime":"","goodsInternalId":"","realTradeCode":"","realCommonName":"百康药房抽取式面巾纸","form":"400张*3包","pack":"袋","sales":"175","channel":"2","distance":"1.1584331851680167","goodsSignType":"","goodsSubType":"19","goodsType":"1","isOffShelf":False,"attrs":[],"cates":[],"quantity":1}],"signCartText":"","location":"116.397309,39.909473"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商2")
		return self.response


class ApiSearchTerms(httpHandler):
	def __init__(self):
		super(ApiSearchTerms, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/search/terms"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-24FGzuShNsYwdwA"}
		self.params = None
		self.data = {"terms":"感冒发烧"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商3")
		return self.response


class ApiSearchAssociateList(httpHandler):
	def __init__(self):
		super(ApiSearchAssociateList, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/search/associateList"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-25FGzuShNsYwdwA"}
		self.params = None
		self.data = {"text":"感冒"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商4")
		return self.response


class ApiDrugSearch(httpHandler):
	def __init__(self):
		super(ApiDrugSearch, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/drug/search"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-26FGzuShNsYwdwA"}
		self.params = None
		self.data = {"page":1,"searchSource":"1","title":"销量","up":True,"sortField":2,"sortType":1,"searchContent":"四季感冒片","addHistory":"1","isAccurate":"1","location":"116.397309,39.909473","storeId":"","specializeSearch":"","nearbyStores":True,"supplyEshop":"1","isGather":"1","showDrugName":"0"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商5")
		return self.response


class ApiMemberInfo(httpHandler):
	def __init__(self):
		super(ApiMemberInfo, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/member/info"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-27FGzuShNsYwdwA"}
		self.params = None
		self.data = None

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(0)
		self.logger.info(self.path +"	done" + "	电商6")
		return self.response


class ApiUtilGetExpressRule(httpHandler):
	def __init__(self):
		super(ApiUtilGetExpressRule, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/util/getExpressRule"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-28FGzuShNsYwdwA"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商7")
		return self.response


class ApiActivityTemporaryActivity(httpHandler):
	def __init__(self):
		super(ApiActivityTemporaryActivity, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/activity/temporaryActivity"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-29FGzuShNsYwdwA"}
		self.params = None
		self.data = {"category":"3"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商8")
		return self.response


class ApiActivityIssueCoupon(httpHandler):
	def __init__(self):
		super(ApiActivityIssueCoupon, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/activity/issueCoupon"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-30FGzuShNsYwdwA"}
		self.params = None
		self.data = {"type":"1","subStationId":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商9")
		return self.response


class ApiUtilGetNearestStore(httpHandler):
	def __init__(self):
		super(ApiUtilGetNearestStore, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/util/getNearestStore"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-31FGzuShNsYwdwA"}
		self.params = None
		self.data = {"locations":"116.397309,39.909473","subStationId":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商10")
		return self.response


class ApiMemberModalBoxNotify(httpHandler):
	def __init__(self):
		super(ApiMemberModalBoxNotify, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/member/modalBoxNotify"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-32FGzuShNsYwdwA"}
		self.params = None
		self.data = {"modal":"scanGuide"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商11")
		return self.response


class ApiNoticeIndex(httpHandler):
	def __init__(self):
		super(ApiNoticeIndex, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/notice/index"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-33FGzuShNsYwdwA"}
		self.params = None
		self.data = {"locations":"116.397309,39.909473","merchantIdStr":"627,679,36668,688,36668,688,679,679,679","limit":1000}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商12")
		return self.response


class ApiBonusMerchants(httpHandler):
	def __init__(self):
		super(ApiBonusMerchants, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/bonus/merchants"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-34FGzuShNsYwdwA"}
		self.params = None
		self.data = {"stores":[{"distance":"803","channel":"2","storeId":"40460","merchantId":"627","partnerId":"0","storeName":"沙道大药房(直营)","partnerName":"恩施恒信","long":"109.566382","lat":"29.694174","startTime":"06:30:00","endTime":"22:00:00","isOpen":True,"storeAddress":"湖北省恩施土家族苗族自治州宣恩县沙道沟镇东升宾馆酉发商场(中心店)","isOffline":"0"},{"distance":"844","channel":"2","storeId":"6780","merchantId":"679","partnerId":"0","storeName":"天地","partnerName":"北京金象","long":"116.399404","lat":"39.902066","startTime":"10:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"东长安街1号","isOffline":"0"},{"distance":"1160","channel":"2","storeId":"39827","merchantId":"36668","partnerId":"0","storeName":"前门分店","partnerName":"北京高远百康","long":"116.392221","lat":"39.899814","startTime":"00:00:00","endTime":"23:59:59","isOpen":True,"storeAddress":"北京市西城区前门西大街正阳市场4号楼北京市皓阳宾馆一层3号","isOffline":"0"},{"distance":"1496","channel":"2","storeId":"7584","merchantId":"688","partnerId":"0","storeName":"绒线胡同","partnerName":"北京国大","long":"116.369351","lat":"39.896281","startTime":"08:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"西绒线胡同6号楼","isOffline":"0"},{"distance":"2091","channel":"2","storeId":"39899","merchantId":"36668","partnerId":"0","storeName":"珠市口店","partnerName":"北京高远百康","long":"116.403250","lat":"39.891254","startTime":"08:00:00","endTime":"22:00:00","isOpen":True,"storeAddress":"珠市口东大街世纪天鼎东侧百康药房107、108号","isOffline":"0"},{"distance":"2127","channel":"2","storeId":"7570","merchantId":"688","partnerId":"0","storeName":"崇文","partnerName":"北京国大","long":"116.402497","lat":"39.887940","startTime":"00:00:00","endTime":"23:59:59","isOpen":True,"storeAddress":"西城区兴隆都市馨园8号楼","isOffline":"0"},{"distance":"2245","channel":"2","storeId":"6767","merchantId":"679","partnerId":"0","storeName":"地外","partnerName":"北京金象","long":"116.395932","lat":"39.934145","startTime":"08:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"中国北京市西城区地安门外大街139号","isOffline":"0"},{"distance":"2285","channel":"2","storeId":"6760","merchantId":"679","partnerId":"0","storeName":"崇文门","partnerName":"北京金象","long":"116.404983","lat":"39.889805","startTime":"08:30:00","endTime":"22:00:00","isOpen":True,"storeAddress":"崇文门外大街3号","isOffline":"0"},{"distance":"2715","channel":"2","storeId":"6774","merchantId":"679","partnerId":"0","storeName":"和平门","partnerName":"北京金象","long":"116.370468","lat":"39.896403","startTime":"08:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"北新华街29号","isOffline":"0"}],"limit":1000}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商13")
		return self.response


class ApiUtilWeather(httpHandler):
	def __init__(self):
		super(ApiUtilWeather, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/util/weather"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-35FGzuShNsYwdwA"}
		self.params = None
		self.data = {"city":"北京市北京市"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商14")
		return self.response


class ApiCartCheckCart(httpHandler):
	def __init__(self):
		super(ApiCartCheckCart, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/cart/checkCart"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-36FGzuShNsYwdwA"}
		self.params = None
		self.data = {"location":"116.397309,39.909473","specializeSearch":"","supplyEshop":"1","showDrugName":"0","signCartText":""}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商15")
		return self.response


class ApiActivityGetActivityIndex(httpHandler):
	def __init__(self):
		super(ApiActivityGetActivityIndex, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/activity/getActivityIndex"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-37FGzuShNsYwdwA"}
		self.params = None
		self.data = {"locations":"116.397309,39.909473","subStationId":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商16")
		return self.response


class ApiUtilFindSubstationConfig(httpHandler):
	def __init__(self):
		super(ApiUtilFindSubstationConfig, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/util/findSubstationConfig"
		self.headers = {"Content-Type": "application/json", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-38FGzuShNsYwdwA"}
		self.params = None
		self.data = {"subStationId":''}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	电商17")
		return self.response