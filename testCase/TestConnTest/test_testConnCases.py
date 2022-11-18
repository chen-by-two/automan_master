# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.orderCenter.orderCenterApi as orderCenter


import ApiLib.searchCenter.searchCenterApi as searchCenter


import ApiLib.recommend.recommendApi as recommend


import ApiLib.tag.tagApi as tag


class Test_TestConnTest:

	@allure.feature("TestConnTest")
	@allure.severity("normal")
	def test_UnifyorderConfirmCreate_testConn(self):
		"""
		连通性测试1
		"""
		UnifyorderConfirmCreate=orderCenter.UnifyorderConfirmCreate()
		UnifyorderConfirmCreate.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		UnifyorderConfirmCreate.changeEnv("turboradio.cn")
		UnifyorderConfirmCreate.data = {"skuNos":["53219-5062011"],"requestNo":1594976313000,"channel":"8","saleMerchantId":"539","saleStoreId":"74596","assistantId":0,"shareMemberId":0,"commissionNo":"","partnerMerchantId":0,"partnerOpenId":0,"channelId":"0","orderSource":0}
		UnifyorderConfirmCreateRes = UnifyorderConfirmCreate.excute()
		assert UnifyorderConfirmCreateRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UnifyorderConfirmInvoiceChange_testConn(self):
		"""
		连通性测试2
		"""
		UnifyorderConfirmInvoiceChange=orderCenter.UnifyorderConfirmInvoiceChange()
		UnifyorderConfirmInvoiceChange.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		UnifyorderConfirmInvoiceChange.changeEnv("turboradio.cn")
		UnifyorderConfirmInvoiceChange.data = {"confirmNo":"ec85243842af7ab1b360ea0d1b7f6264","invoiceTitleNo":3,"title":"","titleType":"","content":"","taxNo":"","registerAddress":"","registerphone":"","openingBank":"","bankNo":"","mailbox":""}
		UnifyorderConfirmInvoiceChangeRes = UnifyorderConfirmInvoiceChange.excute()
		assert UnifyorderConfirmInvoiceChangeRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UnifyorderOrderCreate_testConn(self):
		"""
		连通性测试3
		"""
		UnifyorderOrderCreate=orderCenter.UnifyorderOrderCreate()
		UnifyorderOrderCreate.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		UnifyorderOrderCreate.changeEnv("turboradio.cn")
		UnifyorderOrderCreate.data = {"confirmNo":"734333451127250ecec913c59ae5e021"}
		UnifyorderOrderCreateRes = UnifyorderOrderCreate.excute()
		assert UnifyorderOrderCreateRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UnifyorderCashierPayModes_testConn(self):
		"""
		连通性测试4
		"""
		UnifyorderCashierPayModes=orderCenter.UnifyorderCashierPayModes()
		UnifyorderCashierPayModes.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		UnifyorderCashierPayModes.changeEnv("turboradio.cn")
		UnifyorderCashierPayModes.data = {"orderNo":"80072005158767125750"}
		UnifyorderCashierPayModesRes = UnifyorderCashierPayModes.excute()
		assert UnifyorderCashierPayModesRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UnifyorderOrderDetail_testConn(self):
		"""
		连通性测试5
		"""
		UnifyorderOrderDetail=orderCenter.UnifyorderOrderDetail()
		UnifyorderOrderDetail.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		UnifyorderOrderDetail.changeEnv("turboradio.cn")
		UnifyorderOrderDetail.data = {"orderNo":"80072005158767125750"}
		UnifyorderOrderDetailRes = UnifyorderOrderDetail.excute()
		assert UnifyorderOrderDetailRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UnifyorderCashierCheck_testConn(self):
		"""
		连通性测试6
		"""
		UnifyorderCashierCheck=orderCenter.UnifyorderCashierCheck()
		UnifyorderCashierCheck.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		UnifyorderCashierCheck.changeEnv("turboradio.cn")
		UnifyorderCashierCheck.data = {"first":False,"orderNo":"80072005158767125750"}
		UnifyorderCashierCheckRes = UnifyorderCashierCheck.excute()
		assert UnifyorderCashierCheckRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_AdvisorListRecommendAdv_testConn(self):
		"""
		连通性测试6
		"""
		AdvisorListRecommendAdv=recommend.AdvisorListRecommendAdv()
		AdvisorListRecommendAdv.headers = {"Content-Type": "application/json;charset=UTF-8"}
		AdvisorListRecommendAdv.changeEnv("turboradio.cn")
		AdvisorListRecommendAdv.data = {"memberId":1,"pharmacyProvinceCode":"10000","pharmacyCityCode":"10001","pharmacyAreaCode":"10002","longitude":13.4,"latitude":23.5,"pageNum":1,"pageSize":10}
		AdvisorListRecommendAdvRes = AdvisorListRecommendAdv.excute()
		assert AdvisorListRecommendAdvRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_WordSuggesterSuggester_testConn(self):
		"""
		连通性测试7
		"""
		WordSuggesterSuggester=searchCenter.WordSuggesterSuggester()
		WordSuggesterSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterSuggester.changeEnv("turboradio.cn")
		WordSuggesterSuggester.data = {"searchContent":"感冒"}
		WordSuggesterSuggesterRes = WordSuggesterSuggester.excute()
		assert WordSuggesterSuggesterRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_GoodsSearchSearchGoodsAll_testConn(self):
		"""
		连通性测试8
		"""
		GoodsSearchSearchGoodsAll=searchCenter.GoodsSearchSearchGoodsAll()
		GoodsSearchSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsAll.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"provinceCodes":["123","234"],"cityCode":["1234","2345"]}
		GoodsSearchSearchGoodsAllRes = GoodsSearchSearchGoodsAll.excute()
		assert GoodsSearchSearchGoodsAllRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_GoodsSearchSearchGoodsByTradeCode_testConn(self):
		"""
		连通性测试9
		"""
		GoodsSearchSearchGoodsByTradeCode=searchCenter.GoodsSearchSearchGoodsByTradeCode()
		GoodsSearchSearchGoodsByTradeCode.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCode.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCode.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}
		GoodsSearchSearchGoodsByTradeCodeRes = GoodsSearchSearchGoodsByTradeCode.excute()
		assert GoodsSearchSearchGoodsByTradeCodeRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_GoodsSearchSearchGoodsGeo_testConn(self):
		"""
		连通性测试10
		"""
		GoodsSearchSearchGoodsGeo=searchCenter.GoodsSearchSearchGoodsGeo()
		GoodsSearchSearchGoodsGeo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsGeo.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsGeo.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}
		GoodsSearchSearchGoodsGeoRes = GoodsSearchSearchGoodsGeo.excute()
		assert GoodsSearchSearchGoodsGeoRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_OtoManageSearch_testConn(self):
		"""
		连通性测试11
		"""
		OtoManageSearch=searchCenter.OtoManageSearch()
		OtoManageSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		OtoManageSearch.changeEnv("turboradio.cn")
		OtoManageSearch.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}
		OtoManageSearchRes = OtoManageSearch.excute()
		assert OtoManageSearchRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_GoodsSearchCorrectSearchContent_testConn(self):
		"""
		连通性测试12
		"""
		GoodsSearchCorrectSearchContent=searchCenter.GoodsSearchCorrectSearchContent()
		GoodsSearchCorrectSearchContent.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchCorrectSearchContent.changeEnv("turboradio.cn")
		GoodsSearchCorrectSearchContent.data = {"searchContent":"生物疝补骗"}
		GoodsSearchCorrectSearchContentRes = GoodsSearchCorrectSearchContent.excute()
		assert GoodsSearchCorrectSearchContentRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_QueryGoodsQueryGoodsBaseInfo_testConn(self):
		"""
		连通性测试13
		"""
		QueryGoodsQueryGoodsBaseInfo=searchCenter.QueryGoodsQueryGoodsBaseInfo()
		QueryGoodsQueryGoodsBaseInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		QueryGoodsQueryGoodsBaseInfo.changeEnv("turboradio.cn")
		QueryGoodsQueryGoodsBaseInfo.data = {"sourceType":"1","queryGoodsBaseInfoDtoList":[{"merchantId":"649","storeId":"56920","goodsInternalId":"600839"},{"merchantId":"649","storeId":"56920","goodsInternalId":"LS5533"}]}
		QueryGoodsQueryGoodsBaseInfoRes = QueryGoodsQueryGoodsBaseInfo.excute()
		assert QueryGoodsQueryGoodsBaseInfoRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_SkuQuery_testConn(self):
		"""
		连通性测试14
		"""
		SkuQuery=searchCenter.SkuQuery()
		SkuQuery.headers = {"Content-Type": "application/json;charset=UTF-8"}
		SkuQuery.changeEnv("turboradio.cn")
		SkuQuery.data = {"page":1,"size":2,"merchantId":649,"storeId":56920}
		SkuQueryRes = SkuQuery.excute()
		assert SkuQueryRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_Sku_testConn(self):
		"""
		连通性测试15
		"""
		Sku=searchCenter.Sku()
		Sku.headers = None
		Sku.changeEnv("turboradio.cn")
		Sku.params = {"None":"625-11953-2-211891"}
		SkuRes = Sku.excute()
		assert SkuRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_SkuSimple_testConn(self):
		"""
		连通性测试16
		"""
		SkuSimple=searchCenter.SkuSimple()
		SkuSimple.headers = {"Content-Type": "application/json;charset=UTF-8"}
		SkuSimple.changeEnv("turboradio.cn")
		SkuSimple.data = {"ids":["649-56920-2-LS4516","649-56920-2-921138"]}
		SkuSimpleRes = SkuSimple.excute()
		assert SkuSimpleRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_GoodsSearchSearchUnify_testConn(self):
		"""
		连通性测试17
		"""
		GoodsSearchSearchUnify=searchCenter.GoodsSearchSearchUnify()
		GoodsSearchSearchUnify.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchUnify.changeEnv("turboradio.cn")
		GoodsSearchSearchUnify.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}
		GoodsSearchSearchUnifyRes = GoodsSearchSearchUnify.excute()
		assert GoodsSearchSearchUnifyRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_GoodsSearchSearch_testConn(self):
		"""
		连通性测试18
		"""
		GoodsSearchSearch=searchCenter.GoodsSearchSearch()
		GoodsSearchSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearch.changeEnv("turboradio.cn")
		GoodsSearchSearch.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}
		GoodsSearchSearchRes = GoodsSearchSearch.excute()
		assert GoodsSearchSearchRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UserPackageBaseCreate_testConn(self):
		"""
		连通性测试19
		"""
		UserPackageBaseCreate=tag.UserPackageBaseCreate()
		UserPackageBaseCreate.headers = {"Content-Type": "application/json;charset=UTF-8"}
		UserPackageBaseCreate.changeEnv("turboradio.cn")
		UserPackageBaseCreate.data = {"clauseType":"IS","tagId":"XB","tagValue":"男"}
		UserPackageBaseCreateRes = UserPackageBaseCreate.excute()
		assert UserPackageBaseCreateRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UserPackageHighlevelCreate_testConn(self):
		"""
		连通性测试20
		"""
		UserPackageHighlevelCreate=tag.UserPackageHighlevelCreate()
		UserPackageHighlevelCreate.headers = {"Content-Type": "application/json;charset=UTF-8"}
		UserPackageHighlevelCreate.changeEnv("turboradio.cn")
		UserPackageHighlevelCreate.data = {"packageIds":[1,3,5],"relationType":"AND"}
		UserPackageHighlevelCreateRes = UserPackageHighlevelCreate.excute()
		assert UserPackageHighlevelCreateRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UserPackageUsersGet_testConn(self):
		"""
		连通性测试21
		"""
		UserPackageUsersGet=tag.UserPackageUsersGet()
		UserPackageUsersGet.headers = {"Content-Type": "application/json;charset=UTF-8"}
		UserPackageUsersGet.changeEnv("turboradio.cn")
		UserPackageUsersGet.data = {"packageId":2,"page":1,"size":1000}
		UserPackageUsersGetRes = UserPackageUsersGet.excute()
		assert UserPackageUsersGetRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_MemberWideInsertMemberPackage_testConn(self):
		"""
		连通性测试22
		"""
		MemberWideInsertMemberPackage=tag.MemberWideInsertMemberPackage()
		MemberWideInsertMemberPackage.headers = {"Content-Type": "application/json;charset=UTF-8"}
		MemberWideInsertMemberPackage.changeEnv("turboradio.cn")
		MemberWideInsertMemberPackage.data = {"conditions":[{"conditionType":1,"valueType":1,"values":["1","2"],"fieldType":1},{"conditionType":2,"valueType":2,"values":["1993"],"fieldType":1},{"conditionType":2,"valueType":3,"values":["1995"],"fieldType":1},{"conditionType":3,"valueType":1,"values":["110000","130000"],"fieldType":1},{"conditionType":4,"valueType":1,"values":["130200","130700"],"fieldType":1}]}
		MemberWideInsertMemberPackageRes = MemberWideInsertMemberPackage.excute()
		assert MemberWideInsertMemberPackageRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_OrderWideInsertOrderPackage_testConn(self):
		"""
		连通性测试23
		"""
		OrderWideInsertOrderPackage=tag.OrderWideInsertOrderPackage()
		OrderWideInsertOrderPackage.headers = {"Content-Type": "application/json;charset=UTF-8"}
		OrderWideInsertOrderPackage.changeEnv("turboradio.cn")
		OrderWideInsertOrderPackage.data = {"conditions":[{"conditionType":1,"valueType":2,"values":["2020-05-06 12:12:12"],"fieldType":1},{"conditionType":1,"valueType":3,"values":["2020-05-07 12:12:12"],"fieldType":1},{"conditionType":2,"valueType":2,"values":["0"],"fieldType":2},{"conditionType":2,"valueType":3,"values":["18"],"fieldType":2}]}
		OrderWideInsertOrderPackageRes = OrderWideInsertOrderPackage.excute()
		assert OrderWideInsertOrderPackageRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UserPackageDelete_testConn(self):
		"""
		连通性测试24
		"""
		UserPackageDelete=tag.UserPackageDelete()
		UserPackageDelete.headers = {"Content-Type": "application/json;charset=UTF-8"}
		UserPackageDelete.changeEnv("turboradio.cn")
		UserPackageDelete.data = {"id" : 2}
		UserPackageDeleteRes = UserPackageDelete.excute()
		assert UserPackageDeleteRes.status_code == 200

	@allure.feature("TestConnTest")
	@allure.severity("blocker")
	def test_UserPackageListMember_testConn(self):
		"""
		连通性测试25
		"""
		UserPackageListMember=tag.UserPackageListMember()
		UserPackageListMember.headers = {"Content-Type": "application/json;charset=UTF-8"}
		UserPackageListMember.changeEnv("turboradio.cn")
		UserPackageListMember.data = {"ids":[1,2,3]}
		UserPackageListMemberRes = UserPackageListMember.excute()
		assert UserPackageListMemberRes.status_code == 200
