# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_qrCodeLink:

	@allure.feature("权益中心-合并面额卡激活（链接二维码）无限制成功")
	@allure.severity("blocker")
	def test_lm_0000(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		updateEquity = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateEquity")
		# 数据预置清理1107820名下的权益卡
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", updateEquity)
	def test_lm_0001(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_1")
		# lm_0001用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0001用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_1)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_1)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "jwt")
		# 读取yaml文件公众号登录的jwt
		mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobiles")
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
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey":cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）无限制重复激活失败")
	@allure.severity("blocker")
	def test_lm_0002(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_1")
		# lm_0002用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0002用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_1)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_1)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单日数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0003(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day")
		# lm_0003用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0003用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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
		#assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（电子码）单日数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0004(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day")
		# lm_0004用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0004用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单日金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0005(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day1")
		# lm_0005用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0005用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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
		#assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,successErrono)

	@allure.feature("权益中心-合并面额卡激活（电子码）单日金额限制外领取失败")
	@allure.severity("blocker")
	def test_lm_0006(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day1")
		# lm_0006用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0006用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day1,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单月 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0007(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day3 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day3")
		# lm_0007用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0007用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day3)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day3)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day3,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单月数量领取上限失败")
	@allure.severity("blocker")
	def test_lm_0008(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day2")
		# lm_0008用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0008用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day2,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day2,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单月 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0009(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day3 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day3")
		# lm_0009用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0009用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day3)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day3)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day3,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单月金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0010(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day5 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day5")
		# lm_0010用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0010用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day5,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单年 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0011(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day6 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day6")
		# lm_0011用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0011用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day6)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day6)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day6,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单年数量限制上限失败")
	@allure.severity("blocker")
	def test_lm_0012(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day7 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day7")
		# lm_0012用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0012用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day7,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day7,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单年 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0013(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day8 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day8")
		# lm_0013用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0013用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day8)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day8)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day8,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单年金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0014(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day9 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day9")
		# lm_0014用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0014用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day9,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）终生 数量限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0015(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day10 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day10")
		# lm_0015用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0015用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day10)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day10)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day10,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）终生数量限制上限失败")
	@allure.severity("blocker")
	def test_lm_0016(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day11 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day11")
		# lm_0016用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0016用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day11,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day11,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）终生 金额限制内领取成功")
	@allure.severity("blocker")
	def test_lm_0017(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day12 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day12")
		# lm_0017用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0017用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day12)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day12)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day12,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）终生金额限制上限失败")
	@allure.severity("blocker")
	def test_lm_0018(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day13 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day13")
		# lm_0018用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0018用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day13,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单日金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0019(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day19 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day19")
		# lm_0019用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0019用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day19,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单日数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0020(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day20 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day20")
		# lm_0020用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0020用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day20,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day20,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		errolimit = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单月金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0021(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day21 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day21")
		# lm_0021用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0021用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day21,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单月数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0022(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day22 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day22")
		# lm_0022用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0022用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day22,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day22,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单年金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0023(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day23 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day23")
		# lm_0023用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0023用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day23,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）单年数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0024(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day24 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day24")
		# lm_0024用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0024用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day24,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day24,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）终身金额优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0025(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day25 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day25")
		# lm_0025用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0025用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day25,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）终身数量优先到达限制领取失败")
	@allure.severity("blocker")
	def test_lm_0026(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day26 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day26")
		# lm_0026用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0026用例：")
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
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day26,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
		# 激活Detail接口
		bkw.thePublicApi_VProjectUserDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 激活NewActivate接口
		data = bkw.thePublicApi_VEquityNewActivate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"channel":channel,"sourceType":"wx"},"env":envt},"dict")
		# 打印提取的错误信息
		ckw.CommonKeyWord().Print_ToControl("提取的错误信息：",data)
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day26,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey1 = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey1)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		data = bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey1,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）金额跟随项目领取成功")
	@allure.severity("blocker")
	def test_lm_0027(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day27 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day27")
		# lm_0027用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0027用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day27)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day27)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day27,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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

	@allure.feature("权益中心-合并面额卡激活（电子码）数量跟随项目领取成功")
	@allure.severity("blocker")
	def test_lm_0028(self):
		# 打开yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/lm/lm1.yaml")
		# 读取yaml文件权益项目ID
		projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId_1")
		# 读取yaml文件权益分组ID
		groupId_day28 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"groupId_day28")
		# lm_0028用例开始打印
		ckw.CommonKeyWord().Print_ToControl("0028用例：")
		# 打印当前权益项目ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益项目ID：",projectId_1)
		# 打印当前权益项目ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益项目ID：",projectId_1)
		# 打印当前权益分组ID到控制台
		ckw.CommonKeyWord().Print_ToControl("当前权益分组ID：",groupId_day28)
		# 读取yaml文件的后台认证
		Authorization = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"Authorization")
		# 打印当前权益分组ID到日志
		ckw.CommonKeyWord().Print_ToLog("当前权益分组ID：",groupId_day28)
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 权益中心生成权益卡
		redeemadd = bkw.equityCenterApi_RedeemAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":Authorization},"parma":{},"data":{"cdKey":None,"userId":None,"name":None,"mobile":None,"verifyName":None,"verifyMobile":None,"verifyIdCard":None,"verifyKeyword1":None,"verifyKeyword2":None,"verifyKeyword3":None,"merchantId": "7","projectId": projectId_1,"groupId":groupId_day28,"customerId":None,"nominalValue":1.00,"nominalTimes":None,"oneTimeValue":None,"idCardType":"01"},"env":envt},"dict")
		# 提取权益中心权益电子兑换码
		cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd,[["data","verify","cdKey"]])
		# 打印提取权益中心权益电子兑换码到控制台
		ckw.CommonKeyWord().Print_ToControl("电子权益兑换码：",cdkey)
		# 读取yaml权益领取方式配置
		channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"channel_1")
		# 打印读取领取方式到控制台
		ckw.CommonKeyWord().Print_ToControl("当前领取方式：",channel)
		# 读取yaml文件公众号登录的jwt
		jwt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"jwt")
		# 激活check接口
		bkw.thePublicApi_VProjectUserCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token_2},"parma":{},"data":{"cdKey": cdkey,"channel":channel},"env":envt},"dict")
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
