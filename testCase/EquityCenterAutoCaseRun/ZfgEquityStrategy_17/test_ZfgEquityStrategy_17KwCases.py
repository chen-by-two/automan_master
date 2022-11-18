# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

Authorization = "1"
token_2 = "2"

class Test_ZfgEquityStrategy_17:

	@allure.feature("鉴权数据全局变量")
	@allure.severity("blocker")
	def test_zfg_0001(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml后台登录手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_16")
		# 读取yaml后台验证码初始化SQL
		updateCaptchaAll = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaAll")
		# 读取yaml后台验证码设定SQL
		updateCaptchaCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateCaptchaCode")
		# 读取yaml设定后台登录验证码
		LoginCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LoginCaptcha")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"LogintCaptchas")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前脚本运行环境域名：",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前脚本运行环境域名：",envt)
		# 执行后台登录验证码初始化SQL
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateCaptchaAll)
		# 执行后台登录验证码设定SQL
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
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_15922577484",LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json"},"parma":{},"data":{"mobile":mobiles,"code":LogintCaptchas},"env":envt},"dict")
		# 公众号登录token提取鉴权
		global token_2
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin,[["data","token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:",token_2)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-电子码")
	@allure.severity("blocker")
	def test_zfg_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_129")
		# 运营后台权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
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
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{ "cdKey":cdKey,"channel":channel},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-雇主清单")
	@allure.severity("blocker")
	def test_zfg_0003(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_130")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 电子码领取权益提交
		vprojectusercheck = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"name":name,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-链接二维码-一码一权益")
	@allure.severity("blocker")
	def test_zfg_0004(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_131")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-链接二维码-通用码")
	@allure.severity("blocker")
	def test_zfg_0005(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_132")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_3")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserGroup({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"groupId":"UWg0NeGuO7eMQgYOVO3_-pxnnng","channel":channel},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-实体卡")
	@allure.severity("blocker")
	def test_zfg_0006(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_133")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_4")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-驻店宝-链接二维码")
	@allure.severity("blocker")
	def test_zfg_0007(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_134")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdKey,"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-驻店宝-指定手机号")
	@allure.severity("blocker")
	def test_zfg_0008(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_135")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_6")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)

	@allure.feature("非合并面额卡-项目数量终身限制内-领取成功验证-手机预分配")
	@allure.severity("blocker")
	def test_zfg_0009(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/FuGguang/ZfgEquityStrategy.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 读取yaml公众号登录手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles_17")
		# 读取yaml文件权益项目ID
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_10")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_136")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":name,"mobile":mobiles,"verifyName":name,"verifyMobile":mobiles,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId,"groupId":groupId,"customerId":None,"nominalValue":5,"nominalTimes":None,"oneTimeValue":None,"idCardType":"1"},"env":envt},"dict")
		# 生成权益卡后权益电子码提取
		cdKey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印cdKey到日志
		ckw.CommonKeyWord().Print_ToLog("当前领取权益cdKey:",cdKey)
		# 读取yaml文件权益领取方式
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印当前领取方式到日志
		ckw.CommonKeyWord().Print_ToLog("当前用户领取方式:",channel)
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 权益卡领取信息
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 权益卡领取激活
		vequitynewactivate = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 提取权益激活errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(vequitynewactivate,[["errno"]])
		# 打印提取errno到日志
		ckw.CommonKeyWord().Print_ToLog("当前激活出参errno:",errno)
		# 读取yaml断言参数
		RightsActivation = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"RightsActivation")
		# 打印预置断言到日志
		ckw.CommonKeyWord().Print_ToLog("当前断言出参errno:",RightsActivation)
		# 断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,RightsActivation)
