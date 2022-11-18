# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

import datetime

import TestFile.DaizhaojiOnly.customkeywords as cuskw

class Test_UserCenterAutoCaseRun2:

	@allure.feature("用户中心用户登录")
	@allure.severity("blocker")
	def setup_class(self):
		print ("setup_class(self)：每个类之前执行一次")
		self.auth = cuskw.BackstageManagementLogin().getauthorization(13333333001)
		print(self.auth)
		self.yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		self.mobile = ckw.CommonKeyWord().Yaml_GetByKey(self.yamlFile, "mobile")


	def test_dzj_user2_001(self):
		print(self.auth)
		print(self.yamlFile)
		print(self.mobile)
		pass

	def test_dzj_user2_002(self):
		print(self.auth)
		pass

	def teardown_class(self):
		print ("teardown_class(self)：每个类之后执行一次")

	def setup_method(self):
		print ("setup_method(self):在每个方法之前执行")

	def teardown_method(self):
		print ("teardown_method(self):在每个方法之后执行")