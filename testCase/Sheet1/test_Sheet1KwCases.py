# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_Sheet1:

	@allure.feature("门店任务-申请线上拜访-已合作/连锁")
	@allure.severity("blocker")
	def test_zjc_ApprovalAdd_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml文件
		yamlFile1 = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取Yaml-token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"token")
		# 读取Yaml-userid
		userid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"userid")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 已合作连锁列表-调取接口
		MerchantAllList = bkw.assistantappApi_MerchantAllList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "userId":userid,
 "page": 1,
 "limit": 10,
 "businessTypeArr": [1, 4],
 "common_name": ""
},"env":env},"dict")
		# 提取已合作连锁列表返回
		MerchantAllListerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantAllList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantAllListerrno:",MerchantAllListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantAllListerrno:",MerchantAllListerrno)
		# 读取yaml已合作连锁列表断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("已合作连锁列表断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantAllListerrno,Errno)

	@allure.feature("门店任务-读取添加新连锁statussql")
	@allure.severity("blocker")
	def test_zjc_ApprovalAdd_003(self):
		# 读取yaml查询客户信息namesql
		GetCustomerInfosql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetCustomerInfo")
		# 读取yaml添加新连锁断言
		CustomerNameAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerNameAssert")
		# 读取yaml删除添加的连锁
		DeleteCustomersql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DeleteCustomersql")
		# mysql执行任意sql-查询客户信息name
		GetCustomerInfo = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_uniondrug_data_service",GetCustomerInfosql)
		# 从数据库提取客户信息name
		GetCustomerName = ckw.CommonKeyWord().Json_GetJsonValue(GetCustomerInfo[0],[["customerName"]])
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(GetCustomerName,CustomerNameAssert)
		# mysql执行任意sql-删除添加的连锁sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",DeleteCustomersql)
