# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_stagnation:

	@allure.feature("公众号-验证码登录")
	@allure.severity("blocker")
	def test_stagnation_statistic_0001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/XiaoWenyao/xwy.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobile")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录公众号发送图形验证码
		bkw.stagnationApi_LoginImageCaptcha({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile},"env":env},"dict")
		# 从redis提取验证码
		captcha = ckw.CommonKeyWord().Db_RedisGet({"host":"192.168.3.193","port":"6379","password":"uniondrug@123","db":"","key":"AUTH_IMAGE_CAPTCHA_15651711729"})
		# 打印图形验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("captcha:",captcha)
		# 登录公众号发送验证码
		captcha = bkw.stagnationApi_LoginSendCaptchaNew({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"captcha":captcha},"env":env},"dict")
		# 从数据库提取验证码-获取原始sql
		tmpSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# 从数据库提取验证码-修改sql where条件
		finSql = ckw.CommonKeyWord().Str_Replace(tmpSql,15651711729,mobile)
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",finSql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",finSql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"udtest.uniondrug.com","port":"6033","username":"test","password":"tset@321abc","database":"cn_uniondrug_module_sms","sql":finSql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",sqlRes)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",sqlRes)
		# 从数据库提取验证码-提取验证码01
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0],[["data"]])
		# 从数据库提取验证码-提取验证码02
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(captcha,[["sms","code"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：",captcha)
		# 打印验证码到日志
		ckw.CommonKeyWord().Print_ToLog("验证码：",captcha)
		# 登录-调取接口
		loginRes = bkw.stagnationApi_LoginLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":captcha,"channel": {}},"env":env},"dict")
		# 登录-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 将获取的token写入yaml文件
		token = bkw.yaml_write("./TestFile/XiaoWenyao/token.yaml")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 获取用户信息-调取接口
		StagnationUserUserInfo = bkw.stagnationApi_StagnationUserUserInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{},"env":env},"dict")
		# 提取接口返回memberId
		memberId = ckw.CommonKeyWord().Json_GetJsonValue(StagnationUserUserInfo,[["data","memberId"]])
		# 将获取的memberId写入yaml文件
		memberId = bkw.yaml_write("./TestFile/XiaoWenyao/token.yaml")
		# 打印memberId到控制台
		ckw.CommonKeyWord().Print_ToControl("memberId:",memberId)
		# 打印memberId到日志
		ckw.CommonKeyWord().Print_ToLog("memberId:",memberId)
		# 个人中心统计数据-调取接口
		StagnationUserStatistic = bkw.stagnationApi_StagnationUserStatistic({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"memberId":memberId},"env":env},"dict")
		# 提取接口返回报文errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(StagnationUserStatistic,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("errno:",errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("errno:",errno)
		# 读取yaml里个人中心数据统计断言
		Assert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Assert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("数据统计断言结果：",Assert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,Assert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("65.0")

	@allure.feature("公众号-验证码登录")
	@allure.severity("blocker")
	def test_stagnation_statistic_0002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/XiaoWenyao/xwy.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobile")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录公众号发送图形验证码
		bkw.stagnationApi_LoginImageCaptcha({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile},"env":env},"dict")
		# 从redis提取验证码
		captcha = ckw.CommonKeyWord().Db_RedisGet({"host":"192.168.3.193","port":"6379","password":"uniondrug@123","db":"","key":"AUTH_IMAGE_CAPTCHA_15651711729"})
		# 打印图形验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("captcha:",captcha)
		# 登录公众号发送验证码
		captcha = bkw.stagnationApi_LoginSendCaptchaNew({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"captcha":captcha},"env":env},"dict")
		# 从数据库提取验证码-获取原始sql
		tmpSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# 从数据库提取验证码-修改sql where条件
		finSql = ckw.CommonKeyWord().Str_Replace(tmpSql,15651711729,mobile)
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",finSql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",finSql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"udtest.uniondrug.com","port":"6033","username":"test","password":"tset@321abc","database":"cn_uniondrug_module_sms","sql":finSql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",sqlRes)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",sqlRes)
		# 从数据库提取验证码-提取验证码01
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0],[["data"]])
		# 从数据库提取验证码-提取验证码02
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(captcha,[["sms","code"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：",captcha)
		# 打印验证码到日志
		ckw.CommonKeyWord().Print_ToLog("验证码：",captcha)
		# 登录-调取接口
		loginRes = bkw.stagnationApi_LoginLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":captcha,"channel": {}},"env":env},"dict")
		# 登录-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 获取用户信息-调取接口
		StagnationUserUserInfo = bkw.stagnationApi_StagnationUserUserInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{},"env":env},"dict")
		# 提取接口返回memberId
		memberId = ckw.CommonKeyWord().Json_GetJsonValue(StagnationUserUserInfo,[["data","memberId"]])
		# 打印memberId到控制台
		ckw.CommonKeyWord().Print_ToControl("memberId:",memberId)
		# 打印memberId到日志
		ckw.CommonKeyWord().Print_ToLog("memberId:",memberId)
		# 发放记录查询-调取接口
		StagnationUserRecordPaging = bkw.stagnationApi_StagnationUserRecordPaging({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"memberId":memberId,"date": "","status": "1","equityNo": "","note": "","page": "1","limit": "10"},"env":env},"dict")
		# 提取接口返回报文errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(StagnationUserRecordPaging,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("errno:",errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("errno:",errno)
		# 读取yaml里个人中心数据统计断言
		Assert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Assert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("数据统计断言结果：",Assert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,Assert)
