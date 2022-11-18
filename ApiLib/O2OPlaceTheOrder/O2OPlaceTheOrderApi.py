# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class ApiDrugSearch(httpHandler):
	def __init__(self):
		super(ApiDrugSearch, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/drug/search"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "page": 1,
 "searchSource": 0,
 "sessionId": "67fe3fd0b29adfc0733f29008485873d",
 "title": "综合排序",
 "sortField": 0,
 "sortType": 0,
 "searchContent": "卤米松乳膏",
 "addHistory": "1",
 "isAccurate": "0",
 "location": "118.779236,31.971867",
 "storeId": "",
 "specializeSearch": "",
 "supplyEshop": "1",
 "isGather": "1",
 "showDrugName": "0",
 "nearbyStores": "False"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-搜索药品")
		return self.response


class ApiCartAddCart(httpHandler):
	def __init__(self):
		super(ApiCartAddCart, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/cart/addCart"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "products": [{
  "scene": "1",
  "isPreTime": "",
  "sourceTradeCode": "1835997af5b1478aa59639f144c4ba85",
  "showName": "澳能 卤米松乳膏",
  "shops": [{
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
   "drugName": "澳能",
   "commonName": "卤米松乳膏",
   "brand": "澳能",
   "price": "26.50",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574992153601.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784489206.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784500348.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784504672.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784508314.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784510639.jpg"],
   "manufacturer": "澳美制药厂",
   "approvalNumber": "HC20181019",
   "description": "对皮质类固醇治疗有效的非感染性炎症性皮肤病，如脂溢性皮炎、接触性皮炎、异位性皮炎、局限性神经性皮炎、钱币状皮炎和寻常型银屑病。",
   "isPrescription": "True",
   "projectId": "2",
   "merchantId": "590",
   "merchantStatus": "1",
   "merchantIsPrescription": "1",
   "storeId": "4711",
   "shopStatus": "1",
   "storeDomestic": "1",
   "storeRider": "1",
   "expressType": "0",
   "storeOnlySelf": "1",
   "storeDistance": "3.0",
   "storeStartTime": "08:00:00",
   "storeEndTime": "23:59:59",
   "goodsInternalId": "9692",
   "realTradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
   "realCommonName": "卤米松乳膏",
   "form": "1g:0.5mg*10g",
   "pack": "盒",
   "sales": "1.0",
   "channel": "2",
   "distance": "0.02445000178892996",
   "scene": "1",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": "False",
   "attrs": ["0", "1", "31073", "2", "3", "31080", "31082", "31274", "30002", "30003", "31027", "31034", "31227", "31038"],
   "cates": ["0", "2", "44004", "44005"]
  }, {
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
   "drugName": "澳能",
   "commonName": "卤米松乳膏",
   "brand": "澳能",
   "price": "26.50",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574992153601.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784489206.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784500348.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784504672.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784508314.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784510639.jpg"],
   "manufacturer": "澳美制药厂",
   "approvalNumber": "HC20181019",
   "description": "对皮质类固醇治疗有效的非感染性炎症性皮肤病，如脂溢性皮炎、接触性皮炎、异位性皮炎、局限性神经性皮炎、钱币状皮炎和寻常型银屑病。",
   "isPrescription": "True",
   "projectId": "2",
   "merchantId": "590",
   "merchantStatus": "1",
   "merchantIsPrescription": "1",
   "storeId": "3739",
   "shopStatus": "1",
   "storeDomestic": "1",
   "storeRider": "1",
   "expressType": "0",
   "storeOnlySelf": "1",
   "storeDistance": "3.0",
   "storeStartTime": "08:00:00",
   "storeEndTime": "21:30:00",
   "goodsInternalId": "9692",
   "realTradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
   "realCommonName": "卤米松乳膏",
   "form": "1g:0.5mg*10g",
   "pack": "盒",
   "sales": "1.0",
   "channel": "2",
   "distance": "1.972615215842138",
   "scene": "1",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": False,
   "attrs": ["0", "1", "31073", "2", "3", "31080", "31082", "31274", "30002", "30003", "31027", "31034", "31227", "31038"],
   "cates": ["0", "2", "44004", "44005"]
  }],
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
  "drugName": "澳能",
  "commonName": "卤米松乳膏",
  "brand": "澳能",
  "price": "26.50",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574992153601.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784489206.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784500348.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784504672.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784508314.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784510639.jpg"],
  "manufacturer": "澳美制药厂",
  "approvalNumber": "HC20181019",
  "description": "对皮质类固醇治疗有效的非感染性炎症性皮肤病，如脂溢性皮炎、接触性皮炎、异位性皮炎、局限性神经性皮炎、钱币状皮炎和寻常型银屑病。",
  "isPrescription": True,
  "projectId": "2",
  "merchantId": "0",
  "merchantStatus": "1",
  "merchantIsPrescription": "1",
  "storeId": "0",
  "shopStatus": "1",
  "storeDomestic": "1",
  "storeRider": "1",
  "expressType": "0",
  "storeOnlySelf": "1",
  "storeDistance": "3.0",
  "storeStartTime": "",
  "storeEndTime": "",
  "goodsInternalId": "",
  "realTradeCode": "",
  "realCommonName": "卤米松乳膏",
  "form": "1g:0.5mg*10g",
  "pack": "盒",
  "sales": "2",
  "channel": "2",
  "distance": "0.02445000178892996",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31073", "2", "3", "31080", "31082", "31274", "30002", "30003", "31027", "31034", "31227", "31038"],
  "cates": ["0", "2", "44004", "44005"],
  "quantity": 1
 }],
 "signCartText": "",
 "location": "106.627393,29.712571"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-加入购物车")
		return self.response


