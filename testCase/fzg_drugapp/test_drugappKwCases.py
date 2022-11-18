# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_drugapp:
	global wechatToken
	sqlToken = "SELECT token FROM `cn_uniondrug_backend_auth`.`member_token` WHERE `memberId` = '16236586' AND `channel` = 'wechat' LIMIT 0,1000 "
	print(sqlToken)
	wechatToken = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data", sqlToken)[0][
		"token"]
# 	wechatToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-9FGzuShNsYwdwA"
# 	print(wechatToken)
	
	@allure.feature("发送验证码")
	@allure.severity("blocker")
	def test_fzg_drugapp_001(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobile")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录发送验证码
		CodeSendRes = bkw.drugappApi_CodeSend({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"usage":"login","sendMethod":"sms","isNew":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CodeSendRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("验证码登录")
	@allure.severity("blocker")
	def test_fzg_drugapp_002(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录发送验证码
		bkw.drugappApi_CodeSend({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"mobile":mobile,"usage":"login","sendMethod":"sms","isNew":"1"},"env":env},"dict")
		# 读取Yaml执行环节
		getLoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# mysql执行sql-查询验证码
		captcha = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data",getLoginCaptcha)
		# 验证码登录
		V4UsersSmslogin1Res = bkw.drugappApi_V4UsersSmslogin1({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"appVersionNumber":"1.0","deviceSerial":"iPhone","deviceUuid":"3ab3747c5ef1d6602fe523a1e39d6ebdd8733eb63c49032d63005e7b586745fe","deviceVersion":"13.6.1","mobile":"18354299687","devicePlatform":"iOS","appVersionRelease":"5.2.0.2","CFBundleDisplayName":"药联药店宝","deviceModel":"iPhone 8","code":captcha,"appName":"药联药店宝","appVersionVode":"5.2.0.2","isNew":"1","appPackageName":"com.xun-ao.udsa"},"env":env},"dict")
		# 获取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(V4UsersSmslogin1Res,[["data","token"]])
		# 获取接口返回值
		memberId = ckw.CommonKeyWord().Json_GetJsonValue(V4UsersSmslogin1Res,[["data","memberId"]])
		# 读取yaml里预期memberId1
		memberId1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"memberId1")
		# 断言memberId
		assert ckw.CommonKeyWord().Assert_ObjAndObj(memberId,memberId1)

	@allure.feature("用户特权列表1")
	@allure.severity("blocker")
	def test_fzg_drugapp_003(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取用户特权列表1接口
		PrivilegeListRes = bkw.drugappApi_PrivilegeList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"assistantId":"20083722","status":"2"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(PrivilegeListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("用户特权列表2")
	@allure.severity("blocker")
	def test_fzg_drugapp_004(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取用户特权列表2接口
		PrivilegeV2ProgressListRes = bkw.drugappApi_PrivilegeV2ProgressList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(PrivilegeV2ProgressListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("分页列表")
	@allure.severity("blocker")
	def test_fzg_drugapp_005(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取分页列表接口
		CiMemberPageRes = bkw.drugappApi_CiMemberPage({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberPageRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)
		# json获取返回值
		dataType = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberPageRes,[["dataType"]])
		# 读取yaml里dataType1
		dataType1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"dataType1")
		# 断言dataType
		assert ckw.CommonKeyWord().Assert_ObjAndObj(dataType,dataType1)

	@allure.feature("会话列表")
	@allure.severity("blocker")
	def test_fzg_drugapp_006(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		CiMemberChatListRes = bkw.drugappApi_CiMemberChatList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"memberId":"111"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberChatListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)
		# json获取返回值
		dataType = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberChatListRes,[["dataType"]])
		# 读取yaml里dataType2
		dataType2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"dataType2")
		# 断言dataType
		assert ckw.CommonKeyWord().Assert_ObjAndObj(dataType,dataType2)

	@allure.feature("单人/群组发起聊天")
	@allure.severity("blocker")
	def test_fzg_drugapp_007(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		CiMemberStartChatRes = bkw.drugappApi_CiMemberStartChat({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"customerMemberId":"16236586","isYdbProgram":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberStartChatRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)
		# json获取返回值
		dataType = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberStartChatRes,[["dataType"]])
		# 读取yaml里dataType3
		dataType3 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"dataType3")
		# 断言dataType
		assert ckw.CommonKeyWord().Assert_ObjAndObj(dataType,dataType3)

	@allure.feature("会员详情")
	@allure.severity("blocker")
	def test_fzg_drugapp_008(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		CiMemberDetailRes = bkw.drugappApi_CiMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"memberId":16236586,"isYdbProgram":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberDetailRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)
		# json获取返回值
		memberId = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberDetailRes,[["data","memberId"]])
		# 读取yaml里memberId1
		memberId1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"memberId1")
		# 断言memberId
		assert ckw.CommonKeyWord().Assert_ObjAndObj(memberId,memberId1)

	@allure.feature("顾问详情")
	@allure.severity("blocker")
	def test_fzg_drugapp_009(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		CiMemberAdvisorDetailRes = bkw.drugappApi_CiMemberAdvisorDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"memberId":"111"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberAdvisorDetailRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)
		# json获取返回值
		assistantId = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberAdvisorDetailRes,[["data","assistantId"]])
		# 读取yaml里assistantId1
		assistantId1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"assistantId1")
		# 断言assistantId
		assert ckw.CommonKeyWord().Assert_ObjAndObj(assistantId,assistantId1)

	@allure.feature("特权规则详情")
	@allure.severity("blocker")
	def test_fzg_drugapp_010(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		PrivilegeRuleDetailRes = bkw.drugappApi_PrivilegeRuleDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(PrivilegeRuleDetailRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("评价列表")
	@allure.severity("blocker")
	def test_fzg_drugapp_011(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		CiMemberEvaluateListRes = bkw.drugappApi_CiMemberEvaluateList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"page":1,"limit":10,"type":0},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberEvaluateListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("banner列表")
	@allure.severity("blocker")
	def test_fzg_drugapp_012(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		ResourceBannerListRes = bkw.drugappApi_ResourceBannerList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ResourceBannerListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("服务列表")
	@allure.severity("blocker")
	def test_fzg_drugapp_013(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		ResourceServiceListRes = bkw.drugappApi_ResourceServiceList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"partnerOrganId":"635"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ResourceServiceListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("删除某个会话")
	@allure.severity("blocker")
	def test_fzg_drugapp_014(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		CiMemberDeleteChatRes = bkw.drugappApi_CiMemberDeleteChat({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"isGroup":"0","memberId":"16236586"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(CiMemberDeleteChatRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("群组新增")
	@allure.severity("blocker")
	def test_fzg_drugapp_015(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		GroupCreateRes = bkw.drugappApi_DrugstoreuserGroupCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"name":"Weee","members":[{"memberId":"16236586"}]},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(GroupCreateRes,[["errno"]])
		print(errno)
		# 读取yaml里errorno
		# errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		errorno = "1710"
		print(errorno)
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("群组详情")
	@allure.severity("blocker")
	def test_fzg_drugapp_016(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取会话列表接口
		GroupDetailRes = bkw.drugappApi_GroupDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer 71d9a016-c0bc-4e02-aa54-cc42292dbe50"},"parma":{},"data":{"groupId":"28","isYdbProgram":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(GroupDetailRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易1")
	@allure.severity("blocker")
	def test_fzg_drugapp_017(self):

		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		OrderCanUseListRes = bkw.drugappApi_OrderCanUseList({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"resource":"2","items":[{"itemUuid":"d2e95199-aaf2-4c04-a26b-b2336c088c7c","goodsNo":"","internalId":"137","internalIdList":"","selectFlag":"1","goodsType":"1","goodsSubType":"11","rxFlag":"1","infusionFlag":"0","unitPrice":"84.00","afterActivityUnitPrice":"0","quantity":"1","merchantId":"159798","storeId":"159932","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"优普洛","realName":"罗替高汀贴片","tradeCode":"10690100000016","image":"https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1596779043602.jpg","approvalNumber":"H20180028","manufacturer":"LTS Lohmann Therapie-Systeme AG","form":"4.5mg:10cm²*7贴","pack":"盒","batchNumber":"","memberPrice":"84.00","originalPrice":"84.00","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"1","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"1","insuranceCode":"","totalAmount":"84.00","directAmount":"0","activityAmount":"42","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":{"activityId":"","requestNo":"","activityAmount":"0","activityType":"0","activityName":""},"activityName":"","itemAttr":{"id":"0","attrs":"0,1,3,31027,30003,31061,31080,31064,31083,31227,31055","cates":"0,44017,44018,2"},"giftDrug":{"itemUuid":"","goodsNo":"","internalId":"","internalIdList":"","selectFlag":"1","goodsType":"","goodsSubType":"0","rxFlag":"0","infusionFlag":"0","unitPrice":"0","afterActivityUnitPrice":"0","quantity":"0","merchantId":"0","storeId":"0","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"","realName":"","tradeCode":"","image":"","approvalNumber":"","manufacturer":"","form":"","pack":"","batchNumber":"0","memberPrice":"0","originalPrice":"0","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"0","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"0","insuranceCode":"","totalAmount":"0","directAmount":"0","activityAmount":"0","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":"","activityName":"","itemAttr":"","giftDrug":"","isHasActivity":"0","weight":"0"},"isHasActivity":"0","weight":"0"}],"serviceItems":[],"eshop":[{"expressType":"5","expressTypeSelect":"0","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊大大","receiveMobile":"18354299687","wayBillNo":"","address":"江苏省南京市雨花台区风信路6号金证橙风里测试","storeName":"","merchantName":"","longitude":"118.779047","latitude":"31.972011","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]},{"expressType":"3","expressTypeSelect":"1","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊战岗","receiveMobile":"18354299687","wayBillNo":"","address":"清水塘街道芙蓉中路一段319号绿地中心裙房103房","storeName":"长沙邻客智慧大药房有限公司","merchantName":"邻客智慧药房DTP","longitude":"112.987239","latitude":"28.210957","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]}],"sign":{"needSign":"0","needCard":"0","agreements":[],"frontCardImage":"","backendCardImage":"","signImageUrl":"","projectId":"","schemeId":""},"temperature":{"isNeed":"0","name":"","idCard":"","mobile":"","symptom":"","temperature":"","isRisk":"0"},"rx":{"isNeedRx":True,"isHasRx":False,"chooseRxType":"0","rxWaterNo":"","rxId":"","type":"0","rxImage":"","reason":"","status":"0","userName":"","userMobile":"","rxText":"","mode":"","supplierId":"0"},"merchantName":"邻客智慧药房DTP","storeName":"长沙邻客智慧大药房有限公司","drugs":[{"itemUuid":"d2e95199-aaf2-4c04-a26b-b2336c088c7c","goodsNo":"","internalId":"137","internalIdList":"","selectFlag":"1","goodsType":"1","goodsSubType":"11","rxFlag":"1","infusionFlag":"0","unitPrice":"84.00","afterActivityUnitPrice":"0","quantity":"1","merchantId":"159798","storeId":"159932","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"优普洛","realName":"罗替高汀贴片","tradeCode":"10690100000016","image":"https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1596779043602.jpg","approvalNumber":"H20180028","manufacturer":"LTS Lohmann Therapie-Systeme AG","form":"4.5mg:10cm²*7贴","pack":"盒","batchNumber":"","memberPrice":"84.00","originalPrice":"84.00","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"1","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"1","insuranceCode":"","totalAmount":"84.00","directAmount":"0","activityAmount":"42","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":{"activityId":"","requestNo":"","activityAmount":"0","activityType":"0","activityName":""},"activityName":"","itemAttr":{"id":"0","attrs":"0,1,3,31027,30003,31061,31080,31064,31083,31227,31055","cates":"0,44017,44018,2"},"giftDrug":{"itemUuid":"","goodsNo":"","internalId":"","internalIdList":"","selectFlag":"1","goodsType":"","goodsSubType":"0","rxFlag":"0","infusionFlag":"0","unitPrice":"0","afterActivityUnitPrice":"0","quantity":"0","merchantId":"0","storeId":"0","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"","realName":"","tradeCode":"","image":"","approvalNumber":"","manufacturer":"","form":"","pack":"","batchNumber":"0","memberPrice":"0","originalPrice":"0","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"0","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"0","insuranceCode":"","totalAmount":"0","directAmount":"0","activityAmount":"0","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":"","activityName":"","itemAttr":"","giftDrug":"","isHasActivity":"0","weight":"0"},"isHasActivity":"0","weight":"0"}],"amounts":[{"type":"2","name":"权益抵扣","resourceName":"","originAmount":"0.00","amount":"0.00"},{"type":"3","name":"平台活动","resourceName":"tq平台活动111","originAmount":"42.00","amount":"42.00"}],"allDiscountAmount":"42.00","saleAmount":"42.00","allDrugDiscountAmount":"42.00","allDrugSaleAmount":"42.00","isHasDtp":"1","services":[],"drugUser":{"drugUserId":"101","name":"樊战岗","idCard":"610523199201086936","mobile":"18354299687"},"businessStartTime":"08:30","businessEndTime":"17:30","storeStatus":"0","storeTimeStatus":"2","storeOpenTime":"0","storeTime":"0","merchantId":"159798","storeId":"159932","channel":"2","orderMethod":"14","assistantMemberId":"0","assistantId":"0","cardId":"","outActivityId":"","feeCardId":"","feeAmount":"0.00","equityUuid":"","equityIds":[],"equityName":"","coupon":{"couponId":"","cardId":"","couponAmount":"0","couponType":"0","schemeId":""},"eshopConfig":{"isUseEquity":"1","isUsePromoteCoupon":"1","isUseCoupon":"1","isUseActivity":"1","isUseFeeCoupon":"1","isUseOutActivity":"1"},"isShowUnionMember":"-1","orderNo":"","mainOrderNo":"","remark":"","isNeedIdentify":"0","isNeedTimelyDistribution":"1","orderAreaLimit":"0","requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","isUpdateRemark":"0"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(OrderCanUseListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易2")
	@allure.severity("blocker")
	def test_fzg_drugapp_018(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		UserWxConfigRes = bkw.drugappApi_UserWxConfig({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"url":"https://wx.uniondrug.net/otoDeal/confirm-order?requestNo3f714ab0b0e0021794b6dcead79ca0b4"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(UserWxConfigRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易3")
	@allure.severity("blocker")
	def test_fzg_drugapp_019(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		UserAddressListRes = bkw.drugappApi_UserAddressList({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"limit":20,"page":1},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(UserAddressListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易4")
	@allure.severity("blocker")
	def test_fzg_drugapp_020(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		OrderUpdatePreOrderRes = bkw.drugappApi_OrderUpdatePreOrder({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"eshop":[{"expressType":"5","expressTypeSelect":"1","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊大大","receiveMobile":"18354299687","wayBillNo":"","address":"江苏省南京市雨花台区风信路6号金证橙风里测试","storeName":"","merchantName":"","longitude":"118.779047","latitude":"31.972011","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]},{"expressType":"3","expressTypeSelect":"0","expressAmount":"0","expressDiscount":"0","mitigateRuleString":"","addressId":"103878","receiveName":"樊战岗","receiveMobile":"18354299687","wayBillNo":"","address":"清水塘街道芙蓉中路一段319号绿地中心裙房103房","storeName":"长沙邻客智慧大药房有限公司","merchantName":"邻客智慧药房DTP","longitude":"112.987239","latitude":"28.210957","distance":"","distanceMi":"","deliveryMethod":"0","deliverTime":"","deliverDistance":"0","deliveryMethods":[]}],"sign":{"needSign":"0","needCard":"0","agreements":[],"frontCardImage":"","backendCardImage":"","signImageUrl":"","projectId":"","schemeId":""},"temperature":{"isNeed":"0","name":"","idCard":"","mobile":"","symptom":"","temperature":"","isRisk":"0"},"rx":{"isNeedRx":True,"isHasRx":False,"chooseRxType":"0","rxWaterNo":"","rxId":"","type":"0","rxImage":"","reason":"","status":"0","userName":"","userMobile":"","rxText":"","mode":"","supplierId":"0"},"merchantName":"邻客智慧药房DTP","storeName":"长沙邻客智慧大药房有限公司","drugs":[{"itemUuid":"d2e95199-aaf2-4c04-a26b-b2336c088c7c","goodsNo":"","internalId":"137","internalIdList":"","selectFlag":"1","goodsType":"1","goodsSubType":"11","rxFlag":"1","infusionFlag":"0","unitPrice":"84.00","afterActivityUnitPrice":"0","quantity":"1","merchantId":"159798","storeId":"159932","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"优普洛","realName":"罗替高汀贴片","tradeCode":"10690100000016","image":"https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/oss/upload/file/goods/1596779043602.jpg","approvalNumber":"H20180028","manufacturer":"LTS Lohmann Therapie-Systeme AG","form":"4.5mg:10cm²*7贴","pack":"盒","batchNumber":"","memberPrice":"84.00","originalPrice":"84.00","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"1","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"1","insuranceCode":"","totalAmount":"84.00","directAmount":"0","activityAmount":"42","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":{"activityId":"","requestNo":"","activityAmount":"0","activityType":"0","activityName":""},"activityName":"","itemAttr":{"id":"0","attrs":"0,1,3,31027,30003,31061,31080,31064,31083,31227,31055","cates":"0,44017,44018,2"},"giftDrug":{"itemUuid":"","goodsNo":"","internalId":"","internalIdList":"","selectFlag":"1","goodsType":"","goodsSubType":"0","rxFlag":"0","infusionFlag":"0","unitPrice":"0","afterActivityUnitPrice":"0","quantity":"0","merchantId":"0","storeId":"0","belongInfusionMerchantId":"0","belongInfusionStoreId":"0","commonName":"","realName":"","tradeCode":"","image":"","approvalNumber":"","manufacturer":"","form":"","pack":"","batchNumber":"0","memberPrice":"0","originalPrice":"0","productId":"0","fromItemInternalId":"","isRule":"0","isDtp":"0","productionDate":"","expireDate":"","buyGifts":"0","isSelectActivity":"0","insuranceCode":"","totalAmount":"0","directAmount":"0","activityAmount":"0","discountAmount":"0","couponAmount":"0","promoteCouponAmount":"0","averageAmount":"0","activity":"","activityName":"","itemAttr":"","giftDrug":"","isHasActivity":"0","weight":"0"},"isHasActivity":"0","weight":"0"}],"amounts":[{"type":"2","name":"权益抵扣","resourceName":"","originAmount":"0.00","amount":"0.00"},{"type":"3","name":"平台活动","resourceName":"tq平台活动111","originAmount":"42.00","amount":"42.00"}],"allDiscountAmount":"42.00","saleAmount":"42.00","allDrugDiscountAmount":"42.00","allDrugSaleAmount":"42.00","isHasDtp":"1","services":[],"drugUser":{"drugUserId":"101","name":"樊战岗","idCard":"610523199201086936","mobile":"18354299687"},"businessStartTime":"08:30","businessEndTime":"17:30","storeStatus":"0","storeTimeStatus":"2","storeOpenTime":"0","storeTime":"0","merchantId":"159798","storeId":"159932","channel":"2","orderMethod":"14","assistantMemberId":"0","assistantId":"0","cardId":"","outActivityId":"","feeCardId":"","feeAmount":"0.00","equityUuid":"","equityIds":[],"equityName":"","coupon":{"couponId":"","cardId":"","couponAmount":"0","couponType":"0","schemeId":""},"eshopConfig":{"isUseEquity":"1","isUsePromoteCoupon":"1","isUseCoupon":"1","isUseActivity":"1","isUseFeeCoupon":"1","isUseOutActivity":"1"},"isShowUnionMember":"-1","orderNo":"","mainOrderNo":"","remark":"","isNeedIdentify":"0","isNeedTimelyDistribution":"1","orderAreaLimit":"0","requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","isUpdateRemark":"0","longitude":"","latitude":""},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(OrderUpdatePreOrderRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易5")
	@allure.severity("blocker")
	def test_fzg_drugapp_021(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		RxRxTabListRes = bkw.drugappApi_RxRxTabList({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(RxRxTabListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易6")
	@allure.severity("blocker")
	def test_fzg_drugapp_022(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		OrderInitRes = bkw.drugappApi_OrderInit({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(OrderInitRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易7")
	@allure.severity("blocker")
	def test_fzg_drugapp_023(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		DrugUserListRes = bkw.drugappApi_DrugUserList({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(DrugUserListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易8")
	@allure.severity("blocker")
	def test_fzg_drugapp_024(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		DrugUserDetailRes = bkw.drugappApi_DrugUserDetail({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"drugUserId":"101"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(DrugUserDetailRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易9")
	@allure.severity("blocker")
	def test_fzg_drugapp_025(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		DrugUserAddRes = bkw.drugappApi_DrugUserAdd({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"name":"樊","idCard":"123","mobile":13211111111,"relation":"朋友","actionType":"1","id":"","requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","kidney":"正常","liver":"正常","allergic":"无","anamnesis":"无","gestational":"无"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(DrugUserAddRes,[["errno"]])
		# 读取yaml里errorno
		# errorno1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno1")
		errorno1 = "6500500"
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno1)

	@allure.feature("好药交易10")
	@allure.severity("blocker")
	def test_fzg_drugapp_026(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		RxApplyRxRes = bkw.drugappApi_RxApplyRx({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"prescriptionPhoto":["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/bi0vu5ves9fv732i1fnmmck654.png"],"offLineApply":{"userName":"樊战岗","userMobile":"18354299687","prescriptionPhoto":["http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.app/bi0vu5ves9fv732i1fnmmck654.png"]},"type":2,"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4","orderNo":"","drugUserId":"101"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(RxApplyRxRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易11")
	@allure.severity("blocker")
	def test_fzg_drugapp_027(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		OrderCreateOrderRes = bkw.drugappApi_OrderCreateOrder({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"requestNo":"3f714ab0b0e0021794b6dcead79ca0b4"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(OrderCreateOrderRes,[["errno"]])
		# 读取yaml里errorno
		errorno2 = "6500001"
			#ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno2")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno2)

	@allure.feature("好药交易12")
	@allure.severity("blocker")
	def test_fzg_drugapp_028(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		OrderPreDetailRes = bkw.drugappApi_OrderPreDetail({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"mainOrderNo":"92050601603437460218"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(OrderPreDetailRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("好药交易13")
	@allure.severity("blocker")
	def test_fzg_drugapp_029(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		OrderRxUrlRes = bkw.drugappApi_OrderRxUrl({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+ wechatToken},"parma":{},"data":{"orderNo":"92050611603437470215","mainOrderNo":"92050601603437460218"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(OrderRxUrlRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商1")
	@allure.severity("blocker")
	def test_fzg_drugapp_030(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口8
		ApiDrugCategoryRes = bkw.drugappApi_ApiDrugCategory({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"page":1,"searchSource":1,"title":"","sortField":2,"sortType":2,"searchContent":"","addHistory":"0","isAccurate":"0","location":"116.397309,39.909473","storeId":"","specializeSearch":"","nearbyStores":True,"supplyEshop":"1","isGather":"1","showDrugName":"0"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiDrugCategoryRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商2")
	@allure.severity("blocker")
	def test_fzg_drugapp_031(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiCartAddCartRes = bkw.drugappApi_ApiCartAddCart({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"products":[{"scene":"1","isPreTime":"","sourceTradeCode":"312a4cb705b3d2dc71b275d4dfb90ef3","showName":"百康药房抽取式面巾纸","shops":[{"isColdChain":"0","isDtp":"0","tradeCode":"TANv%2B%2BcudXzsDTz9Y%2BgH8wlxWOY8","drugName":"","commonName":"百康药房抽取式面巾纸","brand":"","price":"9.00","img":[],"manufacturer":"河北满城县诚信纸业有限公司","approvalNumber":"冀卫消证字（2011）第0015号","description":"","isPrescription":False,"projectId":"2","merchantId":"36668","merchantStatus":"1","merchantIsPrescription":"1","storeId":"39827","shopStatus":"1","storeDomestic":"1","storeRider":"1","expressType":"0","storeOnlySelf":"1","storeDistance":"3.0","storeStartTime":"00:00:00","storeEndTime":"23:59:59","goodsInternalId":"9294","realTradeCode":"TANv%2B%2BcudXzsDTz9Y%2BgH8wlxWOY8","realCommonName":"百康药房抽取式面巾纸","form":"400张*3包","pack":"袋","sales":"175.0","channel":"2","distance":"1.1584331851680167","scene":"1","goodsSignType":"","goodsSubType":"19","goodsType":"1","isOffShelf":False,"attrs":[],"cates":[]}],"isColdChain":"0","isDtp":"0","tradeCode":"TANv%2B%2BcudXzsDTz9Y%2BgH8wlxWOY8","drugName":"","commonName":"百康药房抽取式面巾纸","brand":"","price":"9.00","img":[],"manufacturer":"河北满城县诚信纸业有限公司","approvalNumber":"冀卫消证字（2011）第0015号","description":"","isPrescription":False,"projectId":"2","merchantId":"0","merchantStatus":"1","merchantIsPrescription":"1","storeId":"0","shopStatus":"1","storeDomestic":"1","storeRider":"1","expressType":"0","storeOnlySelf":"1","storeDistance":"3.0","storeStartTime":"","storeEndTime":"","goodsInternalId":"","realTradeCode":"","realCommonName":"百康药房抽取式面巾纸","form":"400张*3包","pack":"袋","sales":"175","channel":"2","distance":"1.1584331851680167","goodsSignType":"","goodsSubType":"19","goodsType":"1","isOffShelf":False,"attrs":[],"cates":[],"quantity":1}],"signCartText":"","location":"116.397309,39.909473"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiCartAddCartRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商3")
	@allure.severity("blocker")
	def test_fzg_drugapp_032(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiSearchTermsRes = bkw.drugappApi_ApiSearchTerms({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"terms":"感冒发烧"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiSearchTermsRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商4")
	@allure.severity("blocker")
	def test_fzg_drugapp_033(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiSearchAssociateListRes = bkw.drugappApi_ApiSearchAssociateList({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"text":"感冒"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiSearchAssociateListRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商5")
	@allure.severity("blocker")
	def test_fzg_drugapp_034(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiDrugSearchRes = bkw.drugappApi_ApiDrugSearch({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"page":1,"searchSource":"1","title":"销量","up":True,"sortField":2,"sortType":1,"searchContent":"四季感冒片","addHistory":"1","isAccurate":"1","location":"116.397309,39.909473","storeId":"","specializeSearch":"","nearbyStores":True,"supplyEshop":"1","isGather":"1","showDrugName":"0"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiDrugSearchRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商6")
	@allure.severity("blocker")
	def test_fzg_drugapp_035(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiMemberInfoRes = bkw.drugappApi_ApiMemberInfo({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiMemberInfoRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商7")
	@allure.severity("blocker")
	def test_fzg_drugapp_036(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiUtilGetExpressRuleRes = bkw.drugappApi_ApiUtilGetExpressRule({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiUtilGetExpressRuleRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商8")
	@allure.severity("blocker")
	def test_fzg_drugapp_037(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiUtilGetExpressRuleRes = bkw.drugappApi_ApiUtilGetExpressRule({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiUtilGetExpressRuleRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商9")
	@allure.severity("blocker")
	def test_fzg_drugapp_038(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiActivityTemporaryActivityRes = bkw.drugappApi_ApiActivityTemporaryActivity({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"category":"3"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiActivityTemporaryActivityRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商10")
	@allure.severity("blocker")
	def test_fzg_drugapp_039(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiActivityIssueCouponRes = bkw.drugappApi_ApiActivityIssueCoupon({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"type":"1","subStationId":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiActivityIssueCouponRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商11")
	@allure.severity("blocker")
	def test_fzg_drugapp_040(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiUtilGetNearestStoreRes = bkw.drugappApi_ApiUtilGetNearestStore({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"locations":"116.397309,39.909473","subStationId":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiUtilGetNearestStoreRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商12")
	@allure.severity("blocker")
	def test_fzg_drugapp_045(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiMemberModalBoxNotifyRes = bkw.drugappApi_ApiMemberModalBoxNotify({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"modal":"scanGuide"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiMemberModalBoxNotifyRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商13")
	@allure.severity("blocker")
	def test_fzg_drugapp_046(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiNoticeIndexRes = bkw.drugappApi_ApiNoticeIndex({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"locations":"116.397309,39.909473","merchantIdStr":"627,679,36668,688,36668,688,679,679,679","limit":1000},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiNoticeIndexRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商14")
	@allure.severity("blocker")
	def test_fzg_drugapp_047(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiBonusMerchantsRes = bkw.drugappApi_ApiBonusMerchants({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"stores":[{"distance":"803","channel":"2","storeId":"40460","merchantId":"627","partnerId":"0","storeName":"沙道大药房(直营)","partnerName":"恩施恒信","long":"109.566382","lat":"29.694174","startTime":"06:30:00","endTime":"22:00:00","isOpen":True,"storeAddress":"湖北省恩施土家族苗族自治州宣恩县沙道沟镇东升宾馆酉发商场(中心店)","isOffline":"0"},{"distance":"844","channel":"2","storeId":"6780","merchantId":"679","partnerId":"0","storeName":"天地","partnerName":"北京金象","long":"116.399404","lat":"39.902066","startTime":"10:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"东长安街1号","isOffline":"0"},{"distance":"1160","channel":"2","storeId":"39827","merchantId":"36668","partnerId":"0","storeName":"前门分店","partnerName":"北京高远百康","long":"116.392221","lat":"39.899814","startTime":"00:00:00","endTime":"23:59:59","isOpen":True,"storeAddress":"北京市西城区前门西大街正阳市场4号楼北京市皓阳宾馆一层3号","isOffline":"0"},{"distance":"1496","channel":"2","storeId":"7584","merchantId":"688","partnerId":"0","storeName":"绒线胡同","partnerName":"北京国大","long":"116.369351","lat":"39.896281","startTime":"08:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"西绒线胡同6号楼","isOffline":"0"},{"distance":"2091","channel":"2","storeId":"39899","merchantId":"36668","partnerId":"0","storeName":"珠市口店","partnerName":"北京高远百康","long":"116.403250","lat":"39.891254","startTime":"08:00:00","endTime":"22:00:00","isOpen":True,"storeAddress":"珠市口东大街世纪天鼎东侧百康药房107、108号","isOffline":"0"},{"distance":"2127","channel":"2","storeId":"7570","merchantId":"688","partnerId":"0","storeName":"崇文","partnerName":"北京国大","long":"116.402497","lat":"39.887940","startTime":"00:00:00","endTime":"23:59:59","isOpen":True,"storeAddress":"西城区兴隆都市馨园8号楼","isOffline":"0"},{"distance":"2245","channel":"2","storeId":"6767","merchantId":"679","partnerId":"0","storeName":"地外","partnerName":"北京金象","long":"116.395932","lat":"39.934145","startTime":"08:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"中国北京市西城区地安门外大街139号","isOffline":"0"},{"distance":"2285","channel":"2","storeId":"6760","merchantId":"679","partnerId":"0","storeName":"崇文门","partnerName":"北京金象","long":"116.404983","lat":"39.889805","startTime":"08:30:00","endTime":"22:00:00","isOpen":True,"storeAddress":"崇文门外大街3号","isOffline":"0"},{"distance":"2715","channel":"2","storeId":"6774","merchantId":"679","partnerId":"0","storeName":"和平门","partnerName":"北京金象","long":"116.370468","lat":"39.896403","startTime":"08:00:00","endTime":"20:00:00","isOpen":True,"storeAddress":"北新华街29号","isOffline":"0"}],"limit":1000},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiBonusMerchantsRes,[["errno"]])
		# 读取yaml里errorno
		errorno = "120008"
		#ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商15")
	@allure.severity("blocker")
	def test_fzg_drugapp_048(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiUtilWeatherRes = bkw.drugappApi_ApiUtilWeather({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"city":"北京市北京市"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiUtilWeatherRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商16")
	@allure.severity("blocker")
	def test_fzg_drugapp_049(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiCartCheckCartRes = bkw.drugappApi_ApiCartCheckCart({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"location":"116.397309,39.909473","specializeSearch":"","supplyEshop":"1","showDrugName":"0","signCartText":""},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiCartCheckCartRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商17")
	@allure.severity("blocker")
	def test_fzg_drugapp_050(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiActivityGetActivityIndexRes = bkw.drugappApi_ApiActivityGetActivityIndex({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"locations":"116.397309,39.909473","subStationId":"1"},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiActivityGetActivityIndexRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)

	@allure.feature("电商18")
	@allure.severity("blocker")
	def test_fzg_drugapp_051(self):
		# 读取yaml文件
		#yamlFile = ckw.CommonKeyWord().Yaml_Read("/Users/a5555555/autotest/automan/TestFile/fanzhangang/fzgtest.yaml")
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/fanzhangang/fzgtest.yaml")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 调取好药交易页1接口
		ApiUtilFindSubstationConfigRes = bkw.drugappApi_ApiUtilFindSubstationConfig({"header":{"Content-Type": "application/json", "Authorization":"Bearer "+wechatToken},"parma":{},"data":{"subStationId":""},"env":env},"dict")
		# json获取返回值
		errno = ckw.CommonKeyWord().Json_GetJsonValue(ApiUtilFindSubstationConfigRes,[["errno"]])
		# 读取yaml里errorno
		errorno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"errorno")
		# 断言errorno
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,errorno)
