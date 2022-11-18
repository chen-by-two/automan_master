# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_financeStatement:

	@allure.feature("财务结算-直付订单清算")
	@allure.severity("blocker")
	def test_lq_financeStatement_0001(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"envt")
		# 查询SQL - deletedSettlementExtend、deletedDirectSettlement
		deleteSettlementExtend = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteSettlementExtend")
		deleteDirectSettlement = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteDirectSettlement")
		# 执行SQL
		deleteSettlementExtend = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",deleteSettlementExtend)
		deleteDirectSettlement = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",deleteDirectSettlement)
		# 执行接口-直付订单清算
		mqAfterDirectCleaned = bkw.financeStatementApi_mqAfterDirectCleaned({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "orderDto": { "orderType": 1, "cleanStatus": 1, "cashAmount": 35.2, "channel": 1, "gmtManualCreated": "2022-06-16 11:39:44", "directAmount": 35.2, "gmtPaid": "2022-06-16 11:40:46", "couponAmount": 0, "billAmount": 35.2, "payAmount": 0, "prescriptionOrderFlag": 0, "refundNo": "", "realDiscount": 88.01, "merchantId": 635, "payMethod": 0, "unitId": 635, "discountType": 1, "directCleanAmount": 30.98, "memberId": 16234825, "saleAmount": 0, "orderSource": 0, "subsidyRate": None, "orderNo": "92061611603549650106", "shortNo": "03549650106", "storeId": 7590, "subsidyAmount": None, "hasHx": 0, "orderMethod": 3, "settledAmount": 35.2, "cooperationCode": "2018090300063453697303", "feeAmount": 0, "totalAmount": 35.2, "counterAmount": 0, "assistantId": 200825, "prescriptionOrderNum": 0, "mainOrderNo": "92061601603549640174", "gmtChanged": "2022-06-16 11:40:46", "settlementAmount": 30.98, "unionSubstituteAmount": 0, "storeCode": "2018090300758953701297" }, "orderItemDtoList": [ { "orderType": 1, "itemType": 1, "itemDiscount": 88, "directAmount": 35.2, "internalId": "2143451", "merchantSubsidyRate": None, "goodsSubType": 11, "itemName": "感冒灵胶囊", "couponAmount": 0, "itemDiscountType": 1, "directCleanAmount": 30.98, "unitPrice": 35.2, "saleAmount": 0, "goodsNo": "635-2143451", "activityAmount": 0, "orderNo": "92061611603549650106", "quantity": 1, "tradeCode": "6923718120188", "approvalNumber": "国药准字Z20055271", "pack": "", "settledAmount": 35.2, "itemId": 9909473, "totalAmount": 35.2, "form": "", "settlementAmount": 30.98, "merchantSubsidyAmount": None, "activityType": 0, "discountModel": 1 } ],"insureMemberDto": { "memberPhone": "15256908297", "memberAge": 26, "cardAddr": "安徽省淮北市濉溪县濉溪镇", "memberName": "梁琪", "cardExpiryStart": "2022-05-27", "cardNo": "340621199508206020", "memberId": "16234825", "cardExpiryEnd": "2042-05-27" }, "orderType": 1, "orderInfoDto": { "orderType": 1, "assistantName": "梁琪", "groupId": 7, "memberName": "梁琪", "unDrug": 0, "merchantName": "国药控股国大药房上海连锁有限公司", "assistantMobile": "15256908297", "merchantId": 635, "goodsQuantity": 1, "erpSn": "", "storeName": "上海国大永和路店", "useMerchantSubsidy": "", "merchantType": 1, "specialDiseaseName": "", "memberId": 16234825, "memberIdCard": "340621199508206020", "specialDiseaseFlag": "", "orderNo": "92061611603549650106", "unitName": "国药控股国大药房上海连锁有限公司", "outType": 0, "sourceOfBusinessName": "药联健康", "assistantId": 200825, "insureType": "", "subsidyRange": "", "internalCode": "102747", "memberMobile": "15256908297", "storeCode": "2018090300758953701297" }, "orderNo": "92061611603549650106", "refundNo": "", "cobrandDetailDto": { "promotAmountDtoList": [], "activityAmountDtoList": [], "matchCobrandResp": "" }, "orderEquityDtoList": [ { "memberIdCard": "340621199508206020", "orderType": 1, "orderNo": "92061611603549650106", "insurerNo": 7, "projectType": 0, "memberInfoSource": 1, "memberName": "梁琪", "policyNo": "", "auditNo": "", "transFromClean": "", "insurerName": "上海聚音信息科技有限公司", "directAmount": 35.2, "insurerCooperationCode": "2018090300000653697798", "equityGroupId": 1651, "equityName": "自付转权益专用项目", "equityNo": "1000191369097877", "equityId": 23434297, "projectName": "自付转权益-勿动", "directCleanAmount": 30.98, "projectId": 477, "memberMobile": "15256908297", "memberId": 16234825 } ], "diseaseResp": "", "orderEquityItemDtoList": [ { "orderType": 1, "itemId": 9909473, "orderNo": "92061611603549650106", "equityId": 23434297, "directCleanAmount": 30.98, "directAmount": 35.2 } ] },"env":envt},"dict")
		print("执行的接口：", mqAfterDirectCleaned, type(mqAfterDirectCleaned))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - selectDirectSettlement、selectSettlementExtend
		selectDirectSettlement = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectDirectSettlement")
		selectSettlementExtend = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectSettlementExtend")
		# 执行SQL
		selectDirectSettlement = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",selectDirectSettlement)
		print("执行查询sql：", selectDirectSettlement, type(selectDirectSettlement))
		selectSettlementExtend = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",selectSettlementExtend)
		# SQL返回-提取数据-提取json中的对象
		sqlDirectSettlement = ckw.CommonKeyWord().Json_GetJsonValue(selectDirectSettlement[0], [["order_no"]])
		print("执行查询sql：", sqlDirectSettlement, type(sqlDirectSettlement))
		# SQL返回-提取数据-提取json中的对象
		sqlSettlementExtend = ckw.CommonKeyWord().Json_GetJsonValue(selectSettlementExtend[0], [["order_no"]])
		print("执行查询sql：", sqlSettlementExtend, type(sqlSettlementExtend))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlDirectSettlement,92061611603549650106)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("财务结算-直付订单商品替换")
	@allure.severity("blocker")
	def test_lq_financeStatement_0002(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - deleteDirectCleanGoods
		deleteDirectCleanGoods = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteDirectCleanGoods")
		# 执行SQL
		deleteDirectCleanGoods = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",deleteDirectCleanGoods)
		# 执行接口-直付订单商品替换
		false=False
		mqAfterDirectGoodsReplaced = bkw.financeStatementApi_mqAfterDirectGoodsReplaced({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"orderType":1,"orderNo":"92061611603549650106","storeInternalCode":"102747","old": None,"specialDiseased":false,"orderGoodDtoList":[{"orderType":1,"itemType":1,"originalGoodsCode":"2143451","projectType":0,"directAmount":35.2,"internalId":"2143451","invoicePriceWithTax":None,"goodsSubType":11,"itemName":"感冒灵胶囊","refundNo":"","itemStatus":0,"directCleanAmount":30.98,"equityId":0,"originalApprovalNo":"国药准字Z20055271","claimProjectType":1,"unitPrice":35.2,"amountWithoutTax":None,"orderNo":"92061611603549650106","quantity":1,"tradeCode":"6923718120188","originalGoodsName":"感冒灵胶囊","approvalNumber":"国药准字Z20055271","pack":"","itemId":9909473,"totalAmount":35.2,"taxRate":-1,"form":"","skuNo":"635-2143451","invoicePriceWithoutTax":None,"taxEdClass":"","taxEd":"","taxAmount":None}],"medicalDeviced":0,"storeName":"上海国大永和路店","supper":"","specialDiseaseType":"","specialDiseaseName":""}, "env": envt}, "dict")
		print("执行的接口：", mqAfterDirectGoodsReplaced, type(mqAfterDirectGoodsReplaced))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - selectDirectCleanGoods
		selectDirectCleanGoods = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectDirectCleanGoods")
		# 执行SQL
		selectDirectCleanGoods = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",selectDirectCleanGoods)
		print("执行查询sql：", selectDirectCleanGoods, type(selectDirectCleanGoods))
		# SQL返回-提取数据-提取json中的对象
		sqlDirectCleanGoods = ckw.CommonKeyWord().Json_GetJsonValue(selectDirectCleanGoods[0], [["order_no"]])
		print("执行查询sql：", sqlDirectCleanGoods, type(sqlDirectCleanGoods))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlDirectCleanGoods, 92061611603549650106)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("财务结算-推送理赔流水")
	@allure.severity("blocker")
	def test_lq_financeStatement_0003(self):
        # 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - updateDirectEquityClaim
		updateDirectEquityClaim = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateDirectEquityClaim")
		# 执行SQL
		updateDirectEquityClaim = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",updateDirectEquityClaim)
		# 执行接口-推送理赔流水到财务结算
		directEquityClaimSync = bkw.financeStatementApi_directEquityClaimSync({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"directPay": 1, "claimType": 0, "orderNo": "92061611603549650106", "claimGoodsList": [{"unitPrice": 35.2, "itemId": 9909473, "claimType": 0, "totalAmount": 35.2, "reverseAmount": 0,"quantity": 1, "claimAmount": 30.98, "claimedAmount": 30.98}], "gmtCreatedStr": "2022-06-28 19:09:58","policyNo": "YPB202201040001", "insurerId": 161205, "claimedAmount": 30.98}, "env": envt}, "dict")
		print("执行的接口：", directEquityClaimSync, type(directEquityClaimSync))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 查询SQL - selectPolicyNo、selectClaimedAmount
		selectPolicyNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectPolicyNo")
		selectClaimedAmount = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectClaimedAmount")
		# 执行SQL
		selectPolicyNo = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",selectPolicyNo)
		print("执行查询sql：", selectPolicyNo, type(selectPolicyNo))
		selectClaimedAmount = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",selectClaimedAmount)
		print("执行查询sql：", selectClaimedAmount, type(selectClaimedAmount))
		# SQL返回-提取数据-提取json中的对象
		sqlPolicyNo = ckw.CommonKeyWord().Json_GetJsonValue(selectPolicyNo[0], [["policy_no"]])
		print("执行查询sql：", sqlPolicyNo, type(sqlPolicyNo))
		sqlClaimedAmount = ckw.CommonKeyWord().Json_GetJsonValue(selectClaimedAmount[0], [["claimed_amount"]])
		print("执行查询sql：", sqlClaimedAmount, type(sqlClaimedAmount))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlPolicyNo, "YPB202201040001")
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlClaimedAmount, 30.98)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