class ApiCartShowCart(httpHandler):
	def __init__(self):
		super(ApiCartShowCart, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/cart/showCart"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-查看购物车")
		return self.response


class ApiOrderCreatePreviewOrder(httpHandler):
	def __init__(self):
		super(ApiOrderCreatePreviewOrder, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/order/createPreviewOrder"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "sellFrom": "1",
 "sellLabel": "",
 "tid": "",
 "contractFulfillmentId": "",
 "subStationId": "1",
 "items": [{
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
  "drugName": "澳能",
  "commonName": "卤米松乳膏",
  "brand": "澳能",
  "price": "26.50",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574992153601.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784489206.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784500348.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784504672.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784508314.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1594784510639.jpg"],
  "manufacturer": "澳美制药厂",
  "approvalNumber": "HC20181019",
  "description": "对皮质类固醇治疗有效的非感染性炎症性皮肤病，如脂溢性皮炎、接触性皮炎、异位性皮炎、局限性神经性皮炎、钱币状皮炎和寻常型银屑病。",
  "isPrescription": True,
  "projectId": "2",
  "merchantId": "590",
  "merchantStatus": "1",
  "merchantIsPrescription": "1",
  "storeId": "4711",
  "shopStatus": "1",
  "storeDomestic": "1",
  "storeRider": "1",
  "expressType": "0",
  "storeOnlySelf": "1",
  "storeDistance": "3.0",
  "storeStartTime": "08:00:00",
  "storeEndTime": "23:59:59",
  "goodsInternalId": "9692",
  "realTradeCode": "E1Ju%2BbB7dn7uDDb5auwE9gl3WOEx",
  "realCommonName": "卤米松乳膏",
  "form": "1g:0.5mg*10g",
  "pack": "盒",
  "sales": "1.0",
  "channel": "2",
  "distance": "0.02445000178892996",
  "scene": "1",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31073", "2", "3", "31080", "31082", "31274", "30002", "30003", "31027", "31034", "31227", "31038"],
  "cates": ["0", "2", "44004", "44005"],
  "stock": "1",
  "goodsId": "9692",
  "internalId": "9692",
  "quantity": "1",
  "leftNums": "0",
  "sourceTradeCode": "1835997af5b1478aa59639f144c4ba85",
  "isDrug": False,
  "onlySelf": "0"
 }],
 "addressId": "103898",
 "resource": 2,
 "merchantId": "590",
 "storeId": "4711",
 "selectActivityId": "",
 "selectEquityId": "",
 "selectCardId": "",
 "memberId": "6422505",
 "openid": "oylyluIX6aPo_UKbO6upJf9kLZMU",
 "wxMemberId": "6422505",
 "longitude": "106.627393",
 "latitude": "29.712571"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-生成预订单（新）")
		return self.response


class RxApplyRx(httpHandler):
	def __init__(self):
		super(RxApplyRx, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/rx/applyRx"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "prescriptionPhoto": ["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/tn3jjs53cfo173jbdgarpf0rp9.png"],
 "offLineApply": {
  "userName": "张俊超",
  "userMobile": "15380905486",
  "prescriptionPhoto": ["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/tn3jjs53cfo173jbdgarpf0rp9.png"]
 },
 "type": 2,
 "requestNo": "3d1e3ea4b4402a6407094e5ceb66418a",
 "orderNo": "",
 "drugUserId": "103"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-上传处方单")
		return self.response


class OrderCreateOrder(httpHandler):
	def __init__(self):
		super(OrderCreateOrder, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/createOrder"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "requestNo": "3d1e3ea4b4402a6407094e5ceb66418a"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-提交订单")
		return self.response


class UnifyorderConfirmUserRuleAddSign(httpHandler):
	def __init__(self):
		super(UnifyorderConfirmUserRuleAddSign, self).__init__()
		self.host = "https://wx.uniondrug.net"
		self.path = "/unifyorder/confirm/userRule/addSign"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "signUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/s8o9228apq960bt17vrmqvejvj.png"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-添加签名")
		return self.response


class MngUserCardDelete(httpHandler):
	def __init__(self):
		super(MngUserCardDelete, self).__init__()
		self.host = "http://gw.uniondrug.net"
		self.path = "/mng-user/user/card/delete"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "memberId": "6422505",
    "typeId": 1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户中心-清除实名认证")
		return self.response


class VMemberEditnamecard(httpHandler):
	def __init__(self):
		super(VMemberEditnamecard, self).__init__()
		self.host = "https://wxapi.uniondrug.net"
		self.path = "/v/member/editnamecard"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "name": "张俊超",
 "cardNum": "412829199304015574"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-添加实名认证信息")
		return self.response


class MemberUpdateUserInfo(httpHandler):
	def __init__(self):
		super(MemberUpdateUserInfo, self).__init__()
		self.host = "https://ps-auth-check.uniondrug.net"
		self.path = "/member/updateUserInfo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "cardName": "张俊超",
 "idcardProcess": "1",
 "idCard": "412829199304015574",
 "imageFrontUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/pgvbl65cci3oj5ragjkago0o3g.jpeg",
 "imageBackUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/7knsjhfs1ksk7s70chab5k86pp.jpeg",
 "gmtExpiryStart": "20200519",
 "gmtExpiryEnd": "20400519",
 "address": "南京市玄武区银城东苑73号302室",
 "authWayTag": ""
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-上传实名认证照片")
		return self.response


class ApiDrugCategory(httpHandler):
	def __init__(self):
		super(ApiDrugCategory, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/drug/category"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "page": 1,
 "searchSource": 1,
 "sessionId": "84ea34cf9ac89f10cd4db09b8fbcfae2",
 "title": "",
 "sortField": 2,
 "sortType": 2,
 "searchContent": "",
 "addHistory": "0",
 "isAccurate": "0",
 "location": "106.627393,29.712571",
 "storeId": "",
 "specializeSearch": "",
 "nearbyStores": True,
 "supplyEshop": "1",
 "isGather": "1",
 "showDrugName": "0"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-分类搜索")
		return self.response


class ApiDrugSearchDtpDrugs(httpHandler):
	def __init__(self):
		super(ApiDrugSearchDtpDrugs, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/drug/searchDtpDrugs"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "page": 1,
 "searchSource": 1,
 "sessionId": "c6874b7dc4455f70d8c03998debba009",
 "title": "综合排序",
 "sortField": 0,
 "sortType": 0,
 "text": "",
 "searchContent": "",
 "addHistory": "0",
 "isAccurate": "0",
 "location": "106.627393,29.712571"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	O2O-dtp专区搜药")
		return self.response


class OrganizebaseDirectChangeStatus(httpHandler):
	def __init__(self):
		super(OrganizebaseDirectChangeStatus, self).__init__()
		self.host = "http://merchant.backend.uniondrug.net"
		self.path = "/organizebase/direct/change/status"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
    "organizationId": "590",
    "isDirectRenewal": 1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	商户中心-开通/关闭直付换新")
		return self.response


class OrderInit(httpHandler):
	def __init__(self):
		super(OrderInit, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/init"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "requestNo": "963cd62cfe50e8076bea59fc142be05f",
 "longitude": "118.779263",
 "latitude": "31.971861"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	平台活动运费资源可用列表")
		return self.response


class OrderUpdatePreOrder(httpHandler):
	def __init__(self):
		super(OrderUpdatePreOrder, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/updatePreOrder"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "sign": {
  "needSign": "1",
  "needCard": "1",
  "agreements": [{
   "resourceId": "0",
   "resourceType": "0",
   "agreementId": "16",
   "agreementName": "lucky专用协议",
   "agreementUrl": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/ucc52b786aadea4e2eb59a7bd90f7e0f72.pdf"
  }, {
   "resourceId": "0",
   "resourceType": "0",
   "agreementId": "17",
   "agreementName": "四季豆",
   "agreementUrl": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/ucc4651344c8ff46e09d6caadbe0beb81c.pdf"
  }],
  "frontCardImage": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/pgvbl65cci3oj5ragjkago0o3g.jpeg",
  "backendCardImage": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/7knsjhfs1ksk7s70chab5k86pp.jpeg",
  "signImageUrl": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/s8o9228apq960bt17vrmqvejvj.png",
  "projectId": "710",
  "schemeId": ""
 },
 "temperature": {
  "isNeed": "0",
  "name": "",
  "idCard": "",
  "mobile": "",
  "symptom": "",
  "temperature": "",
  "isRisk": "0"
 },
 "rx": {
  "isNeedRx": False,
  "isHasRx": False,
  "chooseRxType": "0",
  "rxWaterNo": "",
  "rxId": "",
  "type": "0",
  "rxImage": "",
  "reason": "",
  "status": "0",
  "userName": "",
  "userMobile": "",
  "rxText": "",
  "mode": "",
  "supplierId": "0",
  "isRxPass": "1"
 },
 "merchantName": "泰康在线",
 "storeName": "荣昌区西大街一店",
 "isHasDtp": "0",
 "drugUser": {
  "drugUserId": "103",
  "name": "张俊超",
  "idCard": "412829199304015574",
  "mobile": "15380905486",
  "signUrl": "",
  "cardFrontUrl": "",
  "cardBackUrl": "",
  "address": "",
  "startDate": "",
  "endDate": ""
 },
 "businessStartTime": "08:00",
 "businessEndTime": "21:30",
 "storeStatus": "0",
 "storeTimeStatus": "0",
 "storeOpenTime": "0",
 "storeTime": "0",
 "merchantId": "590",
 "storeId": "3771",
 "channel": "2",
 "orderMethod": "3",
 "assistantMemberId": "0",
 "assistantId": "0",
 "cardId": "",
 "outActivityId": "",
 "feeCardId": "f2b3d679eb2f43dfb604",
 "equityUuid": "e2652001ba87654185f910d9cc0186bd",
 "equityName": "驻店宝-面额卡",
 "isShowUnionMember": "-1",
 "orderNo": "",
 "mainOrderNo": "",
 "remark": "",
 "isNeedIdentify": "0",
 "orderAreaLimit": "0",
 "isLockResource": "0",
 "requestNo": "16508cd3a95158cb676d0f1a48351b0d",
 "isUpdateRemark": "0",
 "isNeedTimelyDistribution": "1",
 "drugs": [{
  "itemUuid": "8726e6a4-e9b9-4041-94dc-e6520884f7b7",
  "goodsNo": "",
  "internalId": "61428",
  "internalIdList": "",
  "selectFlag": "1",
  "goodsType": "1",
  "goodsSubType": "11",
  "rxFlag": "0",
  "infusionFlag": "0",
  "unitPrice": "18.00",
  "afterActivityUnitPrice": "18.00",
  "quantity": "1",
  "merchantId": "590",
  "storeId": "3771",
  "belongInfusionMerchantId": "0",
  "belongInfusionStoreId": "0",
  "commonName": "复方桔梗止咳片",
  "realName": "复方桔梗止咳片",
  "tradeCode": "6943712731678",
  "image": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060483763.jpg",
  "approvalNumber": "国药准字Z20073167",
  "manufacturer": "河南省新四方制药有限公司",
  "form": "0.25克*48片",
  "pack": "盒",
  "batchNumber": "",
  "memberPrice": "18.00",
  "originalPrice": "18.00",
  "productId": "0",
  "fromItemInternalId": "",
  "isRule": "0",
  "isDtp": "0",
  "productionDate": "",
  "expireDate": "",
  "buyGifts": "0",
  "isSelectActivity": "1",
  "insuranceCode": "",
  "totalAmount": "18.00",
  "directAmount": "0",
  "activityAmount": "0",
  "discountAmount": "0",
  "couponAmount": "0",
  "promoteCouponAmount": "0",
  "averageAmount": "0",
  "activity": {
   "activityId": "",
   "requestNo": "",
   "activityAmount": "0",
   "activityType": "0",
   "activityName": ""
  },
  "activityName": "",
  "itemAttr": {
   "id": "0",
   "attrs": "0,1,31201,2,30003,6,31080,31083",
   "cates": "0,43968,2,43979"
  },
  "giftDrug": {
   "itemUuid": "",
   "goodsNo": "",
   "internalId": "",
   "internalIdList": "",
   "selectFlag": "1",
   "goodsType": "",
   "goodsSubType": "0",
   "rxFlag": "0",
   "infusionFlag": "0",
   "unitPrice": "0",
   "afterActivityUnitPrice": "0",
   "quantity": "0",
   "merchantId": "0",
   "storeId": "0",
   "belongInfusionMerchantId": "0",
   "belongInfusionStoreId": "0",
   "commonName": "",
   "realName": "",
   "tradeCode": "",
   "image": "",
   "approvalNumber": "",
   "manufacturer": "",
   "form": "",
   "pack": "",
   "batchNumber": "0",
   "memberPrice": "0",
   "originalPrice": "0",
   "productId": "0",
   "fromItemInternalId": "",
   "isRule": "0",
   "isDtp": "0",
   "productionDate": "",
   "expireDate": "",
   "buyGifts": "0",
   "isSelectActivity": "0",
   "insuranceCode": "",
   "totalAmount": "0",
   "directAmount": "0",
   "activityAmount": "0",
   "discountAmount": "0",
   "couponAmount": "0",
   "promoteCouponAmount": "0",
   "averageAmount": "0",
   "activity": "",
   "activityName": "",
   "itemAttr": "",
   "giftDrug": "",
   "isHasActivity": "0",
   "weight": "0"
  },
  "isHasActivity": "0",
  "weight": "0"
 }],
 "amounts": [{
  "type": "2",
  "name": "权益抵扣",
  "resourceName": "驻店宝-面额卡",
  "originAmount": "0.00",
  "amount": "0.00"
 }, {
  "type": "3",
  "name": "平台活动",
  "resourceName": "",
  "originAmount": "0.00",
  "amount": "0.00"
 }, {
  "type": "4",
  "name": "运费券",
  "resourceName": "",
  "originAmount": "2.00",
  "amount": "2.00"
 }],
 "allDiscountAmount": "2.00",
 "allDrugDiscountAmount": "2.00",
 "allDrugSaleAmount": "27.00",
 "saleAmount": "27.00",
 "feeAmount": "11.00",
 "eshopConfig": {
  "isUseEquity": "1",
  "isUsePromoteCoupon": "1",
  "isUseCoupon": "1",
  "isUseActivity": "1",
  "isUseFeeCoupon": "1",
  "isUseOutActivity": "1"
 },
 "coupon": {
  "id": "0",
  "trolleyId": "0",
  "cardId": "",
  "couponId": "",
  "couponAmount": "0",
  "couponType": "0",
  "schemeId": ""
 },
 "equityIds": ["23420789", "23422587"],
 "eshop": [{
  "expressType": "4",
  "expressAmount": "11",
  "expressDiscount": "0",
  "mitigateRuleString": "",
  "addressId": "103898",
  "receiveName": "张大大",
  "receiveMobile": "15380905486",
  "wayBillNo": "2207055110148100100579214",
  "address": "重庆市重庆市渝北区万家燕大药房(两路碧津店)测试",
  "storeName": "",
  "merchantName": "",
  "longitude": "106.627393",
  "latitude": "29.712571",
  "distance": "",
  "distanceMi": "",
  "deliveryMethod": "0",
  "deliverTime": "",
  "deliverDistance": "0",
  "deliveryMethods": [],
  "expressTypeSelect": "0"
 }, {
  "expressType": "3",
  "expressAmount": "0",
  "expressDiscount": "0",
  "mitigateRuleString": "",
  "addressId": "103898",
  "receiveName": "张俊超",
  "receiveMobile": "15380905486",
  "wayBillNo": "",
  "address": "荣昌县昌元街道西大街中医院斜对面",
  "storeName": "荣昌区西大街一店",
  "merchantName": "泰康在线",
  "longitude": "105.587387",
  "latitude": "29.400658",
  "distance": "1293.98km",
  "distanceMi": "1",
  "deliveryMethod": "0",
  "deliverTime": "",
  "deliverDistance": "0",
  "deliveryMethods": [],
  "expressTypeSelect": "1"
 }],
 "services": [],
 "longitude": "118.779245",
 "latitude": "31.971877"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	更新预订单")
		return self.response


class CanUseList(httpHandler):
	def __init__(self):
		super(CanUseList, self).__init__()
		self.host = "https://pm-dpsp-tc-order.uniondrug.net"
		self.path = "/order/canUseList"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "resource": "2",
 "items": [{
  "itemUuid": "4d14bf34-a5b6-4ee2-a104-d80b96f7fa1c",
  "goodsNo": "",
  "internalId": "61428",
  "internalIdList": "",
  "selectFlag": "1",
  "goodsType": "1",
  "goodsSubType": "11",
  "rxFlag": "0",
  "infusionFlag": "0",
  "unitPrice": "18.00",
  "afterActivityUnitPrice": "18.00",
  "quantity": "1",
  "merchantId": "590",
  "storeId": "3771",
  "belongInfusionMerchantId": "0",
  "belongInfusionStoreId": "0",
  "commonName": "复方桔梗止咳片",
  "realName": "复方桔梗止咳片",
  "tradeCode": "6943712731678",
  "image": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060483763.jpg",
  "approvalNumber": "国药准字Z20073167",
  "manufacturer": "河南省新四方制药有限公司",
  "form": "0.25克*48片",
  "pack": "盒",
  "batchNumber": "",
  "memberPrice": "18.00",
  "originalPrice": "18.00",
  "productId": "0",
  "fromItemInternalId": "",
  "isRule": "0",
  "isDtp": "0",
  "productionDate": "",
  "expireDate": "",
  "buyGifts": "0",
  "isSelectActivity": "1",
  "insuranceCode": "",
  "totalAmount": "18.00",
  "directAmount": "0",
  "activityAmount": "0",
  "discountAmount": "0",
  "couponAmount": "0",
  "promoteCouponAmount": "0",
  "averageAmount": "0",
  "activity": {
   "activityId": "",
   "requestNo": "",
   "activityAmount": "0",
   "activityType": "0",
   "activityName": ""
  },
  "activityName": "",
  "itemAttr": {
   "id": "0",
   "attrs": "0,1,31201,2,30003,6,31080,31083",
   "cates": "0,43968,2,43979"
  },
  "giftDrug": {
   "itemUuid": "",
   "goodsNo": "",
   "internalId": "",
   "internalIdList": "",
   "selectFlag": "1",
   "goodsType": "",
   "goodsSubType": "0",
   "rxFlag": "0",
   "infusionFlag": "0",
   "unitPrice": "0",
   "afterActivityUnitPrice": "0",
   "quantity": "0",
   "merchantId": "0",
   "storeId": "0",
   "belongInfusionMerchantId": "0",
   "belongInfusionStoreId": "0",
   "commonName": "",
   "realName": "",
   "tradeCode": "",
   "image": "",
   "approvalNumber": "",
   "manufacturer": "",
   "form": "",
   "pack": "",
   "batchNumber": "0",
   "memberPrice": "0",
   "originalPrice": "0",
   "productId": "0",
   "fromItemInternalId": "",
   "isRule": "0",
   "isDtp": "0",
   "productionDate": "",
   "expireDate": "",
   "buyGifts": "0",
   "isSelectActivity": "0",
   "insuranceCode": "",
   "totalAmount": "0",
   "directAmount": "0",
   "activityAmount": "0",
   "discountAmount": "0",
   "couponAmount": "0",
   "promoteCouponAmount": "0",
   "averageAmount": "0",
   "activity": "",
   "activityName": "",
   "itemAttr": "",
   "giftDrug": "",
   "isHasActivity": "0",
   "weight": "0"
  },
  "isHasActivity": "0",
  "weight": "0"
 }],
 "serviceItems": [{
  "type": "0",
  "isSelect": "1",
  "productId": "8",
  "goodsType": "4",
  "merchantId": "539",
  "storeId": "74596",
  "infusionFlag": "0",
  "unitPrice": "5.00",
  "commonName": "药品过期换新服务",
  "goodsNo": "539-782604824003739648",
  "discountAmount": "5.00",
  "couponAmount": "0",
  "coupons": []
 }],
 "sign": {
  "needSign": "1",
  "needCard": "1",
  "agreements": [{
   "resourceId": "0",
   "resourceType": "0",
   "agreementId": "16",
   "agreementName": "lucky专用协议",
   "agreementUrl": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/ucc52b786aadea4e2eb59a7bd90f7e0f72.pdf"
  }, {
   "resourceId": "0",
   "resourceType": "0",
   "agreementId": "17",
   "agreementName": "四季豆",
   "agreementUrl": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/ucc4651344c8ff46e09d6caadbe0beb81c.pdf"
  }],
  "frontCardImage": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/pgvbl65cci3oj5ragjkago0o3g.jpeg",
  "backendCardImage": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/7knsjhfs1ksk7s70chab5k86pp.jpeg",
  "signImageUrl": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/s8o9228apq960bt17vrmqvejvj.png",
  "projectId": "710",
  "schemeId": ""
 },
 "temperature": {
  "isNeed": "0",
  "name": "",
  "idCard": "",
  "mobile": "",
  "symptom": "",
  "temperature": "",
  "isRisk": "0"
 },
 "rx": {
  "isNeedRx": False,
  "isHasRx": False,
  "chooseRxType": "0",
  "rxWaterNo": "",
  "rxId": "",
  "type": "0",
  "rxImage": "",
  "reason": "",
  "status": "0",
  "userName": "",
  "userMobile": "",
  "rxText": "",
  "mode": "",
  "supplierId": "0",
  "isRxPass": "1"
 },
 "merchantName": "泰康在线",
 "storeName": "荣昌区西大街一店",
 "isHasDtp": "0",
 "drugUser": {
  "drugUserId": "103",
  "name": "张俊超",
  "idCard": "412829199304015574",
  "mobile": "15380905486",
  "signUrl": "",
  "cardFrontUrl": "",
  "cardBackUrl": "",
  "address": "",
  "startDate": "",
  "endDate": ""
 },
 "businessStartTime": "08:00",
 "businessEndTime": "21:30",
 "storeStatus": "0",
 "storeTimeStatus": "0",
 "storeOpenTime": "0",
 "storeTime": "0",
 "merchantId": "590",
 "storeId": "3771",
 "channel": "2",
 "orderMethod": "3",
 "assistantMemberId": "0",
 "assistantId": "0",
 "cardId": "",
 "outActivityId": "",
 "feeCardId": "f2b3d679eb2f43dfb604",
 "equityUuid": "e2652001ba87654185f910d9cc0186bd",
 "equityName": "驻店宝-面额卡",
 "isShowUnionMember": "-1",
 "orderNo": "",
 "mainOrderNo": "",
 "remark": "",
 "isNeedIdentify": "0",
 "orderAreaLimit": "0",
 "isLockResource": "0",
 "requestNo": "7a04b1738e5705486dcd35a2cdf00f90",
 "isUpdateRemark": "0",
 "isNeedTimelyDistribution": "1",
 "drugs": [{
  "itemUuid": "4d14bf34-a5b6-4ee2-a104-d80b96f7fa1c",
  "goodsNo": "",
  "internalId": "61428",
  "internalIdList": "",
  "selectFlag": "1",
  "goodsType": "1",
  "goodsSubType": "11",
  "rxFlag": "0",
  "infusionFlag": "0",
  "unitPrice": "18.00",
  "afterActivityUnitPrice": "18.00",
  "quantity": "1",
  "merchantId": "590",
  "storeId": "3771",
  "belongInfusionMerchantId": "0",
  "belongInfusionStoreId": "0",
  "commonName": "复方桔梗止咳片",
  "realName": "复方桔梗止咳片",
  "tradeCode": "6943712731678",
  "image": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060483763.jpg",
  "approvalNumber": "国药准字Z20073167",
  "manufacturer": "河南省新四方制药有限公司",
  "form": "0.25克*48片",
  "pack": "盒",
  "batchNumber": "",
  "memberPrice": "18.00",
  "originalPrice": "18.00",
  "productId": "0",
  "fromItemInternalId": "",
  "isRule": "0",
  "isDtp": "0",
  "productionDate": "",
  "expireDate": "",
  "buyGifts": "0",
  "isSelectActivity": "1",
  "insuranceCode": "",
  "totalAmount": "18.00",
  "directAmount": "0",
  "activityAmount": "0",
  "discountAmount": "0",
  "couponAmount": "0",
  "promoteCouponAmount": "0",
  "averageAmount": "0",
  "activity": {
   "activityId": "",
   "requestNo": "",
   "activityAmount": "0",
   "activityType": "0",
   "activityName": ""
  },
  "activityName": "",
  "itemAttr": {
   "id": "0",
   "attrs": "0,1,31201,2,30003,6,31080,31083",
   "cates": "0,43968,2,43979"
  },
  "giftDrug": {
   "itemUuid": "",
   "goodsNo": "",
   "internalId": "",
   "internalIdList": "",
   "selectFlag": "1",
   "goodsType": "",
   "goodsSubType": "0",
   "rxFlag": "0",
   "infusionFlag": "0",
   "unitPrice": "0",
   "afterActivityUnitPrice": "0",
   "quantity": "0",
   "merchantId": "0",
   "storeId": "0",
   "belongInfusionMerchantId": "0",
   "belongInfusionStoreId": "0",
   "commonName": "",
   "realName": "",
   "tradeCode": "",
   "image": "",
   "approvalNumber": "",
   "manufacturer": "",
   "form": "",
   "pack": "",
   "batchNumber": "0",
   "memberPrice": "0",
   "originalPrice": "0",
   "productId": "0",
   "fromItemInternalId": "",
   "isRule": "0",
   "isDtp": "0",
   "productionDate": "",
   "expireDate": "",
   "buyGifts": "0",
   "isSelectActivity": "0",
   "insuranceCode": "",
   "totalAmount": "0",
   "directAmount": "0",
   "activityAmount": "0",
   "discountAmount": "0",
   "couponAmount": "0",
   "promoteCouponAmount": "0",
   "averageAmount": "0",
   "activity": "",
   "activityName": "",
   "itemAttr": "",
   "giftDrug": "",
   "isHasActivity": "0",
   "weight": "0"
  },
  "isHasActivity": "0",
  "weight": "0"
 }],
 "amounts": [{
  "type": "2",
  "name": "权益抵扣",
  "resourceName": "驻店宝-面额卡",
  "originAmount": "0.00",
  "amount": "0.00"
 }, {
  "type": "3",
  "name": "平台活动",
  "resourceName": "",
  "originAmount": "0.00",
  "amount": "0.00"
 }],
 "allDiscountAmount": "0.00",
 "allDrugDiscountAmount": "0.00",
 "allDrugSaleAmount": "18.00",
 "saleAmount": "18.00",
 "feeAmount": "0.00",
 "services": [{
  "type": "0",
  "isSelect": "1",
  "productId": "8",
  "goodsType": "4",
  "merchantId": "539",
  "storeId": "74596",
  "infusionFlag": "0",
  "unitPrice": "5.00",
  "commonName": "药品过期换新服务",
  "goodsNo": "539-782604824003739648",
  "discountAmount": "5.00",
  "couponAmount": "0",
  "coupons": []
 }],
 "eshopConfig": {
  "isUseEquity": "1",
  "isUsePromoteCoupon": "1",
  "isUseCoupon": "1",
  "isUseActivity": "1",
  "isUseFeeCoupon": "1",
  "isUseOutActivity": "1"
 },
 "coupon": {
  "id": "0",
  "trolleyId": "0",
  "cardId": "",
  "couponId": "",
  "couponAmount": "0",
  "couponType": "0",
  "schemeId": ""
 },
 "equityIds": ["23420789", "23422587"],
 "eshop": [{
  "expressType": "4",
  "expressTypeSelect": "0",
  "expressAmount": "11",
  "expressDiscount": "0",
  "mitigateRuleString": "",
  "addressId": "103898",
  "receiveName": "张大大",
  "receiveMobile": "15380905486",
  "wayBillNo": "",
  "address": "重庆市重庆市渝北区万家燕大药房(两路碧津店)测试",
  "storeName": "",
  "merchantName": "",
  "longitude": "106.627393",
  "latitude": "29.712571",
  "distance": "",
  "distanceMi": "",
  "deliveryMethod": "0",
  "deliverTime": "",
  "deliverDistance": "0",
  "deliveryMethods": []
 }, {
  "expressType": "3",
  "expressTypeSelect": "1",
  "expressAmount": "0",
  "expressDiscount": "0",
  "mitigateRuleString": "",
  "addressId": "103898",
  "receiveName": "张俊超",
  "receiveMobile": "15380905486",
  "wayBillNo": "",
  "address": "荣昌县昌元街道西大街中医院斜对面",
  "storeName": "荣昌区西大街一店",
  "merchantName": "泰康在线",
  "longitude": "105.587387",
  "latitude": "29.400658",
  "distance": "1293.98km",
  "distanceMi": "1",
  "deliveryMethod": "0",
  "deliverTime": "",
  "deliverDistance": "0",
  "deliveryMethods": []
 }]
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	订单优惠权益资源可用列表")
		return self.response


class VoucherCreate(httpHandler):
	def __init__(self):
		super(VoucherCreate, self).__init__()
		self.host = "http://admincustomercenter.backend.uniondrug.net"
		self.path = "/voucher/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
    "memberId": "6422505",
    "schemeId": "20220706095111937161",
    "requestNo": "2022-07-06 10:15:25"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	客服中心-发放优惠券")
		return self.response


class ApiWxJssdk(httpHandler):
	def __init__(self):
		super(ApiWxJssdk, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/wx/jssdk"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "url": "https://wx.uniondrug.net/v2/open?to=shop&merchantId=590&storeMerchantId=4711"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	解析门店二维码链接")
		return self.response


class ApiSweepGetPartnerStores(httpHandler):
	def __init__(self):
		super(ApiSweepGetPartnerStores, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/api/sweep/getPartnerStores"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
 "merchantId": "590",
 "storeMerchantId": "4711"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取连锁门店信息")
		return self.response


class AdminApiExpressSetExpressRule(httpHandler):
	def __init__(self):
		super(AdminApiExpressSetExpressRule, self).__init__()
		self.host = "https://eshop.uniondrug.net"
		self.path = "/admin/api/express/setExpressRule"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Token"}
		self.params = None
		self.data = {
    "id": "2",
    "projectId": "2",
    "conditionPrice": "5.00",
    "minusPrice": "1.00",
    "startDate": "2020-10-28 11:13:15",
    "endDate": "2025-01-26 17:11:46",
    "description": "满5减1",
    "status": "1",
    "weight": "2",
    "deliveryType": "1,2,4",
    "chooseChannel": "0",
    "channelIds": ""
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	开启运费活动")
		return self.response