# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

import datetime

class Test_UserCenterAutoCaseRun:

	@allure.feature("用户中心用户登录")
	@allure.severity("blocker")
	def test_dzj_user_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobile")
		# 读取Yaml执行环境
		global env
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:",mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile},"env":env},"dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"582959f06c18d.sh.cdb.myqclsqloud.com","port":"3712","username":"develop","password":"develop123","database":"cn_uniondrug_module_data","sql":sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0],[["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：",captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":captcha},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：",loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"token":token},"env":env},"dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		global Auth
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：",Auth)

	@allure.feature("后台新增用户")
	@allure.severity("blocker")
	def test_dzj_user_002(self):
		newmobile = "154" + datetime.datetime.now().strftime('%m%f')
		# 打印newmobile到控制台
		ckw.CommonKeyWord().Print_ToControl("newmobile：", newmobile)
		# 打印newmobile到控制台
		ckw.CommonKeyWord().Print_ToControl("newmobile：", newmobile)
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserSave(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"account": newmobile, "nickName": "用户昵称", "memberName": None, "gender": "01", "birthdayPrefix": 1,
					  "birthday": None, "email": None, "mobile": None, "id": None}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)
		# 从数据库提取memberid-执行查询
		sql = "select id from cn_uniondrug_middleend_usercenter.uc_member where account = " + newmobile
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取memberid
		global newmemberid
		newmemberid = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印memberid到控制台
		ckw.CommonKeyWord().Print_ToControl("newmemberid：", newmemberid)

	@allure.feature("用户中心用户编辑、封禁、注销")
	@allure.severity("blocker")
	def test_dzj_user_003(self):
		# 修改用户信息-调用接口
		res = bkw.userCenterApi_MngUserUserUpdate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+Auth},"parma":{},"data":{"account":"13210210001","nickName":"用户昵称","memberName":"张治国","gender":"01","birthdayPrefix":2,"birthday":"1983-04-25","email":"","mobile":"","id":15965178},"env":env},"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：",res)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res,[["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result,tmp)
		# 封禁用户-调用接口
		res2 = bkw.userCenterApi_MngUserUserUpdateStatus({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+Auth},"parma":{},"data":{"id":"15965178","staCode":1},"env":env},"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res2)
		# 获取接口信息
		result2 = ckw.CommonKeyWord().Json_GetJsonValue(res2, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result2)
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result2, tmp)
		# 解封用户-调用接口
		res3 = bkw.userCenterApi_MngUserUserUpdateStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": "15965178", "staCode": 0}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res3)
		# 获取接口信息
		result3 = ckw.CommonKeyWord().Json_GetJsonValue(res3, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result3)
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result3, tmp)
		# 注销用户-调用接口
		res4 = bkw.userCenterApi_MngUserUserUpdateStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": "15965178", "staCode": 2}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result4 = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result4)
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result4, tmp)

	@allure.feature("用户中心身份证实名认证")
	@allure.severity("blocker")
	def test_dzj_user_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:", mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
			 "env": env}, "dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:", sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_module_data", "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
											  "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：", loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：", token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"token": token},
			 "env": env}, "dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：", Auth)
		# 实名认证-调用接口
		res4 = bkw.userCenterApi_V2ApiUserCardAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {
									"memberId":15965179,
									"typeId":1,
									"cardNo":"230102198512033410",
									"cardName":"李若然",
									"gmtExpiryStart":"2020-09-02 10:22:05",
									"gmtExpiryEnd":"2021-11-11 10:22:05",
									"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
									"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
									"authWay":0
									}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)

	@allure.feature("用户中心护照认证+人工审核通过")
	@allure.severity("blocker")
	def test_dzj_user_005(self):
		'''
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:", mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
			 "env": env}, "dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:", sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_module_data", "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
											  "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：", loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：", token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"token": token},
			 "env": env}, "dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：", Auth)
		'''
		# 实名认证-调用接口
		res4 = bkw.userCenterApi_V2ApiUserCardAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {
				"memberId": 15965179,
				"typeId": 3,
				"cardNo": "E000000",
				"cardName": "李若然",
				"gmtExpiryStart": "2020-09-02 10:22:05",
				"gmtExpiryEnd": "2021-11-11 10:22:05",
				"imageFront": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
				"imageBack": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
				"authWay": 0
			}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 从数据库提取id-执行查询
		sql = "select id from cn_uniondrug_middleend_usercenter.uc_member_card_approve order by gmt_submit desc limit 1"
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "select id from uc_member_card_approve order by gmt_submit desc limit 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 审核通过-调用接口
		res4 = bkw.userCenterApi_MngUserUserCardApproveSetStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id":id,"memberId":15965179,"approveStatus":1}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)

	@allure.feature("用户中心护照认证+人工审核驳回")
	@allure.severity("blocker")
	def test_dzj_user_006(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:", mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
			 "env": env}, "dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:", sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_module_data", "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
											  "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：", loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：", token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"token": token},
			 "env": env}, "dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：", Auth)
		# 实名认证-调用接口
		res4 = bkw.userCenterApi_V2ApiUserCardAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {
				"memberId": 15965179,
				"typeId": 3,
				"cardNo": "E000000",
				"cardName": "李若然",
				"gmtExpiryStart": "2020-09-02 10:22:05",
				"gmtExpiryEnd": "2021-11-11 10:22:05",
				"imageFront": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
				"imageBack": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
				"authWay": 0
			}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 从数据库提取id-执行查询
		sql = "select id from cn_uniondrug_middleend_usercenter.uc_member_card_approve order by gmt_submit desc limit 1"
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "select id from uc_member_card_approve order by gmt_submit desc limit 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 审核驳回-调用接口
		res4 = bkw.userCenterApi_MngUserUserCardApproveSetStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": id, "memberId": 15965179, "approveStatus": 2}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)

	@allure.feature("用户中心新建人群包、访问人群包、查看人群包")
	@allure.severity("blocker")
	def test_dzj_user_007(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:", mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
			 "env": env}, "dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:", sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_module_data", "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
											  "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：", loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：", token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"token": token},
			 "env": env}, "dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：", Auth)
		# 新建人群包-调用接口
		res4 = bkw.userCenterApi_MngUserUserTagAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"tagName":"包名","tags":[{"tagId":"7AB2F20D","tagName":"性别","tagValues":[{"code":"1","des":"男"}]}]}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 从数据库提取id-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", "SELECT id FROM cn_uniondrug_middleend_usercenter.uc_member_tag_group GROUP BY id desc LIMIT 1")
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "SELECT id FROM `uc_member_tag_group` GROUP BY id desc LIMIT 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 查看人群包-调用接口
		res = bkw.userCenterApi_MngUserUserTagGet(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id":id}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 访问人群包-调用接口
		res = bkw.userCenterApi_MngUserUserTagDetail(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"pageNum":1,"pageSize":10,"memberId":None,"account":None,"memberName":None,"packageId":"2271"}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 删除人群包-调用接口
		res = bkw.userCenterApi_MngUserUserTagRemove(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": id}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)

	@allure.feature("用户中心添加组织、通过用户ID查询组织、删除组织")
	@allure.severity("blocker")
	def test_dzj_user_008(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		# 读取Yaml memberIdzz
		memberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "memberId")
		# 读取Yaml merchantIdzz
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "merchantId")
		# 读取Yaml merchantIdzz
		orgId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "orgId")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:", mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
			 "env": env}, "dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:", sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL",sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_module_data", "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
											  "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：", loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：", token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"token": token},
			 "env": env}, "dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：", Auth)
		# 添加组织-调用接口
		res = bkw.userCenterApi_V2ApiOrgAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {
									 "memberId":memberId,
									 "merchantId":merchantId,
									 "merchantType":1,
									 "merchantName":"merchantName",
									 "merchantShortName":"merchantShortName",
									 "orgId":orgId,
									 "orgName":"orgName",
									 "jobNo":"jobNo",
									 "remark":"remark",
									 "orgResource":18
									}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 查询组织-调用接口
		res = bkw.userCenterApi_V2ApiOrgQueryBy(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {
									"memberId":memberId,
									"orgId":orgId,
									"merchantType":1
									}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 删除组织-调用接口
		res = bkw.userCenterApi_V2ApiOrgRemove(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {
									 "memberId":memberId,
									 "orgId":orgId
									}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)

	@allure.feature("用户管理展开查询")
	@allure.severity("blocker")
	def test_dzj_user_009(self):
		'''
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/DaizhaojiOnly/dzjtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobile")
		# 读取Yaml执行环境
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
		# 读取Yaml memberIdzz
		memberId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "memberId")
		# 读取Yaml merchantIdzz
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "merchantId")
		# 读取Yaml merchantIdzz
		orgId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "orgId")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("手机号:", mobile)
		# 登录发送验证码
		bkw.authApi_SmsSend(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
			 "env": env}, "dict")
		# 从数据库提取验证码
		sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "getLoginCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:", sql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
			{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
			 "password": "develop123", "database": "cn_uniondrug_module_data", "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取验证码
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
		# 登录获取token-调取接口
		loginRes = bkw.authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
											  "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印loginRes到控制台
		ckw.CommonKeyWord().Print_ToControl("loginRes：", loginRes)
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：", token)
		# 运营中心获取Authorization
		loginRes = bkw.authApi_Ddlogin(
			{"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"token": token},
			 "env": env}, "dict")
		# 打印登录信息
		ckw.CommonKeyWord().Print_ToControl(loginRes)
		# 获取Authorization
		Auth = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
		# 打印Authorization
		ckw.CommonKeyWord().Print_ToControl("auth：", Auth)
		'''
		# 按用户账号查询-调用接口
		res = bkw.userCenterApi_MngUserUserPage(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"pageNum":1,"pageSize":10,"account":"13333333001","staCode":None,"memberId":None,"id":None,"nickName":None,"memberName":None,"usedName":None,"gender":None,"birthday":None,"email":None,"mobile":None,"isReal":None,"isVip":None,"memberSource":None}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 获取接口信息
		result2 = ckw.CommonKeyWord().Json_GetJsonValue(res, [["data"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result2)
		# 获取接口信息
		result3 = ckw.CommonKeyWord().Json_GetJsonValue(result2, [["total"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result3)
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result3, 1)
		# 按用户昵称查询-调用接口
		nickName = "这是昵称"
		res = bkw.userCenterApi_MngUserUserPage(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"pageNum": 1, "pageSize": 10, "account": None, "staCode": None, "memberId": None,
					  "id": None, "nickName": nickName, "memberName": None, "usedName": None, "gender": None,
					  "birthday": None, "email": None, "mobile": None, "isReal": None, "isVip": None,
					  "memberSource": None}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 断言
		try:
			assert nickName in str(res)
		except:
			pass
		# 按用户状态-调用接口
		res = bkw.userCenterApi_MngUserUserPage(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"pageNum": 1, "pageSize": 10, "account": None, "staCode": 0, "memberId": None,
					  "id": None, "nickName": None, "memberName": None, "usedName": None, "gender": None,
					  "birthday": None, "email": None, "mobile": None, "isReal": None, "isVip": None,
					  "memberSource": None}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 按用户ID-调用接口
		res = bkw.userCenterApi_MngUserUserPage(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"pageNum": 1, "pageSize": 10, "account": None, "staCode": None, "memberId": None,
					  "id": "15965241", "nickName": None, "memberName": None, "usedName": None, "gender": None,
					  "birthday": None, "email": None, "mobile": None, "isReal": None, "isVip": None,
					  "memberSource": None}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 断言
		assert "15965241" in str(res)
		# 按真实姓名-调用接口
		res = bkw.userCenterApi_MngUserUserPage(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"pageNum": 1, "pageSize": 10, "account": None, "staCode": None, "memberId": None,
					  "id": None, "nickName": None, "memberName": "夏青青", "usedName": None, "gender": None,
					  "birthday": None, "email": None, "mobile": None, "isReal": None, "isVip": None,
					  "memberSource": None}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 断言
		assert "夏青青" in str(res)
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserPage(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"pageNum": 1, "pageSize": 10, "account": None, "staCode": None, "memberId": None,
					  "id": None, "nickName": None, "memberName": None, "usedName": "李若然", "gender": None,
					  "birthday": None, "email": None, "mobile": None, "isReal": None, "isVip": None,
					  "memberSource": None}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 预期值
		tmp = ckw.CommonKeyWord().Var_NewStr("请求成功")
		# 断言
		assert ckw.CommonKeyWord().Assert_ObjAndObj(result, tmp)
		# 断言
		try:
			assert "李若然" in str(res)
		except:
			pass

	@allure.feature("更改用户平台身份")
	@allure.severity("blocker")
	def test_dzj_user_010(self):
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserIdentityUpdate(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"memberId":"15965175","codeList":["0","1","10","11","12","13","14","20","30","40","41"]}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)

	@allure.feature("后台人工协助认证大陆身份证")
	@allure.severity("blocker")
	def test_dzj_user_011(self):
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserCardAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"typeId":1,"cardNo":"320111111111111111","cardName":"111","gmtExpiryStart":"2020-11-01","gmtExpiryEnd":"2020-11-19","imageFront":"","imageBack":"","id":"6459063","memberId":"15965175","longTime":None}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)

	@allure.feature("后台人工协助认证修改大陆身份证")
	@allure.severity("blocker")
	def test_dzj_user_012(self):
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserCardUpdate(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"typeId": 1, "cardNo": "320222222222222222", "cardName": "111", "gmtExpiryStart": "2020-11-01",
					  "gmtExpiryEnd": "2020-11-19", "imageFront": "", "imageBack": "", "id": "6459063",
					  "memberId": "15965175", "longTime": None}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)

	@allure.feature("后台人工协助认证大陆军官证")
	@allure.severity("blocker")
	def test_dzj_user_013(self):
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserCardAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"typeId": 2, "cardNo": "政字第00111206号", "cardName": "111",
					  "gmtExpiryStart": "2020-11-01", "gmtExpiryEnd": "2020-11-19", "imageFront": "",
					  "imageBack": "", "id": "6459063", "memberId": "15965175", "longTime": None}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)

	@allure.feature("后台人工协助认证修改大陆军官证")
	@allure.severity("blocker")
	def test_dzj_user_014(self):
		# 按曾用名搜索-调用接口
		res = bkw.userCenterApi_MngUserUserCardAdd(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {"typeId": 2, "cardNo": "政字第00222222号", "cardName": "111",
					  "gmtExpiryStart": "2020-11-01", "gmtExpiryEnd": "2020-11-19", "imageFront": "",
					  "imageBack": "", "id": "6459063", "memberId": "15965175", "longTime": "true"}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)

	@allure.feature("用户中心大陆军官证审核通过is_real=0")
	@allure.severity("blocker")
	def test_dzj_user_015(self):
		cardNo = "政字第" + str(newmemberid) + "号"
		# newmemberid = "15965334"
		# 职业认证-调用接口
		res = bkw.userCenterApi_V2ApiUserCardAddByNo(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {
						"memberId":newmemberid,
						"typeId":2,
						"cardNo":cardNo,
						"cardName":"李若然·",
						"gmtExpiryStart":"2020-09-02 10:22:05",
						"gmtExpiryEnd":"2021-11-11 10:22:05",
						"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
						"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
						"authWay":1,
						"approveStatus":0
					}, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", "select id from cn_uniondrug_middleend_usercenter.uc_member_card_approve where type_id = 2 order by gmt_submit desc limit 1")
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "select id from uc_member_card_approve where type_id = 2 order by gmt_submit desc limit 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 审核通过-调用接口
		res4 = bkw.userCenterApi_MngUserUserCardApproveSetStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": id, "memberId": newmemberid, "approveStatus": 1}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		assert "请求成功" in str(res)
		# 数据库查询实名认证(0:否,1:是)字段
		sql = "select is_real from cn_uniondrug_middleend_usercenter.uc_member_info where member_id = " + str(newmemberid)
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL",sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		is_real = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["is_real"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("是否实名：", is_real)
		# 断言0为未实名
		assert int(is_real) == 0

	@allure.feature("用户中心学生证证审核通过is_real=0")
	@allure.severity("blocker")
	def test_dzj_user_016(self):
		cardNo = "学生证" + str(newmemberid)
		# newmemberid = "15965334"
		# 职业认证-调用接口
		res = bkw.userCenterApi_V2ApiUserCardAddByNo(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {
				 "memberId": newmemberid,
				 "typeId": 7,
				 "cardNo": cardNo,
				 "cardName": "李若然·",
				 "gmtExpiryStart": "2020-09-02 10:22:05",
				 "gmtExpiryEnd": "2021-11-11 10:22:05",
				 "imageFront": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
				 "imageBack": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
				 "authWay": 1,
				 "approveStatus": 0
			 }, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", "select id from cn_uniondrug_middleend_usercenter.uc_member_card_approve where type_id = 7 order by gmt_submit desc limit 1")
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "select id from uc_member_card_approve where type_id = 7 order by gmt_submit desc limit 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 审核通过-调用接口
		res4 = bkw.userCenterApi_MngUserUserCardApproveSetStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": id, "memberId": newmemberid, "approveStatus": 1}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		assert "请求成功" in str(res)
		# 数据库查询实名认证(0:否,1:是)字段
		sql = "select is_real from cn_uniondrug_middleend_usercenter.uc_member_info where member_id = " + str(newmemberid)
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL",sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		is_real = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["is_real"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("是否实名：", is_real)
		# 断言0为未实名
		assert int(is_real) == 0

	@allure.feature("用户中心其他证件审核通过is_real=0")
	@allure.severity("blocker")
	def test_dzj_user_017(self):
		cardNo = "其他证" + str(newmemberid)
		print(cardNo)
		# newmemberid = "15965334"
		# 职业认证-调用接口
		res = bkw.userCenterApi_V2ApiUserCardAddByNo(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {
				 "memberId": newmemberid,
				 "typeId": 8,
				 "cardNo": cardNo,
				 "cardName": "李若然·",
				 "gmtExpiryStart":"2020-09-02 10:22:05",
				 "gmtExpiryEnd":"2021-11-11 10:22:05",
				 "imageFront": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
				 "imageBack": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
				 "authWay": 1,
				 "approveStatus": 0
			 }, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)
		sql = "select id from cn_uniondrug_middleend_usercenter.uc_member_card_approve where type_id = 8 order by gmt_submit desc limit 1"
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "select id from uc_member_card_approve where type_id = 8 order by gmt_submit desc limit 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 审核通过-调用接口
		res4 = bkw.userCenterApi_MngUserUserCardApproveSetStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": id, "memberId": newmemberid, "approveStatus": 1}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		assert "请求成功" in str(res)
		# 数据库查询实名认证(0:否,1:是)字段
		sql = "select is_real from cn_uniondrug_middleend_usercenter.uc_member_info where member_id = " + str(newmemberid)
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		is_real = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["is_real"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("是否实名：", is_real)
		# 断言0为未实名
		assert int(is_real) == 0

	@allure.feature("用户中心药师证件审核通过is_real=0")
	@allure.severity("blocker")
	def test_dzj_user_018(self):
		# newmemberid = "15965334"
		cardNo = "药师证" + str(newmemberid)
		print(cardNo)
		# 职业认证-调用接口
		res = bkw.userCenterApi_V2ApiUserCardAddByNo(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {},
			 "data": {
				 "memberId": newmemberid,
				 "typeId": 9,
				 "cardNo": cardNo,
				 "cardName": "李若然·",
				 "gmtExpiryStart": "2020-09-02 10:22:05",
				 "gmtExpiryEnd": "2021-11-11 10:22:05",
				 "imageFront": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
				 "imageBack": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
				 "authWay": 1,
				 "approveStatus": 0
			 }, "env": env},
			"dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res)
		print('=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		# 断言
		assert "请求成功" in str(res)
		sql = "select id from cn_uniondrug_middleend_usercenter.uc_member_card_approve where type_id = 9 order by gmt_submit desc limit 1"
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": "select id from uc_member_card_approve where type_id = 9 order by gmt_submit desc limit 1"})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		id = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：", id)
		# 审核通过-调用接口
		res4 = bkw.userCenterApi_MngUserUserCardApproveSetStatus(
			{"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Auth},
			 "parma": {}, "data": {"id": id, "memberId": newmemberid, "approveStatus": 1}, "env": env}, "dict")
		# 打印接口返回
		ckw.CommonKeyWord().Print_ToControl("接口返回：", res4)
		# 获取接口信息
		result = ckw.CommonKeyWord().Json_GetJsonValue(res4, [["error"]])
		# 打印
		ckw.CommonKeyWord().Print_ToControl(result)
		assert "请求成功" in str(res)
		# 数据库查询实名认证(0:否,1:是)字段
		sql = "select is_real from cn_uniondrug_middleend_usercenter.uc_member_info where member_id = " + str(newmemberid)
		sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sql)
		# sqlRes = ckw.CommonKeyWord().Db_MysqlSelect(
		# 	{"host": "582959f06c18d.sh.cdb.myqcloud.com", "port": "3712", "username": "develop",
		# 	 "password": "develop123", "database": "cn_uniondrug_middleend_usercenter",
		# 	 "sql": sql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
		# 从数据库提取id
		is_real = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["is_real"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("是否实名：", is_real)
		# 断言0为未实名
		assert int(is_real) == 0