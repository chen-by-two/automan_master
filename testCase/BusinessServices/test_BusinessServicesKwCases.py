# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_BusinessServices:

	@allure.feature("商家服务平台-登录")
	@allure.severity("blocker")
	def test_BusinessServices_UserLogin_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Businessmobile")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录商家服务平台-调取接口
		UserLogin = bkw.BusinessServicesApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{
    "mobile":mobile,
    "password": "111111",
    "remember": "true"
},"env":env},"dict")
		# 获取后台的token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(UserLogin,[["data","token"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# token写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any("./TestFile/BusinessServices/token.yaml","token",token)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("首页-门店和店员数据")
	@allure.severity("blocker")
	def test_BusinessServices_MrchantStoreClerkCount_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 门店和店员数据-调取接口
		MrchantStoreClerkCount = bkw.BusinessServicesApi_MrchantStoreClerkCount({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "merchantId":merchantId
},"env":env},"dict")
		# 提取领取门店和店员数据成功返回
		MrchantStoreClerkCounterrno = ckw.CommonKeyWord().Json_GetJsonValue(MrchantStoreClerkCount,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MrchantStoreClerkCounterrno:",MrchantStoreClerkCounterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MrchantStoreClerkCounterrno:",MrchantStoreClerkCounterrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("断言结果：",Errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MrchantStoreClerkCounterrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("首页-经营数据（销售额）")
	@allure.severity("blocker")
	def test_BusinessServices_HomePageOperateData_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 经营数据（销售额）-调取接口
		HomePageOperateData = bkw.BusinessServicesApi_HomePageOperateData({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"type": "d",
    "merchantId":merchantId
},"env":env},"dict")
		# 提取经营数据（销售额）成功返回
		HomePageOperateDataerrno = ckw.CommonKeyWord().Json_GetJsonValue(HomePageOperateData,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("HomePageOperateDataerrno:",HomePageOperateDataerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("HomePageOperateDataerrno:",HomePageOperateDataerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(HomePageOperateDataerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("首页-月度门店Top5")
	@allure.severity("blocker")
	def test_BusinessServices_HomePageMonthStoreTop_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 读取yaml文件month
		month = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"month")
		# 月度门店Top5-调取接口
		MonthStoreTopData = bkw.BusinessServicesApi_HomePageMonthStoreTop({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"page": 1,
    "limit": 5,
    "merchantId":merchantId,
    "month": month
},"env":env},"dict")
		# 提取月度门店Top5成功返回
		MonthStoreToprrno = ckw.CommonKeyWord().Json_GetJsonValue(MonthStoreTopData,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MonthStoreToperrno:",MonthStoreToprrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MonthStoreToperrno:",MonthStoreToprrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("断言结果：",Errno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MonthStoreToprrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("首页-月度店员Top5")
	@allure.severity("blocker")
	def test_BusinessServices_HomePageMonthClerkTop_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 读取yaml文件month
		month = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"month")
		# 月度店员Top5-调取接口
		MonthClerkTop = bkw.BusinessServicesApi_HomePageMonthClerkTop({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"page": 1,
    "limit": 5,
    "merchantId":merchantId,
    "month": month
},"env":env},"dict")
		# 提取月度店员Top5成功返回
		MonthClerkToprrno = ckw.CommonKeyWord().Json_GetJsonValue(MonthClerkTop,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MonthClerkToperrno:",MonthClerkToprrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MonthClerkToperrno:",MonthClerkToprrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MonthClerkToprrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("首页-连锁数据质量")
	@allure.severity("blocker")
	def test_BusinessServices_merchantDataQuality_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 首页-连锁数据质量-调取接口
		MerchantDataQuality = bkw.BusinessServicesApi_HomePageMerchantDataQuality({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "merchantId":merchantId
},"env":env},"dict")
		# 提取首页-连锁数据质量成功返回
		MerchantDataQualityerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantDataQuality,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantDataQualityerrno:",MerchantDataQualityerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantDataQualityerrno:",MerchantDataQualityerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantDataQualityerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("强制等待")
	@allure.severity("blocker")
	def test_BusinessServices_HomePageGetBusinessInfo_001(self):
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("首页-今日数据")
	@allure.severity("blocker")
	def test_BusinessServices_HomePageTodayData_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 读取yaml文件month
		statisDate = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"statisDate")
		# 首页-今日数据-调取接口
		HomePageTodayData = bkw.BusinessServicesApi_HomePageTodayData({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "merchantId":merchantId,
    "statisDate": statisDate
},"env":env},"dict")
		# 提取首页-今日数据成功返回
		HomePageTodayDataerrno = ckw.CommonKeyWord().Json_GetJsonValue(HomePageTodayData,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("HomePageTodayDataerrno:",HomePageTodayDataerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("HomePageTodayDataerrno:",HomePageTodayDataerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(HomePageTodayDataerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("企业信息-企业信息")
	@allure.severity("blocker")
	def test_BusinessServices_MerchantInfo_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 企业信息-企业信息-调取接口
		MerchantInfo = bkw.BusinessServicesApi_MerchantInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
   "merchantId":merchantId
},"env":env},"dict")
		# 提取企业信息-企业信息成功返回
		MerchantInfoerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantInfo,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantInfoerrno:",MerchantInfoerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantInfoerrno:",MerchantInfoerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantInfoerrno,Errno)

	@allure.feature("是否已开通普惠3.0")
	@allure.severity("blocker")
	def test_BusinessServices_InclusiveCheckApply_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/Bussiness.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/BusinessServices/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件merchantId
		merchantId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchantId")
		# 是否已开通普惠3.0-调取接口
		InclusiveCheckApply = bkw.BusinessServicesApi_InclusiveCheckApply({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
   "merchantId":merchantId
},"env":env},"dict")
		# 提取领取是否已开通普惠3.0成功返回
		InclusiveCheckApplyerrno = ckw.CommonKeyWord().Json_GetJsonValue(InclusiveCheckApply,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InclusiveCheckApplyerrno:",InclusiveCheckApplyerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InclusiveCheckApplyerrno:",InclusiveCheckApplyerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InclusiveCheckApplyerrno,Errno)
