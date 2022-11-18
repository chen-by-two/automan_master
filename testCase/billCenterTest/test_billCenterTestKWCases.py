# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_billCenter:

	@allure.feature("票据中心-创建直付结算单")
	@allure.severity("blocker")
	def test_lq_billCenterTest_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 执行接口-发起结算
		payoutStatement = bkw.billCenterApi_directStatementCreate({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "partnerId": 635, "partnerName": "国药控股国大药房上海连锁有限公司", "organizationId": 635, "organizationName": "国药控股国大药房上海连锁有限公司", "statementBeginDate": "2022-04-18", "statementEndDate": "2022-04-18", "businessType": 1, "statementLevel": 1, "subsidyAmount": "0", "workerId": 847, "workerName": "梁琪" },"env":envt},"dict")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("直付结算单创建返回结果:",payoutStatement)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("直付结算单创建返回结果:",payoutStatement)
		# 提取数据-接口返回的生成的结算单(dict)
		payoutStatementNo = ckw.CommonKeyWord().Json_GetJsonValue(payoutStatement,[["data"]])
		print("提取数据-接口返回的生成的结算单",payoutStatementNo,type(payoutStatementNo))
		# # 将数组转化成json
		# payoutStatementNo1 = ckw.CommonKeyWord().Json_GetJsonValue(payoutStatementNo)
		# print("将数组转化成json", payoutStatementNo1, type(payoutStatementNo1))
		# 提取生成的结算单
		statementNo = ckw.CommonKeyWord().Json_GetJsonValue(payoutStatementNo,[["statementNo"]])
		print("提取生成的结算单", statementNo, type(statementNo))
		# 打印提取的结算单结果到控制台
		ckw.CommonKeyWord().Print_ToControl("直付结算单:",statementNo)
		# 打印提取的结算单结果到日志
		ckw.CommonKeyWord().Print_ToLog("直付结算单:",statementNo)
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 查询SQL-结算单
		selectPayoutStatemntNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectPayoutStatemntNo")
		# 执行SQL
		PayoutStatemntNo = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_udc_fin_bill",selectPayoutStatemntNo)
		# 将数组转化成json
		PayoutStatemntNo1 = ckw.CommonKeyWord().Json_oneCharList2json(PayoutStatemntNo)
		# 提取json中的对象
		payoutStatemntNos = ckw.CommonKeyWord().Json_GetJsonValue(PayoutStatemntNo1,[["statement_no"]])
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(payoutStatemntNos,statementNo)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("票据中心-创建应付开票单")
	@allure.severity("blocker")
	def test_lq_billCenterTest_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 审核通过结算单
		bkw.billCenterApi_directStatementAuditAccept({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "statementNo": "statementNo" },"env":envt},"dict")
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("10.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 查询生成的开票单
		selectPayBillNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectPayBillNo")
		# 执行SQL
		payoutBillNo = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_udc_fin_bill",selectPayBillNo)
		# 将数组转化成json
		payoutBillNo1 = ckw.CommonKeyWord().Json_oneCharList2json(payoutBillNo)
		# 提取json中的对象
		payoutBillNos = ckw.CommonKeyWord().Json_GetJsonValue(payoutBillNo1,[["bill_no"]])
		# 打印提取的开票单结果到控制台
		ckw.CommonKeyWord().Print_ToControl("直付开票单:",payoutBillNos)
		# 打印提取的开票单结果到日志
		ckw.CommonKeyWord().Print_ToLog("直付开票单:",payoutBillNos)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("20.0")

	@allure.feature("票据中心-查询应付开票单")
	@allure.severity("blocker")
	def test_lq_billCenterTest_0003(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCapthaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCapthaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_data",updateCapthaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_data",updateCaptchaCode)
		# 财务共享平台登录获取authToken
		ddmodbilelogin = bkw.financeApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 财务共享平台authToken提取
		authToken_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data","authToken"]])
		# 财务共享平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("财务共享平台authToken:",authToken_1)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳",time)
		# 执行查询应付开票单接口
		payoutBillPaging = bkw.billCenterApi_payoutBillPaging({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+authToken_1},"parma":{},"data":{ "page":1, "limit":10, "pageData":"2022-04-28T08:49:32.586Z", "selectIndex":0, "billStatus":"1", "businessNo":"statementNo" , "expressStatus":"" },"env":envt},"dict")
		# 提取应付开票单列表
		payoutBillNos = ckw.CommonKeyWord().Json_GetJsonValue(payoutBillPaging,[["data"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("payoutBillNos:",payoutBillNos)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("payoutBillNos:",payoutBillNos)
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 读取yaml文件获取billNo
		selectPayBillNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectPayBillNo")
		# 运行后台执行SQL
		payoutBillNo = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_udc_fin_bill",selectPayBillNo)
		# 将数组转化成json
		payoutBillNo1 = ckw.CommonKeyWord().Json_oneCharList2json(payoutBillNo)
		# 提取json中的对象
		bill_no = ckw.CommonKeyWord().Json_GetJsonValue(payoutBillNo1,[["bill_no"]])
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(payoutBillNos,bill_no)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("票据中心-重置订单")
	@allure.severity("blocker")
	def test_lq_billCenterTest_0004(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 查询重置直付付款单-订单表
		updateDirectSettlement1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateDirectSettlement1")
		# 查询重置直付付款单-商品替换后的表
		updateDirectSettlement2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateDirectSettlement2")
		# 执行SQL-重置直付付款单-订单表
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_udc_fin_bill",updateDirectSettlement1)
		# 执行SQL-重置直付付款单-商品替换后的表
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_udc_fin_bill",updateDirectSettlement2)
