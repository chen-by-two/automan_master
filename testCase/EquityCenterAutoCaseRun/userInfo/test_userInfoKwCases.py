# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_userInfo:

	@allure.feature("权益中心-预制数据清空数据")
	@allure.severity("blocker")
	def test_lm_0000(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# 打印当前sql到控制台
		ckw.CommonKeyWord().Print_ToControl("数据预制当前sql：",updateRadeemCode)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）无限制成功")
	@allure.severity("blocker")
	def test_lm_0057(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件权益分组ID
		groupId_57 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_57")
		# lm_0057用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0057用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_57)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_57)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":"416479","groupId":groupId_57,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
		# 读取yaml文件公众号登录验证码
		LogintCaptchas = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "LogintCaptchas")
		# 造公众号登录验证码
		ckw.CommonKeyWord().Db_ConfRedisSet("test_redis", "verifyCode_valid_17366352172", LogintCaptchas)
		ckw.CommonKeyWord().Print_ToControl("验证码：", LogintCaptchas)
		# 公众号登录
		Loginlogin = bkw.authApi_LoginLogin({"header": {"Content-Type": "application/json"}, "parma": {},
											 "data": {"mobile": mobiles, "code": LogintCaptchas}, "env": envt}, "dict")
		# 公众号登录token提取鉴权
		global token_2
		token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin, [["data", "token"]])
		# 打印公众号token到日志
		ckw.CommonKeyWord().Print_ToLog("公众号token:", token_2)
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）无限制重复激活失败")
	@allure.severity("blocker")
	def test_lm_0058(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId_57 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_57")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0058用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0058用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_57)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_57)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_2,"groupId":groupId_57,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 重复提交激活
		erroData = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",erroData)
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 读取权益重复激活断言
		repeatErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"repeatErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",repeatErrono)
		# 打印权益重复激活断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",repeatErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroData,repeatErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单日数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0059(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId59 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId599")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0059用例开始打印.
		ckw.CommonKeyWord().Print_ToControl("0059用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId59)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId59)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId59,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单日数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0060(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId59 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId59")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0060用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0060用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId59)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId59)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId59,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId59,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 等待
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单日数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单日数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单日金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0061(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId61 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId611")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0061用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0061用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId61)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId61)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId61,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单日金额限制外领取失败")
	@allure.severity("blocker")
	def test_lm_0062(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId61 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId61")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 当前时间
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间
		ckw.CommonKeyWord().Print_ToControl("时间：",time)
		# 等待
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", updateRadeemCode)
		# 打印当前sql到控制台
		ckw.CommonKeyWord().Print_ToControl("数据预制当前sql：", updateRadeemCode)
		# lm_0062用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0062用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId61)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId61)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId61,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_2,"groupId":groupId61,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 等待
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单日数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"userInfoErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单日数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 等待
		ckw.CommonKeyWord().Time_Sleep("5.0")
		# 权益激活断言执行
		#assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单月 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0063(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId63 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId633")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0063用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0063用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId63)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId63)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId63,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}

,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单月数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0064(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId644")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", updateRadeemCode)
		# lm_0064用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0064用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}

,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}

,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单月数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单月数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单月 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0065(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId65 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId611")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0065用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0065用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId65)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId65)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId65,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单月金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0066(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId66")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0066用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0066用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 等待
		ckw.CommonKeyWord().Time_Sleep("5.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单月数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单月数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单年 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0067(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId67 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId633")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0067用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0067用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId67)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId67)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId67,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单年数量限制上限失败")
	@allure.severity("blocker")
	def test_lm_0068(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId68")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# 打印当前sql到控制台
		ckw.CommonKeyWord().Print_ToControl("数据预制当前sql：",updateRadeemCode)
		# lm_0068用例开始打印
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", updateRadeemCode)
		# 打印当前sql到控制台
		ckw.CommonKeyWord().Print_ToControl("数据预制当前sql：", updateRadeemCode)
		ckw.CommonKeyWord().Print_ToControl("0068用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_2,"groupId":groupId,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 等待3s
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单年数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"userInfoErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单年数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 等待3s
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# 权益激活断言执行
		# assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单年 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0069(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId69")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0069用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0069用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单年金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0070(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId70 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId70")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0070用例开始打印
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", updateRadeemCode)
		# 打印当前sql到控制台
		ckw.CommonKeyWord().Print_ToControl("数据预制当前sql：", updateRadeemCode)
		ckw.CommonKeyWord().Print_ToControl("0070用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId70)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId70)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId70,"customerId":None,"nominalValue":"99.00","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 等待
		ckw.CommonKeyWord().Time_Sleep("3.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单年金额上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单年金额上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）终生 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0071(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId71 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId71")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0071用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0071用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId71)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId71)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId71,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）终生数量限制上限失败")
	@allure.severity("blocker")
	def test_lm_0072(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId72")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0072用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0072用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 当前时间
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间
		ckw.CommonKeyWord().Print_ToControl("时间：",time)
		# 等待
		ckw.CommonKeyWord().Time_Sleep("5.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）终生 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0073(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId733")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0073用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0073用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）终生金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0074(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId74")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0074用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0074用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 当前时间
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间
		ckw.CommonKeyWord().Print_ToControl("时间：",time)
		# 等待
		ckw.CommonKeyWord().Time_Sleep("5.0")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生金额上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生金额上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单日金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0075(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId75")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0075用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0075用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_2,"groupId":groupId,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生金额上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生金额上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单日数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0076(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId76")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0076用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0076用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		errolimit = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",errolimit)
		# 读取终生数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errolimit,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单月金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0077(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day21")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0077用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0077用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生金额上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生金额上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单月数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0078(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId78")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0078用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0078用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单年金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0079(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day23")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0079用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0079用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生金额上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生金额上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）单年数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0080(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day24")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0080用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0080用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）终身金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0081(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day25")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0081用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0081用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生金额上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生金额上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）终身数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0082(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day26")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0082用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0082用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取终生数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权终生数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）金额跟随项目领取成功")
	@allure.severity("blocker")
	def test_lm_0083(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId83")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0083用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0083用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（雇主清单）数量跟随项目领取成功")
	@allure.severity("blocker")
	def test_lm_0084(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_2")
		# 读取yaml文件权益分组ID
		groupId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId83")
		# 读取yaml文件姓名
		cardName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardName")
		# 读取yaml文件身份证
		cardNum = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"cardNum")
		# lm_0084用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0084用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_2)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_2)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":cardName,"mobile":None,"verifyName":cardName,"verifyMobile":None,"verifyIdCard":cardNum,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId":"7","projectId":projectId_2,"groupId":groupId,"customerId":None,"nominalValue":"0.10","nominalTimes":None,"oneTimeValue":None,"idCardType":"1"}
,"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_2")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"name":cardName,"idCardType":"1","idCard":cardNum,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel},"env":envt},"dict")
		# 提取激活成功错误码errno
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(data,[["errno"]])
		# 打印提取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("提取激活成功的错误码：",erroNo)
		# 读取权益激活错误码
		successErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"successErrono")
		# 打印读取激活成功的错误码
		ckw.CommonKeyWord().Print_ToControl("读取激活成功的错误码：",successErrono)
		# 接口返回错误码比对
		assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)
