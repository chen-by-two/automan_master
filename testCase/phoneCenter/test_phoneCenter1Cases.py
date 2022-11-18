# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.phoneCenter.phoneCenterApi as phoneCenter


import ApiLib.promoteCenter.promoteCenterApi as promoteCenter


class Test_phoneCenter:

	@allure.feature("phoneCenter")
	@allure.severity("blocker")
	@pytest.mark.flaky(retun=1,runs_delay=2)
	def test_Phone_test1(self):
		"""
		手机号归属地查询API接口
		"""
		Phone=phoneCenter.Phone()
		Phone.headers = {"Content-Type":"application/json;charset=UTF-8"}
		Phone.changeEnv("api.vvhan.com")
		Phone.params = {"tel": "15951652383"}
		PhoneRes = Phone.excute()
		assert PhoneRes.text.__contains__("江苏移动全球通卡")

	@allure.feature("phoneCenter")
	@allure.severity("blocker")
	@pytest.mark.flaky(retun=1,runs_delay=2)
	def test_CardQueryMyRecord_test2(self):
		"""
		查询我的卡列表
		"""
		CardQueryMyRecord=promoteCenter.CardQueryMyRecord()
		CardQueryMyRecord.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardQueryMyRecord.changeEnv("uniondrug.net")
		CardQueryMyRecord.data = {"memberId":228,"cardType":"1","status":1,"tagList":["49","35","169","116","165"]}
		CardQueryMyRecordRes = CardQueryMyRecord.excute()
		assert CardQueryMyRecordRes.text.__contains__("21595263016d47a782d8")
