# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
import ApiLib.im.imApi as im


class Test_im:

	@allure.feature("im")
	@allure.severity("blocker")
	def test_MyCustomers_MyCustomers(self):
		"""
		顾问端-我的顾客
		"""
		MyCustomers=im.MyCustomers()
		MyCustomers.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MyCustomers.changeEnv("turboradio.cn")
		MyCustomers.data = {"pageSize":"100","pageNo":1,"advisorId":"2033048","name":""}
		MyCustomersRes = MyCustomers.excute()
		assert MyCustomersRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor1_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表查询
		"""
		GetRecommendAdvisor1=im.GetRecommendAdvisor1()
		GetRecommendAdvisor1.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor1.changeEnv("turboradio.cn")
		GetRecommendAdvisor1.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":1}
		GetRecommendAdvisor1Res = GetRecommendAdvisor1.excute()
		assert GetRecommendAdvisor1Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetRecommendAdvisor2_GetRecommendAdvisor1(self):
		"""
		顾客端-推荐顾问列表距离最近查询
		"""
		GetRecommendAdvisor2=im.GetRecommendAdvisor2()
		GetRecommendAdvisor2.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetRecommendAdvisor2.changeEnv("turboradio.cn")
		GetRecommendAdvisor2.data = {"pageNum":1,"pageSize":20,"latitude":31.973886489868164,"longitude":118.77415466308594,"memberId":15961031,"pharmacyProvinceCode":"","pharmacyCityCode":"","pharmacyAreaCode":"","sortField":2}
		GetRecommendAdvisor2Res = GetRecommendAdvisor2.excute()
		assert GetRecommendAdvisor2Res.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetAdvisorInfo_getAdvisorInfo(self):
		"""
		顾客端-顾问详情
		"""
		GetAdvisorInfo=im.GetAdvisorInfo()
		GetAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetAdvisorInfo.changeEnv("turboradio.cn")
		GetAdvisorInfo.data = {"memberId":"200341","latitude":"","longitude":""}
		GetAdvisorInfoRes = GetAdvisorInfo.excute()
		assert GetAdvisorInfoRes.status_code == 200

	@allure.feature("im")
	@allure.severity("blocker")
	def test_GetBindAdvisorInfo_GetBindAdvisorInfo(self):
		"""
		顾客端-绑定顾问信息
		"""
		GetBindAdvisorInfo=im.GetBindAdvisorInfo()
		GetBindAdvisorInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GetBindAdvisorInfo.changeEnv("turboradio.cn")
		GetBindAdvisorInfo.data = {"memberId":"15961031"}
		GetBindAdvisorInfoRes = GetBindAdvisorInfo.excute()
		assert GetBindAdvisorInfoRes.status_code == 200
