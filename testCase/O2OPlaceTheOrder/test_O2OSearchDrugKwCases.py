# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_O2OSearchDrug:

	@allure.feature("O2O-获取用户token")
	@allure.severity("blocker")
	def test_O2O_FindToken_001(self):
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

	@allure.feature("O2O-搜索药品-药品名称")
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

	@allure.feature("O2O-搜索药品-药品内码")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_002(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 读取yaml文件获取搜索药品关键词
		searchContent = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"goodsInternalId")
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
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-药品条码")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_003(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 读取yaml文件获取搜索药品关键词
		searchContent = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"goodstradeCode")
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
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# # 读取yaml里药品名称
		# commonNameyaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"commonName")
		# # 打印结果到日志
		# ckw.CommonKeyWord().Print_ToLog("药品名称断言结果：",commonNameyaml)
		# # 断言对比字典
		# assert ckw.CommonKeyWord().Assert_ObjAndObj(commonName,commonNameyaml)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-药品病症接触性皮炎")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_004(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 读取yaml文件获取搜索药品关键词
		searchContent = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"symptoms1")
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
		# # 提取药品名称
		# commonName = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["data","body",0,"items",0,"shops",0,"commonName"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# # 打印药品名称到控制台
		# ckw.CommonKeyWord().Print_ToControl("commonName:",commonName)
		# # 打印药品名称到日志
		# ckw.CommonKeyWord().Print_ToLog("commonName:",commonName)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-dtp搜索-综合排序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_005(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugSearchDtpDrugs({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
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
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-dtp搜索-销量升序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_006(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugSearchDtpDrugs({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 1,
 "sessionId": "0789897e31e6c787c62614592d734737",
 "title": "销量",
 "up": True,
 "sortField": 2,
 "sortType": 1,
 "addHistory": "0",
 "isAccurate": "0",
 "location": "106.627393,29.712571"
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-dtp搜索-销量降序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_007(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugSearchDtpDrugs({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 1,
 "sessionId": "0789897e31e6c787c62614592d734737",
 "title": "销量",
 "up": True,
 "sortField": 2,
 "sortType": 2,
 "addHistory": "0",
 "isAccurate": "0",
 "location": "106.627393,29.712571"
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-dtp搜索-价格升序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_008(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugSearchDtpDrugs({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 1,
 "sessionId": "0789897e31e6c787c62614592d734737",
 "title": "价格",
 "up": True,
 "sortField": 1,
 "sortType": 1,
 "addHistory": "0",
 "isAccurate": "0",
 "location": "106.627393,29.712571"
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-dtp搜索-价格降序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_009(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugSearchDtpDrugs({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 1,
 "sessionId": "0789897e31e6c787c62614592d734737",
 "title": "价格",
 "up": True,
 "sortField": 1,
 "sortType": 2,
 "addHistory": "0",
 "isAccurate": "0",
 "location": "106.627393,29.712571"
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-分类搜索-综合排序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_010(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugCategory({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
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
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-分类搜索-销量升序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_011(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugCategory({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 0,
 "sessionId": "eb26d27565aa54954a71aa62c87b5c52",
 "title": "销量",
 "up": True,
 "sortField": 2,
 "sortType": 1,
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
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-分类搜索-销量降序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_012(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugCategory({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 0,
 "sessionId": "eb26d27565aa54954a71aa62c87b5c52",
 "title": "销量",
 "up": True,
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
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-分类搜索-价格升序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_013(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugCategory({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 0,
 "sessionId": "eb26d27565aa54954a71aa62c87b5c52",
 "title": "价格",
 "up": True,
 "sortField": 1,
 "sortType": 1,
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
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("O2O-搜索药品-分类搜索-价格降序")
	@allure.severity("blocker")
	def test_O2O_SearchDrug_014(self):
		# 读取yaml文件
		yamlFiletoken = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/token.yaml")
		# 读取yaml文件
		yamlFileinfo = ckw.CommonKeyWord().Yaml_Read("./TestFile/O2OPlaceTheOrder/O2OInfo.yaml")
		# 读取yaml文件查询微信token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFiletoken,"token")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"env")
		# 搜索药品-调取接口
		DrugSearch = bkw.O2OPlaceTheOrderApi_ApiDrugCategory({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": 1,
 "searchSource": 0,
 "sessionId": "eb26d27565aa54954a71aa62c87b5c52",
 "title": "价格",
 "up": True,
 "sortField": 1,
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
},"env":env},"dict")
		# 提取搜索药品errno
		DrugSearcherrno = ckw.CommonKeyWord().Json_GetJsonValue(DrugSearch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("DrugSearcherrno:",DrugSearcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("DrugSearcherrno:",DrugSearcherrno)
		# 读取yaml里成功返回断言
		success_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFileinfo,"success_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("成功返回断言结果：",success_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(DrugSearcherrno,success_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")
