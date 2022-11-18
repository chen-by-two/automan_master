# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_O2OAddSignNameCard:

	@allure.feature("O2O-清除实名认证-登录运营中心后台")
	@allure.severity("blocker")
	def test_O2O_DeleteNameCard_001(self):
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
		# 清除实名认证-调取接口
		UserCardDelete = bkw.O2OPlaceTheOrderApi_MngUserCardDelete({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "memberId": memberId,
    "typeId": 1
},"env":env},"dict")
		# 提取清除实名认证errno
		UserCardDeleteerrno = ckw.CommonKeyWord().Json_GetJsonValue(UserCardDelete,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("UserCardDeleteerrno:",UserCardDeleteerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("UserCardDeleteerrno:",UserCardDeleteerrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"successno")
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(UserCardDeleteerrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-清除用户签名")
	@allure.severity("blocker")
	def test_O2O_DeleteSign_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件清除用户签名的aql
		delete_sign = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"delete_sign")
		# mysql执行任意sql-清除用户签名
		delete_sign = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_middleend_usercenter",delete_sign)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",delete_sign)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",delete_sign)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-获取用户token")
	@allure.severity("blocker")
	def test_O2O_FindToken_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件获取微信token的aql
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

	@allure.feature("O2O-搜索药品")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_001(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 读取yaml文件获取搜索药品关键词
		searchContent = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"searchContent")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugSearch({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 0,
 "sessionId": "67fe3fd0b29adfc0733f29008485873d",
 "title": "综合排序",
 "sortField": 0,
 "sortType": 0,
 "searchContent": searchContent,
 "addHistory": "1",
 "isAccurate": "0",
 "location": "118.779236,31.971867",
 "storeId": "",
 "specializeSearch": "",
 "supplyEshop": "1",
 "isGather": "1",
 "showDrugName": "0",
 "nearbyStores": ""
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 提取药品名称
		commonName = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["data","body",0,"items",0,"shops",0,"commonName"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 打印药品名称到控制台
		ckw.CommonKeyWord().Print_ToControl("commonName:",commonName)
		# 打印药品名称到日志
		ckw.CommonKeyWord().Print_ToLog("commonName:",commonName)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 读取yaml里药品名称
		commonNameyaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"commonName")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("药品名称断言结果：",commonNameyaml)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(commonName,commonNameyaml)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-加入购物车")
	@allure.severity("blocker")
	def test_O2O_AddCart_001(self):
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
   "isPrescription": True,
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

	@allure.feature("O2O-添加实名认证信息")
	@allure.severity("blocker")
	def test_O2O_EditNameCard_001(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 添加实名认证信息-调取接口
		Editnamecard = bkw.O2OPlaceTheOrderApi_VMemberEditnamecard({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token},"parma":{},"data":{
 "name": "张俊超",
 "cardNum": "412829199304015574"
},"env":env},"dict")
		# 添加实名认证信息errno
		Editnamecarderrno = ckw.CommonKeyWord().Json_GetJsonValue(Editnamecard,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Editnamecarderrno:",Editnamecarderrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Editnamecarderrno:",Editnamecarderrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(Editnamecarderrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-生成预订单")
	@allure.severity("blocker")
	def test_O2O_CreatePreviewOrder_001(self):
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

	@allure.feature("O2O-上传处方单")
	@allure.severity("blocker")
	def test_O2O_ApplyRx_001(self):
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
		# 上传处方单-调取接口
		RxApplyRx = bkw.O2OPlaceTheOrderApi_RxApplyRx({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "prescriptionPhoto": ["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/tn3jjs53cfo173jbdgarpf0rp9.png"],
 "offLineApply": {
  "userName": "张俊超",
  "userMobile": "15380905486",
  "prescriptionPhoto": ["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/tn3jjs53cfo173jbdgarpf0rp9.png"]
 },
 "type": 2,
 "requestNo":requestNo ,
 "orderNo": "",
 "drugUserId": "103"
},"env":env},"dict")
		# 提取上传处方单errno
		RxApplyRxerrno = ckw.CommonKeyWord().Json_GetJsonValue(RxApplyRx,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("RxApplyRxerrno:",RxApplyRxerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("RxApplyRxerrno:",RxApplyRxerrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(RxApplyRxerrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-添加签名")
	@allure.severity("blocker")
	def test_O2O_AddSign_001(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 添加签名-调取接口
		AddSign = bkw.O2OPlaceTheOrderApi_UnifyorderConfirmUserRuleAddSign({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "signUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/s8o9228apq960bt17vrmqvejvj.png"
},"env":env},"dict")
		# 提取添加签名errno
		AddSignerrno = ckw.CommonKeyWord().Json_GetJsonValue(AddSign,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AddSignerrno:",AddSignerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AddSignerrno:",AddSignerrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"successno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AddSignerrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

# 	@allure.feature("O2O-上传实名认证照片")
# 	@allure.severity("blocker")
# 	def test_O2O_updateUserInfo_001(self):
# 		# 读取yaml文件
# 		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
# 		# 读取yaml文件
# 		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
# 		# 读取yaml文件查询微信token
# 		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
# 		# 读取Yaml执行环节
# 		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
# 		# 上传实名认证照片-调取接口
# 		UpdateUserInfo = bkw.O2OPlaceTheOrderApi_MemberUpdateUserInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token},"parma":{},"data":{
#  "cardName": "张俊超",
#  "idcardProcess": "1",
#  "idCard": "412829199304015574",
#  "imageFrontUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/pgvbl65cci3oj5ragjkago0o3g.jpeg",
#  "imageBackUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/7knsjhfs1ksk7s70chab5k86pp.jpeg",
#  "gmtExpiryStart": "20200519",
#  "gmtExpiryEnd": "20400519",
#  "address": "南京市玄武区银城东苑73号302室",
#  "authWayTag": ""
# },"env":env},"dict")
# 		# 提取上传实名认证照片errno
# 		UpdateUserInfoerrno = ckw.CommonKeyWord().Json_GetJsonValue(UpdateUserInfo,[["errno"]])
# 		# 打印结果到控制台
# 		ckw.CommonKeyWord().Print_ToControl("UpdateUserInfoerrno:",UpdateUserInfoerrno)
# 		# 打印结果到日志
# 		ckw.CommonKeyWord().Print_ToLog("UpdateUserInfoerrno:",UpdateUserInfoerrno)
# 		# 读取yaml里成功返回断言
# 		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
# 		# 打印结果到日志
# 		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
# 		# 断言对比字典
# 		assert ckw.CommonKeyWord().Assert_ObjAndObj(UpdateUserInfoerrno,success_errno)
# 		# 强制等待
# 		ckw.CommonKeyWord().Time_Sleep("1.0")

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
