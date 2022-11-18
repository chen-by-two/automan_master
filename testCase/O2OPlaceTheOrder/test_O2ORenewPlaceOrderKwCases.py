# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_O2ORenewPlaceOrder:

	@allure.feature("O2O-开启直付附加换新-登录运营中心后台")
	@allure.severity("blocker")
	def test_O2O_OpenRenew_001(self):
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
		# 开启直付附加换新-调取接口
		DirectChangeStatus = bkw.O2OPlaceTheOrderApi_OrganizebaseDirectChangeStatus({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "organizationId": "590",
    "isDirectRenewal": 1
},"env":env},"dict")
		# 提取开启直付附加换新errno
		DirectChangeStatuserrno = ckw.CommonKeyWord().Json_GetJsonValue(DirectChangeStatus,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DirectChangeStatuserrno:",DirectChangeStatuserrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DirectChangeStatuserrno:",DirectChangeStatuserrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DirectChangeStatuserrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-获取用户token")
	@allure.severity("blocker")
	def test_O2O_FindToken_002(self):
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

	@allure.feature("O2O-加入购物车")
	@allure.severity("blocker")
	def test_O2O_AddCart_002(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 加入购物车-调取接口
		AddCart = bkw.O2OPlaceTheOrderApi_ApiCartAddCart({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "products": [{
  "scene": "2",
  "isPreTime": "",
  "sourceTradeCode": "1da09041d99670e0ce93ba64e29dd9d9",
  "showName": "盛杰奥 复方桔梗止咳片",
  "shops": [{
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "TlJirrYoJX7sDTv%2FbewF8wpzXOYw",
   "drugName": "复方桔梗止咳片",
   "commonName": "复方桔梗止咳片",
   "brand": "盛杰奥",
   "price": "18.00",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060483763.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060481034.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060489393.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060481808.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060486705.jpg"],
   "manufacturer": "河南省新四方制药有限公司",
   "approvalNumber": "国药准字Z20073167",
   "description": "镇咳、祛痰。",
   "isPrescription": False,
   "projectId": "2",
   "merchantId": "590",
   "merchantStatus": "1",
   "merchantIsPrescription": "1",
   "storeId": "3771",
   "shopStatus": "1",
   "storeDomestic": "1",
   "storeRider": "1",
   "expressType": "0",
   "storeOnlySelf": "1",
   "storeDistance": "3.0",
   "storeStartTime": "08:00:00",
   "storeEndTime": "21:30:00",
   "goodsInternalId": "61428",
   "realTradeCode": "TlJirrYoJX7sDTv%2FbewF8wpzXOYw",
   "realCommonName": "复方桔梗止咳片",
   "form": "0.25克*48片",
   "pack": "盒",
   "sales": "1.0",
   "channel": "2",
   "distance": "",
   "scene": "2",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": False,
   "attrs": ["0", "1", "31201", "2", "30003", "6", "31080", "31083"],
   "cates": ["0", "43968", "2", "43979"]
  }],
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "TlJirrYoJX7sDTv%2FbewF8wpzXOYw",
  "drugName": "复方桔梗止咳片",
  "commonName": "复方桔梗止咳片",
  "brand": "盛杰奥",
  "price": "18.00",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060483763.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060481034.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060489393.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060481808.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060486705.jpg"],
  "manufacturer": "河南省新四方制药有限公司",
  "approvalNumber": "国药准字Z20073167",
  "description": "镇咳、祛痰。",
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
  "realCommonName": "复方桔梗止咳片",
  "form": "0.25克*48片",
  "pack": "盒",
  "sales": "1",
  "channel": "2",
  "distance": "",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31201", "2", "30003", "6", "31080", "31083"],
  "cates": ["0", "43968", "2", "43979"],
  "quantity": 2
 }],
 "signCartText": "",
 "location": "106.627393,29.712571"
},"env":env},"dict")
		# 提取加入购物车errno
		AddCarterrno = ckw.CommonKeyWord().Json_GetJsonValue(AddCart,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AddCarterrno:",AddCarterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AddCarterrno:",AddCarterrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AddCarterrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-生成预订单")
	@allure.severity("blocker")
	def test_O2O_CreatePreviewOrder_002(self):
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
 "tid": "",
 "contractFulfillmentId": "",
 "subStationId": "1",
 "items": [{
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "TlJirrYoJX7sDTv%2FbewF8wpzXOYw",
  "drugName": "复方桔梗止咳片",
  "commonName": "复方桔梗止咳片",
  "brand": "盛杰奥",
  "price": "18.00",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060483763.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060481034.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060489393.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060481808.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1619060486705.jpg"],
  "manufacturer": "河南省新四方制药有限公司",
  "approvalNumber": "国药准字Z20073167",
  "description": "镇咳、祛痰。",
  "isPrescription": False,
  "projectId": "2",
  "merchantId": "590",
  "merchantStatus": "1",
  "merchantIsPrescription": "1",
  "storeId": "3771",
  "shopStatus": "1",
  "storeDomestic": "1",
  "storeRider": "1",
  "expressType": "0",
  "storeOnlySelf": "1",
  "storeDistance": "3.0",
  "storeStartTime": "08:00:00",
  "storeEndTime": "21:30:00",
  "goodsInternalId": "61428",
  "realTradeCode": "TlJirrYoJX7sDTv%2FbewF8wpzXOYw",
  "realCommonName": "复方桔梗止咳片",
  "form": "0.25克*48片",
  "pack": "盒",
  "sales": "1.0",
  "channel": "2",
  "distance": "",
  "scene": "2",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31201", "2", "30003", "6", "31080", "31083"],
  "cates": ["0", "43968", "2", "43979"],
  "stock": "1",
  "goodsId": "61428",
  "internalId": "61428",
  "quantity": "1",
  "leftNums": "1",
  "sourceTradeCode": "1da09041d99670e0ce93ba64e29dd9d9",
  "isDrug": True,
  "onlySelf": "0"
 }],
 "addressId": "103898",
 "resource": 2,
 "merchantId": "590",
 "storeId": "3771",
 "selectActivityId": "",
 "selectEquityId": "",
 "selectCardId": "",
 "longitude": "106.627393",
 "latitude": "29.712571"
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
	def test_O2O_OrderInit_001(self):
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
		# 平台活动运费资源-调取接口
		OrderInit = bkw.O2OPlaceTheOrderApi_OrderInit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "requestNo":requestNo,
 "longitude": "118.779263",
 "latitude": "31.971861"
},"env":env},"dict")
		# 提取平台活动运费资源errno
		OrderIniterrno = ckw.CommonKeyWord().Json_GetJsonValue(OrderInit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CreateOrdererrno:",OrderIniterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CreateOrdererrno:",OrderIniterrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(OrderIniterrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-更新预订单--自提")
	@allure.severity("blocker")
	def test_O2O_UpdatePreOrder_001(self):
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
		# 更新预订单-调取接口
		UpdatePreOrder = bkw.O2OPlaceTheOrderApi_OrderUpdatePreOrder({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
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
 "requestNo": requestNo,
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
},"env":env},"dict")
		# 提取更新预订单errno
		UpdatePreOrdererrno = ckw.CommonKeyWord().Json_GetJsonValue(UpdatePreOrder,[["errno"]])
		# 提取更新预订单commonName
		commonName = ckw.CommonKeyWord().Json_GetJsonValue(UpdatePreOrder,[["data","services",0,"commonName"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("UpdatePreOrdererrno:",UpdatePreOrdererrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("UpdatePreOrdererrno:",UpdatePreOrdererrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(UpdatePreOrdererrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-优惠权益资源可用列表")
	@allure.severity("blocker")
	def test_O2O_CanUseList_001(self):
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
		# 优惠权益资源可用列表-调取接口
		CanUseList = bkw.O2OPlaceTheOrderApi_CanUseList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
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
 "requestNo": requestNo,
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
},"env":env},"dict")
		# 提取优惠权益资源可用列表errno
		CanUseListerrno = ckw.CommonKeyWord().Json_GetJsonValue(CanUseList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CanUseListerrno:",CanUseListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CanUseListerrno:",CanUseListerrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CanUseListerrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-提交订单")
	@allure.severity("blocker")
	def test_O2O_CreateOrder_001(self):
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
		# 提取订单信息
		orderinfo = ckw.CommonKeyWord().Json_GetJsonValues(CreateOrder,[["data","orderNo"],["data","totalAmount"],["data","saleAmount"],["data","directAmount"]])
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
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CreateOrdererrno,success_errno)
		# mainOrderNo写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","mainOrderNo",mainOrderNo)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-统一支付回调")
	@allure.severity("blocker")
	def test_O2O_NotifyPayment_001(self):
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

	@allure.feature("O2O-关闭直付附加换新-登录运营中心后台")
	@allure.severity("blocker")
	def test_O2O_CloseRenew_001(self):
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
		# 关闭直付附加换新-调取接口
		DirectChangeStatus = bkw.O2OPlaceTheOrderApi_OrganizebaseDirectChangeStatus({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "organizationId": "590",
    "isDirectRenewal": 0
},"env":env},"dict")
		# 提取关闭直付附加换新errno
		DirectChangeStatuserrno = ckw.CommonKeyWord().Json_GetJsonValue(DirectChangeStatus,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DirectChangeStatuserrno:",DirectChangeStatuserrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DirectChangeStatuserrno:",DirectChangeStatuserrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DirectChangeStatuserrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")