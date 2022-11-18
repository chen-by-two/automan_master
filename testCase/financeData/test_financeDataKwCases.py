# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_financeData:

	@allure.feature("连接公共数据数据库")
	@allure.severity("blocker")
	def test_fql_financedata_connect(self):
		# 定义全局变量financeDataDB
		global financeDataDB
		# 全局变量赋值
		financeDataDB = ckw.CommonKeyWord().Db_SshConfRCMysqlConnect("DATABASE_RC_cn_uds_fin_com")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("数据库连接成功返回：",financeDataDB)

	@allure.feature("财务基础数据-商户明细")
	@allure.severity("blocker")
	def test_fql_financedata_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的组织ID
		organizationId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"organizationId")
		# 读取yaml文件中的状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 根据组织ID查询商户详情
		partnerDetail = bkw.financeDataApi_partnerDetail({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "organizationId":organizationId },"env":envt},"dict")
		# 获取商户详情中的merchantExtend
		merchantExtend = ckw.CommonKeyWord().Dict_GetByKey(partnerDetail,"data")
		# 获取接口状态代码
		merchantExtendStatusCode = ckw.CommonKeyWord().Dict_GetByKey(partnerDetail,"errno")
		# 断言接口返回的状态码
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(merchantExtendStatusCode))
		# 获取merchantExtend中的组织ID
		organId = ckw.CommonKeyWord().Dict_GetByKey(merchantExtend,"organizationId")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("入参：",organizationId,"出参：",organId)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("入参：",organizationId,"出参：",organId)
		# 断言对比结果
		assert ckw.CommonKeyWord().Assert_ObjAndObj(int(organId),organizationId)

	@allure.feature("财务基础数据-商户组织信息")
	@allure.severity("blocker")
	def test_fql_financedata_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的组织ID
		organizationId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"organizationId")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 根据组织ID查询商户详情
		merchantInfo = bkw.financeDataApi_merchantInfo({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "organizationId":organizationId },"env":envt},"dict")
		# 获取商户详情中的merchantExtend
		merchantExtend = ckw.CommonKeyWord().Dict_GetByKey(merchantInfo,"data")
		# 获取merchantExtend中的组织ID
		organId = ckw.CommonKeyWord().Dict_GetByKey(merchantExtend,"organizationId")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("入参：",organizationId,"出参：",organId)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("入参：",organizationId,"出参：",organId)
		# 断言对比结果
		assert ckw.CommonKeyWord().Assert_ObjAndObj(int(organId),organizationId)

	@allure.feature("财务基础数据-核算单位票据信息")
	@allure.severity("blocker")
	def test_fql_financedata_0003(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的核算单位ID
		unitId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"unitId")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中查询核算单位的票据信息SQL
		selectBillInfo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectBillInfo")
		# 根据核算单位ID查询核算单位信息
		billInfo = bkw.financeDataApi_partnerBillInfo({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "unitId": unitId },"env":envt},"dict")
		# 提取纳税人识别号
		taxpayerIdNumber = ckw.CommonKeyWord().Json_GetJsonValue(billInfo,[["data","taxpayerIdNumber"]])
		# 执行SQL获取纳税人识别号
		sqlTaxpayerIdNumber = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectBillInfo)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("域名：",envt,"入参：",unitId,"[接口]纳税人识别号：",taxpayerIdNumber,"[SQL]纳税人识别号：",sqlTaxpayerIdNumber)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("域名：",envt,"入参：",unitId,"[接口]纳税人识别号：",taxpayerIdNumber,"[SQL]纳税人识别号：",sqlTaxpayerIdNumber)
		# 断言对比纳税人识别号
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlTaxpayerIdNumber,taxpayerIdNumber)

	@allure.feature("财务基础数据-核算单位结算配置")
	@allure.severity("blocker")
	def test_fql_financedata_0004(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的核算单位ID
		organizationId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"organizationId")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中查询核算单位的连锁配置的SQL
		selectMerchantSettings = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectMerchantSettings")
		# 根据核算单位ID查询核算单位信息
		partnerSetting = bkw.financeDataApi_partnerSetting({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "organizationId": organizationId },"env":envt},"dict")
		# 提取开票范围invoiceRules
		invoiceRules = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","invoiceRules"]])
		# 提取计划付款天数planPayDays
		planPayDays = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","planPayDays"]])
		# 提取投保方式insureType
		insureType = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","insureType"]])
		# 提取是否开启直赔directClaim
		directClaim = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","directClaim"]])
		# 提取发票理赔状态invoiceClaimStatus
		invoiceClaimStatus = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","invoiceClaimStatus"]])
		# 提取报案理赔状态reportClaimStatus
		reportClaimStatus = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","reportClaimStatus"]])
		# 提取付款单生成节点paymentNode
		paymentNode = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","paymentNode"]])
		# 提取换新结算单自动结算配置autoCreateHx
		autoCreateHx = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","autoCreateHx"]])
		# 提取换新开票单自动生成配置autoCreateHxBill
		autoCreateHxBill = ckw.CommonKeyWord().Json_GetJsonValue(partnerSetting,[["data","autoCreateHxBill"]])
		# 执行SQL获取商户结算配置信息
		sqlPartnerSetting = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectMerchantSettings)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("域名：",envt,"[接口]连锁配置信息",partnerSetting,"[SQL]连锁配置信息",sqlPartnerSetting)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("域名：",envt,"[接口]连锁配置信息",partnerSetting,"[SQL]连锁配置信息",sqlPartnerSetting)
		# sql提取开票范围invoiceRules
		sqlInvoiceRules = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"invoiceRules")
		# sql提取计划付款天数planPayDays
		sqlPlanPayDays = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"planPayDays")
		# sql提取投保方式insureType
		sqlInsureType = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"insureType")
		# sql提取是否开启直赔directClaim
		sqlDirectClaim = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"directClaim")
		# sql提取发票理赔状态invoiceClaimStatus
		sqlInvoiceClaimStatus = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"invoiceClaimStatus")
		# sql提取报案理赔状态reportClaimStatus
		sqlReportClaimStatus = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"reportClaimStatus")
		# sql提取付款单生成节点paymentNode
		sqlPaymentNode = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"paymentNode")
		# sql提取换新结算单自动结算配置autoCreateHx
		sqlAutoCreateHx = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"autoCreateHx")
		# sql提取换新开票单自动生成配置autoCreateHxBill
		sqlAutoCreateHxBill = ckw.CommonKeyWord().Dict_GetByKey(sqlPartnerSetting[0],"autoCreateHxBill")
		# 断言对比开票范围invoiceRules
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlInvoiceRules,invoiceRules)
		# 断言对比计划付款天数planPayDays
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlPlanPayDays,planPayDays)
		# 断言对比投保方式insureType
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlInsureType,int(insureType))
		# 断言对比是否开启直赔directClaim
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlDirectClaim,int(directClaim))
		# 断言对比发票理赔状态invoiceClaimStatus
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlInvoiceClaimStatus,int(invoiceClaimStatus))
		# 断言对比报案理赔状态reportClaimStatus
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlReportClaimStatus,int(reportClaimStatus))
		# 断言对比付款单生成节点paymentNode
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlPaymentNode,int(paymentNode))
		# 断言对比换新结算单自动结算配置autoCreateHx
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlAutoCreateHx,int(autoCreateHx))
		# 断言对比换新开票单自动生成配置autoCreateHxBill
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlAutoCreateHxBill,int(autoCreateHxBill))

	@allure.feature("财务基础数据-vip申请在线开票明细")
	@allure.severity("blocker")
	def test_fql_financedata_0005(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的核算单位ID
		organizationId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"onlineInvoiceUnitId")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中查询核算单位的连锁配置的SQL
		selectApplyVip = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectApplyVip")
		# 根据核算单位ID查询核算单位信息
		vipDetail = bkw.financeDataApi_vipDetail({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "unitId": organizationId },"env":envt},"dict")
		# 断言接口返回状态
		assert ckw.CommonKeyWord().Assert_BcharInAchar("0.0",vipDetail["errno"])
		# 提取核算单位名称unitName
		unitName = ckw.CommonKeyWord().Json_GetJsonValue(vipDetail,[["data","unitName"]])
		# 提取在线开票状态status
		status = ckw.CommonKeyWord().Json_GetJsonValue(vipDetail,[["data","status"]])
		# 执行SQL获取核算单位在线开票信息
		sqlVipDetail = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectApplyVip)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("域名：",envt,"[接口]核算单位在线开票",vipDetail,"[SQL]核算单位在线开票",sqlVipDetail)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("域名：",envt,"[接口]核算单位在线开票",vipDetail,"[SQL]核算单位在线开票",sqlVipDetail)
		# sql提取开票范围invoiceRules
		sqlUnitName = ckw.CommonKeyWord().Dict_GetByKey(sqlVipDetail[0],"unitName")
		# sql提取计划付款天数planPayDays
		sqlStatus = ckw.CommonKeyWord().Dict_GetByKey(sqlVipDetail[0],"status")
		# sql提取投保方式insureType
		sqlOnlineInvoice = ckw.CommonKeyWord().Dict_GetByKey(sqlVipDetail[0],"onlineInvoice")
		# 断言对比核算单位名称
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlUnitName,unitName)
		# 断言对比在线开票状态
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlStatus,status)
		# 断言对比票据信息中的在线开票状态与applyVip的状态
		assert ckw.CommonKeyWord().Assert_ObjAndObj(sqlOnlineInvoice,sqlStatus)

	@allure.feature("财务基础数据-连锁待办事项")
	@allure.severity("blocker")
	def test_fql_financedata_0006(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的核算单位ID
		unitId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"todoUnitId")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中查询核算单位的连锁配置的SQL
		selectPartnerTodoList = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectPartnerTodoList")
		# 根据核算单位ID查询连锁的待办事项列表
		partnerTodoList = bkw.financeDataApi_partnerTodoList({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "unitId": unitId },"env":envt},"dict")
		# 断言接口返回状态
		assert ckw.CommonKeyWord().Assert_BcharInAchar("0.0",partnerTodoList["errno"])
		# 提取连锁的待办事项列表
		partnerTodoList_body = ckw.CommonKeyWord().Json_GetJsonValues(partnerTodoList,[["data","body"]])
		# 提取连锁的待办事项总数
		partnerTodoList_num = ckw.CommonKeyWord().Json_GetJsonValues(partnerTodoList,[["data","paging","totalItems"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("提取待办事项：",len(partnerTodoList_body),"待办事项总数：",partnerTodoList_num)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("提取待办事项：",len(partnerTodoList_body),"待办事项总数：",partnerTodoList_num)

	@allure.feature("财务基础数据-保司信息")
	@allure.severity("blocker")
	def test_fql_financedata_0007(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的组织ID
		organizationId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"insurerId")
		# 读取yaml文件中查询保司信息配置的SQL
		selectInsurerInfo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectInsurerById")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 根据组织ID查询保司详情
		InsurerDetail = bkw.financeDataApi_insurerInfo({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "organizationId":organizationId },"env":envt},"dict")
		# 获取保司详情中的保司主表信息
		insurerInfo = ckw.CommonKeyWord().Dict_GetByKey(InsurerDetail,"data")
		# 执行SQL获取保司的主信息
		sqlInsureInfo = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectInsurerInfo)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("[接口]保司信息",insurerInfo,"[SQL]保司信息",sqlInsureInfo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("[接口]保司信息",insurerInfo,"[SQL]保司信息",sqlInsureInfo)
		# 断言对比保司ID是否一致
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlInsureInfo,insurerInfo["organizationId"])
		# 断言对比保司名称是否一致
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlInsureInfo,insurerInfo["name"])
		# 断言对比商户类型是否一致
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlInsureInfo,insurerInfo["businessType"])

	@allure.feature("商家服务平台版本信息")
	@allure.severity("blocker")
	def test_fql_financedata_0008(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 读取yaml文件中查询最新版本信息的SQL
		selectVersionControl = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectVersionControl")
		# 接口请求获取最新版本信息
		versionControl = bkw.financeDataApi_versionControl({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{},"env":envt},"dict")
		# 读取yaml文件中查询最新版本信息的SQL
		selectVersionControl = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectVersionControl")
		# 获取接口状态代码
		VersionControlStatusCode = ckw.CommonKeyWord().Dict_GetByKey(versionControl,"errno")
		# 断言接口的状态码为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(VersionControlStatusCode))
		# SQL执行获取最新版本信息
		sqlVersionControl = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectVersionControl)
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("[接口]最新版本信息",versionControl,"[SQL]最新版本信息",sqlVersionControl)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("[接口]最新版本信息",versionControl,"[SQL]最新版本信息",sqlVersionControl)

	@allure.feature("核算单位的基础信息和票据信息")
	@allure.severity("blocker")
	def test_fql_financedata_0009(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中的核算单位ID
		unitId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"unitId")
		# 读取yaml文件中状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 接口请求获取核算单位的基础信息和票据信息
		unitBillInfo = bkw.financeDataApi_unitBillInfo({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "unitId": unitId },"env":envt},"dict")
		# 获取接口状态代码
		unitBillInfoStatusCode = ckw.CommonKeyWord().Dict_GetByKey(unitBillInfo,"errno")
		# 断言接口的状态码为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(unitBillInfoStatusCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("[接口]核算单位的基础信息和票据信息",unitBillInfo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("[接口]核算单位的基础信息和票据信息",unitBillInfo)

	@allure.feature("核算单位和商业公司关系")
	@allure.severity("blocker")
	def test_fql_financedata_0010(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中的核算单位ID
		unitId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"unitId")
		# 读取yaml文件中状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 接口请求获取核算单位和商业公司关系
		unitRelationship = bkw.financeDataApi_unitRelationship({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "organizationId": unitId },"env":envt},"dict")
		# 获取接口状态代码
		unitRelationshipStatusCode = ckw.CommonKeyWord().Yaml_GetByKey(unitRelationship,"errno")
		# 断言接口的状态码为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(unitRelationshipStatusCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("[接口]核算单位和商业公司关系",unitRelationship)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("[接口]核算单位和商业公司关系",unitRelationship)

	@allure.feature("商户下某用户明细（连锁）")
	@allure.severity("blocker")
	def test_fql_financedata_0011(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中的核算单位ID
		unitId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"unitId")
		# 读取yaml文件中状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 读取yaml文件中用户memberId
		rcMemberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"rcMemberId")
		# 接口请求获取用户在连锁下的信息
		workerExistTypeDict = bkw.financeDataApi_workerExist({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "unitId": unitId , "memberId":rcMemberId,"type":"1"},"env":envt},"dict")
		# 获取接口状态代码
		workerExistTypeStatusCode = ckw.CommonKeyWord().Yaml_GetByKey(workerExistTypeDict,"errno")
		# 获取接口中返回的worker信息
		workerExistWorker = ckw.CommonKeyWord().Json_GetJsonValue(workerExistTypeDict,[["data","worker"]])
		# 断言接口的状态码为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(workerExistTypeStatusCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("[接口]连锁用户明细",workerExistWorker)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("[接口]连锁用户明细",workerExistWorker)

	@allure.feature("核算单位的换新服务协议")
	@allure.severity("blocker")
	def test_fql_financedata_0012(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中的核算单位ID
		unitId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"unitId")
		# 读取yaml文件中的查询有效的换新协议的SQL
		selectRenewalCount = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectRenewalCount")
		# 读取yaml文件中状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 接口请求获取用户在连锁下的信息
		partnerRenewalDict = bkw.financeDataApi_partnerRenewal({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{  "organizationId": unitId },"env":envt},"dict")
		# SQL执行获取核算单位有效的换新协议
		sqlRenewalCount = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectRenewalCount)
		# 获取接口状态代码
		partnerRenewalStatusCode = ckw.CommonKeyWord().Yaml_GetByKey(partnerRenewalDict,"errno")
		# 获取body消息体
		partnerRenewalStatusBody = ckw.CommonKeyWord().Json_GetJsonValue(partnerRenewalDict,[["data","body"]])
		# 断言接口的状态码为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(partnerRenewalStatusCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("[接口]核算单位的换新服务协议",partnerRenewalStatusBody)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("[接口]核算单位的换新服务协议",partnerRenewalStatusBody)
		# 断言：接口返回与SQL查询是否一致
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlRenewalCount,len(partnerRenewalStatusBody))

	@allure.feature("商品的税收分类编码信息")
	@allure.severity("blocker")
	def test_fql_financedata_0013(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件中的环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件中的商品名称
		productName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"productName")
		# 读取yaml文件中的批准文号
		approvalNumber = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"approvalNumber")
		# 读取yaml文件中的查询商品税收分类编码信息的SQL
		selectTaxClassificationbyApproveNumber = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectTaxClassificationbyApproveNumber")
		# 读取yaml文件中状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 接口请求获取商品税收分类编码信息
		taxClassificationDict = bkw.financeDataApi_taxClassification({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"productName":productName,"approvalNumber":approvalNumber,"skuNo":""},"env":envt},"dict")
		# SQL执行获取商品税收分类编码信息
		sqlTaxClassificationbyApproveNumber = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectTaxClassificationbyApproveNumber)
		# 获取接口状态代码
		taxClassificationCode = ckw.CommonKeyWord().Yaml_GetByKey(taxClassificationDict,"errno")
		# 获取body消息体
		taxClassificationData = ckw.CommonKeyWord().Yaml_GetByKey(taxClassificationDict,"data")
		# 断言接口的状态码为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(taxClassificationCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("【接口】商品税收分类编码信息",taxClassificationData,"【SQL】商品税收分类编码信息",sqlTaxClassificationbyApproveNumber)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("【接口】商品税收分类编码信息",taxClassificationData,"【SQL】商品税收分类编码信息",sqlTaxClassificationbyApproveNumber)

	@allure.feature("用户管理-查询用户信息")
	@allure.severity("blocker")
	def test_fql_financedata_0014(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件：环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml文件：用户memberId
		memberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"rcMemberId")
		# 读取yaml文件：不存在的memberId
		notExistMemberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"notExistMemberId")
		# 读取yaml文件：用户信息SQL
		selectWorkerByMemberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectWorkerByMemberId")
		# 读取yaml文件：药联公司信息SQL
		selectCompany = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectCompany")
		# 读取yaml文件：用户角色SQL
		selectWorkerManByMemberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectWorkerManByMemberId")
		# 读取yaml文件：状态码
		statusCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"statusCode")
		# 接口请求用户信息（用户不存在）
		companyNoWorkerDitc = bkw.financeDataApi_companyWorker({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"memberId":notExistMemberId ,"type": 4},"env":envt},"dict")
		# 接口请求用户信息
		companyWorkerDict = bkw.financeDataApi_companyWorker({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"memberId": memberId,"type": 4},"env":envt},"dict")
		# 执行SQL：获取用户信息
		sqlWorker = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectWorkerByMemberId)
		# 执行SQL：获取药联公司信息
		sqlCompany = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectCompany)
		# 执行SQL：获取用户角色信息
		sqlWorkerMan = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectWorkerManByMemberId)
		# 用户不存在body消息体中的errno
		companyNoWorkerCode = ckw.CommonKeyWord().Yaml_GetByKey(companyNoWorkerDitc,"errno")
		# 用户存在body消息体中的errno
		companyWorkerCode = ckw.CommonKeyWord().Yaml_GetByKey(companyWorkerDict,"errno")
		# 用户存在body消息体
		companyWorkerBody = ckw.CommonKeyWord().Json_GetJsonValue(companyWorkerDict,[["data","body"]])
		# 断言接口状态码：用户不存在为0
		assert ckw.CommonKeyWord().Assert_ObjAndObj(statusCode,int(companyNoWorkerCode))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("【接口】用户信息",companyWorkerBody)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("【接口】用户信息",companyWorkerBody)

	@allure.feature("查询字典项详情")
	@allure.severity("blocker")
	def test_fql_financedata_0015(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件：环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		dictDetail = bkw.financeDataApi_dictDetailByName(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
				"data": {"dictKey": "自动生成金蝶凭证"}, "env": envt}, "dict")
		dictKey = ckw.CommonKeyWord().Json_GetJsonValue(dictDetail, [["data", "dictKey"]])
		assert ckw.CommonKeyWord().Assert_ObjAndObj(dictKey, "自动生成金蝶凭证")

	@allure.feature("指定连锁日期的协议扣率详情")
	@allure.severity("blocker")
	def test_fql_financedata_0016(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FangQianLing/FinanceData.yaml")
		# 读取yaml文件：环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		discountDetail = bkw.financeDataApi_partnerDiscountDetailByTime(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
				"data": {"organizationId": 578, "times": "2022-07-20 16:30:57", "balanceType": 1, "channel": 1},
				"env": envt}, "dict")
		ckw.CommonKeyWord().Print_ToLog("协议扣率详情", discountDetail)
		data = ckw.CommonKeyWord().Json_GetJsonValue(discountDetail, [["data"]])
		assert bool(data)

	@allure.feature("关闭公共数据数据库")
	@allure.severity("blocker")
	def test_fql_financedata_close(self):
		# 关闭公共数据数据库
		ckw.CommonKeyWord().Db_SshConfRCMysqlClose(financeDataDB)
