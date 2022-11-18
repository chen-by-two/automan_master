# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_financeBusiness:

	@allure.feature("连接公共数据数据库")
	@allure.severity("blocker")
	def test_lq_financedata_connect(self):
		# 定义全局变量financeDataDB
		global financeDataDB
		# 全局变量赋值
		financeDataDB = ckw.CommonKeyWord().Db_SshConfRCMysqlConnect("DATABASE_RC_cn_uds_fin_com")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("数据库连接成功返回：", financeDataDB)

	@allure.feature("商家-获取菜单权限")
	@allure.severity("blocker")
	def test_lq_financeBusiness_0001(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-mobile
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile")
		# 读取yaml文件-password
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"password")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名",envt)
		# 登录商家服务平台
		PasswordLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", PasswordLogin)# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin,[["data","token"]])
		# 商家服务平台提取token打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台token:",token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin,[["data", "sign"]])
		# 商家服务平台提取sign打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台sign:",sign)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳",time)
		# 执行接口-查询菜单权限
		systemRoleWorkertree = bkw.financeBusinessApi_systemRoleWorkertree({"header":{"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma":{},"data":{},"env":envt},"dict")
		# 提取接口返回的参数
		systemRoleWorkertrees = ckw.CommonKeyWord().Json_GetJsonValue(systemRoleWorkertree,[["data","body"]])
		# 提取菜单-财务管理
		financeManage = ckw.CommonKeyWord().Json_GetJsonValue(systemRoleWorkertrees[1],[["menuName"]])
		# 打印提取的菜单结果到控制台
		ckw.CommonKeyWord().Print_ToControl("商家服务平台财务中心菜单:",financeManage)
		# 商家服务平台提取菜单打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台财务中心菜单:",financeManage)
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(financeManage,"财务中心")
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("3.0")

	@allure.feature("商家-判断是否开通财税")
	@allure.severity("blocker")
	@pytest.mark.flaky(rerun=1)  # 失败重试后立即重跑一次
	@pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
	def test_lq_financeBusiness_0002(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-mobile
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile1")
		# 读取yaml文件-password
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"password")
		# 读取yaml文件-selectOnlineInvoice
		selectOnlineInvoice = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectOnlineInvoice")
		# 执行查询sql
		selectOnlineInvoice = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectOnlineInvoice)
		print("执行查询sql：", selectOnlineInvoice)
		# SQL返回-提取数据-提取json中的对象
		sqlOnlineInvoice = ckw.CommonKeyWord().Json_GetJsonValue(selectOnlineInvoice[0], [["onlineInvoice"]])
		print("执行查询sql：", sqlOnlineInvoice, type(sqlOnlineInvoice))
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名",envt)
		# 登录商家服务平台
		PasswordLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin,[["data","token"]])
		# 商家服务平台提取token打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台token:",token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin,[["data", "sign"]])
		# 商家服务平台提取sign打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台sign:",sign)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳",time)
		# 执行接口-查询登录用户所在连锁是否开通财税账号
		organizeFinanceAccountUnitDetail = bkw.financeBusinessApi_organizeFinanceAccountUnitDetail({"header":{"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma":{},"data":{},"env":envt},"dict")
		# 提取接口返回的参数
		onlineInvoice = ckw.CommonKeyWord().Json_GetJsonValue(organizeFinanceAccountUnitDetail,[["data","onlineInvoice"]])
		# 打印提取的菜单结果到控制台
		ckw.CommonKeyWord().Print_ToControl("商家服务平台-连锁是否开通财税账户:",onlineInvoice)
		# 商家服务平台提取菜单打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台-连锁是否开通财税账户:",onlineInvoice)
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(onlineInvoice,sqlOnlineInvoice)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("3.0")

	@allure.feature("商家-查看连锁公共未读数量")
	@allure.severity("blocker")
	@pytest.mark.flaky(rerun=1)  # 失败重试后立即重跑一次
	@pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
	def test_lq_financeBusiness_0003(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-mobile
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"mobile1")
		# 读取yaml文件-password
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"password")
		# 读取yaml文件-selectAnnouncement
		selectAnnouncement = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectAnnouncement")
		# 执行查询sql
		selectAnnouncementSum = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectAnnouncement)
		print("执行查询sql：", selectAnnouncementSum)
		# SQL返回-提取数据-提取json中的对象
		announcementSum = ckw.CommonKeyWord().Json_GetJsonValue(selectAnnouncementSum[0], [["COUNT(*)"]])
		print("执行查询sql：", announcementSum,type(announcementSum))
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名",envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名",envt)
		# 登录商家服务平台
		PasswordLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin,[["data","token"]])
		# 商家服务平台提取token打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台token:",token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin,[["data", "sign"]])
		# 商家服务平台提取sign打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台sign:",sign)
		# 商家服务平台连锁id提取
		merchantId = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin, [["data", "merchantId"]])
		print("连锁id：",merchantId)
		merchantName = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin, [["data", "merchantName"]])
		print("连锁id：", merchantName)
		# 商家服务平台提取连锁打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台sign:", merchantName)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳",time)
		# 执行接口-查询未读公告数量
		announcementPartnerCountUnread = bkw.financeBusinessApi_announcementPartnerCountUnread({"header":{"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma":{},"data":{},"env":envt},"dict")
		# 提取接口返回的参数
		count = ckw.CommonKeyWord().Json_GetJsonValue(announcementPartnerCountUnread,[["data","count"]])
		print("接口返回的未读通告数：",count,type(count))
		# 打印提取的结果到控制台
		ckw.CommonKeyWord().Print_ToControl("商家服务平台未读公告数:",count)
		# 商家服务平台未读公告数打印到日志
		ckw.CommonKeyWord().Print_ToControl("商家服务平台未读公告数:",count)
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(count,announcementSum)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("3.0")


	@allure.feature("商家-查询结算单")
	@allure.severity("blocker")
	def test_lq_financeBusiness_0004(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		# 读取yaml文件密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名", envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名", envt)
		PasswordLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", PasswordLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取token打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin, [["data", "sign"]])
		print("获取的sign：", sign)
		# 商家服务平台提取sign打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台sign:", sign)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳", time)
		# 执行查询直付结算单接口
		directPayoutStatementPaging = bkw.financeBusinessApi_directPayoutStatementPaging({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma": {},"data": { "page": 1, "limit": 10, "pageData": "2022-05-01T08:51:35.739Z", "businessStatus": "", "statementCycle": [], "settleCycle": [], "blueText": 999, "nzSelectedIndex": 0, "statementType": 1, "statementNo": "DS20220424100002" },"env": envt}, "dict")
		print("查询接口：", directPayoutStatementPaging)
		# 提取结算单列表
		directPayoutStatementNos = ckw.CommonKeyWord().Json_GetJsonValue(directPayoutStatementPaging, [["data"]])
		print("提取的直付结算单1：", directPayoutStatementNos, type(directPayoutStatementNos))
		directPayoutStatementNo = ckw.CommonKeyWord().Json_GetJsonValue(directPayoutStatementNos, [["body"]])
		print("直付结算单000：", directPayoutStatementNo, type(directPayoutStatementNo))
		directPayoutStatementNo1 = ckw.CommonKeyWord().Json_GetJsonValue(directPayoutStatementNo[0], [["id"]])
		print("直付结算单：", directPayoutStatementNo1, type(directPayoutStatementNo1))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("directPayoutStatementNo1:", directPayoutStatementNo1)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("directPayoutStatementNo1:", directPayoutStatementNo1)
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(directPayoutStatementNo1, "DS20220424100002")
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")


	@allure.feature("商家-查询开票单")
	@allure.severity("blocker")
	def test_lq_financeBusiness_0005(self):
		# 查询结算单
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		# 读取yaml文件密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名", envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名", envt)
		PasswordLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", PasswordLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(PasswordLogin, [["data", "sign"]])
		print("获取的sign：", sign)
		# 商家服务平台提取sign打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台sign:", sign)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳", time)
		# 执行查询开票单接口
		payoutBillPaging = bkw.financeBusinessApi_payoutBillPaging({"header": {"Content-Type": "application/json;charsetUTF-8","Authorization": "Bearer " + token,"signature": sign}, "parma": {},"data": { "page": 1, "limit": 100, "pageData": "2022-05-03T08:02:28.759Z", "businessType": "1", "businessStatus": -1, "nzSelectedIndex": 0, "statementNo": "DS20220711100001" },"env": envt}, "dict")
		print("查询开票单接口：", payoutBillPaging)
		# 提取开票单列表
		payoutBillNos = ckw.CommonKeyWord().Json_GetJsonValue(payoutBillPaging, [["data","body"]])
		print("提取的开票单1：", payoutBillNos, type(payoutBillNos))
		payoutBillNo = ckw.CommonKeyWord().Json_GetJsonValue(payoutBillNos[0], [["businessNo"]])
		print("开票单：", payoutBillNo, type(payoutBillNo))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("directPayoutStatementNo1:", payoutBillNo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("directPayoutStatementNo1:", payoutBillNo)
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(payoutBillNo, "DS20220711100001")
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")


	@allure.feature("核算单位的在线开票VIP详情")
	@allure.severity("blocker")
	@pytest.mark.flaky(rerun=1)  # 失败重试后立即重跑一次
	@pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
	def test_lq_financeBusiness_0006(self):
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		selectApplyOnline = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectApplyOnline")
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		applyOnlineStatus = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectApplyOnline)
		res = bkw.financeBusinessApi_applyOnlineUnitDetail({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data":{"unitId":"555"},"env": envt}, "dict")
		status = ckw.CommonKeyWord().Json_GetJsonValue(res, [["data", "status"]])
		applyOnlineStatus2 = str(ckw.CommonKeyWord().Json_GetJsonValue(applyOnlineStatus[0], [["status"]]))
		assert ckw.CommonKeyWord().Assert_ObjAndObj(applyOnlineStatus2,status)

	@allure.feature("在线开票vip详情")
	@allure.severity("blocker")
	def test_lq_financeBusiness_0007(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号、密码、环境域名
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		SmsLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", SmsLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "sign"]])
		print("获取的sign：", sign)
		applyVipDetail = bkw.financeBusinessApi_applyVipDetail({"header": {
			"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma": {}, "data": {}, "env": envt}, "dict")
		unitId = ckw.CommonKeyWord().Json_GetJsonValue(applyVipDetail, [["data", "unitId"]])
		print("接口提取：", unitId, type(unitId))
		assert ckw.CommonKeyWord().Assert_BcharInAchar(unitId, 635)


	@allure.feature("查询连锁未读公告")
	@allure.severity("blocker")
	@pytest.mark.flaky(rerun=1)  # 失败重试后立即重跑一次
	@pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
	def test_lq_financeBusiness_0008(self):
		# 查询连锁的公告
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		# 读取yaml文件密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名", envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名", envt)
		SmsLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": { "account": mobile, "type": 2, "credentials": password, "tenantId": 3 }, "env": envt}, "dict")
		print("登录接口", SmsLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "sign"]])
		print("获取的sign：", sign)
		# 执行接口
		announcementPartnerAvailable = bkw.financeBusinessApi_announcementPartnerAvailable({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign}, "parma": {}, "data": {}, "env": envt}, "dict")
		print("查询接口：", announcementPartnerAvailable)
		# 查询公告名称
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		selectAnnouncement = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectAnnouncement")
		selectAnnouncementSum = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectAnnouncement)
		announcementSum = ckw.CommonKeyWord().Json_GetJsonValue(selectAnnouncementSum[0], [["COUNT(*)"]])
		if (announcementSum>0):
			selectAnnouncementName = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectAnnouncementName")
			selectAnnouncementName = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectAnnouncementName)
			print("执行查询sql：", selectAnnouncementName)
			# SQL返回-提取数据-提取json中的对象
			sqlAnnouncementName = ckw.CommonKeyWord().Json_GetJsonValue(selectAnnouncementName[0], [["name"]])
			print("查询sql提取：", sqlAnnouncementName, type(sqlAnnouncementName))
			# 提取接口返回的			assert ckw.CommonKeyWord().Assert_BcharInAchar(announcementName, selectAnnouncementName)
			announcementName = ckw.CommonKeyWord().Json_GetJsonValue(announcementPartnerAvailable, [["data","name"]])
			print("接口提取内容：", announcementName, type(announcementName))
			# 断言对比对象
			assert ckw.CommonKeyWord().Assert_BcharInAchar(announcementName, sqlAnnouncementName)
		else:
			# 提取接口返回的
			announcementName = ckw.CommonKeyWord().Json_GetJsonValue(announcementPartnerAvailable, [["data","name"]])
			print("接口提取的发票：", announcementName, type(announcementName))
			# 断言对比对象
			assert ckw.CommonKeyWord().Assert_ObjAndObj(bool(announcementName), bool(None))

	@allure.feature("查询连锁公告列表")
	@allure.severity("blocker")
	@pytest.mark.flaky(rerun=1)  # 失败重试后立即重跑一次
	@pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
	def test_lq_financeBusiness_0009(self):
		# 查询连锁的公告
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		# 读取yaml文件密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名", envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名", envt)
		SmsLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", SmsLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "sign"]])
		print("获取的sign：", sign)
		# 执行接口
		announcementPartnerPaging = bkw.financeBusinessApi_announcementPartnerPaging({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma": {}, "data": {},"env": envt}, "dict")
		print("查询接口：", announcementPartnerPaging)
		# 查询公告id
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		selectAnnouncement = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectAnnouncement")
		selectAnnouncementSum = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectAnnouncement)
		announcementSum = ckw.CommonKeyWord().Json_GetJsonValue(selectAnnouncementSum[0], [["COUNT(*)"]])
		if (announcementSum > 0):
			selectAnnouncementId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectAnnouncementId")
			selectAnnouncementId = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectAnnouncementId)
			print("执行查询sql：", selectAnnouncementId)
			# SQL返回-提取数据-提取json中的对象
			sqlAnnouncementId = ckw.CommonKeyWord().Json_GetJsonValue(selectAnnouncementId[0], [["announcementId"]])
			print("查询sql提取：", sqlAnnouncementId, type(sqlAnnouncementId))
			# 提取接口返回的
			announcementPartnerPaging = ckw.CommonKeyWord().Json_GetJsonValue(announcementPartnerPaging, [["data", "body"]])
			print("接口提取内容：", announcementPartnerPaging, type(announcementPartnerPaging))
			announcementId = ckw.CommonKeyWord().Json_GetJsonValue(announcementPartnerPaging[0], [["announcementId"]])
			print("接口提取内容：", announcementId, type(announcementId))
			# 断言对比对象
			assert ckw.CommonKeyWord().Assert_BcharInAchar(announcementId, sqlAnnouncementId)
		else:
			# 提取接口返回的
			nnouncementPartnerPaging = ckw.CommonKeyWord().Json_GetJsonValue(announcementPartnerPaging,[["data", "body"]])
			announcementId = ckw.CommonKeyWord().Json_GetJsonValue(nnouncementPartnerPaging[0], [["announcementId"]])
			print("接口提取：", announcementId, type(announcementId))
			# 断言对比对象
			assert ckw.CommonKeyWord().Assert_ObjAndObj(bool(announcementId), bool(None))


	@allure.feature("商家服务平台版本")
	@allure.severity("blocker")
	@pytest.mark.flaky(rerun=1)  # 失败重试后立即重跑一次
	@pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
	def test_lq_financeBusiness_0010(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号、密码、环境域名
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询sql
		selectBusinessCenterVersion = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectBusinessCenterVersion")
		selectBusinessCenterVersion = ckw.CommonKeyWord().Db_SshConfRCMysqlExecuteAfterConnect(financeDataDB,selectBusinessCenterVersion)
		print("执行查询sql：", selectBusinessCenterVersion)
		SmsLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", SmsLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		# 商家服务平台sign提取
		sign = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "sign"]])
		print("获取的sign：", sign)
		businessCenterVersionDetail = bkw.financeBusinessApi_businessCenterVersionDetail({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token, "signature": sign},"parma": {}, "data": {}, "env": envt}, "dict")
		version = ckw.CommonKeyWord().Json_GetJsonValue(businessCenterVersionDetail, [["data", "version"]])
		print("接口提取：", version, type(version))
		# SQL返回-提取数据-提取json中的对象
		sqlBusinessCenterVersion = ckw.CommonKeyWord().Json_GetJsonValue(selectBusinessCenterVersion[0], [["version"]])
		print("查询sql提取：", sqlBusinessCenterVersion, type(sqlBusinessCenterVersion))
		assert ckw.CommonKeyWord().Assert_ObjAndObj(version, sqlBusinessCenterVersion)

	@allure.feature("查询用户UUID")
	@allure.severity("blocker")
	def test_lq_financeBusiness_0011(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号、密码、环境域名
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		SmsLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		print("登录接口", SmsLogin)
		# 商家服务平台token提取
		token = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "token"]])
		print("获取的token：", token)
		# 商家服务平台提取authToken打印到日志
		ckw.CommonKeyWord().Print_ToLog("商家服务平台平台token:", token)
		uuidRes = bkw.financeBusiness_userUuid({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},"parma": {}, "data": {}, "env": envt}, "dict")
		# SQL返回-提取数据-提取json中的对象
		uuid = ckw.CommonKeyWord().Json_GetJsonValue(uuidRes, [["data","uuid"]])
		assert ckw.CommonKeyWord().Assert_ObjAndObj(bool(uuid), True)

	@allure.feature("商家交易订单页面")
	@allure.severity("blocker")
	def test_lq_financeBusiness_0012(self):
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件后台登录帐号、密码、环境域名
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile1")
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "password")
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		SmsLogin = bkw.financeApi_SmsLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"account": mobile, "type": 2, "credentials": password,"tenantId": 3}, "env": envt}, "dict")
		token = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "token"]])
		signature = ckw.CommonKeyWord().Json_GetJsonValue(SmsLogin, [["data", "sign"]])
		transactionOrdersPaging = bkw.financeBusiness_transactionOrdersPaging({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token,"signature":signature},"parma": {}, "data": {"pageNo":1,"pageSize":10,"pageData":"2022-07-20T08:26:37.376Z","payTime":None,"nzSelectedIndex":0,"blueText":-30,"startDate":"2022-06-20 00:00:00","endDate":"2022-07-20 23:59:59"}, "env": envt}, "dict")
		# SQL返回-提取数据-提取json中的对象
		transactionOrders = ckw.CommonKeyWord().Json_GetJsonValue(transactionOrdersPaging, [["data"]])
		print(transactionOrders)
		assert bool(transactionOrders)

	@allure.feature("关闭公共数据数据库")
	@allure.severity("blocker")
	def test_lq_financedata_close(self):
		# 关闭公共数据数据库
		ckw.CommonKeyWord().Db_SshConfRCMysqlClose(financeDataDB)