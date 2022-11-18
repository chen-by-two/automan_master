# -*- coding: utf-8 -*-
import pytest, os, allure, pymysql
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

import datetime

class Test_CreditCenterAutoCaseRun:

	@allure.feature("类预制")
	@allure.severity("blocker")
	def setup_class(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取Yaml执行环境
		global env
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		test_host = ckw.CommonKeyWord(	).Yaml_GetByKey(yamlFile, "test_host")
		test_user = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "test_user")
		test_passwd = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "test_passwd")
		test_port = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "test_port")
		self.db = pymysql.connect(host = test_host,
								 user = test_user,
								 passwd = test_passwd,
								 port = test_port)
		self.cursor = self.db.cursor()


	def teardown_class(self):
		self.cursor.close()
		self.db.close()
		print ("teardown_class(self)：每个类之后执行一次")


	@allure.feature("流水积分校验接口")
	@allure.severity("blocker")
	def test_dzj_credit_001(self):
		# 流水积分校验接口
		res = bkw.creditCenterApi_CreditCompanySettleTradeCheckCompanyCredit(
			{"header": {"Content-Type": "application/json;charsetUTF-8"},
			 "parma": {},
			 "data": {
						"merchantId": "578",
						"startDate": "2021-01-25 00:00:00",
						"endDate": "2021-01-25 23:59:59",
						"checkType": 2,
						"amount": 202
					}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 打印到日志
		ckw.CommonKeyWord().Print_ToLog("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "success" in str(res)

	@allure.feature("连锁流水拉取接口")
	@allure.severity("blocker")
	def test_dzj_credit_002(self):
		# 流水积分校验接口
		res = bkw.creditCenterApi_CreditCompanySettleTradePullCompanyRecords(
			{"header": {"Content-Type": "application/json;charsetUTF-8"},
			 "parma": {},
			 "data": {"orderNo":"81012511605002010159"}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 打印到日志
		ckw.CommonKeyWord().Print_ToLog("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "成功" in str(res)

	@allure.feature("添加积分预发方记录")
	@allure.severity("blocker")
	def test_dzj_credit_003(self):
		# 流水积分校验接口
		res = bkw.creditCenterApi_CreditPreAccountTradePreAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8"},
			 "parma": {},
			 "data": {"requestSeq":"wx1234",
						"memberId": "15964339",
						"accountId": "1",
						"opType": 1,
						"opAmount": 1.0,
						"channel": 1,
						"status": "1",
						"remark": "remark自动化",
						"identify": "assistant"}, "env": env},
						"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		ckw.CommonKeyWord().Print_ToLog("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 获取接口信息data.id
		result2 = ckw.CommonKeyWord().Json_GetJsonValue(res, [["data"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl("data:",result2)
		ckw.CommonKeyWord().Print_ToLog("data:", result2)
		# 获取接口信息data.id
		result3 = res["data"]["id"]
		# 打印
		ckw.CommonKeyWord().Print_ToControl("id:", result3)
		ckw.CommonKeyWord().Print_ToLog("id:", result3)
		# 断言
		assert "已到账" in str(res)
		# 数据库查询
		sql = "select * from cn_ud_mid_creditcenter.pre_account_records where id = " + str(result3)
		# sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		self.cursor.execute(sql)
		sqlRes = self.cursor.fetchall()
		# 打印
		ckw.CommonKeyWord().Print_ToControl("sql查询结果:", sqlRes)
		ckw.CommonKeyWord().Print_ToLog("sql查询结果:", sqlRes)
		ckw.CommonKeyWord().Print_ToControl("sql查询结果:", sqlRes[0])
		ckw.CommonKeyWord().Print_ToLog("sql查询结果:", sqlRes[0])
		# 断言
		assert sqlRes[0][1] == 15964339

	@allure.feature("批量审核积分预发放记录")
	@allure.severity("blocker")
	def test_dzj_credit_004(self):
		# 流水积分校验接口
		res = bkw.creditCenterApi_CreditPreAccountTradeEditBatch(
			{"header": {"Content-Type": "application/json;charsetUTF-8"},
			 "parma": {},
			 "data": {
						"ids": [88097, 88096],
						"userId": 15964339,
						"userName": "张三",
						"status": 1,
						"auditDetail": "审核意见"
					}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		ckw.CommonKeyWord().Print_ToLog("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		assert "'success': True" in str(res)

	@allure.feature("积分确认提现接口")
	@allure.severity("blocker")
	def test_dzj_credit_005(self):
		# 流水积分校验接口
		res = bkw.creditCenterApi_CreditIntegralTradeConfirmWithdraw(
			{"header": {"Content-Type": "application/json;charsetUTF-8"},
			 "parma": {},
			 "data": {
						"memberId": 15964339,
						"memberName": "",
						"accountRecordsId": "8359026",
						"integralRecordsId": "13",
						"status": 1,
						"checkDesc": "",
						"identify": "consumer"
						}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		ckw.CommonKeyWord().Print_ToLog("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		assert "审核" in str(res)

	@allure.feature("积分统计列表")
	@allure.severity("blocker")
	def test_dzj_credit_006(self):
		# 流水积分校验接口
		res = bkw.creditCenterApi_CreditAccountQueryPreCount(
			{"header": {"Content-Type": "application/json;charsetUTF-8"},
			 "parma": {},
			 "data": {
						"accountNo": "13301120002",
						"memberName": "",
						"status": "",
						"identity": "",
						"partnerId": "",
						"storeId": "",
						"reason": "",
						"productName": "",
						"orderNo": "",
						"channel": "1"
					}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		ckw.CommonKeyWord().Print_ToLog("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		assert "'success': True" in str(res)