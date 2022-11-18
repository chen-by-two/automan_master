# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_insure:

	@allure.feature("查询流量池")
	@allure.severity("blocker")
	def test_zjy_Insure_001(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/edz/PycharmProjects/automan/TestFile/ZhuJingYu/zjy.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件里的环境变量
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"env")
		# 读取yaml文件里的开始时间
		startDate = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"startDate")
		# 读取yaml文件里的结束时间
		endDate = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"endDate")
		# 读取yaml文件里的投保纬度
		latitude = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"latitude")
		# 查询流量池
		queryPoolClaimAmount = bkw.insureApi_queryPoolClaimAmount({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"startDate":startDate,"endDate":endDate,"latitude":latitude,"directPay": 1,"medicalDeviced": 0, "drugType": 0, "insureCompanyId": 7},"env":env},"dict")
		# 提取流量池金额
		poolClaim = ckw.CommonKeyWord().Json_GetJsonValue(queryPoolClaimAmount,[["data"]])
		# 打印流量金额到控制台
		ckw.CommonKeyWord().Print_ToControl("流量池金额",poolClaim)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("5.0")

	@allure.feature("查询保单手续费")
	@allure.severity("blocker")
	def test_zjy_Insure_002(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/edz/PycharmProjects/automan/TestFile/ZhuJingYu/zjy.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件里的环境变量
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"env")
		# 读取yaml文件里的保单id
		policyIds = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"policyIds")
		# 查询保单手续费
		feeAmount = bkw.insureApi_listFeeBill({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"policyIds": policyIds},"env":env},"dict")
		# 提取手续费
		fee = ckw.CommonKeyWord().Json_GetJsonValue(feeAmount,[["data"]])
		# 打印手续费到控制台
		ckw.CommonKeyWord().Print_ToControl("保单手续费",fee)

	@allure.feature("根据项目id查询保单详情")
	@allure.severity("blocker")
	def test_zjy_Insure_003(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/edz/PycharmProjects/automan/TestFile/ZhuJingYu/zjy.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件里的环境变量
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"env")
		# 读取yaml文件里的项目id
		projectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"projectId")
		# 查询保单详情
		projectId = bkw.insureApi_getByProjectId({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"projectId": projectId},"env":env},"dict")
		# 提取保单详情
		policyinfo = ckw.CommonKeyWord().Json_GetJsonValue(projectId,[["data"]])
		# 打印保单详情到控制台
		ckw.CommonKeyWord().Print_ToControl("保单详情",policyinfo)

	@allure.feature("获取保单的保费和服务费计划")
	@allure.severity("blocker")
	def test_zjy_Insure_004(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/edz/PycharmProjects/automan/TestFile/ZhuJingYu/zjy.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件里的环境变量
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"env")
		# 读取yaml文件里的保单id
		policyNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"policyNo")
		# 查询保单分页
		infoPaging = bkw.insureApi_InfoPaging({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "insurerId": 7, "policyNo": policyNo, "policyType": 2, "insureMethod": 1, "claimMethod": 1, "startTime": "2022-05-20 00:00:00" },"env":env},"dict")
		# 提取保单分页详情
		paging = ckw.CommonKeyWord().Json_GetJsonValue(infoPaging,[["data"]])
		# 打印分页详情到控制台
		ckw.CommonKeyWord().Print_ToControl("保单分页详情",paging)

	@allure.feature("批次报案总额校验")
	@allure.severity("blocker")
	def test_zjy_Insure_005(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/edz/PycharmProjects/automan/TestFile/ZhuJingYu/zjy.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件里的环境变量
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"env")
		# 读取yaml文件里的billno
		billNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"billNo")
		# 校验批次
		dataCheck = bkw.insureApi_dataCheck({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "billNo": billNo, "sumClaim": 65.43, "totalNum": 2 },"env":env},"dict")
		# 提取批次详情
		batch = ckw.CommonKeyWord().Json_GetJsonValue(dataCheck,[["data"]])
		# 打印批次详情到控制台
		ckw.CommonKeyWord().Print_ToControl("批次报案总额校验",batch)

	@allure.feature("根据保司id、保单号 获取保单详情")
	@allure.severity("blocker")
	def test_zjy_Insure_006(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/edz/PycharmProjects/automan/TestFile/ZhuJingYu/zjy.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件里的环境变量
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"env")
		# 读取yaml文件里的投保人ID
		insurerId = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"insurerId")
		# 读取yaml文件里的保单号
		policyNo1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"policyNo1")
		# 查询保单详情
		getByInsurerIdAndPolicyNo = bkw.insureApi_getByInsurerIdAndPolicyNo({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "insurerId":insurerId , "policyNo": policyNo1 },"env":env},"dict")
		# 提取保单详情
		policyinfo = ckw.CommonKeyWord().Json_GetJsonValue(getByInsurerIdAndPolicyNo,[["data"]])
		# 打印保单详情到控制台
		ckw.CommonKeyWord().Print_ToControl("保单详情",policyinfo)


	@allure.feature("mbs-商品清算入投保理赔")
	@allure.severity("blocker")
	def test_lq_Insure_007(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - deleteOrder
		deleteOrder = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteOrder")
		# 查询SQL - deleteEquity
		deleteEquity = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteEquity")
		# 执行SQL
		deleteOrder = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",deleteOrder)
		# 执行SQL
		deleteEquity = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure", deleteEquity)
		# 执行接口-直付订单商品清算
		mbsOrderClearing = bkw.insureApi_mbsOrderClearing({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data":{ "orderDto": { "orderType": 1, "cleanStatus": 1, "cashAmount": 35.2, "channel": 1, "gmtManualCreated": "2022-06-16 11:39:44", "directAmount": 35.2, "gmtPaid": "2022-06-16 11:40:46", "couponAmount": 0, "billAmount": 35.2, "payAmount": 0, "prescriptionOrderFlag": 0, "refundNo": None, "realDiscount": 88.01, "merchantId": 635, "payMethod": 0, "unitId": 635, "discountType": 1, "directCleanAmount": 30.98, "memberId": 16234825, "saleAmount": 0, "orderSource": 0, "subsidyRate": None, "orderNo": "92061611603549650106", "shortNo": "03549650106", "storeId": 7590, "subsidyAmount": None, "hasHx": 0, "orderMethod": 3, "settledAmount": 35.2, "cooperationCode": "2018090300063453697303", "feeAmount": 0, "totalAmount": 35.2, "counterAmount": 0, "assistantId": 200825, "prescriptionOrderNum": 0, "mainOrderNo": "92061601603549640174", "gmtChanged": "2022-06-16 11:40:46", "settlementAmount": 30.98, "unionSubstituteAmount": 0, "storeCode": "2018090300758953701297" }, "orderItemDtoList": [ { "orderType": 1, "itemType": 1, "itemDiscount": 88, "directAmount": 35.2, "internalId": "2143451", "merchantSubsidyRate": None, "goodsSubType": 11, "itemName": "感冒灵胶囊", "couponAmount": 0, "itemDiscountType": 1, "directCleanAmount": 30.98, "unitPrice": 35.2, "saleAmount": 0, "goodsNo": "635-2143451", "activityAmount": 0, "orderNo": "92061611603549650106", "quantity": 1, "tradeCode": "6923718120188", "approvalNumber": "国药准字Z20055271", "pack": "", "settledAmount": 35.2, "itemId": 9909473, "totalAmount": 35.2, "form": "", "settlementAmount": 30.98, "merchantSubsidyAmount": None, "activityType": 0, "discountModel": 1 } ], "insureMemberDto": { "memberPhone": "15256908297", "memberAge": 26, "cardAddr": "安徽省淮北市濉溪县濉溪镇", "memberName": "梁琪", "cardExpiryStart": "2012-08-13", "cardNo": "340621199508206020", "memberId": None, "cardExpiryEnd": "2022-08-13" }, "orderType": 1, "orderInfoDto": { "orderType": 1, "assistantName": "梁琪", "groupId": 7, "memberName": "梁琪", "unDrug": 0, "merchantName": "国药控股国大药房上海连锁有限公司", "assistantMobile": "15256908297", "merchantId": 635, "goodsQuantity": 1, "erpSn": None, "storeName": "上海国大永和路店", "useMerchantSubsidy": None, "merchantType": 1, "specialDiseaseName": None, "memberId": 16234825, "memberIdCard": "340621199508206020", "specialDiseaseFlag": None, "orderNo": "92061611603549650106", "unitName": "国药控股国大药房上海连锁有限公司", "outType": 0, "sourceOfBusinessName": "药联健康", "assistantId": 200825, "insureType": None, "subsidyRange": None, "internalCode": "102747", "memberMobile": "15256908297", "storeCode": "2018090300758953701297" }, "orderNo": "92061611603549650106", "refundNo": None, "cobrandDetailDto": { "promotAmountDtoList": [], "activityAmountDtoList": [], "matchCobrandResp": None }, "orderEquityDtoList": [ { "memberIdCard": "340621199508206020", "orderType": 1, "orderNo": "92061611603549650106", "insurerNo": 7, "projectType": 0, "memberInfoSource": 1, "memberName": "梁琪", "policyNo": None, "auditNo": None, "transFromClean": None, "insurerName": "上海聚音信息科技有限公司", "directAmount": 35.2, "insurerCooperationCode": "2018090300000653697798", "equityGroupId": 1651, "equityName": "自付转权益专用项目", "equityNo": "1000191369097877", "equityId": 23434297, "projectName": "自付转权益-勿动", "directCleanAmount": 30.98, "projectId": 477, "memberMobile": "15256908297", "memberId": 16234825 } ], "diseaseResp": None, "orderEquityItemDtoList": [ { "orderType": 1, "itemId": 9909473, "orderNo": "92061611603549650106", "equityId": 23434297, "directCleanAmount": 30.98, "directAmount": 35.2 } ] } ,"env":envt},"dict")
		print("执行的接口：", mbsOrderClearing, type(mbsOrderClearing))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - selectEquity
		selectEquity = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectEquity")
		# 查询SQL - selectOrder
		selectOrder = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectOrder")
		# 执行SQL
		selectOrder = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure", selectOrder)
		print("执行查询sql：", selectOrder, type(selectOrder))
		# 执行SQL
		selectEquity = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",selectEquity)
		print("执行查询sql：", selectEquity, type(selectEquity))
		# SQL返回-提取数据-提取json中的对象
		sqlOrder = ckw.CommonKeyWord().Json_GetJsonValue(selectOrder[0], [["order_no"]])
		print("执行查询sql：", sqlOrder, type(sqlOrder))
		sqlEquity = ckw.CommonKeyWord().Json_GetJsonValue(selectEquity[0], [["order_no"]])
		print("执行查询sql：", sqlEquity, type(sqlEquity))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlOrder, 92061611603549650106)
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlEquity, 92061611603549650106)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("mbs-商品替换入投保理赔")
	@allure.severity("blocker")
	def test_lq_Insure_008(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - deleteEquityGoods
		deleteEquityGoods = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteEquityGoods")
		# 执行SQL
		deleteEquityGoods = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",deleteEquityGoods)
		# 执行接口-直付订单商品替换
		false = False
		mbsGoodsReplace = bkw.insureApi_mbsGoodsReplace({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": { "orderType": 1, "orderNo": "92061611603549650106", "storeInternalCode": "102747", "old": None, "specialDiseased": false, "orderGoodDtoList": [ { "orderType": 1, "itemType": 1, "originalGoodsCode": "2143451", "projectType": 0, "directAmount": 35.2, "internalId": "2143451", "invoicePriceWithTax": None, "goodsSubType": 11, "itemName": "感冒灵胶囊", "refundNo": None, "itemStatus": 0, "directCleanAmount": 30.98, "equityId": 0, "originalApprovalNo": "国药准字Z20055271", "claimProjectType": 1, "unitPrice": 35.2, "amountWithoutTax": None, "orderNo": "92061611603549650106", "quantity": 1, "tradeCode": "6923718120188", "originalGoodsName": "感冒灵胶囊", "approvalNumber": "国药准字Z20055271", "pack": "", "itemId": 9909473, "totalAmount": 35.2, "taxRate": -1, "form": "", "skuNo": "635-2143451", "invoicePriceWithoutTax": None, "taxEdClass": None, "taxEd": None, "taxAmount": None } ], "medicalDeviced": 0, "storeName": "上海国大永和路店", "supper": None, "specialDiseaseType": None, "specialDiseaseName": None }, "env": envt}, "dict")
		print("执行的接口：", mbsGoodsReplace, type(mbsGoodsReplace))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - selectEquityGoods
		selectEquityGoods = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectEquityGoods")
		# 执行SQL
		selectEquityGoods = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",selectEquityGoods)
		print("执行查询sql：", selectEquityGoods, type(selectEquityGoods))
		# SQL返回-提取数据-提取json中的对象
		sqlEquityGoods = ckw.CommonKeyWord().Json_GetJsonValue(selectEquityGoods[0], [["order_no"]])
		print("执行查询sql：", sqlEquityGoods, type(sqlEquityGoods))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(sqlEquityGoods, 92061611603549650106)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("MBS-财务结算推未理赔直付订单")
	@allure.severity("blocker")
	def test_zjy_Insure_009(self):
	    # 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 查询SQL - deleteIpackageOrder、deleteIpackageOrderReceipt
		deleteIpackageOrder = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteIpackageOrder")
		deleteIpackageOrderReceipt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteIpackageOrderReceipt")
		deleteClaim = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteIpackageOrderReceipt")
		# 执行SQL
		deleteIpackageOrder = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",deleteIpackageOrder)
		deleteIpackageOrderReceipt = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",deleteIpackageOrderReceipt)
		deleteClaim = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",deleteClaim)
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 执行接口
		mbsClaimSattleClaim = bkw.insureApi_mbsClaimSattleClaim({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": { "statementNo": "DS20220628100002", "orderNo": "92061611603549650106", "endDate": "2022-06-16", "startDate": "2022-06-16" }, "env": envt}, "dict")
		print("执行的接口：", mbsClaimSattleClaim, type(mbsClaimSattleClaim))
		# 提取数据-提取json中的对象
		mbsClaimSattleClaim = ckw.CommonKeyWord().Json_GetJsonValue(mbsClaimSattleClaim, [["data"]])
		print("提取的json：", mbsClaimSattleClaim, type(mbsClaimSattleClaim))
		mbsClaimSattleClaimOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(mbsClaimSattleClaim, [["orderNo"]])
		print("提取的data：", mbsClaimSattleClaimOrderNo, type(mbsClaimSattleClaimOrderNo))
		# # 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# # 相对路径，用于提交到Jenkins跑接口
		# # yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# # 查询SQL - deleteIpackageOrder、deleteIpackageOrderReceipt
		# selectIpackageOrder = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectIpackageOrder")
		# selectIpackageOrder = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udm_insure",selectIpackageOrder)
		# print("sql：", selectIpackageOrder, type(selectIpackageOrder))
		# # SQL返回-提取数据-提取json中的对象
		# sqlIpackageOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(selectIpackageOrder[0], [["order_no"]])
		# print("sql提取的data：", sqlIpackageOrderNo, type(sqlIpackageOrderNo))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(mbsClaimSattleClaimOrderNo, 92061611603549650106)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("MBS-推送订单理赔材料")
	@allure.severity("blocker")
	def test_zjy_Insure_010(self):
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - deleteOrderAttach
		deleteOrderAttach = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteOrderAttach")
		# 执行SQL
		deleteOrderAttach = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_middleend_mbs2",deleteOrderAttach)
		# 执行接口-MBS-推送订单理赔材料
		mbsOrderAttach = bkw.insureApi_mbsOrderAttach({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"guardianImgFront":None,"insuredImgFront":"","gmtCreated":None,"sign":None,"completeSnapshot":None,"insuredImgNegative":"","merchantName":"药联健康","insuredMemberIdCard":"411403199509056955","guardianMemberIdCard":None,"guardianCardTimeBegin":None,"insuredCardTimeEnd":"2120-01-01 00:00:00","guardianMemberName":None,"zghCompleteSnapshot":None,"storeName":"增值服务开放平台","id":None,"relationship":None,"transactionSnapshot":None,"orderNo":"92062911603641531777","insuredMemberName":"李开放","guardianMemberMobile":None,"insuredCardTimeBegin":"2020-01-01 00:00:00","cooperationCode":"2018090300053853697066","zghTransactionSnapshot":None,"prescriptionIds":None,"guardianCardTimeEnd":None,"prescription":None,"storeAddress":"上海市上海市","guardianAddress":None,"mainOrderNo":"92062901603641521733","insuredMemberMobile":"18238746835","gmtUpdated":None,"insuredAddress":"","claimSnapshot":None,"guardianImgNegative":None,"storeCode":"2018090303213953717200"}, "env": envt}, "dict")
		print("执行的接口：", mbsOrderAttach, type(mbsOrderAttach))
		# 提取数据-提取json中的对象
		errno = ckw.CommonKeyWord().Json_GetJsonValue(mbsOrderAttach, [["errno"]])
		print("提取的json：", mbsOrderAttach, type(mbsOrderAttach))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		# 相对路径，用于提交到Jenkins跑接口
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-环境域名
		# envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 查询SQL - selectOrderAttach
		# selectOrderAttach = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectOrderAttach")
		# # 执行SQL
		# selectOrderAttach = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_middleend_mbs2", selectOrderAttach)
		# # SQL返回-提取数据-提取json中的对象
		# sqlOrderAttach = ckw.CommonKeyWord().Json_GetJsonValue(selectOrderAttach[0], [["count(*)"]])
		# print("执行查询sql：", sqlOrderAttach, type(sqlOrderAttach))
		# 断言字段包含
		assert ckw.CommonKeyWord().Assert_BcharInAchar(errno, '0')
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")



