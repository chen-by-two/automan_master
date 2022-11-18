# -*- coding: utf-8 -*-
import pytest,os,allure
import requests

import KeyWordDriver.CommonKeyWord as ckw
import KeyWordDriver.BusinesskeyWord as bkw

class Test_coinService:


	@allure.feature("连接资金系统和短信数据库")
	@allure.severity("blocker")
	def test_fzs_connect(self):
		# 定义全局变量coinServiceDB，moduleDataDB
		global coinServiceDB
		global moduleDataDB
		# 全局变量赋值
		moduleDataDB = ckw.CommonKeyWord().Db_SshConfRCMysqlConnect("DATABASE_RC_cn_uniondrug_module_data")
		coinServiceDB = ckw.CommonKeyWord().Db_SshConfRCMysqlConnect("DATABASE_RC_cn_uniondrug_middleend_coin")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("数据库连接成功返回：",moduleDataDB,coinServiceDB)


	@allure.feature("获取登录成功后的token")
	@allure.severity("blocker")
	def test_fzs_getToken(self):
		# 定义全局变量coinToken
		global coinToken
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/Fzs/fzs.yaml")
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCapthaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCapthaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envr")
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(moduleDataDB,updateCapthaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(moduleDataDB,updateCaptchaCode)
		# 资金系统登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envr},"dict")
		# 打印登录接口1出参到日志
		ckw.CommonKeyWord().Print_ToLog("登录接口出参获取token:",ddmodbilelogin)
		# 登录接口出参token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("登录接口出参token:",token_1)
		# 资金系统登录获取Authorization
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envr},"dict")
		# 打印登录接口2出参到日志
		ckw.CommonKeyWord().Print_ToLog("登录接口出参:",ddlogin)
		# 资金系统Authorization提取
		coinToken = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 打印Authorization到日志
		ckw.CommonKeyWord().Print_ToLog("登录接口出参Authorization:",coinToken)

	@allure.feature("资金系统-付款单新建成功")
	@allure.severity("blocker")
	def test_fzs_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/Fzs/fzs.yaml")
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		# 读取yaml文件内删除付款单SQL
		deletePayment = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"deletePayment")
		# 读取yaml文件内查询付款单号SQL
		selectPaymentCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectPaymentCode")
		# 运行设定后台删除付款单SQL
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,deletePayment)
		# 资金系统创建付款单
		paymentCreate = bkw.coinServiceApi_paymentCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+coinToken},"parma":{},"data":{"id":None,"paymentCode":None,"operator":{"workerId":"395","workerName":"方倩玲"},"serialId":"1650873465025307691","businessNo":"SS1122334455","payer":None,"payerId":"7","payerName":"上海聚音信息科技有限公司","payerAccount":"1001101719100022593","payerAccountName":"上海聚音信息科技有限公司","payerBank":"中国工商银行股份有限公司","payerBankHouse":"中国工商银行股份有限公司上海市大连路支行","payerCnaps":"102290010174","payeeType":"0","recipientId":None,"recipientType":"1","recipientName":"FZS公司","recipientAccount":"666688889999","recipientAccountName":"FZS公司","recipientBankObject":{"bankId":"308","name":"招商银行股份有限公司","code":"308"},"recipientBank":"招商银行股份有限公司","recipientBankHouseObject":{"name":"招商银行股份有限公司石河子分行","cnaps":"308902839018"},"recipientBankHouse":"招商银行股份有限公司石河子分行","recipientCnaps":"308902839018","confirmDate":None,"planPayDate":"2022-06-25","paidAmount":"188.00","payDate":None,"payAmount":188,"deductAmount":"0","payMethod":"电汇（T/T）","channel":"1","status":0,"businessType":"直付结算","openRechargeFund":0,"annexs":[],"removeAnnexIds":None,"createAnnexs":None,"outSerialId":None,"taxServiceDeductAmount":None,"payComment":None,"coinCode":"1122334455","remark":"测试","payableCompanyName":None,"payableCompanyId":None,"sourceMode":1},"env":envr},"dict")
		# 打印创建付款单出参到日志
		ckw.CommonKeyWord().Print_ToLog("创建付款单接口出参：",paymentCreate)
		# 提取付款单号
		paymentCode = ckw.CommonKeyWord().Json_GetJsonValue(paymentCreate,[["data","paymentCode"]])
		# 打印接口出参付款单号到日志
		ckw.CommonKeyWord().Print_ToLog("创建付款单接口出参pamentCode：",paymentCode)
		# 运行设定后台查询付款单号SQL
		paymentCode_1 = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,selectPaymentCode)
		# 打印查询付款单号SQL结果到日志
		ckw.CommonKeyWord().Print_ToLog("数据库出参pamentCode：",paymentCode_1)
		# 提取付款单号
		paymentCode_2 = ckw.CommonKeyWord().Json_GetJsonValue(paymentCode_1[0],[["payment_code"]])
		# 断言字符等于
		assert ckw.CommonKeyWord().Assert_ObjAndObj(paymentCode_2,paymentCode)

	@allure.feature("资金系统-分页查询向药联付款的组织已认领交易记录")
	@allure.severity("blocker")
	def test_fzs_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/Fzs/fzs.yaml")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCapthaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateCapthaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "LoginCaptcha")
		# 读取yaml文件环境域名
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名", envr)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名", envr)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(moduleDataDB, updateCapthaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(moduleDataDB, updateCaptchaCode)
		# 资金系统登录获取token
		ddmodbilelogin = bkw.financeApi_DdMobilelogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
			 "data": {"mobile": "15952059927", "code": "123456"}, "env": envr}, "dict")
		# 打印登录接口1出参到日志
		ckw.CommonKeyWord().Print_ToLog("登录接口出参获取token:", ddmodbilelogin)
		# 登录接口出参token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin, [["data"]])
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(token_1, [["authToken"]])
		# 资金系统创建付款单
		bankChaimPageByPayer = bkw.coinServiceApi_bankChaimPageByPayer(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
			 "parma": {}, "data": {"page": 1, "limit": 10, "pageData": "2022-06-17T06:33:00.163Z", "chaim": "3",
								   "payerOrganizationId": "161136"}, "env": envr}, "dict")
		# 断言字符包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(bankChaimPageByPayer, '全部关联')

	@allure.feature("资金系统-根据组织id查询资金账户")
	@allure.severity("blocker")
	def test_fzs_0003(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/Fzs/fzs.yaml")
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		fundAccountGetByHolder = bkw.coinServiceApi_fundAccountGetByHolder({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"holderId":"90026","holderType":1},"env":envr},"dict")
		assert ckw.CommonKeyWord().Assert_BcharInAchar(fundAccountGetByHolder,'宁夏国大药房连锁有限公司')

	@allure.feature("资金系统-资金付款对接组回调")
	@allure.severity("blocker")
	def test_fzs_0004(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/Fzs/fzs.yaml")
		updateBankTransfer = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateBankTransfer")
		updatePayment = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updatePayment")
		selectBankTransfer = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectBankTransfer")
		selectPayment = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectPayment")
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,updateBankTransfer)
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,updatePayment)
		bkw.coinServiceApi_connectTransferCallBack({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"voucherNo":"FM20220104311523","waterNo":"20220104134358831768035","status":1,"message":"转账成功","reptImage":"","callback":"java.coin.service.uniondrug.net\/connect\/transferCallBack"},"env":envr},"dict")
		status = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,selectBankTransfer)
		payStatus = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,selectPayment)
		assert ckw.CommonKeyWord().Assert_BcharInAchar(status,'2')
		assert ckw.CommonKeyWord().Assert_BcharInAchar(payStatus,'2')

	@allure.feature("资金系统-换新服务审核通过资金池扣减")
	@allure.severity("blocker")
	def test_fzs_0005(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/Fzs/fzs.yaml")
		deleteFundRecord = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteFundRecord")
		deleteFundRecordDetail = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteFundRecordDetail")
		updateFundOrder = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateFundOrder")
		selectFundRecord = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectFundRecord")
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,deleteFundRecord)
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,deleteFundRecordDetail)
		ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,updateFundOrder)
		bkw.coinServiceApi_mbsAuditCenter({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"reason":None,"orderNo":"92070411603677670150","productId":"8","capitalPool":"5.00","channel":"1","auditNo":"92070468160367768711","capitalStatus":1,"type":"1","guaranteeId":"0","supplierMerchantId":"555","supplierStoreId":"60016","merchantId":"555","auditStatus":1,"mainOrderNo":"92070401603677660176","equityId":"0","status":2},"env":envr},"dict")
		orderNo = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(coinServiceDB,selectFundRecord)
		assert ckw.CommonKeyWord().Assert_BcharInAchar(orderNo,'92070411603677670150')

	@allure.feature("关闭资金系统和短信数据库")
	@allure.severity("blocker")
	def test_fzs_close(self):
		# 关闭资金系统数据库
		ckw.CommonKeyWord().Db_SshConfRCMysqlClose(coinServiceDB)
		# 关闭短信数据库
		ckw.CommonKeyWord().Db_SshConfRCMysqlClose(moduleDataDB)