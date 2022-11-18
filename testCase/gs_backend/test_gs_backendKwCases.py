# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_gs_backend:

	@allure.feature("药店宝创建普通药品购物车")
	@allure.severity("blocker")
	def test_gs_backend_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/GongSheng/GsApp.Backend.yaml")
		# 读取yaml里ExtractToken
		ExtractToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"ExtractToken")
		# 从数据库提取token-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"udtest.uniondrug.com","port":"6033","username":"test","password":"tset@321abc","database":"cn_uniondrug_backend_app","sql":ExtractToken})
		# 提取sql执行结果里最新token
		tokenGs = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0],[["token"]])
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",tokenGs)
		# 读取yaml里环境
		env_gs = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env_gs")
		# 获取购物车接口-调取接口
		cartData = bkw.backendApi_OrdersCart({"header":{"Content-Type": "application/json;charsetUTF-8","version":"4.44","Authorization": "Bearer "+tokenGs},"parma":{},"data":{"gmtScanAt":"2020-12-03 10:52:57","cartRecordId":"0","waterNo":"","cartDrugs":[{"approvalNumber":"国药准字H13024082","commonAliasPinyiin":"ffafwap","commonFullPinyin":"{\"commonFullPinyin\":\"fufanganfenwananpian\",\"memberPrice\":\"297.00\",\"isRule\":false,\"productPoint\":0,\"originalPrice\":\"297.00\",\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}","commonName":"复方氨酚烷胺片","count":1,"form":"14片/盒","hasAdd":"false","id":"69485","internalId":"3254","isChange":"true","isDrug":"true","isDtp":"0","isLast":"false","isRule":"0","isRx":"0","isSelected":"false","isSuper":"0","manufacturer":"","memberPrice":"297.00","money":"297.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"","quantity":"1","tradeCode":"6934366601288","unitPrice":"297.00"}],"orderMethod":3,"isShow":"0","promotions":[],"cartProducts":[{"productId":"50"}],"erpSn":"","equityId":"28811617","entrance":"{\"code\":\"105268421130060953\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811617\",\"orderChannel\":\"wechat\"}","prescriptions":[],"items":[{"internalId":"3254","quantity":"1"}],"memberId":"15961482"},"env":env_gs},"dict")
		# 提取cart接口里的erroNo
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(cartData,[["errno"]])
		# 打印erroNo
		ckw.CommonKeyWord().Print_ToControl("打印erroNo：",erroNo)
		# 读取yaml里预置cart接口反参errno
		CartSuccessData = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CartSuccessData")
		# 打印预置cart接口反参结果到控制台
		ckw.CommonKeyWord().Print_ToControl("预置cart接口反参errno：",CartSuccessData)
		# 对比实际cart反参与预置数据
		# assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,CartSuccessData)

	@allure.feature("药店宝创建DTP药品购物车")
	@allure.severity("blocker")
	def test_gs_backend_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/GongSheng/GsApp.Backend.yaml")
		# 读取yaml里DtpAssistantToken
		DtpAssistantToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DtpAssistantToken")
		# 数据预置执行变更dtp店员token状态的sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",DtpAssistantToken)
		# 读取yaml里环境
		env_gs = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env_gs")
		# 读取yamlDTPtoken
		DtpToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DtpToken")
		# 获取购物车接口-调取接口
		DtpOrdersCart = bkw.backendApi_DtpOrdersCart({"header":{"Content-Type": "application/json;charsetUTF-8","version":"4.44","Authorization": "Bearer "+DtpToken},"parma":{},"data":{"gmtScanAt":"2020-12-03 10:52:57","cartRecordId":"0","waterNo":"","cartDrugs":[{"approvalNumber":"国药准字H13024082","commonAliasPinyiin":"ffafwap","commonFullPinyin":"{\"commonFullPinyin\":\"fufanganfenwananpian\",\"memberPrice\":\"297.00\",\"isRule\":false,\"productPoint\":0,\"originalPrice\":\"297.00\",\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}","commonName":"复方氨酚烷胺片","count":1,"form":"14片/盒","hasAdd":"false","id":"69485","internalId":"3254","isChange":"true","isDrug":"true","isDtp":"1","isLast":"false","isRule":"0","isRx":"0","isSelected":"false","isSuper":"0","manufacturer":"","memberPrice":"297.00","money":"297.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"","quantity":"1","tradeCode":"6934366601288","unitPrice":"297.00"}],"orderMethod":3,"isShow":"0","promotions":[],"cartProducts":[{"productId":"50"}],"erpSn":"","equityId":"28811617","entrance":"{\"code\":\"105268421130060953\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811617\",\"orderChannel\":\"wechat\"}","prescriptions":[],"items":[{"internalId":"3254","quantity":"1"}],"memberId":"15961482"},"env":env_gs},"dict")
		# 提取DtpOrdersCart接口里的erroNo
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(DtpOrdersCart,[["errno"]])
		# 打印erroNo
		ckw.CommonKeyWord().Print_ToControl("打印erroNo：",erroNo)
		# 读取yaml里预置DtpOrdersCart接口反参errno
		DtpCartSuccessData = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DtpCartSuccessData")
		# 对比实际DtpOrdersCart反参与预置数据
		# assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,DtpCartSuccessData)

	@allure.feature("药店宝村医药品购物车")
	@allure.severity("blocker")
	def test_gs_backend_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/GongSheng/GsApp.Backend.yaml")
		# 读取yaml里环境
		env_gs = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env_gs")
		# 获取商户中心接口-调用开通商户为村医模式
		MerhantVillageDoctor = bkw.backendApi_MerhantVillageDoctor({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"organizationId": "132169","isWholesale": "1"},"env":env_gs},"dict")
		# 读取yaml里VillageDoctorToken
		VillageDoctorToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"VillageDoctorToken")
		# 数据预置执行变更村医店员token状态的sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",VillageDoctorToken)
		# 读取yaml村医店员token
		VillageToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"VillageToken")
		# 获取购物车接口-调取接口
		VillageDoctorOrdersCart = bkw.backendApi_VillageDoctorOrdersCart({"header":{"Content-Type": "application/json;charsetUTF-8","version":"4.44","Authorization": "Bearer "+VillageToken},"parma":{},"data":{"gmtScanAt":"2020-12-03 10:52:57","cartRecordId":"0","waterNo":"","cartDrugs":[{"approvalNumber":"国药准字H13024082","commonAliasPinyiin":"ffafwap","commonFullPinyin":"{\"commonFullPinyin\":\"fufanganfenwananpian\",\"memberPrice\":\"297.00\",\"isRule\":false,\"productPoint\":0,\"originalPrice\":\"297.00\",\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}","commonName":"复方氨酚烷胺片","count":1,"form":"14片/盒","hasAdd":"false","id":"69485","internalId":"3254","isChange":"true","isDrug":"true","isDtp":"0","isLast":"false","isRule":"0","isRx":"0","isSelected":"false","isSuper":"0","manufacturer":"","memberPrice":"297.00","money":"297.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"","quantity":"1","tradeCode":"6934366601288","unitPrice":"297.00"}],"orderMethod":3,"isShow":"0","promotions":[],"cartProducts":[{"productId":"50"}],"erpSn":"","equityId":"28811617","entrance":"{\"code\":\"105268421130060953\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811617\",\"orderChannel\":\"wechat\"}","prescriptions":[],"items":[{"internalId":"3254","quantity":"1"}],"memberId":"15961482"},"env":env_gs},"dict")
		# 提取VillageDoctorOrdersCart接口里的erroNo
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(VillageDoctorOrdersCart,[["errno"]])
		# 读取yaml里预置VillageDoctorOrdersCart接口反参errno
		VillageDoctorCartSuccessData = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"VillageDoctorCartSuccessData")
		# 对比实际VillageDoctorOrdersCart反参与预置数据
		#assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,VillageDoctorCartSuccessData)

	@allure.feature("药店宝处方药处方单创建购物车")
	@allure.severity("blocker")
	def test_gs_backend_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/GongSheng/GsApp.Backend.yaml")
		# 读取yaml里环境
		env_gs = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env_gs")
		# 获取商户中心接口-调用开通商户开启处方
		Recipe = bkw.backendApi_Recipe({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"organizationId": "578","isElectronic": "1"},"env":env_gs},"dict")
		# 读取yaml里RecipeWaterNo
		RecipeWaterNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"RecipeWaterNo")
		# 从数据库提取token-执行删除处方流水
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",RecipeWaterNo)
		# 读取yaml里RecipeToken
		RecipeToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"RecipeToken")
		# 从数据库提取token-执行查询
		sqlResl = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL",RecipeToken)
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",sqlResl)
		# 提取sql执行结果里最新token
		tokenGs = ckw.CommonKeyWord().Json_GetJsonValue(sqlResl[0],[["token"]])
		# 获取购物车接口-调取接口
		RecipeCart = bkw.backendApi_RecipeCart({"header":{"Content-Type": "application/json;charsetUTF-8","version":"4.44","Authorization": "Bearer "+tokenGs},"parma":{},"data":{"gmtScanAt":"2021-01-08 11:39:55","cartRecordId":"0","waterNo":"c2507684b339232ada225a49852f4253","cartDrugs":[{"approvalNumber":"国药准字Z41020695","commonAliasPinyiin":"qzxfw","commonFullPinyin":"{\"commonFullPinyin\":\"qizhixiangfuwan\",\"memberPrice\":5,\"isRule\":false,\"productPoint\":0,\"originalPrice\":1000,\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}","commonName":"七制香附丸","count":1,"form":"6g*10袋","hasAdd":"false","id":"3","internalId":"01138","isChange":"true","isDrug":"true","isDtp":"0","isLast":"false","isRule":"false","isRx":"1","isSelected":"false","isSuper":0,"manufacturer":"","memberPrice":"5","money":"1000.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"","quantity":"1","tradeCode":"","unitPrice":"1000"},{"approvalNumber":"国药准字Z22020394","commonAliasPinyiin":"kgzsp","commonFullPinyin":"{\"commonFullPinyin\":\"kangguzengshengpian\",\"memberPrice\":0.01,\"isRule\":false,\"productPoint\":0,\"originalPrice\":288,\"image\":\"http:\\/\\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\\/oss\\/upload\\/file\\/goods\\/1567407661654.jpg\"}","commonName":"抗骨增生片","count":1,"form":"24s","hasAdd":"false","id":"","internalId":"01234","isChange":"true","isDrug":"true","isDtp":"0","isLast":"false","isRule":"false","isRx":"0","isSelected":"false","isSuper":0,"manufacturer":"","memberPrice":"0.01","money":"288.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"预计单件可得11.11积分","quantity":"1","tradeCode":"6943750066107","unitPrice":"288"}],"orderMethod":3,"isShow":"0","promotions":[],"cartProducts":[{"productId":"50"}],"erpSn":"","equityId":"28811598","entrance":"{\"code\":\"103947485544233857\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811598\",\"orderChannel\":\"wechat\"}","prescriptions":[{"image":"","waterNo":"30c92b126e316446adcfb2ad327a05d9"}],"items":[{"internalId":"01138","quantity":"1"},{"internalId":"01234","quantity":"1"}],"memberId":"15961482"},"env":env_gs},"dict")
		# 提取RecipeCart接口里的erroNo
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(RecipeCart,[["errno"]])
		# 读取yaml里预置VRecipeCart接口反参errno
		CartSuccessData = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CartSuccessData")
		# 对比实际VRecipeCart反参与预置数据
		# assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,CartSuccessData)

	@allure.feature("药店宝创建换药理赔订单购物车")
	@allure.severity("blocker")
	def test_gs_backend_005(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/GongSheng/GsApp.Backend.yaml")
		# 读取yaml里环境
		env_gs = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env_gs")
		# 读取yaml里OrderWaterNo
		OrderWaterNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"OrderWaterNo")
		# 从数据库提取token-执行删除订单流水号
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL",OrderWaterNo)
		# 读取yaml里RecipeToken
		RecipeToken = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"RecipeToken")
		# 从数据库提取token-执行查询
		sqlResl = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL",RecipeToken)
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",sqlResl)
		# 提取sql执行结果里最新token
		tokenGs = ckw.CommonKeyWord().Json_GetJsonValue(sqlResl[0],[["token"]])
		# 获取购物车接口-调取接口
		RenewCart = bkw.backendApi_RenewCart({"header":{"Content-Type": "application/json;charsetUTF-8","version":"4.44","Authorization": "Bearer "+tokenGs},"parma":{},"data":{"gmtScanAt":"2021-01-08 15:51:17","cartRecordId":"0","waterNo":"9c0a48c8744dd1f59a1bea4d751aac3d","cartDrugs":[{"approvalNumber":"国药准字Z22020394","commonAliasPinyiin":"kgzsp","commonFullPinyin":"{\"commonFullPinyin\":\"kangguzengshengpian\",\"memberPrice\":0.01,\"isRule\":false,\"productPoint\":0,\"originalPrice\":288,\"image\":\"http:\\/\\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\\/oss\\/upload\\/file\\/goods\\/1567407661654.jpg\"}","commonName":"抗骨增生片","count":1,"form":"24s","hasAdd":"false","id":"","internalId":"01234","isChange":"false","isDrug":"true","isDtp":"0","isLast":"false","isRule":"0","isRx":"0","isSelected":"false","isSuper":"0","manufacturer":"","memberPrice":"0.01","money":"288.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"预计单件可得11.11积分","quantity":"1","tradeCode":"6943750066107","unitPrice":"288"}],"orderMethod":3,"isShow":"0","itemId":"200826470030","promotions":[],"cartProducts":[],"erpSn":"","equityId":"0","entrance":"{\"code\":\"104089288032103429\",\"channel\":\"10\",\"memberId\":\"1107820\",\"entrance\":\"5\",\"claimNo\":\"200826470030\",\"orderChannel\":\"wechat\"}","prescriptions":[],"items":[{"internalId":"01234","quantity":"1"}],"memberId":"1107820"},"env":env_gs},"dict")
		# 提取RenewCart接口里的erroNo
		erroNo = ckw.CommonKeyWord().Json_GetJsonValue(RenewCart,[["errno"]])
		# 读取yaml里预置VRecipeCart接口反参errno
		CartSuccessData = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CartSuccessData")
		# 对比实际VRecipeCart反参与预置数据
 		#assert ckw.CommonKeyWord().Assert_ObjAndObj(erroNo,CartSuccessData)
