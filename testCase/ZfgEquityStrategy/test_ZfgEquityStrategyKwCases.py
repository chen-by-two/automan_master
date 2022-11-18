# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_ZfgEquityStrategy:

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_1")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0002(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_2")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":"张勇","mobile":mobiles,"verifyName":"张勇","verifyMobile":mobiles,"verifyIdCard":"370782198002081135","verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":"张勇","idCardType":"1","idCard":"370782198002081135","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0003(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_3")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0004(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_4")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"RtD1O5xLx4PmvBoSsErjgLrR9Zg","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0005(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_5")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0006(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_6")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0007(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_7")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额终身限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0008(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_1")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_8")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15589788884",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0009(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_9")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":10,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0010(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_10")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":"袁江","mobile":mobiles,"verifyName":"袁江","verifyMobile":mobiles,"verifyIdCard":"512223197309102988","verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":"袁江","idCardType":"1","idCard":"512223197309102988","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0011(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_11")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0012(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_12")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"8_hXJ0olNOSxrWXnvqkuzF7ognk","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0013(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_13")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0014(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_14")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0015(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_15")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每年限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0016(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_2")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_16")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15923868392",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0017(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_17")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡（月限制防止报错）
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":10,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0018(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_18")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":"刘芬","mobile":mobiles,"verifyName":"刘芬","verifyMobile":mobiles,"verifyIdCard":"500224198804155443","verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":"刘芬","idCardType":"1","idCard":"500224198804155443","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0019(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_19")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0020(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_20")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"3EePAN1OzfiRh-oi2CsziF7qsVI","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0021(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_21")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0022(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_22")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0023(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_23")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每月限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0024(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_3")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_3")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_24")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_17725194406",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0025(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_25")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡（月限制防止报错）
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0026(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_26")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":"王力宏","mobile":mobiles,"verifyName":"王力宏","verifyMobile":mobiles,"verifyIdCard":"510223195704280038","verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":"王力宏","idCardType":"1","idCard":"510223195704280038","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0027(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_27")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0028(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_28")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"8lShhE1k1O9-VSiy_oN9QYKUtJU","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0029(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_29")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0030(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_30")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0031(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_31")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目金额每日限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0032(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_4")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_4")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_32")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15002319039",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0033(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_33")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":10,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0034(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_34")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0035(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_35")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0036(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_36")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"1-tdLKnBp9Pmxmgpm3cyqYUfhgY","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"1-tdLKnBp9Pmxmgpm3cyqYUfhgY","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0037(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_37")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0038(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_38")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0039(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_39")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额终身限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0040(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_5")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_40")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13667635241",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组每年终身限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0041(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_41")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":10,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0042(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_42")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0043(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_43")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0044(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_44")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"K-rDsrKgw4IC-oNfhAvsibdw8Ac","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"K-rDsrKgw4IC-oNfhAvsibdw8Ac","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0045(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_45")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0046(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_46")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0047(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_47")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每年限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0048(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_6")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_48")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13658396471",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0049(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_49")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0050(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_50")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0051(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_51")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0052(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_52")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"-N5lAMfWUBvfoUREZKI9A4eNg0k","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"-N5lAMfWUBvfoUREZKI9A4eNg0k","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0053(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_53")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0054(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_54")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0055(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_55")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每月限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0056(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_7")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_56")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13833848839",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0057(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_57")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0058(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_58")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0059(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_59")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0060(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_60")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"fDDGre3G8RkkJ1hjxi4mE2N_w_4","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"fDDGre3G8RkkJ1hjxi4mE2N_w_4","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0061(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_61")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0062(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_62")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0063(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_63")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0064(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_64")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15683885417",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0065(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_65")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0066(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_66")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0067(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_67")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0068(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_68")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"vbM8AC11O04vMzaKNPmV5Mj0nZE","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"vbM8AC11O04vMzaKNPmV5Mj0nZE","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0069(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_69")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0070(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_70")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0071(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_71")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量终身限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0072(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_9")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_72")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15823126331",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0073(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_73")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0074(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_74")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0075(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_75")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0076(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_76")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"vior_afIoM5qzlNhvirb5t_8cHk","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"vior_afIoM5qzlNhvirb5t_8cHk","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0077(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_77")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0078(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_78")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0079(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_79")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每年限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0080(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_10")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_80")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13368186912",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0081(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_81")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0082(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_82")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0083(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_83")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0084(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_84")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"GFvPnbWBzuvXyCNcJd2FxV-nKsc","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"GFvPnbWBzuvXyCNcJd2FxV-nKsc","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0085(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_85")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0086(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_86")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0087(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_87")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每月限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0088(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_11")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_88")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18523591942",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0089(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_89")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0090(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_90")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0091(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_91")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0092(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_92")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"ab0fPtHMa3AOuDl8UM4DOw2zEH4","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"ab0fPtHMa3AOuDl8UM4DOw2zEH4","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0093(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_93")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0094(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_94")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0095(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_95")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-分组数量每日限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0096(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_12")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_96")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13752844989",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0097(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_97")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 权益次卡领取激活
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-雇主清单领取方式")
	@allure.severity("blocker")
	def test_zfg_0098(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_98")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 当前领取用户name提取
		name = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","infoMember","name"]])
		# 当前领取用户cardNum提取
		cardNum = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","cardNum"]])
		# 打印当前领取用户name到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户姓名：",name)
		# 打印当前领取用户cardNum到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户身份证号：",cardNum)
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 雇主清单权益领取提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-连接二维码-一码一权益领取方式")
	@allure.severity("blocker")
	def test_zfg_0099(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_99")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-连接二维码-通用码领取方式")
	@allure.severity("blocker")
	def test_zfg_0100(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_100")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"sYcKflzlTTdNkrF_RdX2eiq64MQ","channel":channel},"env":envt},"dict")
		# 提交激活权益
		Rigres = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"sYcKflzlTTdNkrF_RdX2eiq64MQ","channel":channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-实物卡领取方式")
	@allure.severity("blocker")
	def test_zfg_0101(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_101")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-驻店宝-默认链接二维码领取方式")
	@allure.severity("blocker")
	def test_zfg_0102(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_102")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKeys,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdKey, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-驻店宝-指定手机号领取方式")
	@allure.severity("blocker")
	def test_zfg_0103(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_103")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)

	@allure.feature("非合并分组-项目数量终身限制-面额卡领取失败场景-手机预分配领取方式")
	@allure.severity("blocker")
	def test_zfg_0104(self):
		# 等待2S
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/zifuguang/PycharmProjects/automan/testFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内后台登录账户
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_13")
		# 读取yaml文件内初始化后台登录账户SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml文件内设定后台登录验证码SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml文件内后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 运行后台验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 运行设定后台验证码SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaCode)
		# 运营后台登录获取token
		ddmodbilelogin = bkw.authApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":LoginCaptcha},"env":envt},"dict")
		# 运营后台token提取
		token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin,[["data"]])
		# 运营后台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台token:",token_1)
		# 运营后台Authorization获取
		ddlogin = bkw.authApi_Ddlogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":token_1,"env":envt},"dict")
		# 运营后台Authorization提取
		Authorization = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin,[["data","token"]])
		# 运营后台Authorization打印到日志
		ckw.CommonKeyWord().Print_ToLog("运营后台Authorization:",Authorization)
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_5")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_104")
		# 打印权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID:",projectId)
		# 打印权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID:",groupId)
		# 运营后台权益中心生成权益卡
		redeemadds = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKeys = ckw.CommonKeyWord().Json_GetJsonValue(redeemadds,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKeys)
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_13436196867",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)
		# 获取公众号个人信息
		vmemberdetail = bkw.thePublicApi_VMemberDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Token "+token_2},"parma":{},"data":{},"env":envt},"dict")
		# 当前领取用户memberID提取
		memberid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","cards","memberId"]])
		# 当前领取用户account提取
		account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail,[["data","account"]])
		# 打印当前领取用户memberID到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的memberID:",memberid)
		# 打印当前领取用户account到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取用户的account:",account)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 领取权益手机号提交
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 获取当前权益信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提交激活权益
		bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":30,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile": mobiles, "channel": channel},"env":envt},"dict")
		# 读取yaml文件权益达到领取限制断言
		ReceiveFailureAssertion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"ReceiveFailureAssertion")
		# 打印领取权益接口出参到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取接口出参:",vprojectusercheck)
		# 打印权益领取达到限制断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言预置结果:",ReceiveFailureAssertion)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(vprojectusercheck,ReceiveFailureAssertion)
