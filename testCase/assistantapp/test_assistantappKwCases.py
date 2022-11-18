# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_assistantapp:

	@allure.feature("更新助手表数据-读取文件")
	@allure.severity("blocker")
	def test_zjc_UpdateData_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml删除ob表数据sql
		delete_obsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"delete_ob")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",delete_obsql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",delete_obsql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",delete_obsql)
		# 读取yaml新建ob表数据sql
		create_obsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"create_ob")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",create_obsql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",create_obsql,"111.0")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",create_obsql)
		# 读取yaml新建ob表数据sql
		insert_obsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"insert_ob")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",insert_obsql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",insert_obsql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",insert_obsql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("10.0")

	@allure.feature("更新助手表数据-读取文件")
	@allure.severity("blocker")
	def test_zjc_UpdateData_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml删除oi表数据sql
		delete_oisql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"delete_oi")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",delete_oisql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",delete_oisql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",delete_oisql)
		# 读取yaml新建oi表数据sql
		create_oisql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"create_oi")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",create_oisql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",create_oisql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",create_oisql)
		# 读取yaml新建oi表数据sql
		insert_oisql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"insert_oi")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",insert_oisql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",insert_oisql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",insert_oisql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("10.0")

	@allure.feature("更新助手表数据-读取文件")
	@allure.severity("blocker")
	def test_zjc_UpdateData_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml删除oi表数据sql
		delete_assql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"delete_as")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",delete_assql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",delete_assql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",delete_assql)
		# 读取yaml新建oi表数据sql
		create_assql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"create_as")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",create_assql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",create_assql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",create_assql)
		# 读取yaml新建oi表数据sql
		insert_assql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"insert_as")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",insert_assql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",insert_assql)
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",insert_assql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("10.0")

	@allure.feature("客户管理-查询客户")
	@allure.severity("blocker")
	def test_zjc_CustomerPaging_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录发送验证码
		bkw.assistantappApi_CodeSend({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer"},"parma":{},"data":{"type":"login","mobile":mobile},"env":env},"dict")
		# 从数据库提取验证码-获取原始sql
		tmpSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# 从数据库提取验证码-修改sql where条件
		finSql = ckw.CommonKeyWord().Str_Replace(tmpSql,18099990000,mobile)
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",finSql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",finSql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"udtest.uniondrug.com","port":"6033","username":"test","password":"tset@321abc","database":"cn_uniondrug_module_data","sql":finSql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",sqlRes)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",sqlRes)
		# 从数据库提取验证码-提取验证码01
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0],[["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：",captcha)
		# 打印验证码到日志
		ckw.CommonKeyWord().Print_ToLog("验证码：",captcha)
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserSmsLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":captcha},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 客户管理列表页-调取接口
		CustomerPaging = bkw.assistantappApi_CustomerPaging({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"userId":userid,"page":"1","limit":"10"},"env":env},"dict")
		# 提取客户列表errno
		CustomerPagingerrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerPaging,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Pagingerrno:",CustomerPagingerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Pagingerrno:",CustomerPagingerrno)
		# 读取yaml里客户列表断言
		CustomerPagingAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerPagingAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("客户列表断言结果：",CustomerPagingAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerPagingerrno,CustomerPagingAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("客户管理-查询客户-客户管理详情")
	@allure.severity("blocker")
	def test_zjc_Customerinfo_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 客户管理详情页-调取接口
		CustomerInfo = bkw.assistantappApi_CustomerInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"userId":userid,"customerId": "7159"},"env":env},"dict")
		# 提取客户详情contacts
		contacts = ckw.CommonKeyWord().Json_GetJsonValue(CustomerInfo,[["data","contacts"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("contacts:",contacts)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("contacts:",contacts)
		# 读取yaml里客户详情断言
		CustomerInfoAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerInfoAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("客户详情断言结果：",CustomerInfoAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(contacts,CustomerInfoAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("客户管理-新增客户-密码登录")
	@allure.severity("blocker")
	def test_zjc_Customeradd_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 客户管理新增客户-调取接口
		CustomerAdd = bkw.assistantappApi_CustomerAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"tags":[{"tagId":"50","tagName":"云联业务","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"49","tagName":"自主报名","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"48","tagName":"意向不明","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"47","tagName":"意向签约","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"4","tagName":"短期客户","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"3","tagName":"长期客户","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"2","tagName":"合作意愿弱","is_select":"0","customerId":"","id":"","sort":"0"},{"tagId":"1","tagName":"合作意愿强","is_select":"0","customerId":"","id":"","sort":"0"}],"customerName":"南京艾小宝保险有限公司03","customerType":"2","customerTypeText":"保司","customerStatus":"0","customerStatusText":"未签约","level":"2","levelText":"省级分公司","longitude":"118.778598","latitude":"31.973037","address":"江苏省南京市雨花台区花神大道23号","userId":userid,"customerId":"","contacts":[{"contactName":"啦啦啦","weixinUrl":"","address":"","sex":"1","mobile":"15988663966","position":"测测测","userId":userid,"customerId":""}]},"env":env},"dict")
		# 提取新增客户errno
		CustomerAdderrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerAdd,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Adderrno:",CustomerAdderrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Adderrno:",CustomerAdderrno)
		# 读取yaml新增客户断言
		CustomerAddAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerAddAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("新增客户断言结果：",CustomerAddAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerAdderrno,CustomerAddAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("客户管理-编辑客户")
	@allure.severity("blocker")
	def test_zjc_Customeredit_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 客户管理编辑客户-调取接口
		CustomerEdit = bkw.assistantappApi_CustomerEdit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "contacts": [{
  "contactId": "603",
  "customerId": "5787",
  "userId": "287",
  "contactName": "明年",
  "sex": "0",
  "sexText": "女",
  "mobile": "15233312221",
  "phone": "",
  "department": "",
  "position": "测测",
  "address": "",
  "houseNumber": "",
  "longitude": "0.000000",
  "latitude": "0.000000",
  "weixinUrl": "",
  "remark": "",
  "gmtCreated": "2020-10-26 11:13:59",
  "gmtUpdated": "2020-10-26 11:13:59"
 }],
 "images": [],
 "tags": [{
  "tagId": "50",
  "tagName": "云联业务",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "49",
  "tagName": "自主报名",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "48",
  "tagName": "意向不明",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "47",
  "tagName": "意向签约",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "4",
  "tagName": "短期客户",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "3",
  "tagName": "长期客户",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "2",
  "tagName": "合作意愿弱",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }, {
  "tagId": "1",
  "tagName": "合作意愿强",
  "is_select": "0",
  "customerId": "5787",
  "id": "",
  "sort": "0"
 }],
 "pbmInfo": "",
 "chainInfo": "",
 "report": [],
 "statusText": "",
 "customerId": "5787",
 "userId": "287",
 "type": "1",
 "customerName": "飞龙大药房",
 "pinyin": "",
 "customerType": "4",
 "customerTypeText": "云联门店",
 "customerStatus": "0",
 "customerStatusText": "无意向未签约",
 "grade": "0",
 "gradeText": "未知",
 "mobile": "",
 "level": "1",
 "levelText": "总公司",
 "longitude": "0.000000",
 "latitude": "0.000000",
 "distance": "0",
 "address": "陕西省渭南市",
 "houseNumber": "",
 "zipCode": "",
 "fax": "",
 "remark": "",
 "organizationName": "",
 "cooperationCode": "",
 "organizationId": "0",
 "partnerId": "0",
 "gmtCreated": "2020-09-27 15:46:35",
 "gmtUpdated": "2020-10-26 11:16:09",
 "poolPartnerId": "201984",
 "applyId": "984",
 "applyStoreId": "0",
 "insuranceApplyId": "0",
 "topStatus": "0",
 "visitStatus": "1",
 "visitStatusText": ""
},"env":env},"dict")
		# 提取编辑客户errno
		CustomerEditerrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerEdit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Editerrno:",CustomerEditerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Editerrno:",CustomerEditerrno)
		# 读取yaml编辑客户断言
		CustomerEditAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerEditAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("编辑客户断言结果：",CustomerEditAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerEditerrno,CustomerEditAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("客户管理-删除客户")
	@allure.severity("blocker")
	def test_zjc_Customerdelete_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 客户管理删除客户-调取接口
		CustomerDelete = bkw.assistantappApi_CustomerDelete({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":
{
 "customerId": "7159",
 "reasonId": "1",
 "other": ""
}
  ,"env":env},"dict")
		# 提取删除客户errno
		CustomerDeleteerrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerDelete,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Deleteerrno:",CustomerDeleteerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Deleteerrno:",CustomerDeleteerrno)
		# 读取yaml删除客户断言
		CustomerDeleteAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerDeleteAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("删除客户断言结果：",CustomerDeleteAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerDeleteerrno,CustomerDeleteAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 读取yaml更新客户sql
		updateCustomersql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"updateCustomersql")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",updateCustomersql)
		# 读取yaml删除客户sql
		deleteCustomersql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"deleteCustomersql")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",deleteCustomersql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("客户管理-客户拜访")
	@allure.severity("blocker")
	def test_zjc_Customerconvisit_005(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 客户管理添加拜访-调取接口
		VisitAddCommonVisit = bkw.assistantappApi_VisitAddCommonVisit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":
{
 "userId": "306",
 "userName": "张大仙",
 "customerId": "7159",
 "customerName": "测试新增客户自动化（勿动）",
 "visitType": "1",
 "content": "添加计划拜访",
 "visitDate": "2020-11-06"
},"env":env},"dict")
		# 提取添加拜访errno
		Customervisiterrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitAddCommonVisit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("visiterrno:",Customervisiterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("visiterrno:",Customervisiterrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("添加拜访断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(Customervisiterrno,Errno)
		# 客户管理到达总部-调取接口
		VisitArrivalVisit = bkw.assistantappApi_VisitArrivalVisit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":
{
 "customer": {
  "contacts": [{
   "contactId": "615",
   "customerId": "7159",
   "userId": "306",
   "contactName": "张大仙",
   "sex": "0",
   "sexText": "女",
   "mobile": "15233331112",
   "phone": "",
   "department": "",
   "position": "测测测",
   "address": "",
   "houseNumber": "",
   "longitude": "0.000000",
   "latitude": "0.000000",
   "weixinUrl": "",
   "remark": "",
   "gmtCreated": "2020-11-06 15:27:43",
   "gmtUpdated": "2020-11-06 15:27:43"
  }],
  "images": [],
  "tags": [{
   "tagName": "云联业务",
   "id": "5416",
   "customerId": "7159",
   "tagId": "50",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "自主报名",
   "id": "5417",
   "customerId": "7159",
   "tagId": "49",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "意向不明",
   "id": "5418",
   "customerId": "7159",
   "tagId": "48",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "意向签约",
   "id": "5419",
   "customerId": "7159",
   "tagId": "47",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "短期客户",
   "id": "5420",
   "customerId": "7159",
   "tagId": "4",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "长期客户",
   "id": "5421",
   "customerId": "7159",
   "tagId": "3",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "合作意愿弱",
   "id": "5422",
   "customerId": "7159",
   "tagId": "2",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "合作意愿强",
   "id": "5423",
   "customerId": "7159",
   "tagId": "1",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }],
  "pbmInfo": "",
  "chainInfo": "",
  "report": [],
  "statusText": "",
  "customerId": "7159",
  "userId": "306",
  "type": "1",
  "customerName": "测试新增客户自动化",
  "pinyin": "测试新增客户自动化",
  "customerType": "1",
  "customerTypeText": "连锁药店",
  "customerStatus": "3",
  "customerStatusText": "有意向未签约",
  "grade": "0",
  "gradeText": "未知",
  "mobile": "",
  "level": "2",
  "levelText": "省级分公司",
  "longitude": "118.779335",
  "latitude": "31.971964",
  "distance": "0",
  "address": "江苏省南京市雨花台区凤信路6号金证南京科技园2号楼中梁地产集团财务共享服务中心",
  "houseNumber": "",
  "zipCode": "",
  "fax": "",
  "remark": "",
  "organizationName": "",
  "cooperationCode": "",
  "organizationId": "0",
  "partnerId": "0",
  "gmtCreated": "2020-11-06 15:27:42",
  "gmtUpdated": "2020-11-06 15:27:42",
  "poolPartnerId": "0",
  "applyId": "0",
  "applyStoreId": "0",
  "insuranceApplyId": "0",
  "topStatus": "0",
  "visitStatus": "0",
  "visitStatusText": ""
 },
 "subCustomer": {
  "contacts": [],
  "images": [],
  "tags": [],
  "pbmInfo": {
   "pbmNum": "0",
   "notPbmNum": "0"
  },
  "chainInfo": {
   "store_count_of_partner": "0",
   "assistant_count_of_partner": "0",
   "fund_pool": "0"
  },
  "report": [],
  "statusText": "",
  "customerId": "0",
  "userId": "0",
  "type": "0",
  "customerName": "",
  "pinyin": "",
  "customerType": "0",
  "customerTypeText": "",
  "customerStatus": "0",
  "customerStatusText": "",
  "grade": "0",
  "gradeText": "",
  "mobile": "",
  "level": "0",
  "levelText": "",
  "longitude": "",
  "latitude": "",
  "distance": "0",
  "address": "",
  "houseNumber": "",
  "zipCode": "",
  "fax": "",
  "remark": "",
  "organizationName": "",
  "cooperationCode": "",
  "organizationId": "0",
  "partnerId": "0",
  "gmtCreated": "",
  "gmtUpdated": "",
  "poolPartnerId": "0",
  "applyId": "0",
  "applyStoreId": "0",
  "insuranceApplyId": "0",
  "topStatus": "0",
  "visitStatus": "0",
  "visitStatusText": ""
 },
 "images": [],
 "users": {
  "v4Role": "",
  "id": "306",
  "account": "18099990000",
  "member_id": "15961232",
  "full_name": "张大仙",
  "role": "0",
  "status": "1",
  "created_at": "2020-03-11 01:09:59",
  "updated_at": "2020-11-06 15:26:20",
  "last_login_at": "2020-11-06 15:26:20",
  "head_img": "",
  "app_version": "",
  "superuser": "0",
  "superior": "0",
  "role_id": "0"
 },
 "name": "",
 "userName": "张大仙",
 "isDataComplete": "1",
 "partnerId": "0",
 "visitId": "1331",
 "customerId": "7159",
 "userId": "306",
 "content": "添加计划拜访",
 "visitType": "1",
 "visitTypeText": "常规拜访",
 "visitDate": "2020-11-06",
 "visitStatus": "1",
 "visitStatusText": "计划拜访",
 "arrivalTime": "2020-11-06 15:39:01",
 "departureTime": "",
 "summary": "",
 "description": "",
 "address": "",
 "longitude": "0.000000",
 "latitude": "0.000000",
 "overDistance": "0",
 "gmtCreated": "2020-11-06 15:33:26",
 "gmtUpdated": "2020-11-06 15:39:01",
 "isTempCustomerVisit": "0",
 "comment": "",
 "customerName": "测试新增客户自动化",
 "subCustomerName": ""
},"env":env},"dict")
		# 提取到达总部errno
		VisitArrivalerrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitArrivalVisit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Arrivalerrno:",VisitArrivalerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Arrivalerrno:",VisitArrivalerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("到达总部断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(VisitArrivalerrno,Errno)
		# 读取yaml更新到达时间sql
		updateCustomerTimesql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"updateCustomerTimesql")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",updateCustomerTimesql)
		# 客户管理完成拜访-调取接口
		VisitVisitComplete = bkw.assistantappApi_VisitVisitComplete({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":
{
 "customer": {
  "contacts": [{
   "contactId": "615",
   "customerId": "7159",
   "userId": "306",
   "contactName": "张大仙",
   "sex": "0",
   "sexText": "女",
   "mobile": "15233331112",
   "phone": "",
   "department": "",
   "position": "测测测",
   "address": "",
   "houseNumber": "",
   "longitude": "0.000000",
   "latitude": "0.000000",
   "weixinUrl": "",
   "remark": "",
   "gmtCreated": "2020-11-06 15:27:43",
   "gmtUpdated": "2020-11-06 15:27:43"
  }],
  "images": [],
  "tags": [{
   "tagName": "云联业务",
   "id": "5416",
   "customerId": "7159",
   "tagId": "50",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "自主报名",
   "id": "5417",
   "customerId": "7159",
   "tagId": "49",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "意向不明",
   "id": "5418",
   "customerId": "7159",
   "tagId": "48",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "意向签约",
   "id": "5419",
   "customerId": "7159",
   "tagId": "47",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "短期客户",
   "id": "5420",
   "customerId": "7159",
   "tagId": "4",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "长期客户",
   "id": "5421",
   "customerId": "7159",
   "tagId": "3",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "合作意愿弱",
   "id": "5422",
   "customerId": "7159",
   "tagId": "2",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "合作意愿强",
   "id": "5423",
   "customerId": "7159",
   "tagId": "1",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }],
  "pbmInfo": "",
  "chainInfo": "",
  "report": [],
  "statusText": "",
  "customerId": "7159",
  "userId": "306",
  "type": "1",
  "customerName": "测试新增客户自动化",
  "pinyin": "测试新增客户自动化",
  "customerType": "1",
  "customerTypeText": "连锁药店",
  "customerStatus": "3",
  "customerStatusText": "有意向未签约",
  "grade": "0",
  "gradeText": "未知",
  "mobile": "",
  "level": "2",
  "levelText": "省级分公司",
  "longitude": "118.779335",
  "latitude": "31.971964",
  "distance": "0",
  "address": "江苏省南京市雨花台区凤信路6号金证南京科技园2号楼中梁地产集团财务共享服务中心",
  "houseNumber": "",
  "zipCode": "",
  "fax": "",
  "remark": "",
  "organizationName": "",
  "cooperationCode": "",
  "organizationId": "0",
  "partnerId": "0",
  "gmtCreated": "2020-11-06 15:27:42",
  "gmtUpdated": "2020-11-06 15:27:42",
  "poolPartnerId": "0",
  "applyId": "0",
  "applyStoreId": "0",
  "insuranceApplyId": "0",
  "topStatus": "0",
  "visitStatus": "0",
  "visitStatusText": ""
 },
 "subCustomer": {
  "contacts": [],
  "images": [],
  "tags": [],
  "pbmInfo": {
   "pbmNum": "0",
   "notPbmNum": "0"
  },
  "chainInfo": {
   "store_count_of_partner": "0",
   "assistant_count_of_partner": "0",
   "fund_pool": "0"
  },
  "report": [],
  "statusText": "",
  "customerId": "0",
  "userId": "0",
  "type": "0",
  "customerName": "",
  "pinyin": "",
  "customerType": "0",
  "customerTypeText": "",
  "customerStatus": "0",
  "customerStatusText": "",
  "grade": "0",
  "gradeText": "",
  "mobile": "",
  "level": "0",
  "levelText": "",
  "longitude": "",
  "latitude": "",
  "distance": "0",
  "address": "",
  "houseNumber": "",
  "zipCode": "",
  "fax": "",
  "remark": "",
  "organizationName": "",
  "cooperationCode": "",
  "organizationId": "0",
  "partnerId": "0",
  "gmtCreated": "",
  "gmtUpdated": "",
  "poolPartnerId": "0",
  "applyId": "0",
  "applyStoreId": "0",
  "insuranceApplyId": "0",
  "topStatus": "0",
  "visitStatus": "0",
  "visitStatusText": ""
 },
 "images": [{
  "imgUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/v3063oba4f3m9r4idtbbrni1us.jpg",
  "visitId": "1331"
 }],
 "users": {
  "v4Role": "",
  "id": "306",
  "account": "18099990000",
  "member_id": "15961232",
  "full_name": "张大仙",
  "role": "0",
  "status": "1",
  "created_at": "2020-03-11 01:09:59",
  "updated_at": "2020-11-06 15:26:20",
  "last_login_at": "2020-11-06 15:26:20",
  "head_img": "",
  "app_version": "",
  "superuser": "0",
  "superior": "0",
  "role_id": "0"
 },
 "name": "",
 "userName": "张大仙",
 "isDataComplete": "1",
 "partnerId": "0",
 "visitId": "1331",
 "customerId": "7159",
 "userId": "306",
 "content": "添加计划拜访",
 "visitType": "1",
 "visitTypeText": "常规拜访",
 "visitDate": "2020-11-06",
 "visitStatus": "2",
 "visitStatusText": "已到达",
 "arrivalTime": "2020-11-06 15:40:37",
 "departureTime": "",
 "summary": "测试拜访自动化",
 "description": "",
 "address": "",
 "longitude": "0.000000",
 "latitude": "0.000000",
 "overDistance": "0",
 "gmtCreated": "2020-11-06 15:33:26",
 "gmtUpdated": "2020-11-06 15:40:37",
 "isTempCustomerVisit": "0",
 "comment": "",
 "subCustomerId": "0",
 "customerName": "测试新增客户自动化",
 "customerStatus": "3",
 "customerStatusText": "有意向未签约"
},"env":env},"dict")
		# 提取完成拜访errno
		VisitCompleteerrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitVisitComplete,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Arrivalerrno:",VisitCompleteerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Arrivalerrno:",VisitCompleteerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("完成常规拜访断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(VisitCompleteerrno,Errno)
		# 读取yaml删除客户sql
		deleteCommonVisitsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"deleteCommonVisitsql")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",deleteCommonVisitsql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("客户管理-客户临时拜访")
	@allure.severity("blocker")
	def test_zjc_Customertemvisit_006(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 添加临时拜访-调取接口
		VisitAddInterimVisit = bkw.assistantappApi_VisitAddInterimVisit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":
{
 "userId": "306",
 "visitId": "",
 "userName": "张大仙",
 "customerId": "7159",
 "customerName": "测试新增客户自动化（勿动）",
 "subCustomerName": "",
 "subCustomerAddress": "",
 "customerLongitude": "",
 "customerLatitude": "",
 "visitType": "2",
 "content": "",
 "visitDate": "2020-11-18",
 "overDistance": "0",
 "longitude": "118.779335",
 "latitude": "31.971964"
},"env":env},"dict")
		# 提取添加拜访errno
		InterimVisiterrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitAddInterimVisit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InterimVisiterrno:",InterimVisiterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InterimVisiterrno:",InterimVisiterrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("添加临时拜访断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InterimVisiterrno,Errno)
		# 完成临时拜访-调取接口
		VisitVisitComplete = bkw.assistantappApi_VisitVisitComplete({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":
{
 "customer": {
  "contacts": [{
   "contactId": "615",
   "customerId": "7159",
   "userId": "306",
   "contactName": "张大仙",
   "sex": "0",
   "sexText": "女",
   "mobile": "15233331112",
   "phone": "",
   "department": "",
   "position": "测测测",
   "address": "",
   "houseNumber": "",
   "longitude": "0.000000",
   "latitude": "0.000000",
   "weixinUrl": "",
   "remark": "",
   "gmtCreated": "2020-11-06 15:27:43",
   "gmtUpdated": "2020-11-06 15:27:43"
  }],
  "images": [],
  "tags": [{
   "tagName": "云联业务",
   "id": "5416",
   "customerId": "7159",
   "tagId": "50",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "自主报名",
   "id": "5417",
   "customerId": "7159",
   "tagId": "49",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "意向不明",
   "id": "5418",
   "customerId": "7159",
   "tagId": "48",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "意向签约",
   "id": "5419",
   "customerId": "7159",
   "tagId": "47",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "短期客户",
   "id": "5420",
   "customerId": "7159",
   "tagId": "4",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "长期客户",
   "id": "5421",
   "customerId": "7159",
   "tagId": "3",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "合作意愿弱",
   "id": "5422",
   "customerId": "7159",
   "tagId": "2",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }, {
   "tagName": "合作意愿强",
   "id": "5423",
   "customerId": "7159",
   "tagId": "1",
   "sort": "0",
   "is_select": "0",
   "selectText": "未选中"
  }],
  "pbmInfo": "",
  "chainInfo": "",
  "report": [],
  "statusText": "",
  "customerId": "7159",
  "userId": "306",
  "type": "1",
  "customerName": "测试新增客户自动化（勿动）",
  "pinyin": "测试新增客户自动化（勿动）",
  "customerType": "1",
  "customerTypeText": "连锁药店",
  "customerStatus": "3",
  "customerStatusText": "有意向未签约",
  "grade": "0",
  "gradeText": "未知",
  "mobile": "",
  "level": "2",
  "levelText": "省级分公司",
  "longitude": "118.779335",
  "latitude": "31.971964",
  "distance": "0",
  "address": "江苏省南京市雨花台区凤信路6号金证南京科技园2号楼中梁地产集团财务共享服务中心",
  "houseNumber": "",
  "zipCode": "",
  "fax": "",
  "remark": "",
  "organizationName": "",
  "cooperationCode": "",
  "organizationId": "0",
  "partnerId": "0",
  "gmtCreated": "2020-11-06 15:27:42",
  "gmtUpdated": "2020-11-18 15:46:06",
  "poolPartnerId": "0",
  "applyId": "0",
  "applyStoreId": "0",
  "insuranceApplyId": "0",
  "topStatus": "0",
  "visitStatus": "1",
  "visitStatusText": ""
 },
 "subCustomer": {
  "contacts": [],
  "images": [],
  "tags": [],
  "pbmInfo": {
   "pbmNum": "0",
   "notPbmNum": "0"
  },
  "chainInfo": {
   "store_count_of_partner": "0",
   "assistant_count_of_partner": "0",
   "fund_pool": "0"
  },
  "report": [],
  "statusText": "",
  "customerId": "0",
  "userId": "0",
  "type": "0",
  "customerName": "",
  "pinyin": "",
  "customerType": "0",
  "customerTypeText": "",
  "customerStatus": "0",
  "customerStatusText": "",
  "grade": "0",
  "gradeText": "",
  "mobile": "",
  "level": "0",
  "levelText": "",
  "longitude": "",
  "latitude": "",
  "distance": "0",
  "address": "",
  "houseNumber": "",
  "zipCode": "",
  "fax": "",
  "remark": "",
  "organizationName": "",
  "cooperationCode": "",
  "organizationId": "0",
  "partnerId": "0",
  "gmtCreated": "",
  "gmtUpdated": "",
  "poolPartnerId": "0",
  "applyId": "0",
  "applyStoreId": "0",
  "insuranceApplyId": "0",
  "topStatus": "0",
  "visitStatus": "0",
  "visitStatusText": ""
 },
 "images": [{
  "imgUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/d8a1l2eiklq1jpca7kgoovmmc9.jpg",
  "visitId": "1359"
 }],
 "users": {
  "v4Role": "",
  "id": "306",
  "account": "18099990000",
  "member_id": "15961232",
  "full_name": "张大仙",
  "role": "0",
  "status": "1",
  "created_at": "2020-03-11 01:09:59",
  "updated_at": "2020-11-18 16:48:17",
  "last_login_at": "2020-11-18 16:48:17",
  "head_img": "",
  "app_version": "",
  "superuser": "0",
  "superior": "0",
  "role_id": "0"
 },
 "name": "",
 "userName": "张大仙",
 "isDataComplete": "1",
 "partnerId": "0",
 "visitId": "1359",
 "customerId": "7159",
 "userId": "306",
 "content": "",
 "visitType": "2",
 "visitTypeText": "临时拜访",
 "visitDate": "2020-11-18",
 "visitStatus": "2",
 "visitStatusText": "已到达",
 "arrivalTime": "2020-11-18 16:51:18",
 "departureTime": "",
 "summary": "咯您嘻嘻嘻一下",
 "description": "",
 "address": "",
 "longitude": "0.000000",
 "latitude": "0.000000",
 "overDistance": "0",
 "gmtCreated": "2020-11-18 16:51:18",
 "gmtUpdated": "2020-11-18 16:51:18",
 "isTempCustomerVisit": "0",
 "comment": "",
 "subCustomerId": "0",
 "customerName": "测试新增客户自动化（勿动）",
 "customerStatus": "3",
 "customerStatusText": "有意向未签约"
},"env":env},"dict")
		# 提取完成拜访errno
		VisitCompleteerrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitVisitComplete,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Arrivalerrno:",VisitCompleteerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Arrivalerrno:",VisitCompleteerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("完成临时拜访断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(VisitCompleteerrno,Errno)
		# 读取yaml删除客户sql
		deletelnterimVisitsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"deletelnterimVisitsql")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",deletelnterimVisitsql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("客户拜访-查询拜访列表")
	@allure.severity("blocker")
	def test_zjc_Customervisitinfo_007(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 拜访列表页-调取接口
		VisitPaging = bkw.assistantappApi_VisitPaging({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "visitStatus": [3, 5],
 "fromDate": "2020-11-18",
 "endDate": "2020-11-18",
 "manageId": "",
 "manageName": "",
 "customerName": "",
 "page": "1"
},"env":env},"dict")
		# 提取拜访列表errno
		VisitPagingerrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitPaging,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("VisitPagingerrno:",VisitPagingerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("VisitPagingerrno:",VisitPagingerrno)
		# 读取yaml里客户列表断言
		CustomerPagingAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerPagingAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("客户列表断言结果：",CustomerPagingAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(VisitPagingerrno,CustomerPagingAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")
		# 拜访详情页-调取接口
		VisitInfo = bkw.assistantappApi_VisitInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"userId":userid,"visitId": "1359"},"env":env},"dict")
		# 提取拜访详情errno
		VisitInfoerrno = ckw.CommonKeyWord().Json_GetJsonValue(VisitInfo,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("VisitInfoerrno:",VisitInfoerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("VisitInfoerrno:",VisitInfoerrno)
		# 读取yaml里客户列表断言
		CustomerPagingAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerPagingAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("客户列表断言结果：",CustomerPagingAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(VisitInfoerrno,CustomerPagingAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("巡店管理-新建巡店计划")
	@allure.severity("blocker")
	def test_zjc_CustomerInspect_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 新建巡店距离过远-调取接口
		InspectStart = bkw.assistantappApi_InspectStart({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "mapLon": "189.779305",
 "storeId": "105981",
 "remark": "距离过远自动化测试",
 "mapLat": "31.971830",
 "address": "江苏省南京市雨花台区凤信路靠近泽天能源东楼"
},"env":env},"dict")
		# 提取新建巡店计划返回
		InspectStarterrno = ckw.CommonKeyWord().Json_GetJsonValue(InspectStart,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InspectStarterrno:",InspectStarterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InspectStarterrno:",InspectStarterrno)
		# 读取yaml添加拜访断言
		InspectStartAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"InspectStartAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("新建巡店距离过远断言结果：",InspectStartAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InspectStarterrno,InspectStartAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("巡店管理-新建巡店成功")
	@allure.severity("blocker")
	def test_zjc_CustomerInspect_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 新建巡店计划完成-调取接口
		InspectStart1 = bkw.assistantappApi_InspectStart({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "mapLon": "118.779305",
 "storeId": "133444",
 "remark": "新建巡店计划成功",
 "mapLat": "31.971830",
 "address": "江苏省南京市雨花台区凤信路靠近泽天能源东楼"
},"env":env},"dict")
		# 提取新建巡店计划返回
		InspectStarterrno1 = ckw.CommonKeyWord().Json_GetJsonValue(InspectStart1,[["errno"]])
		# 提取新建巡店计划id
		InspectStartid = ckw.CommonKeyWord().Json_GetJsonValue(InspectStart1,[["data","id"]])
		# 打印id到控制台
		ckw.CommonKeyWord().Print_ToControl("id：",InspectStartid)
		# 打印id到日志
		ckw.CommonKeyWord().Print_ToLog("id：",InspectStartid)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("新建巡店计划成功断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InspectStarterrno1,Errno)
		# 读取yaml更新到达时间sql
		updateInspectTimesql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"updateInspectTimesql")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",updateInspectTimesql)
		# 完成巡店计划成功-调取接口
		InspectUpdate = bkw.assistantappApi_InspectUpdate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "address": "江苏省南京市雨花台区文竹路6号靠近金证南京科技园(装修中)",
    "mapLat": "31.971863",
    "images": [
        {
            "type": "1",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/rj2vsa87p50vbrsk4kpmc9fv00.jpg"
        },
        {
            "type": "2",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/1jpt6pvehpumq0mr8q6bre5v3g.jpg"
        },
        {
            "type": "2",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/rt94ajrbkvu3gg8d21totdigtd.jpg"
        },
        {
            "type": "3",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/h641j3t4hophjsu7hdgpgj1dl8.jpg"
        },
        {
            "type": "3",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/rv2mddludqqa98tg861fjns6gq.jpg"
        },
        {
            "type": "5",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/89o81r4t7tubni5p64qq68nnhk.jpg"
        },
        {
            "type": "5",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/v3480umh9pflma937iel2pvjco.jpg"
        },
        {
            "type": "4",
            "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/i34o0su3qr5lutdo023e8po0gs.jpg"
        }
    ],
    "inspectId": InspectStartid,
    "remark": "自动化测试巡店完成",
    "summary": [
        "1",
        "2",
        "3",
        "4"
    ],
    "storeId": "133444",
    "mapLon": "118.779335"
},"env":env},"dict")
		# 提取完成巡店成功返回
		InspectUpdateerrno = ckw.CommonKeyWord().Json_GetJsonValue(InspectUpdate,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InspectStarterrno:",InspectUpdateerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InspectStarterrno:",InspectUpdateerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("完成巡店计划成功断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InspectUpdateerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("巡店管理-巡店记录列表")
	@allure.severity("blocker")
	def test_zjc_CustomerInspect_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 巡店记录列表-调取接口
		InspectList = bkw.assistantappApi_InspectList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "endTime": "2020-11-18 23:59:59",
 "partnerId": "",
 "limit": "10",
 "storeName": "",
 "storeId": "",
 "startTime": "2020-11-18 00:00:00",
 "page": "1"
},"env":env},"dict")
		# 提取巡店记录列表返回
		InspectListerrno = ckw.CommonKeyWord().Json_GetJsonValue(InspectList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InspectListerrno:",InspectListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InspectListerrno:",InspectListerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("巡店记录列表成功断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InspectListerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("巡店管理-巡店记录详情")
	@allure.severity("blocker")
	def test_zjc_CustomerInspect_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 巡店记录详情-调取接口
		InspectDetail = bkw.assistantappApi_InspectDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "id": "50511"
},"env":env},"dict")
		# 提取巡店记录详情返回
		InspectDetailerrno = ckw.CommonKeyWord().Json_GetJsonValue(InspectDetail,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InspectDetailerrno:",InspectDetailerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InspectDetailerrno:",InspectDetailerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("巡店记录详情成功断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(InspectDetailerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("商户管理-商户管理列表")
	@allure.severity("blocker")
	def test_zjc_MerchantList_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 商户管理列表-调取接口
		MerchantList = bkw.assistantappApi_MerchantList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "limit": "10",
 "page": "1",
 "common_name": "",
 "userId": "306"
},"env":env},"dict")
		# 提取商户管理列表返回
		MerchantListerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantListerrno:",MerchantListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantListerrno:",MerchantListerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("商户管理列表断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantListerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("商户管理-商户管理详情")
	@allure.severity("blocker")
	def test_zjc_MerchantInfo_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 商户管理详情-调取接口
		MerchantInfo = bkw.assistantappApi_MerchantInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"partnerId":"3"},"env":env},"dict")
		# 提取商户管理详情返回
		MerchantInfoerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantInfo,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantInfoerrno:",MerchantInfoerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantInfoerrno:",MerchantInfoerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("商户管理详情断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantInfoerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店管理-门店管理列表")
	@allure.severity("blocker")
	def test_zjc_MerchantStore_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 门店管理列表-调取接口
		MerchantStoreList = bkw.assistantappApi_MerchantStoreList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": "1"
},"env":env},"dict")
		# 提取门店管理列表返回
		MerchantStoreListerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantStoreList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantStoreListerrno:",MerchantStoreListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantStoreListerrno:",MerchantStoreListerrno)
		# 读取yaml添加拜访断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店管理列表断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantStoreListerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店管理-门店管理详情")
	@allure.severity("blocker")
	def test_zjc_MerchantStore_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 门店管理详情-调取接口
		MerchantStoreDetail = bkw.assistantappApi_MerchantStoreDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "storeId": "125756"
},"env":env},"dict")
		# 提取门店管理详情返回
		MerchantStoreDetailstoreId = ckw.CommonKeyWord().Json_GetJsonValue(MerchantStoreDetail,[["data","storeId"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantStoreDetailstoreId:",MerchantStoreDetailstoreId)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantStoreDetailstoreId:",MerchantStoreDetailstoreId)
		# 读取yaml添加拜访断言
		AsertStoreId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"AsertStoreId")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店管理详情断言结果：",AsertStoreId)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantStoreDetailstoreId,AsertStoreId)
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml删除店员sql
		deleteAssistantsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"deleteAssistantsql")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",deleteAssistantsql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",deleteAssistantsql,"222.0")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_clerk",deleteAssistantsql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("门店管理-添加店员")
	@allure.severity("blocker")
	def test_zjc_MerchantStore_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 添加店员获取验证码-调取接口
		V4CodeSend = bkw.assistantappApi_V4CodeSend({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer"+token},"parma":{},"data":{"mobile":"15122222223","sendMethod":"sms","usage":"register"}
,"env":env},"dict")
		# 提取添加店员返回
		V4CodeSenderrno = ckw.CommonKeyWord().Json_GetJsonValue(V4CodeSend,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("V4CodeSenderrno:",V4CodeSenderrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("V4CodeSenderrno:",V4CodeSenderrno)
		# 读取yaml添加店员断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("添加店员验证码断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(V4CodeSenderrno,Errno)
		# 从数据库提取验证码-获取原始sql
		AssistantSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getAssistantCaptcha")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",AssistantSql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",AssistantSql)
		# 从数据库提取验证码-执行查询
		sqlReturn = ckw.CommonKeyWord().Db_MysqlSelect({"host":"udtest.uniondrug.com","port":"6033","username":"test","password":"tset@321abc","database":"cn_uniondrug_module_data","sql":AssistantSql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",sqlReturn)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",sqlReturn)
		# 从数据库提取验证码-提取验证码as
		ascaptcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlReturn[0],[["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：",ascaptcha)
		# 打印验证码到日志
		ckw.CommonKeyWord().Print_ToLog("验证码：",ascaptcha)
		# 门店管理添加店员-调取接口
		AssistantRegister = bkw.assistantappApi_AssistantRegister({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "partnerId":"92910",
    "storeId":"106017",
    "fullName":"自动化1",
    "account":"15122222223",
    "code":ascaptcha,
    "role":"2",
    "jobNumber":"",
    "userId":"306",
    "partnerName":"广州民信",
    "storeName":"钟落潭分店",
    "autoLogin":"0",
    "newAide":"1",   "idCard":"320123199901010101"
}
,"env":env},"dict")
		# 提取添加店员返回
		AssistantRegistererrno = ckw.CommonKeyWord().Json_GetJsonValue(AssistantRegister,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AssistantRegistererrno:",AssistantRegistererrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AssistantRegistererrno:",AssistantRegistererrno)
		# 读取yaml添加店员断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("添加店员断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AssistantRegistererrno,Errno)
		# 读取yaml删除店员sql
		deleteAssistantsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"deleteAssistantsql")
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",deleteAssistantsql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",deleteAssistantsql,"222.0")
		# mysql执行任意sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_clerk",deleteAssistantsql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("2.0")

	@allure.feature("门店管理-编辑门店信息")
	@allure.severity("blocker")
	def test_zjc_MerchantStore_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 编辑门店信息-调取接口
		MerchantStoreUpdate = bkw.assistantappApi_MerchantStoreUpdate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "businessStartTime": "06:30",
 "image": "",
 "isAllDay": "false",
 "subAddress": "测测测测测自动化门店编辑",
 "address": "门店编辑自动化测试",
 "mapLon": "124.242450",
 "storePhone": "0434-5577657",
 "mapLat": "43.665540",
 "shortName": "钟落潭分店",
 "businessEndTime": "21:00",
 "storeId": "106017",
 "isDirect": "false"
},"env":env},"dict")
		# 提取添加店员返回
		StoreUpdateerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantStoreUpdate,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("StoreUpdateerrno:",StoreUpdateerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("StoreUpdateerrno:",StoreUpdateerrno)
		# 读取yaml编辑门店断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("编辑门店信息断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(StoreUpdateerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("店员管理-店员列表")
	@allure.severity("blocker")
	def test_zjc_AssistantLists_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 店员列表-调取接口
		AssistantLists = bkw.assistantappApi_AssistantLists({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "page": "1"
},"env":env},"dict")
		# 提取添加店员返回
		AssistantListserrno = ckw.CommonKeyWord().Json_GetJsonValue(AssistantLists,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AssistantListserrno:",AssistantListserrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AssistantListserrno:",AssistantListserrno)
		# 读取yaml编辑门店断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("编辑门店信息断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AssistantListserrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("店员管理-店员详情")
	@allure.severity("blocker")
	def test_zjc_AssistantLists_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 店员详情-调取接口
		AssistantDetail = bkw.assistantappApi_AssistantDetail({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "id": "200268"
},"env":env},"dict")
		# 提取添加店员返回
		AssistantDetailerrno = ckw.CommonKeyWord().Json_GetJsonValue(AssistantDetail,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AssistantDetailerrno:",AssistantDetailerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AssistantDetailerrno:",AssistantDetailerrno)
		# 读取yaml编辑门店断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("店员详情断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AssistantDetailerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("店员管理-店员调店")
	@allure.severity("blocker")
	def test_zjc_AssistantLists_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 店员调店-调取接口
		AssistantStoreTransfer = bkw.assistantappApi_AssistantStoreTransfer({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "chainIdBefore":"125610",
    "chainNameBefore":"梨树县信康大药房连锁有限公司",
    "storeIdBefore":"125755",
    "storeNameBefore":"恒升分店",
 "assistantId": "200268",
    "chainIdAfter":"125610",
    "chainNameAfter":"梨树县信康大药房连锁有限公司",
 "storeIdAfter": "125755",
    "storeNameAfter":"恒升分店",
    "submitReason":"cecece"
},"env":env},"dict")
		# 提取添加店员返回
		AssistantStoreTransfererrno = ckw.CommonKeyWord().Json_GetJsonValue(AssistantStoreTransfer,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AssistantStoreTransfererrno:",AssistantStoreTransfererrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AssistantStoreTransfererrno:",AssistantStoreTransfererrno)
		# 读取yaml编辑门店断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("店员调店断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AssistantStoreTransfererrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("店员管理-店员编辑工号/调岗")
	@allure.severity("blocker")
	def test_zjc_AssistantLists_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 店员编辑工号/调岗-调取接口
		AssistantUpdate = bkw.assistantappApi_AssistantUpdate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "role": "1",
 "account": "15899663122"
},"env":env},"dict")
		# 提取添加店员返回
		AssistantUpdateerrno = ckw.CommonKeyWord().Json_GetJsonValue(AssistantUpdate,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AssistantUpdateerrno:",AssistantUpdateerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AssistantUpdateerrno:",AssistantUpdateerrno)
		# 读取yaml编辑门店断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("编辑门店信息断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AssistantUpdateerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-任务列表")
	@allure.severity("blocker")
	def test_zjc_WorkLists_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 获取当前日期
		TodayDate = ckw.CommonKeyWord().Time_Timestamp("43831.0")
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("TodayDate:",TodayDate)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("TodayDate:",TodayDate)
		# 读取yaml更新大数据门店表用户信息sql
		UpdateStoreInfosql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"UpdateStoreInfo")
		# 读取yaml更新大数据门店表日期sql
		UpdateStoreDatesql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"UpdateStoreDate")
		# 读取yaml更新大数据执行日期表门店任务日期为昨天sql
		UpdateSyncDatesql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"UpdateSyncDate")
		# 读取yaml删除任务数据sql
		DeleteWorksql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DeleteWork")
		# 读取yaml删除任务数据sql
		DeleteWork_recordsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DeleteWork_record")
		# 读取yaml插入任务数据sql
		INSERTWork1sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"INSERTWork1")
		# 读取yaml插入任务数据sql
		INSERTWork2sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"INSERTWork2")
		# 读取yaml插入任务数据sql
		INSERTWork3sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"INSERTWork3")
		# 读取yaml插入任务数据sql
		INSERTWork4sql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"INSERTWork4")
		# mysql执行任意sql-更新大数据门店表日期
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_data_dm",  "UPDATE `cn_uniondrug_data_dm`.`store_operation_info_ed` SET `statis_date` = '{}' WHERE `om_user_id` = 323;".format(ckw.CommonKeyWord.Time_Yesterday('')))
		# mysql执行任意sql-更新大数据执行日期表门店任务日期为今天
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_data_dm","UPDATE `cn_uniondrug_data_dm`.`user_table_sync_date` SET `last_sync_date` = '{}' WHERE `table_name` = 'store_operation_info_ed';".format(ckw.CommonKeyWord.Time_TodayTime('')))
		# mysql执行任意sql-删除任务数据
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_assistant",DeleteWorksql)
		# 门店任务-删除原任务记录数据
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_assistant",DeleteWork_recordsql)
		# mysql执行任意sql-插入任务数据
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_assistant",INSERTWork1sql)
		# mysql执行任意sql-插入任务数据
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_assistant",INSERTWork2sql)
		# mysql执行任意sql-插入任务数据
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_assistant",INSERTWork3sql)
		# mysql执行任意sql-插入任务数据
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_module_assistant",INSERTWork4sql)
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 门店任务脚本-调取接口
		bkw.assistantappApi_WorkJob({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{},"env":env},"dict")
		# 任务列表-调取接口
		WorkList = bkw.assistantappApi_WorkList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"userId":"306"},"env":env},"dict")
		# 提取任务列表返回
		WorkListerrno = ckw.CommonKeyWord().Json_GetJsonValue(WorkList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkListStorenum:",WorkListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkListStorenum:",WorkListerrno)
		# 读取yaml门店任务列表断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WorkListerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-取消任务")
	@allure.severity("blocker")
	def test_zjc_WorkLists_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml查询任务数据idsql
		GetCanceldsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetCanceld")
		# 读取yaml查询任务数据statuasql
		GetCancestatussql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetCancestatus")
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Canceldsql：",GetCanceldsql)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("Canceldsql：",GetCanceldsql)
		# mysql执行任意sql-查询Canceld
		GetCanceld = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_uniondrug_data_service",GetCanceldsql)
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",GetCanceld)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",GetCanceld)
		# 从数据库提取Canceld-提取Canceld
		GetCanceld1 = ckw.CommonKeyWord().Json_GetJsonValue(GetCanceld[0],[["id"]])
		# 取消门店任务-调取接口
		WorkCancel = bkw.assistantappApi_WorkCancel({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"id":GetCanceld1,"remark":"","type":"1","userId":"306"},"env":env},"dict")
		# 提取取消门店任务返回
		WorkCancelerrno = ckw.CommonKeyWord().Json_GetJsonValue(WorkCancel,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkCancelerrno:",WorkCancelerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkCancelerrno:",WorkCancelerrno)
		# 读取yaml取消门店任务断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WorkCancelerrno,Errno)
		# mysql执行任意sql-查询status
		GetCancestatus = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_module_assistant",GetCancestatussql)
		# 从数据库提取任务status-提取任务status
		GetCancestatus1 = ckw.CommonKeyWord().Json_GetJsonValue(GetCancestatus[0],[["status"]])
		# 读取yaml取消门店状态断言
		Cancestatus = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Cancestatus")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",Cancestatus)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(GetCancestatus1,Cancestatus)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-领取任务")
	@allure.severity("blocker")
	def test_zjc_WorkLists_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 领取门店任务-调取接口
		WorkAccept = bkw.assistantappApi_WorkAccept({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"workId":"88888"},"env":env},"dict")
		# 提取领取门店任务返回
		WorkAccepterrno = ckw.CommonKeyWord().Json_GetJsonValue(WorkAccept,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkCancelerrno:",WorkAccepterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkCancelerrno:",WorkAccepterrno)
		# 读取yaml领取门店任务断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("领取门店任务断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WorkAccepterrno,Errno)
		# 读取yaml查询领取任务数据statuasql
		GetAcceptstatussql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetAcceptstatus")
		# mysql执行任意sql-查询status
		GetAcceptstatus = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_module_assistant",GetAcceptstatussql)
		# 从数据库提取任务status-提取任务status
		GetAcceptstatus1 = ckw.CommonKeyWord().Json_GetJsonValue(GetAcceptstatus[0],[["status"]])
		# 读取yaml取消门店状态断言
		Acceptstatus = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Acceptstatus")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",Acceptstatus)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(GetAcceptstatus1,Acceptstatus)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-开始任务")
	@allure.severity("blocker")
	def test_zjc_WorkLists_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 开始门店任务-调取接口
		WInspectStart = bkw.assistantappApi_InspectStart({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "mapLon": "118.779322",
 "storeId": "4338",
 "workId": "88888",
 "mapLat": "31.971852",
 "remark": "自动化开始门店任务"
},"env":env},"dict")
		# 提取开始门店任务返回
		WInspectStarterrno = ckw.CommonKeyWord().Json_GetJsonValue(WInspectStart,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WInspectStarterrno:",WInspectStarterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WInspectStarterrno:",WInspectStarterrno)
		# 读取yaml开始门店任务断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("开始门店任务断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WInspectStarterrno,Errno)
		# 读取yaml查询开始任务statuasql
		GetStartstatussql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetStartstatus")
		# mysql执行任意sql-查询status
		GetStartstatus = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_module_assistant",GetStartstatussql)
		# 从数据库提取任务status-提取任务status
		GetStartstatus1 = ckw.CommonKeyWord().Json_GetJsonValue(GetStartstatus[0],[["status"]])
		# 读取yaml开始门店任务状态断言
		Startstatus = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Startstatus")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",Startstatus)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(GetStartstatus1,Startstatus)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-完成线下拜访")
	@allure.severity("blocker")
	def test_zjc_WorkLists_005(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml查询任务数据idsql
		Getinspectldsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Getinspectld")
		# 读取yaml查询任务数据idsql
		updateInspectTimesql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"updateInspectTimesql")
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("inspectldsql：",Getinspectldsql)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("inspectldsql：",Getinspectldsql)
		# mysql执行任意sql-查询Inspectid
		WInspectid = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_uniondrug_data_service",Getinspectldsql)
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",WInspectid)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",WInspectid)
		# 从数据库提取Inspectid-提取Inspectid
		WInspectid1 = ckw.CommonKeyWord().Json_GetJsonValue(WInspectid[0],[["id"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("巡店id：",WInspectid1)
		# 打印验证码到日志
		ckw.CommonKeyWord().Print_ToLog("巡店id：",WInspectid1)
		# mysql执行任意sql-更新拜访开始时间
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",updateInspectTimesql)
		# 完成门店线下任务-调取接口
		WInspectUpdate = bkw.assistantappApi_InspectUpdate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "address": "江苏省南京市雨花台区文竹路6号靠近金证南京科技园(装修中)",
    "mapLat": "31.971852",
    "images": [
        {
            "type": "1",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/kdmatv0nh01egs1847cv9f2bsu.jpg"
        },
        {
            "type": "2",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/6or6ks7ivmnoabv2i074kc2a90.jpg"
        },
        {
            "type": "2",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/fjlfe6l470bkfdjut5nkol8dja.jpg"
        },
        {
            "type": "3",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/efsg761jj284d3jsjgm9kvcfm2.jpg"
        },
        {
            "type": "3",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/m3vvlh2bl8umc1b6g15vgjm0tv.jpg"
        },
        {
            "type": "5",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/7tue4rur23375hr465f1ntlglo.jpg"
        },
        {
            "type": "5",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/42hnh8jloe32hb79ir7u3fi9h3.jpg"
        },
        {
            "type": "4",
            "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/r25tottrth47dfeg0qjedaorqv.jpg"
        }
    ],
    "inspectId": WInspectid1,
    "remark": "",
    "summary": [
        "1",
        "2",
        "3",
        "4"
    ],
    "storeId": "4338",
    "mapLon": "118.77937"
},"env":env},"dict")
		# 提取完成门店线下任务返回
		WInspectUpdateerrno = ckw.CommonKeyWord().Json_GetJsonValue(WInspectUpdate,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("InspectUpdateerrno:",WInspectUpdateerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("InspectUpdateerrno:",WInspectUpdateerrno)
		# 读取yaml完成门店线下任务断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("完成门店线下任务断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WInspectUpdateerrno,Errno)
		# 读取yaml查询完成线下任务statuasql
		InspectUpdatestatussql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"InspectUpdatestatus")
		# mysql执行任意sql-查询status
		Inspectstatus = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_module_assistant",InspectUpdatestatussql)
		# 从数据库提取任务status-提取任务status
		Inspectstatus1 = ckw.CommonKeyWord().Json_GetJsonValue(Inspectstatus[0],[["status"]])
		# 读取yaml完成线下状态断言
		yamlInspectstatus = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Inspectstatus")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",yamlInspectstatus)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(Inspectstatus1,yamlInspectstatus)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-完成线上拜访-电话语音")
	@allure.severity("blocker")
	def test_zjc_WorkLists_006(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 领取门店任务-调取接口
		WorkAccept = bkw.assistantappApi_WorkAccept({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"workId":"66666"},"env":env},"dict")
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")
		# 开始门店任务-调取接口
		WRecordStart = bkw.assistantappApi_WorkRecordCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "appealInfo": {},
    "appealReason": "3",
    "communicateType": "2",
    "workId": "66666"
},"env":env},"dict")
		# 提取开始门店电话语音任务返回
		WorkRecordStarterrno = ckw.CommonKeyWord().Json_GetJsonValue(WRecordStart,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkRecordStarterrno:",WorkRecordStarterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkRecordStarterrno:",WorkRecordStarterrno)
		# 完成门店电话任务-调取接口
		WorkRecordComplete = bkw.assistantappApi_WorkRecordComplete({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "communicateImages": [
        "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/qalrl3lteu3ngf7hoks22qqvc6.jpg"
    ],
    "communicateType": "2",
    "remark": "线上拜访自动化测试结束",
    "summary": [
        "5",
        "6"
    ],
    "workId": "66666"
},"env":env},"dict")
		# 提取完成门店电话语音任务返回
		WorkRecordCompleteerrno = ckw.CommonKeyWord().Json_GetJsonValue(WorkRecordComplete,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkRecordCompleteerrno:",WorkRecordCompleteerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkRecordCompleteerrno:",WorkRecordCompleteerrno)
		# 读取yaml完成门店线下任务断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("完成门店电话语音任务断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WorkRecordCompleteerrno,Errno)
		# 读取yaml查询完成电话语音任务statuasql
		Getvideotatussql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Getvideotatus")
		# mysql执行任意sql-查询status
		Getvideotatus = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_module_assistant",Getvideotatussql)
		# 从数据库提取任务status-提取任务status
		Getvideotatus1 = ckw.CommonKeyWord().Json_GetJsonValue(Getvideotatus[0],[["status"]])
		# 读取yaml完成电话语音任务状态断言
		videostatus = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"videostatus")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",videostatus)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(Getvideotatus1,videostatus)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-完成线上拜访-微信文字")
	@allure.severity("blocker")
	def test_zjc_WorkLists_007(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml登录密码
		password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"password")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":password},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 写入yaml文件
		ckw.CommonKeyWord().Yaml_Write("./TestFile/ZhangJunChao/token.yaml",token,"userid",userid)
		# 领取门店任务-调取接口
		WorkAccept = bkw.assistantappApi_WorkAccept({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"workId":"77777"},"env":env},"dict")
		# 开始门店任务-调取接口
		WRecordStart = bkw.assistantappApi_WorkRecordCreate({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "appealInfo": {},
    "appealReason": "3",
    "communicateType": "3",
    "workId": "77777"
},"env":env},"dict")
		# 提取开始门店电话语音任务返回
		WorkRecordStarterrno = ckw.CommonKeyWord().Json_GetJsonValue(WRecordStart,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkRecordStarterrno:",WorkRecordStarterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkRecordStarterrno:",WorkRecordStarterrno)
		# 完成门店微信文字任务-调取接口
		WorkRecordComplete = bkw.assistantappApi_WorkRecordComplete({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "communicateImages": [
        "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/qalrl3lteu3ngf7hoks22qqvc6.jpg"
    ],
    "communicateType": "3",
    "remark": "线上拜访自动化测试结束",
    "summary": [
        "7",
        "8"
    ],
    "workId": "77777"
},"env":env},"dict")
		# 提取完成门店微信文字任务返回
		WorkRecordCompleteerrno = ckw.CommonKeyWord().Json_GetJsonValue(WorkRecordComplete,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("WorkRecordCompleteerrno:",WorkRecordCompleteerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("WorkRecordCompleteerrno:",WorkRecordCompleteerrno)
		# 读取yaml完成门店微信文字任务断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("完成门店微信文字任务断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(WorkRecordCompleteerrno,Errno)
		# 读取yaml查询完成微信文字任务statuasql
		Gettextstatussql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Gettextstatus")
		# mysql执行任意sql-查询status
		Gettextstatus = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_module_assistant",Gettextstatussql)
		# 从数据库提取任务status-提取任务status
		Gettextstatus1 = ckw.CommonKeyWord().Json_GetJsonValue(Gettextstatus[0],[["status"]])
		# 读取yaml完成微信文字任务状态断言
		textstatus = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"textstatus")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("门店任务列表断言结果：",textstatus)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(Gettextstatus1,textstatus)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-申请线上拜访-已合作/连锁")
	@allure.severity("blocker")
	def test_zjc_ApprovalAdd_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml文件
		yamlFile1 = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取Yaml-token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"token")
		# 读取Yaml-userid
		userid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"userid")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 已合作连锁列表-调取接口
		MerchantAllList = bkw.assistantappApi_MerchantAllList({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "userId":userid,
 "page": "1",
 "limit": "10",
 "businessTypeArr": [1, 4],
 "common_name": ""
},"env":env},"dict")
		# 提取已合作连锁列表返回
		MerchantAllListerrno = ckw.CommonKeyWord().Json_GetJsonValue(MerchantAllList,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("MerchantAllListerrno:",MerchantAllListerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("MerchantAllListerrno:",MerchantAllListerrno)
		# 读取yaml已合作连锁列表断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("已合作连锁列表断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(MerchantAllListerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-申请线上拜访-未合作/连锁")
	@allure.severity("blocker")
	def test_zjc_ApprovalAdd_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml文件
		yamlFile1 = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取Yaml-token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"token")
		# 读取Yaml-userid
		userid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"userid")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 未合作连锁列表-调取接口
		CustomerPaging = bkw.assistantappApi_CustomerPaging({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "userId":userid,
 "page": "1",
 "limit": "10",
 "customerName": "",
 "customerType": "1",
 "all": "1",
 "orderBy": "createTime",
 "customerStatusList": [0, 3, 4, 5]
},"env":env},"dict")
		# 提取未合作连锁列表返回
		CustomerPagingerrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerPaging,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CustomerPagingerrno:",CustomerPagingerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CustomerPagingerrno:",CustomerPagingerrno)
		# 读取yaml未合作连锁列表断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("未合作连锁列表断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerPagingerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-申请线上拜访-添加新连锁")
	@allure.severity("blocker")
	def test_zjc_ApprovalAdd_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml文件
		yamlFile1 = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取Yaml-token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"token")
		# 读取Yaml-userid
		userid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"userid")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 添加新连锁-调取接口
		CustomerAdd = bkw.assistantappApi_CustomerAdd({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "userId": userid,
 "customerName": "自动化熄灯大药房",
 "customerType": "1",
 "customerStatus": "4",
 "customerStatusText": "进入签约阶段",
 "longitude": "118.778455",
 "latitude": "31.971711",
 "address": "江苏省南京市雨花台区凤信路6号南京市雨花区金证科技园",
 "customerShortName": "自动化熄灯药房",
 "contacts": [{
  "contactName": "南京",
  "mobile": "15988831116",
  "position": "运营负责人"
 }]
},"env":env},"dict")
		# 提取添加新连锁返回
		CustomerAdderrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerAdd,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CustomerAdderrno:",CustomerAdderrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CustomerAdderrno:",CustomerAdderrno)
		# 读取yaml添加新连锁断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("添加新连锁断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerAdderrno,Errno)
		# 读取yaml查询客户信息namesql
		GetCustomerInfosql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetCustomerInfo")
		# 读取yaml添加新连锁断言
		CustomerNameAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerNameAssert")
		# 读取yaml删除添加的连锁
		DeleteCustomersql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"DeleteCustomersql")
		# mysql执行任意sql-查询客户信息name
		GetCustomerInfo = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_uniondrug_data_service",GetCustomerInfosql)
		# 从数据库提取客户信息name
		GetCustomerName = ckw.CommonKeyWord().Json_GetJsonValue(GetCustomerInfo[0],[["customerName"]])
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(GetCustomerName,CustomerNameAssert)
		# mysql执行任意sql-删除添加的连锁sql
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_uniondrug_data_service",DeleteCustomersql)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("门店任务-申请连锁拜访-已合作")
	@allure.severity("blocker")
	def test_zjc_ApprovalAdd_004(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/zjctest.yaml")
		# 读取yaml文件
		yamlFile1 = ckw.CommonKeyWord().Yaml_Read("./TestFile/ZhangJunChao/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取Yaml-token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"token")
		# 读取Yaml-userid
		userid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile1,"userid")
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 申请连锁拜访-调取接口
		ApprovalAddApprovalVisit = bkw.assistantappApi_ApprovalAddApprovalVisit({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
 "businessType": "1",
 "isCooperation": "1",
 "merchantId": "240329",
 "merchantName": "成大方圆医药连锁有限公司抚顺地区",
 "merchantAddress": "",
 "merchantSigning": "",
 "isReserved": "1",
 "visitDate": "2021-07-8",
 "visitTimes": "0",
 "visitTarget": [{
  "name": "秘密",
  "mobile": "88993744",
  "positionType": "2",
  "positionTypeText": "运营负责人",
  "positionOther": ""
 }],
 "visitContent": [{
  "goalId": "2",
  "departmentId": "1",
  "typeId": "1",
  "cooperationStatus": "1",
  "cooperationStatusText": "已合作",
  "signStatus": "0",
  "signStatusText": "未知",
  "display": "1",
  "displayText": "显示",
  "goal": "超级会员日活动业务上线沟通",
  "summary": "完成超级会员日活动政策上线沟通及确定连锁已充分了解政策并确定上线节点",
  "guideTitle": "",
  "guideContent": "",
  "gmtCreated": "2021-01-19 15:54:59",
  "gmtUpdated": "2021-01-19 15:54:59"
 }],
 "approval": {
  "approveType": "18",
  "applyName": "连锁拜访",
  "approveSettingId": "18",
  "processList": [{
   "taskSetting": [],
   "processSettingId": "1507",
   "approveSettingId": "18",
   "processType": "2",
   "customDuplicater": "0",
   "processName": "抄送人",
   "approverType": "1",
   "operateType": "1",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "1506",
   "gmtCreated": "2021-04-12 18:31:11",
   "gmtUpdated": "2021-04-12 18:31:11",
   "processUserList": [{
    "approverSettingId": "4491",
    "processSettingId": "1507",
    "approverGenre": "1",
    "relatedId": "323",
    "relatedName": "张俊超02",
    "avatar": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u2834285391,2876082627&fm26&gp0.jpg",
    "mobile": "15380905486",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "323",
    "userName": "张俊超02"
   }]
  }, {
   "taskSetting": [],
   "processSettingId": "1506",
   "approveSettingId": "18",
   "processType": "1",
   "customDuplicater": "0",
   "processName": "运营审批",
   "approverType": "1",
   "operateType": "2",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "1505",
   "gmtCreated": "2021-04-12 18:31:11",
   "gmtUpdated": "2021-04-12 18:31:11",
   "processUserList": [{
    "approverSettingId": "4487",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "238",
    "userName": "康小强"
   }, {
    "approverSettingId": "4488",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "4129",
    "relatedName": "陈斌",
    "avatar": "",
    "mobile": "15905147519",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "4129",
    "userName": "陈斌"
   }, {
    "approverSettingId": "4489",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "287",
    "relatedName": "张俊超",
    "avatar": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u2834285391,2876082627&fm26&gp0.jpg",
    "mobile": "15150578643",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "287",
    "userName": "张俊超"
   }, {
    "approverSettingId": "4490",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "4186",
    "relatedName": "肖文瑶",
    "avatar": "https://gimg2.baidu.com/image_search/srchttp%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&referhttp%3A%2F%2F5b0988e595225.cdn.sohucs.com&app2002&sizef9999,10000&qa80&n0&g0n&fmtjpeg?sec1628154553",
    "mobile": "15651711729",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "4186",
    "userName": "肖文瑶"
   }]
  }, {
   "taskSetting": [],
   "processSettingId": "1505",
   "approveSettingId": "18",
   "processType": "2",
   "customDuplicater": "0",
   "processName": "抄送人",
   "approverType": "1",
   "operateType": "1",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "0",
   "gmtCreated": "2021-04-12 18:31:11",
   "gmtUpdated": "2021-04-12 18:31:11",
   "processUserList": [{
    "approverSettingId": "4486",
    "processSettingId": "1505",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "238",
    "userName": "康小强"
   }]
  }]
 }
},"env":env},"dict")
		# 提取申请连锁拜访返回
		ApprovalAddApprovalVisiterrno = ckw.CommonKeyWord().Json_GetJsonValue(ApprovalAddApprovalVisit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("ApprovalAddApprovalVisiterrno:",ApprovalAddApprovalVisiterrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("ApprovalAddApprovalVisiterrno:",ApprovalAddApprovalVisiterrno)
		# 读取yaml添加新连锁断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("申请连锁拜访断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(ApprovalAddApprovalVisiterrno,Errno)
		# 读取yaml连锁拜访name
		GetApproveVissitAsert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"ApproveVissitAsert")
		# 读取yaml连锁拜访sql
		GetApproveVissitsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"GetApproveVissit")
		# mysql执行任意sql-查询拜访类型
		GetApproveVissit = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_ud_mod_approval",GetApproveVissitsql)
		# 从数据库提取拜访类型
		GetApproveVissitName = ckw.CommonKeyWord().Json_GetJsonValue(GetApproveVissit[0],[["applyName"]])
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(GetApproveVissitName,GetApproveVissitAsert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")
