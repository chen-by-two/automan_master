# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class demo_Test_Unify:

	@allure.feature("统一交易下单")
	@allure.severity("blocker")
	def test_UnifyBuyProductByEquity(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobile")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml里skuNo
		skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"skuNo1")
		# 读取yaml里equityNo
		equityNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"equityNo")
		# 登录发送验证码
		bkw.authApi_LoginSendCaptcha({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile},"env":env},"dict")
		# 从数据库提取验证码-获取原始sql
		tmpSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# 从数据库提取验证码-修改sql where条件
		finSql = ckw.CommonKeyWord().Str_Replace(tmpSql,15005150023,mobile)
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",finSql,"2212.0","kkwk")
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",finSql,"2213.0","wwq","222.0")
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"582959f06c18d.sh.cdb.myqcloud.com","port":"3712","username":"develop","password":"develop123","database":"cn_uniondrug_module_sms","sql":finSql})
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
		# 登录获取token-调取接口
		loginRes = bkw.authApi_LoginLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":captcha},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 商品详情页获取waterNo-调取接口
		prdDetRes = bkw.goodCenterApi_UnifyproductDetails({"header":{},"parma":{},"data":{"skuNo":skuNo,"channel":"8","channelId":0},"env":env},"dict")
		# 商品详情页获取waterNo-提取waterNo
		waterNo = ckw.CommonKeyWord().Json_GetJsonValue(prdDetRes,[["data","waterNo"]])
		# 打印waterNo到控制台
		ckw.CommonKeyWord().Print_ToControl("waterNo：",waterNo)
		# 打印waterNo到日志
		ckw.CommonKeyWord().Print_ToLog("waterNo：",waterNo)
		# 获取时间戳
		timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 等一秒
		ckw.CommonKeyWord().Time_Sleep("1.0")
		# 创建确认单获取confirmNo-调取接口
		confCre = bkw.orderCenterApi_UnifyorderConfirmCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+token},"parma":{},"data":{"skuNos":[skuNo],"requestNo":timeStamp,"channel":"2","saleMerchantId":"539","saleStoreId":"74596","assistantId":0,"shareMemberId":0,"commissionNo":"","partnerMerchantId":131389,"partnerOpenId":"81091692a7c9c85dd987c161f05e","channelId":"0","orderSource":0},"env":env},"dict")
		# 创建确认单获取confirmNo-提取confirmNo
		confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(confCre,[["data","confirmNo"]])
		# 打印confirmNo到控制台
		ckw.CommonKeyWord().Print_ToControl("confirmNo：",confirmNo)
		# 打印confirmNo到日志
		ckw.CommonKeyWord().Print_ToLog("confirmNo：",confirmNo)
		# 获取可用权益-调取接口
		mebEquQue = bkw.equityCenterApi_UnifyorderMemberEquityQuery({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+token},"parma":{},"data":{"confirmNo":confirmNo},"env":env},"dict")
		# 获取可用权益-提取可用权益
		canUseEquity = ckw.CommonKeyWord().Json_GetJsonValue(mebEquQue,[["data","canUseds"]])
		# 指定权益卡
		equityCard = bkw.getEquityInfo_byCardNo(canUseEquity,equityNo)
		# 打印权益卡到控制台
		ckw.CommonKeyWord().Print_ToControl("权益卡：",equityCard)
		# 打印权益卡到日志
		ckw.CommonKeyWord().Print_ToLog("权益卡：",equityCard)
		# 给权益卡增加confirmNo
		chgEqu = ckw.CommonKeyWord().Dict_ModifyByKey(equityCard,"confirmNo",confirmNo)
		# 切换使用权益
		confEquChg = bkw.equityCenterApi_UnifyorderConfirmEquityChange({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+token},"parma":{},"data":chgEqu,"env":env},"dict")
		# 创建订单
		createRes = bkw.orderCenterApi_UnifyorderOrderCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+token},"parma":{},"data":{"confirmNo":confirmNo},"env":env},"dict")
		# 提取主订单号
		mainOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(createRes,[["data","shipment","mainOrderNo"]])
		# 支付
		bkw.orderCenterApi_UnifyorderCashierCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+token},"parma":{},"data":{"orderNo":mainOrderNo,"payMode":"CWXPAY"},"env":env},"dict")
		# 检查支付结果
		checkRes = bkw.orderCenterApi_UnifyorderCashierCheck({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer "+token},"parma":{},"data":{"first":False,"orderNo":mainOrderNo},"env":env},"dict")
		# 提取支付结果
		result = ckw.CommonKeyWord().Json_GetJsonValue(checkRes,[["success"]])
		# 提取支付结果
		tmp = ckw.CommonKeyWord().Var_NewStr("True")
		# 提取支付结果
		assert ckw.CommonKeyWord().Assert_ObjAndObj(str(result),tmp)
