# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_phone:

	@allure.feature("权益中心-预制数据清空数据")
	@allure.severity("blocker")
	def test_lm_0000(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# 读取yaml文件的预制数据sql
		uodateNmae = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"uodateNmae")
		# 读取yaml文件的预制数据sql
		updateEquity = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateEquity")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",uodateNmae)
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateEquity)
		# 打印当前sql到控制台
		ckw.CommonKeyWord().Print_ToControl("数据预制当前sql：",updateRadeemCode)

	@allure.feature("权益中心-合并面额卡激活（手机预分配）无限制成功")
	@allure.severity("blocker")
	def test_lm_0029(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day29 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day29")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0029用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0029用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day29)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前后台的认证
		ckw.CommonKeyWord().Print_ToControl("后台认证：",Authorization)
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day29)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day29,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 打印当前的公众号jwt
		ckw.CommonKeyWord().Print_ToControl("jwt：",jwt)
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
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机预分配）无限制重复激活失败")
	@allure.severity("blocker")
	def test_lm_0030(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day29 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day29")
		# lm_0030用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0030用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day29)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day29)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day29,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 重复提交激活
		erroData = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单日数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0031(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId31 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId31")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0031用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0031用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId31)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId31)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId31,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单日数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0032(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId32 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId34")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0032用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0032用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId32)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId32)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId32,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data1 = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 首次打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("首次提取的错误信息：",data1)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId32,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单日金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0033(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId33 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId33")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0033用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0033用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId33)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId33)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId33,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单日数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0034(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId34")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0034用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0034用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day1)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day1)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单月 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0035(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId35 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId35")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0035用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0035用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId35)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId35)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId35,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单月数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0036(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId36")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0036用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0036用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day2)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day2)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day2,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day2,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单月 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0037(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId37 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId37")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0037用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0037用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId37)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId37)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId37,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单月金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0038(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day5 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId38")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0038用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0038用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day5)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day5)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day5,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单年 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0039(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId39 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId39")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0039用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0039用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId39)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId39)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId39,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单年数量限制上限失败")
	@allure.severity("blocker")
	def test_lm_0040(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day7 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId40")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0040用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0040用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day7)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day7)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day7,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day7,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 读取单年数量上限激活断言
		limitErrono = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"limitErrono")
		# 打印读取的错误码
		ckw.CommonKeyWord().Print_ToControl("读取的断言预置：",limitErrono)
		# 打印权单年数量上限断言到日志
		ckw.CommonKeyWord().Print_ToLog("读取的断言预置：",limitErrono)
		# 权益激活断言执行
		assert ckw.CommonKeyWord().Assert_ObjAndObj(data,limitErrono)

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单年 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0041(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId41 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId41")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0041用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0041用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId41)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId41)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId41,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单年金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0042(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day9 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId422")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0042用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0042用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day9)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day9)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day9,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）终生 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0043(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId43 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId43")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0043用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0043用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId43)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId43)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId43,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）终生数量限制上限失败")
	@allure.severity("blocker")
	def test_lm_0044(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day11 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId44")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0044用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0044用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day11)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day11)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day11,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", updateRadeemCode)
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day11,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day11,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）终生 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0045(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId45 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId45")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0045用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0045用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId45)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId45)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId45,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）终生金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0046(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day13 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId46")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# 读取yaml文件的预制数据sql
		updateRadeemCode = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"updateRadeemCode")
		# 执行sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",updateRadeemCode)
		# lm_0046用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0046用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day13)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day13)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day13,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单日金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0047(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day19 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day19")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0047用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0047用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day19)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day19)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day19,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单日数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0048(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day20 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day20")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0048用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0048用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day20)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day20)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day20,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单月金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0049(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day21 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day21")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0049用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0049用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day21)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day21)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day21,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单月数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0050(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day22 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day22")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0050用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0050用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day22)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day22)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day22,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单年金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0051(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day23 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day23")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0051用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0051用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day23)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day23)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day23,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）单年数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0052(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day24 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day24")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0052用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0052用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day24)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day24)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day24,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）终身金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0053(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day25 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day25")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0053用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0053用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day25)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day25)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day25,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）终身数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0054(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day26 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day26")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0054用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0054用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day26)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day26)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day26,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）金额跟随项目领取成功")
	@allure.severity("blocker")
	def test_lm_0055(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId55 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId55")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0055用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0055用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId55)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId55)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId55,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（手机号预分配）数量跟随项目领取成功")
	@allure.severity("blocker")
	def test_lm_0056(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId56 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId56")
		# 读取yaml的权益领取手机号
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
		# lm_0056用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0056用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId56)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId56)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":mobiles,"verifyName":None,"verifyMobile":mobiles,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId56,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_5")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"mobile":mobiles,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
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
