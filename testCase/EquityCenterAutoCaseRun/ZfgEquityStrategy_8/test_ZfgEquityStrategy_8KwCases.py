# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

Authorization = "1"
token_2 = "2"

class Test_ZfgEquityStrategy_8:

	@allure.feature("非合并分组-分组金额每日限制-面额卡领取失败场景-电子码领取方式")
	@allure.severity("blocker")
	def test_zfg_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
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
		global Authorization
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
		global token_2
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
	def test_zfg_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
	def test_zfg_0003(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 领取权益信息提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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
	def test_zfg_0004(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
	def test_zfg_0005(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
	def test_zfg_0006(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
	def test_zfg_0007(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
	def test_zfg_0008(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件内公众号登录账户
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_8")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
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
		# 由于权益接收mbs消息存在延迟设定等待时间
		ckw.CommonKeyWord().Time_Sleep("2.0")
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
