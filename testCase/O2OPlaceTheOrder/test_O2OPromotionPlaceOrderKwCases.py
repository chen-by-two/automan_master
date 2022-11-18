# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_O2OPromotionPlaceOrder:

	@allure.feature("O2O-获取用户token")
	@allure.severity("blocker")
	def test_O2O_PromotionPlaceOrder_001(self):
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
	def test_O2O_PromotionPlaceOrder_002(self):
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
  "scene": "1",
  "isPreTime": "",
  "sourceTradeCode": "f91b0c7d48029b237647e5808c2a0a09",
  "showName": "奥泰灵 盐酸氨基葡萄糖胶囊",
  "shops": [{
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
   "drugName": "盐酸氨基葡萄糖胶囊",
   "commonName": "盐酸氨基葡萄糖胶囊",
   "brand": "奥泰灵",
   "price": "58.00",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181242284.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181241870.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181237567.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181236679.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615184732988.jpg"],
   "manufacturer": "澳美制药厂",
   "approvalNumber": "HC20160008",
   "description": "治疗和预防全身各种关节的骨性关节炎，包括膝关节、肩关节、髋关节、手腕关节、颈及脊椎关节和踝关节等，可缓解和消除骨性关节炎的疼痛、肿胀等症状，改善关节活动功能。",
   "isPrescription": False,
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
   "goodsInternalId": "59522",
   "realTradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
   "realCommonName": "盐酸氨基葡萄糖胶囊",
   "form": "0.24克*36粒",
   "pack": "盒",
   "sales": "11.0",
   "channel": "2",
   "distance": "0.02445000178892996",
   "scene": "1",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": False,
   "attrs": ["0", "1", "31073", "30002", "2", "31027", "5", "31080", "31082", "31227"],
   "cates": ["0", "2", "44051", "44047"]
  }, {
   "isColdChain": "0",
   "isDtp": "0",
   "tradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
   "drugName": "盐酸氨基葡萄糖胶囊",
   "commonName": "盐酸氨基葡萄糖胶囊",
   "brand": "奥泰灵",
   "price": "58.00",
   "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181242284.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181241870.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181237567.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181236679.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615184732988.jpg"],
   "manufacturer": "澳美制药厂",
   "approvalNumber": "HC20160008",
   "description": "治疗和预防全身各种关节的骨性关节炎，包括膝关节、肩关节、髋关节、手腕关节、颈及脊椎关节和踝关节等，可缓解和消除骨性关节炎的疼痛、肿胀等症状，改善关节活动功能。",
   "isPrescription": False,
   "projectId": "2",
   "merchantId": "590",
   "merchantStatus": "1",
   "merchantIsPrescription": "1",
   "storeId": "3735",
   "shopStatus": "1",
   "storeDomestic": "1",
   "storeRider": "1",
   "expressType": "0",
   "storeOnlySelf": "1",
   "storeDistance": "3.0",
   "storeStartTime": "08:00:00",
   "storeEndTime": "21:30:00",
   "goodsInternalId": "59522",
   "realTradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
   "realCommonName": "盐酸氨基葡萄糖胶囊",
   "form": "0.24克*36粒",
   "pack": "盒",
   "sales": "11.0",
   "channel": "2",
   "distance": "0.7359302167655565",
   "scene": "1",
   "goodsSignType": "",
   "goodsSubType": "11",
   "goodsType": "1",
   "isOffShelf": False,
   "attrs": ["0", "1", "31073", "30002", "2", "31027", "5", "31080", "31082", "31227"],
   "cates": ["0", "2", "44051", "44047"]
  }],
  "isColdChain": "0",
  "isDtp": "0",
  "tradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
  "drugName": "盐酸氨基葡萄糖胶囊",
  "commonName": "盐酸氨基葡萄糖胶囊",
  "brand": "奥泰灵",
  "price": "58.00",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181242284.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181241870.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181237567.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181236679.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615184732988.jpg"],
  "manufacturer": "澳美制药厂",
  "approvalNumber": "HC20160008",
  "description": "治疗和预防全身各种关节的骨性关节炎，包括膝关节、肩关节、髋关节、手腕关节、颈及脊椎关节和踝关节等，可缓解和消除骨性关节炎的疼痛、肿胀等症状，改善关节活动功能。",
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
  "realCommonName": "盐酸氨基葡萄糖胶囊",
  "form": "0.24克*36粒",
  "pack": "盒",
  "sales": "22",
  "channel": "2",
  "distance": "0.02445000178892996",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31073", "30002", "2", "31027", "5", "31080", "31082", "31227"],
  "cates": ["0", "2", "44051", "44047"],
  "quantity": 1
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
	def test_O2O_PromotionPlaceOrder_003(self):
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
  "tradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
  "drugName": "盐酸氨基葡萄糖胶囊",
  "commonName": "盐酸氨基葡萄糖胶囊",
  "brand": "奥泰灵",
  "price": "58.00",
  "img": ["https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181242284.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181241870.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181237567.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181236679.jpg", "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615184732988.jpg"],
  "manufacturer": "澳美制药厂",
  "approvalNumber": "HC20160008",
  "description": "治疗和预防全身各种关节的骨性关节炎，包括膝关节、肩关节、髋关节、手腕关节、颈及脊椎关节和踝关节等，可缓解和消除骨性关节炎的疼痛、肿胀等症状，改善关节活动功能。",
  "isPrescription": False,
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
  "goodsInternalId": "59522",
  "realTradeCode": "G1Nu%2BbUrK3vuDDb5auwE9gl6WeYw",
  "realCommonName": "盐酸氨基葡萄糖胶囊",
  "form": "0.24克*36粒",
  "pack": "盒",
  "sales": "11.0",
  "channel": "2",
  "distance": "0.02445000178892996",
  "scene": "1",
  "goodsSignType": "",
  "goodsSubType": "11",
  "goodsType": "1",
  "isOffShelf": False,
  "attrs": ["0", "1", "31073", "30002", "2", "31027", "5", "31080", "31082", "31227"],
  "cates": ["0", "2", "44051", "44047"],
  "stock": "11",
  "goodsId": "59522",
  "internalId": "59522",
  "quantity": "1",
  "leftNums": "0",
  "sourceTradeCode": "f91b0c7d48029b237647e5808c2a0a09",
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
	def test_O2O_PromotionPlaceOrder_004(self):
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
		# 提取商家活动activityId
		activityId = ckw.CommonKeyWord().Json_GetJsonValue(OrderInit,[["data","drugs",0,"activity","activityId"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CreateOrdererrno:",OrderIniterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CreateOrdererrno:",OrderIniterrno)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CreateOrdererrno:",activityId)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CreateOrdererrno:",activityId)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 读取yaml里成功返回断言
		activityIdAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"activityId")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(OrderIniterrno,success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(activityIdAssert,activityId)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-优惠权益资源可用列表")
	@allure.severity("blocker")
	def test_O2O_PromotionPlaceOrder_005(self):
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
  "itemUuid": "a79ad0f6-849f-4bc8-83da-5e82db3d1a66",
  "goodsNo": "",
  "internalId": "59522",
  "internalIdList": "",
  "selectFlag": "1",
  "goodsType": "1",
  "goodsSubType": "11",
  "rxFlag": "0",
  "infusionFlag": "0",
  "unitPrice": "58.00",
  "afterActivityUnitPrice": "46.40",
  "quantity": "1",
  "merchantId": "590",
  "storeId": "4711",
  "belongInfusionMerchantId": "0",
  "belongInfusionStoreId": "0",
  "commonName": "盐酸氨基葡萄糖胶囊",
  "realName": "盐酸氨基葡萄糖胶囊",
  "tradeCode": "4895013208378",
  "image": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181242284.jpg",
  "approvalNumber": "HC20160008",
  "manufacturer": "澳美制药厂",
  "form": "0.24克*36粒",
  "pack": "盒",
  "batchNumber": "",
  "memberPrice": "58.00",
  "originalPrice": "58.00",
  "productId": "0",
  "fromItemInternalId": "",
  "isRule": "0",
  "isDtp": "0",
  "productionDate": "",
  "expireDate": "",
  "buyGifts": "0",
  "isSelectActivity": "1",
  "insuranceCode": "",
  "totalAmount": "58.00",
  "directAmount": "0",
  "activityAmount": "11.6",
  "discountAmount": "0",
  "couponAmount": "0",
  "promoteCouponAmount": "0",
  "averageAmount": "0",
  "activity": {
   "activityId": "20220617100953427267",
   "requestNo": "6ac7917984f9474",
   "activityAmount": "11.6",
   "activityType": "3",
   "activityName": "自动化测试活动-xwy"
  },
  "activityName": "",
  "itemAttr": {
   "id": "0",
   "attrs": "0,1,31073,30002,2,31027,5,31080,31082,31227",
   "cates": "0,2,44051,44047"
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
 "serviceItems": [],
 "eshop": [{
  "expressType": "1",
  "expressTypeSelect": "1",
  "expressAmount": "9",
  "expressDiscount": "9",
  "mitigateRuleString": "运费满20减2元",
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
  "expressTypeSelect": "0",
  "expressAmount": "0",
  "expressDiscount": "0",
  "mitigateRuleString": "",
  "addressId": "103898",
  "receiveName": "张俊超",
  "receiveMobile": "15380905486",
  "wayBillNo": "",
  "address": "渝北区双龙大道92号",
  "storeName": "泰康在线测试专用药店",
  "merchantName": "泰康在线",
  "longitude": "106.627600",
  "latitude": "29.712700",
  "distance": "1187.62km",
  "distanceMi": "1",
  "deliveryMethod": "0",
  "deliverTime": "",
  "deliverDistance": "0",
  "deliveryMethods": []
 }],
 "sign": {
  "needSign": "0",
  "needCard": "0",
  "agreements": [],
  "frontCardImage": "",
  "backendCardImage": "",
  "signImageUrl": "",
  "projectId": "",
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
 "storeName": "泰康在线测试专用药店",
 "drugs": [{
  "itemUuid": "a79ad0f6-849f-4bc8-83da-5e82db3d1a66",
  "goodsNo": "",
  "internalId": "59522",
  "internalIdList": "",
  "selectFlag": "1",
  "goodsType": "1",
  "goodsSubType": "11",
  "rxFlag": "0",
  "infusionFlag": "0",
  "unitPrice": "58.00",
  "afterActivityUnitPrice": "46.40",
  "quantity": "1",
  "merchantId": "590",
  "storeId": "4711",
  "belongInfusionMerchantId": "0",
  "belongInfusionStoreId": "0",
  "commonName": "盐酸氨基葡萄糖胶囊",
  "realName": "盐酸氨基葡萄糖胶囊",
  "tradeCode": "4895013208378",
  "image": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/test/1615181242284.jpg",
  "approvalNumber": "HC20160008",
  "manufacturer": "澳美制药厂",
  "form": "0.24克*36粒",
  "pack": "盒",
  "batchNumber": "",
  "memberPrice": "58.00",
  "originalPrice": "58.00",
  "productId": "0",
  "fromItemInternalId": "",
  "isRule": "0",
  "isDtp": "0",
  "productionDate": "",
  "expireDate": "",
  "buyGifts": "0",
  "isSelectActivity": "1",
  "insuranceCode": "",
  "totalAmount": "58.00",
  "directAmount": "0",
  "activityAmount": "11.6",
  "discountAmount": "0",
  "couponAmount": "0",
  "promoteCouponAmount": "0",
  "averageAmount": "0",
  "activity": {
   "activityId": "20220617100953427267",
   "requestNo": "6ac7917984f9474",
   "activityAmount": "11.6",
   "activityType": "3",
   "activityName": "自动化测试活动-xwy"
  },
  "activityName": "",
  "itemAttr": {
   "id": "0",
   "attrs": "0,1,31073,30002,2,31027,5,31080,31082,31227",
   "cates": "0,2,44051,44047"
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
 "allDiscountAmount": "11.60",
 "saleAmount": "46.40",
 "allDrugDiscountAmount": "11.60",
 "allDrugSaleAmount": "46.40",
 "isHasDtp": "0",
 "services": [],
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
 "businessEndTime": "23:59",
 "storeStatus": "0",
 "storeTimeStatus": "0",
 "storeOpenTime": "0",
 "storeTime": "0",
 "merchantId": "590",
 "storeId": "4711",
 "channel": "2",
 "orderMethod": "3",
 "assistantMemberId": "0",
 "assistantId": "0",
 "cardId": "",
 "outActivityId": "",
 "feeCardId": "",
 "feeAmount": "0.00",
 "equityUuid": "e2652001ba87654185f910d9cc0186bd",
 "equityIds": ["23420789", "23422587"],
 "equityName": "驻店宝-面额卡",
 "coupon": {
  "couponId": "",
  "cardId": "",
  "couponAmount": "0",
  "couponType": "0",
  "schemeId": ""
 },
 "eshopConfig": {
  "isUseEquity": "1",
  "isUsePromoteCoupon": "1",
  "isUseCoupon": "1",
  "isUseActivity": "1",
  "isUseFeeCoupon": "1",
  "isUseOutActivity": "1"
 },
 "isShowUnionMember": "-1",
 "orderNo": "",
 "mainOrderNo": "",
 "remark": "",
 "isNeedIdentify": "0",
 "orderAreaLimit": "0",
 "isLockResource": "0",
 "requestNo": requestNo,
 "isUpdateRemark": "0",
 "isNeedTimelyDistribution": "1"
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
	def test_O2O_PromotionPlaceOrder_006(self):
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
		saleAmountAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"saleAmount")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",saleAmountAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CreateOrdererrno,success_errno)
		# 断言对比字典
		# assert ckw.CommonKeyWord().Assert_ObjAndObj(saleAmountAssert,saleAmount)
		# mainOrderNo写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/O2OPlaceTheOrder/token.yaml","mainOrderNo",mainOrderNo)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-统一支付回调")
	@allure.severity("blocker")
	def test_O2O_PromotionPlaceOrder_007(self):
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
