# -*- coding: utf-8 -*-
import json
import time

import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw
import KeyWordDriver.BusinesskeyWord as bkw

class Test_financeReplace:
	@allure.feature("商品替换-订单是否包含中广核实物")
	@allure.severity("blocker")
	def test_fzs_0001(self):
		"""
		订单是否包含中广核实物
		"""
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/fuzhangsong/PycharmProjects/automan/TestFile/Fzs/fzs.yaml")
		# 读取yaml文件环境域名
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		# 执行查询接口
		extreplaceReplaceOne = bkw.financeReplaceApi_replaceQueryJudeZghItem({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{ "orderNo": "92042111603412970777", "orderType": 1 },"env":envr},"dict")
		ckw.CommonKeyWord().Print_ToLog("查询订单是否包含中广核实物出参：", extreplaceReplaceOne)
		# 提取返回参数
		extreplaceReplaceOnerep = ckw.CommonKeyWord().Json_GetJsonValue(extreplaceReplaceOne,[["data"]])
		# 断言是否匹配成功
		ckw.CommonKeyWord().Assert_ObjAndObj(extreplaceReplaceOnerep, "True")


	@allure.feature("商品替换-订单商品替换")
	@allure.severity("blocker")
	def test_fzs_0002(self):
		# 读取yaml文件
		yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/fuzhangsong/PycharmProjects/automan/TestFile/Fzs/fzs.yaml")
		# 读取yaml文件预置测试订单号
		grOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"grOrderGoodsOrderno")
		# 读取yaml文件删除替换表数据SQL
		deleteGrOrderGoods = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"deleteGrOrderGoods")
		# 读取yaml文件查询替换表数据SQL
		selectGrOrderGoods = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile,"selectGrOrderGoods")
		# 读取yaml文件环境域名
		envr = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envr")
		# 执行读取的删除替换表数据SQL
		ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_union_finance", deleteGrOrderGoods)
		# 执行商品替换
		extreplaceReplaceOne = bkw.financeReplaceApi_replaceReplaceOne({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"orderDto":{"orderType":1,"cleanStatus":1,"cashAmount":0,"channel":1,"gmtManualCreated":"2022-05-06 10:07:19","directAmount":49.51,"gmtPaid":"2022-05-06 10:07:27","couponAmount":0,"billAmount":50.01,"payAmount":0,"prescriptionOrderFlag":1,"refundNo":None,"realDiscount":89.01,"merchantId":578,"payMethod":0,"unitId":161148,"discountType":1,"directCleanAmount":44.07,"memberId":16234580,"saleAmount":0,"orderSource":0,"subsidyRate":None,"orderNo":"92050611603434670103","shortNo":"03434670103","storeId":4123,"subsidyAmount":None,"hasHx":0,"orderMethod":3,"settledAmount":49.51,"cooperationCode":"2018090300057753697914","feeAmount":0,"totalAmount":50.01,"counterAmount":0,"assistantId":200760,"prescriptionOrderNum":1,"mainOrderNo":"92050601603434660162","gmtChanged":"2022-05-06 10:07:43","settlementAmount":44.07,"unionSubstituteAmount":0,"storeCode":"2018090300412253699198"},"orderItemDtoList":[{"orderType":1,"itemType":1,"itemDiscount":89,"directAmount":48.01,"internalId":"1000340","merchantSubsidyRate":None,"goodsSubType":11,"itemName":"复方感冒灵片","couponAmount":0,"itemDiscountType":1,"directCleanAmount":42.73,"unitPrice":48.01,"saleAmount":0,"goodsNo":"578-1000340","activityAmount":0,"orderNo":"92050611603434670103","quantity":1,"tradeCode":"6927771401932","approvalNumber":"国药准字Z44022554","pack":"瓶","settledAmount":48.01,"itemId":9902496,"totalAmount":48.01,"form":"6.25g*100片","settlementAmount":42.73,"merchantSubsidyAmount":None,"activityType":0,"discountModel":1},{"orderType":1,"itemType":1,"itemDiscount":89,"directAmount":0.5,"internalId":"01138","merchantSubsidyRate":None,"goodsSubType":11,"itemName":"七制香附丸","couponAmount":0,"itemDiscountType":1,"directCleanAmount":0.45,"unitPrice":1,"saleAmount":0,"goodsNo":"578-01138","activityAmount":0.5,"orderNo":"92050611603434670103","quantity":1,"tradeCode":"6931183901520","approvalNumber":"国药准字Z41020695","pack":"","settledAmount":0.5,"itemId":9902497,"totalAmount":1,"form":"6g*10袋","settlementAmount":0.45,"merchantSubsidyAmount":None,"activityType":0,"discountModel":1},{"orderType":1,"itemType":1,"itemDiscount":89,"directAmount":1,"internalId":"01138","merchantSubsidyRate":None,"goodsSubType":11,"itemName":"七制香附丸","couponAmount":0,"itemDiscountType":1,"directCleanAmount":0.89,"unitPrice":1,"saleAmount":0,"goodsNo":"578-01138","activityAmount":0,"orderNo":"92050611603434670103","quantity":1,"tradeCode":"6931183901520","approvalNumber":"国药准字Z41020695","pack":"","settledAmount":1,"itemId":9902498,"totalAmount":1,"form":"6g*10袋","settlementAmount":0.89,"merchantSubsidyAmount":None,"activityType":0,"discountModel":1}],"orderType":1,"orderInfoDto":{"orderType":1,"assistantName":"朱登虎","groupId":7,"memberName":"朱登虎","unDrug":0,"merchantName":"产品测试（商户全称）","assistantMobile":"13813904992","merchantId":578,"goodsQuantity":3,"erpSn":None,"storeName":"产品测试门店1-2（简称）","useMerchantSubsidy":None,"merchantType":1,"specialDiseaseName":None,"memberId":16234580,"memberIdCard":"320723198511280037","specialDiseaseFlag":None,"orderNo":"92050611603434670103","unitName":"RC环境测试连锁的核算单位01","outType":0,"sourceOfBusinessName":"药联健康","assistantId":200760,"insureType":None,"subsidyRange":None,"internalCode":"222","memberMobile":"13813904992","storeCode":"2018090300412253699198"},"orderNo":"92050611603434670103","refundNo":None,"cobrandDetailDto":{"promotAmountDtoList":[],"activityAmountDtoList":[],"matchCobrandResp":None},"orderEquityDtoList":[{"memberIdCard":"320723198511280037","orderType":1,"orderNo":"92050611603434670103","insurerNo":7,"projectType":0,"memberInfoSource":1,"memberName":"朱登虎","policyNo":None,"auditNo":None,"transFromClean":None,"insurerName":"上海聚音信息科技有限公司","directAmount":49.51,"insurerCooperationCode":"2018090300000653697798","equityGroupId":500840,"equityName":"药联健康权益","equityNo":"1000594258081844","equityId":23430110,"projectName":"测试项目-031601","directCleanAmount":44.07,"projectId":500093,"memberMobile":"13813904992","memberId":16234580}],"diseaseResp":None,"orderEquityItemDtoList":[{"orderType":1,"itemId":9902496,"orderNo":"92050611603434670103","equityId":23430110,"directCleanAmount":42.73,"directAmount":48.01},{"orderType":1,"itemId":9902497,"orderNo":"92050611603434670103","equityId":23430110,"directCleanAmount":0.45,"directAmount":0.5},{"orderType":1,"itemId":9902498,"orderNo":"92050611603434670103","equityId":23430110,"directCleanAmount":0.89,"directAmount":1}]},"env":envr},"dict")
		print(extreplaceReplaceOne)
		# 执行读取的查询替换表数据SQL
		time.sleep(1)
		orderNo = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_union_finance", selectGrOrderGoods)
		# 提取order_no
		print(orderNo)
		orderNo2 = ckw.CommonKeyWord().Json_GetJsonValue(orderNo[0],[["order_no"]])
		# 断言订单号
		ckw.CommonKeyWord().Assert_ObjAndObj(orderNo2, grOrderNo)


