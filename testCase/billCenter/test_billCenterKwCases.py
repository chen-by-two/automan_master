# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_billCenter:

	@allure.feature("票据中心-推送销售清单")
	@allure.severity("blocker")
	def test_lq_billCenter_0001(self):
		# 查询发票列表
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-deleteBillSale、updateBill
		deleteBillSale = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "deleteBillSale")
		updateBill = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateBill")
		# 执行sql
		deleteBillSale = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_bill",deleteBillSale)
		# print("执行查询sql：", deleteBillSale,type(deleteBillSale))
		updateBill = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_bill",updateBill)
		# print("执行查询sql：", updateBill,type(deleteBillSale))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 执行接口
		mbsBillSaleSave = bkw.billCenterApi_mbsBillSaleSave({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": { "approvalNo": "国药准字Z20055271", "taxRate": -1, "classificationCode": "", "goodsCount": 1, "form": "", "classificationName": "", "invoiceAmount": 30.98, "goodsCode": "2143451", "billNo": "20220628100679", "goodsName": "感冒灵胶囊", "pack": "" }, "env": envt}, "dict")
		print("查询接口：", mbsBillSaleSave,type(mbsBillSaleSave))
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-selectBillSale
		selectBillSale = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectBillSale")
		# 执行SQL
		selectBillSale = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_statement",selectBillSale)
		print("执行查询sql：", selectBillSale, type(selectBillSale))
		# SQL返回-提取数据-提取json中的对象
		sqlBillSale = ckw.CommonKeyWord().Json_GetJsonValue(selectBillSale[0], [["bill_no"]])
		print("执行查询sql：", sqlBillSale, type(sqlBillSale))
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(selectBillSale, 20220628100679)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("票据中心-查询发票列表")
	@allure.severity("blocker")
	def test_lq_billCenter_0002(self):
		# 查询发票列表
		# 读取yaml文件
		# yamlfile = ckw.CommonKeyWord().Yaml_Read("/Users/liangqi/PycharmProjects/automan/TestFile/LiangQi/lq.yaml")
		yamlfile = ckw.CommonKeyWord().Yaml_Read("TestFile/LiangQi/lq.yaml")
		# 读取yaml文件-selectInvoiceNo
		selectInvoiceNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "selectInvoiceNo")
		# 执行查询sql
		selectOnlineInvoice = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_udc_fin_bill",selectInvoiceNo)
		print("执行查询sql：", selectOnlineInvoice)
		# SQL返回-提取数据-提取json中的对象
		sqlInvoiceNo = ckw.CommonKeyWord().Json_GetJsonValue(selectOnlineInvoice[0], [["invoice_no"]])
		print("执行查询sql：", sqlInvoiceNo, type(sqlInvoiceNo))
		# 读取yaml文件环境域名
		envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
		# 打印域名到日志
		ckw.CommonKeyWord().Print_ToLog("当前环境脚本运行环境域名", envt)
		# 打印域名到控制台
		ckw.CommonKeyWord().Print_ToControl("当前环境脚本运行环境域名", envt)
		# 获取当前时间戳
		time = ckw.CommonKeyWord().Time_UnixTimestamp()
		# 打印当前时间戳
		ckw.CommonKeyWord().Print_ToLog("当前时间戳", time)
		# 执行查询发票信息接口
		invoicePage = bkw.billCenterApi_invoicePage({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},"data": {"page": 1, "limit": 10, "billNo": "20220517100517", "billNos": ["20220517100517"],"invoiceNo": "", "invoiceCode": "", "expressNo": "", "expressCode": "", "expressType": 1, "invoiceStatus": 2}, "env": envt}, "dict")
		print("查询发票接口：", invoicePage)
		# 提取发票列表
		invoiceNos = ckw.CommonKeyWord().Json_GetJsonValue(invoicePage, [["data", "body"]])
		print("接口提取的发票：", invoiceNos, type(invoiceNos))
		# 提取查询的第一张发票
		invoiceNo = ckw.CommonKeyWord().Json_GetJsonValue(invoiceNos[0], [["invoiceNo"]])
		print("提取的发票：", invoiceNo, type(invoiceNo))
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("invoiceNo:", invoiceNo)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("invoiceNo:", invoiceNo)
		# 断言对比对象
		assert ckw.CommonKeyWord().Assert_BcharInAchar(invoiceNo, sqlInvoiceNo)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")


