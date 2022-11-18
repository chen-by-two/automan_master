# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_O2OFreightActivity:

	@allure.feature("O2O-开启运费活动")
	@allure.severity("blocker")
	def test_O2O_SetExpressRule_001(self):
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"mobile")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 获取默认登录验证码123456-调取接口
		bkw.activityApi_SmsReset({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile},"env":env},"dict")
		# 手机号获取后台登录的token-调取接口
		DdMobilelogin = bkw.activityApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code": "123456"},"env":env},"dict")
		# 获取登录后台的token-提取token
		logintoken = ckw.CommonKeyWord().Json_GetJsonValue(DdMobilelogin,[["data","token"]])
		# 登录运营中心后台-调取接口
		DdLogin = bkw.activityApi_DdLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"token":logintoken},"env":env},"dict")
		# 获取后台的token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(DdLogin,[["data","token"]])
		# 登录获取userid-提取userid
		memberId = ckw.CommonKeyWord().Json_GetJsonValue(DdLogin,[["data","memberId"]])
		# 开启运费活动-调取接口
		SetExpressRule = bkw.O2OPlaceTheOrderApi_AdminApiExpressSetExpressRule({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
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
},"env":env},"dict")
		# 提取开启运费活动errno
		SetExpressRuleerrno = ckw.CommonKeyWord().Json_GetJsonValue(SetExpressRule,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("VoucherCreateerrno:",SetExpressRuleerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("VoucherCreateerrno:",SetExpressRuleerrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(SetExpressRuleerrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-获取用户token")
	@allure.severity("blocker")
	def test_O2O_FindWxToken_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件获取微信token
		find_wx_token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"find_wx_token")
		# mysql执行任意sql-获取用户token
		wx_token = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_backend_auth",find_wx_token)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",wx_token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",wx_token)
		# 提取sql中微信token
		token = ckw.CommonKeyWord().Array_GetByIndex(wx_token,"0.0")
		# 提取sql中微信token
		token = ckw.CommonKeyWord().Array_GetByIndex(token,"0.0")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# token写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any("./TestFile/O2OPlaceTheOrder/token.yaml","token",token)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-生成预订单")
	@allure.severity("blocker")
	def test_O2O_CreatePreviewOrder_003(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 生成预订单-调取接口
		CreatePreviewOrder = bkw.O2OPlaceTheOrderApi_ApiOrderCreatePreviewOrder({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "sellFrom": "1",
 "sellLabel": "",
 "tid": None,
 "contractFulfillmentId": "",
 "subStationId": "1",
 "items": [{
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
  "drugName": "京都念慈菴蜜炼川贝枇杷膏",
  "commonName": "京都念慈菴蜜炼川贝枇杷膏",
  "brand": "念慈菴",
  "price": "57.27",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574937149293.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705819482.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830171.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830992.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705839605.jpg"],
  "manufacturer": "",
  "approvalNumber": "ZC20160006",
  "description": "润肺化痰、止咳平喘、护喉利咽、生津补气、调心降火。本品适用于伤风咳嗽、痰稠、痰多气喘、咽喉干痒及声音嘶哑。",
  "isPrescription": False,
  "projectId": "2",
  "merchantId": "555",
  "merchantStatus": "1",
  "merchantIsPrescription": "1",
  "storeId": "2981",
  "shopStatus": "1",
  "storeDomestic": "1",
  "storeRider": "1",
  "expressType": "0",
  "storeOnlySelf": "1",
  "storeDistance": "3.0",
  "storeStartTime": "07:30:00",
  "storeEndTime": "21:30:00",
  "goodsInternalId": "1058",
  "realTradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
  "realCommonName": "京都念慈菴蜜炼川贝枇杷膏",
  "form": "每瓶装300毫升/瓶,玻璃瓶装",
  "pack": "瓶",
  "sales": "13.0",
  "channel": "2",
  "distance": "1.2144400009174292",
  "scene": "1",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31201", "31073", "2", "3", "5", "31080", "31082", "30002", "30003", "31027", "31192", "31227"],
  "cates": ["0", "43968", "2", "43979"],
  "stock": "7",
  "goodsId": "1058",
  "internalId": "1058",
  "quantity": "1",
  "leftNums": "0",
  "sourceTradeCode": "e2b1af360ddd4f2f77bf4600c023b331",
  "isDrug": False,
  "onlySelf": "0"
 }],
 "addressId": "103898",
 "resource": 2,
 "merchantId": "555",
 "storeId": "2981",
 "selectActivityId": None,
 "selectEquityId": "",
 "selectCardId": None,
 "memberId": "6422505",
 "openid": "oylyluIX6aPo_UKbO6upJf9kLZMU",
 "wxMemberId": "6422505",
 "longitude": "121.424751",
 "latitude": "31.220537",
 "cartItems": [{
  "scene": "1",
  "isPreTime": "",
  "sourceTradeCode": "e2b1af360ddd4f2f77bf4600c023b331",
  "showName": "京都念慈菴蜜炼川贝枇杷膏",
  "shops": [{
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
   "drugName": "京都念慈菴蜜炼川贝枇杷膏",
   "commonName": "京都念慈菴蜜炼川贝枇杷膏",
   "brand": "念慈菴",
   "price": "57.27",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574937149293.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705819482.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830171.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830992.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705839605.jpg"],
   "manufacturer": "",
   "approvalNumber": "ZC20160006",
   "description": "润肺化痰、止咳平喘、护喉利咽、生津补气、调心降火。本品适用于伤风咳嗽、痰稠、痰多气喘、咽喉干痒及声音嘶哑。",
   "isPrescription": False,
   "projectId": "2",
   "merchantId": "555",
   "merchantStatus": "1",
   "merchantIsPrescription": "1",
   "storeId": "60015",
   "shopStatus": "1",
   "storeDomestic": "1",
   "storeRider": "1",
   "expressType": "0",
   "storeOnlySelf": "1",
   "storeDistance": "3.0",
   "storeStartTime": "08:00:00",
   "storeEndTime": "20:00:00",
   "goodsInternalId": "1058",
   "realTradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
   "realCommonName": "京都念慈菴蜜炼川贝枇杷膏",
   "form": "每瓶装300毫升/瓶,玻璃瓶装",
   "pack": "瓶",
   "sales": "13.0",
   "channel": "2",
   "distance": "0.1722221893211168",
   "scene": "1",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": False,
   "attrs": ["0", "1", "31201", "31073", "2", "3", "5", "31080", "31082", "30002", "30003", "31027", "31192", "31227"],
   "cates": ["0", "43968", "2", "43979"]
  }, {
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
   "drugName": "京都念慈菴蜜炼川贝枇杷膏",
   "commonName": "京都念慈菴蜜炼川贝枇杷膏",
   "brand": "念慈菴",
   "price": "57.27",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574937149293.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705819482.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830171.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830992.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705839605.jpg"],
   "manufacturer": "",
   "approvalNumber": "ZC20160006",
   "description": "润肺化痰、止咳平喘、护喉利咽、生津补气、调心降火。本品适用于伤风咳嗽、痰稠、痰多气喘、咽喉干痒及声音嘶哑。",
   "isPrescription": False,
   "projectId": "2",
   "merchantId": "555",
   "merchantStatus": "1",
   "merchantIsPrescription": "1",
   "storeId": "2981",
   "shopStatus": "1",
   "storeDomestic": "1",
   "storeRider": "1",
   "expressType": "0",
   "storeOnlySelf": "1",
   "storeDistance": "3.0",
   "storeStartTime": "07:30:00",
   "storeEndTime": "21:30:00",
   "goodsInternalId": "1058",
   "realTradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
   "realCommonName": "京都念慈菴蜜炼川贝枇杷膏",
   "form": "每瓶装300毫升/瓶,玻璃瓶装",
   "pack": "瓶",
   "sales": "13.0",
   "channel": "2",
   "distance": "1.2144400009174292",
   "scene": "1",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": False,
   "attrs": ["0", "1", "31201", "31073", "2", "3", "5", "31080", "31082", "30002", "30003", "31027", "31192", "31227"],
   "cates": ["0", "43968", "2", "43979"]
  }],
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "HQZt%2BeV4JSzqDD7%2FbOkE8gh0Uuc",
  "drugName": "京都念慈菴蜜炼川贝枇杷膏",
  "commonName": "京都念慈菴蜜炼川贝枇杷膏",
  "brand": "念慈菴",
  "price": "57.27",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1574937149293.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705819482.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830171.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705830992.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1582705839605.jpg"],
  "manufacturer": "",
  "approvalNumber": "ZC20160006",
  "description": "润肺化痰、止咳平喘、护喉利咽、生津补气、调心降火。本品适用于伤风咳嗽、痰稠、痰多气喘、咽喉干痒及声音嘶哑。",
  "isPrescription": False,
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
  "realCommonName": "京都念慈菴蜜炼川贝枇杷膏",
  "form": "每瓶装300毫升/瓶,玻璃瓶装",
  "pack": "瓶",
  "sales": "26",
  "channel": "2",
  "distance": "0.1722221893211168",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31201", "31073", "2", "3", "5", "31080", "31082", "30002", "30003", "31027", "31192", "31227"],
  "cates": ["0", "43968", "2", "43979"],
  "quantity": "1",
  "isDisplay": True,
  "selectForm": "",
  "createTime": "1658812886",
  "check": True
 }]
},"env":env},"dict")
		# 提取生成预订单errno
		CreatePreviewOrdererrno = ckw.CommonKeyWord().Json_GetJsonValue(CreatePreviewOrder,[["errno"]])
		# 提取订单号
		requestNo = ckw.CommonKeyWord().Json_GetJsonValue(CreatePreviewOrder,[["data","requestNo"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CreatePreviewOrdererrno:",CreatePreviewOrdererrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CreatePreviewOrdererrno:",CreatePreviewOrdererrno)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("requestNo:",requestNo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("requestNo:",requestNo)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CreatePreviewOrdererrno,success_errno)
		# requestNo写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","requestNo",requestNo)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-平台活动运费资源可用列表")
	@allure.severity("blocker")
	def test_O2O_OrderInit_004(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取yaml文件requestNo
		requestNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"requestNo")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 平台活动运费资源可用列表-调取接口
		OrderInit = bkw.O2OPlaceTheOrderApi_OrderInit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "requestNo": requestNo,
 "longitude": "118.779228",
 "latitude": "31.971933"
},"env":env},"dict")
		# 提取资源可用列表errno
		OrderIniterrno = ckw.CommonKeyWord().Json_GetJsonValue(OrderInit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("OrderIniterrno:",OrderIniterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("OrderIniterrno:",OrderIniterrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(OrderIniterrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-提交订单")
	@allure.severity("blocker")
	def test_O2O_OrderCreateOrder_005(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取yaml文件requestNo
		requestNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"requestNo")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 提交订单-调取接口
		CreateOrder = bkw.O2OPlaceTheOrderApi_OrderCreateOrder({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "requestNo":requestNo
},"env":env},"dict")
		# 提取提交订单errno
		CreateOrdererrno = ckw.CommonKeyWord().Json_GetJsonValue(CreateOrder,[["errno"]])
		# 提取主订单号
		mainOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(CreateOrder,[["data","mainOrderNo"]])
		# mainOrderNo写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","mainOrderNo",mainOrderNo)
		# 提取订单信息
		orderinfo = ckw.CommonKeyWord().Json_GetJsonValues(CreateOrder,[["data","orderNo"],["data","totalAmount"],["data","saleAmount"],["data","directAmount"]])
		# 提取订单试算后合计金额
		saleAmount = ckw.CommonKeyWord().Json_GetJsonValue(CreateOrder,[["data","saleAmount"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CreateOrdererrno:",CreateOrdererrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CreateOrdererrno:",CreateOrdererrno)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("mainOrderNo:",mainOrderNo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("mainOrderNo:",mainOrderNo)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("orderNo,totalAmount,saleAmount,directAmount:",orderinfo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("orderNo,totalAmount,saleAmount,directAmount:",orderinfo)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 读取yaml里试算后合计金额
		saleAmountAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"FreightActivitySaleAmount")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",saleAmountAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CreateOrdererrno,success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(saleAmountAssert,saleAmount)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-统一支付回调")
	@allure.severity("blocker")
	def test_O2O_NotifyPayment_006(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取yaml文件requestNo
		requestNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"requestNo")
		# 读取yaml文件mainOrderNo
		mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"mainOrderNo")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# mysql执行任意sql-获取统一交易支付信息payment_no
		payment_no = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_middleend_paymentcenter","SELECT payment_no FROM `cn_uniondrug_middleend_paymentcenter`.`pmc_pay_cashier` WHERE `out_trade_no` ={}".format(mainOrderNo))
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# mysql执行任意sql-获取统一交易支付信息trade_no
		trade_no = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_middleend_paymentcenter","SELECT trade_no FROM `cn_uniondrug_middleend_paymentcenter`.`pmc_pay_cashier` WHERE `out_trade_no` ={}".format(mainOrderNo))
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# mysql执行任意sql-获取统一交易支付信息pay_account_id
		pay_account_id = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_middleend_paymentcenter","SELECT pay_account_id FROM `cn_uniondrug_middleend_paymentcenter`.`pmc_pay_cashier` WHERE `out_trade_no` = {}".format(mainOrderNo))
		# 提取sql中微信payment_no
		payment_no = ckw.CommonKeyWord().Array_GetByIndex(payment_no,"0.0")
		# 提取sql中微信payment_no
		payment_no = ckw.CommonKeyWord().Array_GetByIndex(payment_no,"0.0")
		# 提取sql中微信trade_no
		trade_no = ckw.CommonKeyWord().Array_GetByIndex(trade_no,"0.0")
		# 提取sql中微信trade_no
		trade_no = ckw.CommonKeyWord().Array_GetByIndex(trade_no,"0.0")
		# 提取sql中微信pay_account_id
		pay_account_id = ckw.CommonKeyWord().Array_GetByIndex(pay_account_id,"0.0")
		# 提取sql中微信pay_account_id
		pay_account_id = ckw.CommonKeyWord().Array_GetByIndex(pay_account_id,"0.0")
		# 获取当前时间作为支付时间
		NowTime = ckw.CommonKeyWord().Time_NowTime()
		# 打印payment_no到控制台
		ckw.CommonKeyWord().Print_ToControl("payment_no：",payment_no)
		# 打印payment_no到日志
		ckw.CommonKeyWord().Print_ToLog("payment_no：",payment_no)
		# 打印trade_no到控制台
		ckw.CommonKeyWord().Print_ToControl("trade_no：",trade_no)
		# 打印trade_no到日志
		ckw.CommonKeyWord().Print_ToLog("trade_no：",trade_no)
		# 打印pay_account_id到控制台
		ckw.CommonKeyWord().Print_ToControl("pay_account_id：",pay_account_id)
		# 打印pay_account_id到日志
		ckw.CommonKeyWord().Print_ToLog("pay_account_id：",pay_account_id)
		# payment_no写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","payment_no",payment_no)
		# trade_no写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","trade_no",trade_no)
		# pay_account_id写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","pay_account_id",pay_account_id)
		# 统一支付回调-调取接口
		NotifyPayment = bkw.unifyOrderCenterApi_UnifyorderNotifyPayment({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
"paymentNo": payment_no,
"accountId": pay_account_id,
"methodCode": "CWXPAY",
"openid": "oylyluIX6aPo_UKbO6upJf9kLZMU",
"tradeType": "",
"bankType": "",
"totalFee": "0.01",
"cashFee": "0.01",
"transactionId": "220418124017062801",
"outTradeNo": trade_no,
"timeEnd": NowTime,
"refundId": "",
"outRefundNo": "",
"tradeStatus": "",
"refundAmount": "",
"gmtRefund": "",
"paymentType": "PD",
"traceNo": ""
},"env":env},"dict")
		# 统一支付回调errno
		NotifyPaymenterrno = ckw.CommonKeyWord().Json_GetJsonValue(NotifyPayment,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("NotifyPaymenterrno:",NotifyPaymenterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("NotifyPaymenterrno:",NotifyPaymenterrno)
		# 读取yaml里成功返回断言
		successno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"successno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",successno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(NotifyPaymenterrno,successno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")
