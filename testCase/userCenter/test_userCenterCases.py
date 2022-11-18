# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
import ApiLib.userCenter.userCenterApi as userCenter


class Test_userCenter:

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicAddOrQuery_test1(self):
		"""
		添加用户已存在则查询用户
		"""
		UserBasicAddOrQuery=userCenter.UserBasicAddOrQuery()
		UserBasicAddOrQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicAddOrQuery.changeEnv("turboradio.cn")
		UserBasicAddOrQuery.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}
		UserBasicAddOrQueryRes = UserBasicAddOrQuery.excute()
		assert UserBasicAddOrQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardAdd_test2(self):
		"""
		身份证实名认证接口
		"""
		UserCardAdd=userCenter.UserCardAdd()
		UserCardAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardAdd.changeEnv("turboradio.cn")
		UserCardAdd.data = {"memberId":15965194,"typeId":1,"cardNo":" 210423199308061827 ","cardName":"张丽军","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}
		UserCardAddRes = UserCardAdd.excute()
		assert UserCardAddRes.text.__contains__("证件号已认证")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetById_test3(self):
		"""
		通过memberId查询实名认证信息
		"""
		UserCardGetById=userCenter.UserCardGetById()
		UserCardGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetById.changeEnv("turboradio.cn")
		UserCardGetById.data = {"memberId":15965194,"typeId":1}
		UserCardGetByIdRes = UserCardGetById.excute()
		result = UserCardGetByIdRes.json()
		print("UserCardGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardBatchByIds_test4(self):
		"""
		通过memberId集合批量查询用户实名信息
		"""
		UserCardBatchByIds=userCenter.UserCardBatchByIds()
		UserCardBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardBatchByIds.changeEnv("turboradio.cn")
		UserCardBatchByIds.data = {"memberIds":[15965194],"typeId":1}
		UserCardBatchByIdsRes = UserCardBatchByIds.excute()
		result = UserCardBatchByIdsRes.json()
		print("UserCardBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorBatchByMemberIds_test5(self):
		"""
		通过memberId批量查询用户信息
		"""
		UserMajorBatchByMemberIds=userCenter.UserMajorBatchByMemberIds()
		UserMajorBatchByMemberIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorBatchByMemberIds.changeEnv("turboradio.cn")
		UserMajorBatchByMemberIds.data = {"memberIds":[15965194]}
		UserMajorBatchByMemberIdsRes = UserMajorBatchByMemberIds.excute()
		result = UserMajorBatchByMemberIdsRes.json()
		print("UserMajorBatchByMemberIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserTagContainsTagValuesBatch_test6(self):
		"""
		批量判断标签下所有值是否包含用户
		"""
		UserTagContainsTagValuesBatch=userCenter.UserTagContainsTagValuesBatch()
		UserTagContainsTagValuesBatch.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserTagContainsTagValuesBatch.changeEnv("turboradio.cn")
		UserTagContainsTagValuesBatch.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}
		UserTagContainsTagValuesBatchRes = UserTagContainsTagValuesBatch.excute()
		result = UserTagContainsTagValuesBatchRes.json()
		print("UserTagContainsTagValuesBatchRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["tagId"])
		assert p == "071AC4E0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPageGet_test7(self):
		"""
		查询用户收货地址
		"""
		UserAddressPageGet=userCenter.UserAddressPageGet()
		UserAddressPageGet.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPageGet.changeEnv("turboradio.cn")
		UserAddressPageGet.data = {"id":29433}
		UserAddressPageGetRes = UserAddressPageGet.excute()
		result = UserAddressPageGetRes.json()
		print("UserAddressPageGetRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["mobile"])
		assert p == "18761600408"
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["consigneeName"])
		assert p == "李四1"
		p = str(r_data["isDefault"])
		assert p == "0"
		p = str(r_data["street"])
		assert p == "tvyvsq"
		p = str(r_data["fullAddress"])
		assert p == "啦啦啦"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleGetOne_test8(self):
		"""
		查询用户组织
		"""
		UserRoleGetOne=userCenter.UserRoleGetOne()
		UserRoleGetOne.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleGetOne.changeEnv("turboradio.cn")
		UserRoleGetOne.data = {"memberId":15965194,"codeList":[645,556]}
		UserRoleGetOneRes = UserRoleGetOne.excute()
		assert UserRoleGetOneRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQuery_test9(self):
		"""
		查询用户签名规则
		"""
		UserRuleQuery=userCenter.UserRuleQuery()
		UserRuleQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQuery.changeEnv("turboradio.cn")
		UserRuleQuery.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}
		UserRuleQueryRes = UserRuleQuery.excute()
		assert UserRuleQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserInfoGetRealByCarNo_test10(self):
		"""
		通过证件号码查询实名的用户信息
		"""
		UserInfoGetRealByCarNo=userCenter.UserInfoGetRealByCarNo()
		UserInfoGetRealByCarNo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserInfoGetRealByCarNo.changeEnv("turboradio.cn")
		UserInfoGetRealByCarNo.data = {"cardNo":"210423199308061827"}
		UserInfoGetRealByCarNoRes = UserInfoGetRealByCarNo.excute()
		result = UserInfoGetRealByCarNoRes.json()
		print("UserInfoGetRealByCarNoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["cardName"])
		assert p == "张丽军"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserGuardianQuery_test11(self):
		"""
		查询监护人信息
		"""
		UserGuardianQuery=userCenter.UserGuardianQuery()
		UserGuardianQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserGuardianQuery.changeEnv("turboradio.cn")
		UserGuardianQuery.data = {"memberId":15965194}
		UserGuardianQueryRes = UserGuardianQuery.excute()
		result = UserGuardianQueryRes.json()
		print("UserGuardianQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["relationship"])
		assert p == "妈妈"
		p = str(r_data["account"])
		assert p == "17327890317"
		p = str(r_data["cardNo"])
		assert p == "210423196203121826"
		p = str(r_data["typeId"])
		assert p == "1"
		p = str(r_data["address"])
		assert p == "江苏省南京市雨花台区金证科技园2栋"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressPage_test12(self):
		"""
		分页查询用户收货地址列表
		"""
		UserAddressPage=userCenter.UserAddressPage()
		UserAddressPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressPage.changeEnv("turboradio.cn")
		UserAddressPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserAddressPageRes = UserAddressPage.excute()
		assert UserAddressPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetReal_test13(self):
		"""
		通过memberID查询实名证件
		"""
		UserCardGetReal=userCenter.UserCardGetReal()
		UserCardGetReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetReal.changeEnv("turboradio.cn")
		UserCardGetReal.data = {"memberId":15965194}
		UserCardGetRealRes = UserCardGetReal.excute()
		result = UserCardGetRealRes.json()
		print("UserCardGetRealRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicBatchByIds_test14(self):
		"""
		批量查看用户详情
		"""
		UserBasicBatchByIds=userCenter.UserBasicBatchByIds()
		UserBasicBatchByIds.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicBatchByIds.changeEnv("turboradio.cn")
		UserBasicBatchByIds.data = {"memberIds":[15965194]}
		UserBasicBatchByIdsRes = UserBasicBatchByIds.excute()
		result = UserBasicBatchByIdsRes.json()
		print("UserBasicBatchByIdsRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicQuery_test15(self):
		"""
		查询用户基本信息
		"""
		UserBasicQuery=userCenter.UserBasicQuery()
		UserBasicQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicQuery.changeEnv("turboradio.cn")
		UserBasicQuery.data = {"id":15965194,"account":"18761600404"}
		UserBasicQueryRes = UserBasicQuery.excute()
		result = UserBasicQueryRes.json()
		print("UserBasicQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["mobile"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryBy_test16(self):
		"""
		通过memberId和account查询
		"""
		UserMajorQueryBy=userCenter.UserMajorQueryBy()
		UserMajorQueryBy.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryBy.changeEnv("turboradio.cn")
		UserMajorQueryBy.data = {"memberId":15965194,"account":"18761600404"}
		UserMajorQueryByRes = UserMajorQueryBy.excute()
		result = UserMajorQueryByRes.json()
		print("UserMajorQueryByRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["account"])
		assert p == "18761600404"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdQuery_test17(self):
		"""
		查询第三方平台授权
		"""
		UserThirdQuery=userCenter.UserThirdQuery()
		UserThirdQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdQuery.changeEnv("turboradio.cn")
		UserThirdQuery.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}
		UserThirdQueryRes = UserThirdQuery.excute()
		result = UserThirdQueryRes.json()
		print("UserThirdQueryRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["oauthName"])
		assert p == "药联健康"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["oauthType"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserMajorQueryByOpenId_test18(self):
		"""
		查询第三方平台授权
		"""
		UserMajorQueryByOpenId=userCenter.UserMajorQueryByOpenId()
		UserMajorQueryByOpenId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserMajorQueryByOpenId.changeEnv("turboradio.cn")
		UserMajorQueryByOpenId.data = {"openId":"oRGmzszxvbZ-vQ9mk2lIFAnM6G74","oauthType":1}
		UserMajorQueryByOpenIdRes = UserMajorQueryByOpenId.excute()
		assert UserMajorQueryByOpenIdRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserPage_test19(self):
		"""
		分页查询用户服务资格
		"""
		UserPage=userCenter.UserPage()
		UserPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserPage.changeEnv("turboradio.cn")
		UserPage.data = {"page":1,"limit":10,"memberId":15965194}
		UserPageRes = UserPage.excute()
		assert UserPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardGetRealInfo_test20(self):
		"""
		通过memberId查询实名证件
		"""
		UserCardGetRealInfo=userCenter.UserCardGetRealInfo()
		UserCardGetRealInfo.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardGetRealInfo.changeEnv("turboradio.cn")
		UserCardGetRealInfo.data = {"memberId":15965194}
		UserCardGetRealInfoRes = UserCardGetRealInfo.excute()
		result = UserCardGetRealInfoRes.json()
		print("UserCardGetRealInfoRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["isReal"])
		assert p == "1"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["isRealText"])
		assert p == "已实名"
		p = str(r_data["typeName"])
		assert p == "大陆身份证"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["checkStatus"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["typeId"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdPage_test21(self):
		"""
		分页查询第三方平台授权列表
		"""
		UserThirdPage=userCenter.UserThirdPage()
		UserThirdPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdPage.changeEnv("turboradio.cn")
		UserThirdPage.data = {"pageNum":1,"pageSize":10,"memberId":15965194}
		UserThirdPageRes = UserThirdPage.excute()
		assert UserThirdPageRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserFamilyQueryByMemberId_test22(self):
		"""
		通过用户ID查询家庭关系列表
		"""
		UserFamilyQueryByMemberId=userCenter.UserFamilyQueryByMemberId()
		UserFamilyQueryByMemberId.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserFamilyQueryByMemberId.changeEnv("turboradio.cn")
		UserFamilyQueryByMemberId.data = {"memberId":15965194}
		UserFamilyQueryByMemberIdRes = UserFamilyQueryByMemberId.excute()
		result = UserFamilyQueryByMemberIdRes.json()
		print("UserFamilyQueryByMemberIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["relationship_name"])
		assert p == "父亲"
		p = str(r_data["gender"])
		assert p == "02"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["familyName"])
		assert p == "张六"
		p = str(r_data["relationship"])
		assert p == "0"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRuleQueryGetSign_test23(self):
		"""
		查询用户签名规则
		"""
		UserRuleQueryGetSign=userCenter.UserRuleQueryGetSign()
		UserRuleQueryGetSign.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRuleQueryGetSign.changeEnv("turboradio.cn")
		UserRuleQueryGetSign.data = {"memberId":15965194}
		UserRuleQueryGetSignRes = UserRuleQueryGetSign.excute()
		result = UserRuleQueryGetSignRes.json()
		print("UserRuleQueryGetSignRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserThirdBind_test24(self):
		"""
		绑定第三方平台授权
		"""
		UserThirdBind=userCenter.UserThirdBind()
		UserThirdBind.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserThirdBind.changeEnv("turboradio.cn")
		UserThirdBind.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}
		UserThirdBindRes = UserThirdBind.excute()
		result = UserThirdBindRes.json()
		print("UserThirdBindRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["unionId"])
		assert p == "52"
		p = str(r_data["oauthName"])
		assert p == "张小三"
		p = str(r_data["openId"])
		assert p == "52"
		p = str(r_data["appId"])
		assert p == "52"
		p = str(r_data["staCode"])
		assert p == "1"
		p = str(r_data["memberId"])
		assert p == "15965194"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressAdd_test25(self):
		"""
		添加收货地址
		"""
		UserAddressAdd=userCenter.UserAddressAdd()
		UserAddressAdd.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressAdd.changeEnv("turboradio.cn")
		UserAddressAdd.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}
		UserAddressAddRes = UserAddressAdd.excute()
		result = UserAddressAddRes.json()
		print("UserAddressAddRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["city"])
		assert p == "wypgpc"
		p = str(r_data["provinceCode"])
		assert p == "65120"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["street"])
		assert p == "23423424"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserRoleContainsIdentity_test26(self):
		"""
		校验用户身份
		"""
		UserRoleContainsIdentity=userCenter.UserRoleContainsIdentity()
		UserRoleContainsIdentity.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserRoleContainsIdentity.changeEnv("turboradio.cn")
		UserRoleContainsIdentity.data = {"memberId":15965194,"identityCode":0}
		UserRoleContainsIdentityRes = UserRoleContainsIdentity.excute()
		result = UserRoleContainsIdentityRes.json()
		print("UserRoleContainsIdentityRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["contains"])
		assert p == "True"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserAddressGetDefault_test27(self):
		"""
		获取默认地址
		"""
		UserAddressGetDefault=userCenter.UserAddressGetDefault()
		UserAddressGetDefault.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserAddressGetDefault.changeEnv("turboradio.cn")
		UserAddressGetDefault.data = {"memberId":15965194}
		UserAddressGetDefaultRes = UserAddressGetDefault.excute()
		result = UserAddressGetDefaultRes.json()
		print("UserAddressGetDefaultRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["consigneeName"])
		assert p == "赵五"
		p = str(r_data["isDefault"])
		assert p == "1"
		p = str(r_data["staCode"])
		assert p == "1"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserBasicUpdate_test28(self):
		"""
		编辑用户基本信息
		"""
		UserBasicUpdate=userCenter.UserBasicUpdate()
		UserBasicUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserBasicUpdate.changeEnv("turboradio.cn")
		UserBasicUpdate.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}
		UserBasicUpdateRes = UserBasicUpdate.excute()
		result = UserBasicUpdateRes.json()
		print("UserBasicUpdateRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["gender"])
		assert p == "01"
		p = str(r_data["memberName"])
		assert p == "张丽军"
		p = str(r_data["staCode_name"])
		assert p == "正常"
		p = str(r_data["memberId"])
		assert p == "15965194"
		p = str(r_data["mobile"])
		assert p == "18761600404"
		p = str(r_data["account"])
		assert p == "18761600404"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_UserCardCheck_test29(self):
		"""
		校验大陆身份证
		"""
		UserCardCheck=userCenter.UserCardCheck()
		UserCardCheck.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		UserCardCheck.changeEnv("turboradio.cn")
		UserCardCheck.data = {"cardName":"张丽军","cardNo":"210423199308061827"}
		UserCardCheckRes = UserCardCheck.excute()
		result = UserCardCheckRes.json()
		print("UserCardCheckRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["code"])
		assert p == "1"
		p = str(r_data["codeText"])
		assert p == "有效"
		p = str(r_data["cardName"])
		assert p == "张丽军"
		p = str(r_data["cardNo"])
		assert p == "210423199308061827"
		p = str(r_data["province"])
		assert p == "辽宁"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_PromoteUpdate_test30(self):
		"""
		优惠权益mbs消费接口
		"""
		PromoteUpdate=userCenter.PromoteUpdate()
		PromoteUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		PromoteUpdate.changeEnv("turboradio.cn")
		PromoteUpdate.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}
		PromoteUpdateRes = PromoteUpdate.excute()
		assert PromoteUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MbsLogin_test31(self):
		"""
		用户登录mbs
		"""
		MbsLogin=userCenter.MbsLogin()
		MbsLogin.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MbsLogin.changeEnv("turboradio.cn")
		MbsLogin.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}
		MbsLoginRes = MbsLogin.excute()
		assert MbsLoginRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_EquityUpdate_test32(self):
		"""
		权益mbs消费接口
		"""
		EquityUpdate=userCenter.EquityUpdate()
		EquityUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		EquityUpdate.changeEnv("turboradio.cn")
		EquityUpdate.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}
		EquityUpdateRes = EquityUpdate.excute()
		assert EquityUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GuaranteeUpdate_test33(self):
		"""
		保障mbs消费接口
		"""
		GuaranteeUpdate=userCenter.GuaranteeUpdate()
		GuaranteeUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GuaranteeUpdate.changeEnv("turboradio.cn")
		GuaranteeUpdate.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}
		GuaranteeUpdateRes = GuaranteeUpdate.excute()
		assert GuaranteeUpdateRes.text.__contains__("更新成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_GiftUpdate_test34(self):
		"""
		增值礼包mbs消费接口
		"""
		GiftUpdate=userCenter.GiftUpdate()
		GiftUpdate.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GiftUpdate.changeEnv("turboradio.cn")
		GiftUpdate.data = {"memberId":"15965194","recordId":"1129","state":"1"}
		GiftUpdateRes = GiftUpdate.excute()
		assert GiftUpdateRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_ResourceQuery_test35(self):
		"""
		用户资源混合查询
		"""
		ResourceQuery=userCenter.ResourceQuery()
		ResourceQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		ResourceQuery.changeEnv("turboradio.cn")
		ResourceQuery.data = {"memberId":15965194,"sort":0,"couponType":2}
		ResourceQueryRes = ResourceQuery.excute()
		assert ResourceQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyQuery_test36(self):
		"""
		查询商家补贴方案
		"""
		SubsidyQuery=userCenter.SubsidyQuery()
		SubsidyQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyQuery.changeEnv("turboradio.cn")
		SubsidyQuery.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}
		SubsidyQueryRes = SubsidyQuery.excute()
		assert SubsidyQueryRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_SubsidyGetById_test37(self):
		"""
		查询方案详情
		"""
		SubsidyGetById=userCenter.SubsidyGetById()
		SubsidyGetById.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SubsidyGetById.changeEnv("turboradio.cn")
		SubsidyGetById.data = {"id":89}
		SubsidyGetByIdRes = SubsidyGetById.excute()
		result = SubsidyGetByIdRes.json()
		print("SubsidyGetByIdRes: {0} ".format(result))
		if "OBJECT" == result["dataType"]:
			r_data = result["data"]
		elif "LIST" == result["dataType"]:
			r_data = result["data"][0]
		p = str(r_data["id"])
		assert p == "89"
		p = str(r_data["subsidyWay"])
		assert p == "1"
		p = str(r_data["subsidyRange"])
		assert p == "1"
		p = str(r_data["subsidyTarget"])
		assert p == "2"

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_MemberReal_test38(self):
		"""
		会员
		"""
		MemberReal=userCenter.MemberReal()
		MemberReal.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		MemberReal.changeEnv("turboradio.cn")
		MemberReal.data = {"memberId":"15965194"}
		MemberRealRes = MemberReal.excute()
		assert MemberRealRes.text.__contains__("成功")

	@allure.feature("userCenter")
	@allure.severity("blocker")
	def test_DataTimePage_test39(self):
		"""
		DataTimePage
		"""
		DataTimePage=userCenter.DataTimePage()
		DataTimePage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		DataTimePage.changeEnv("turboradio.cn")
		DataTimePage.data = {"memberId":"15965194"}
		DataTimePageRes = DataTimePage.excute()
		assert DataTimePageRes.text.__contains__("孙统帅")
