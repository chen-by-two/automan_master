# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_moduleCompensate:

	@allure.feature("连接智赔数据库")
	@allure.severity("blocker")
	def test_fql_moduleCompensate_connect(self):
		# 定义全局变量moduleCompensateDB
		global moduleCompensateDB
		# 全局变量赋值
		moduleCompensateDB = ckw.CommonKeyWord().Db_SshConfRCMysqlConnect("DATABASE_RC_cn_uniondrug_module_compensate")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("数据库连接成功返回：",moduleCompensateDB)

	@allure.feature("ai智赔-权益项目列表信息")
	@allure.severity("blocker")
	def test_fql_compensate_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		#yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/xuezhengwei/PycharmProjects/automan/TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 请求权益中心的项目列表信息
		projectList = bkw.compensateApi_projectList({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{},"env":envt},"dict")
		# 获取权益项目数量
		projectCount= ckw.CommonKeyWord().Json_GetJsonValues(projectList,[["data","paging","totalItems"]])
		# 获取接口状态代码
		projectListCode = ckw.CommonKeyWord().Dict_GetByKey(projectList,"errno")
		# 断言接口返回的状态码
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(projectListCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("权益项目数量：",projectCount)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("权益项目数量：",projectCount)

	@allure.feature("ai智赔-项目的分组统计")
	@allure.severity("blocker")
	def test_fql_compensate_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		#yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/xuezhengwei/PycharmProjects/automan/TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 请求权益中心的项目列表信息
		groupSum= bkw.compensateApi_groupSum({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"groupIds": [ "3960"]},"env":envt},"dict")
		# 获取接口状态代码
		projectListCode = ckw.CommonKeyWord().Dict_GetByKey(groupSum,"errno")
		# 断言接口返回的状态码
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(projectListCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("项目的分组统计：",groupSum)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("项目的分组统计：",groupSum)

	@allure.feature("ai智赔-订单中是否含已激活的保障")
	@allure.severity("blocker")
	def test_fql_compensate_0003(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/xuezhengwei/PycharmProjects/automan/TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "statusCode")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 请求该订单是否含保障且保障是否已激活信息
		guaranteesActive = bkw.compensateApi_guaranteesActive({"header":{"Content-Type":"application/json;charsetUTF-8"},"parma":{},"data":{"guaranteeId":"","orderNo":"92080101603753652181"},"env":envt},"dict")
		# 获取接口状态代码
		guaranteesActiveCode = ckw.CommonKeyWord().Dict_GetByKey(guaranteesActive,"errno")
		# 获取接口返回的message
		guaranteesMessage = ckw.CommonKeyWord().Json_GetJsonValue(guaranteesActive,[["data","message"]])
		# 断言接口返回的状态码
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode, int(guaranteesActiveCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("接口返回的message：",guaranteesMessage)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("接口返回的message：",guaranteesMessage)


	@allure.feature("关闭智赔数据库")
	@allure.severity("blocker")
	def test_fql_compensate_close(self):
		# 关闭公共数据数据库
		ckw.CommonKeyWord().Db_SshConfRCMysqlClose(moduleCompensateDB)
