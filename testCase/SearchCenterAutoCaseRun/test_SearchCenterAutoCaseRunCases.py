# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.searchCenter.searchCenterApi as searchCenter


class Test_SearchCenterAutoCaseRun:

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterSuggester_testConn(self):
		"""
		查询商品
		"""
		WordSuggesterSuggester=searchCenter.WordSuggesterSuggester()
		WordSuggesterSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterSuggester.changeEnv("turboradio.cn")
		WordSuggesterSuggester.data = {"searchContent":"感冒"}
		WordSuggesterSuggesterRes = WordSuggesterSuggester.excute()
		assert WordSuggesterSuggesterRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsAll_testConn(self):
		"""
		商品搜索引擎查询-全国搜索
		"""
		GoodsSearchSearchGoodsAll=searchCenter.GoodsSearchSearchGoodsAll()
		GoodsSearchSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsAll.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"provinceCodes":["123","234"],"cityCode":["1234","2345"]}
		GoodsSearchSearchGoodsAllRes = GoodsSearchSearchGoodsAll.excute()
		assert GoodsSearchSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCode_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsByTradeCode=searchCenter.GoodsSearchSearchGoodsByTradeCode()
		GoodsSearchSearchGoodsByTradeCode.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCode.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCode.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}
		GoodsSearchSearchGoodsByTradeCodeRes = GoodsSearchSearchGoodsByTradeCode.excute()
		assert GoodsSearchSearchGoodsByTradeCodeRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsGeo_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsGeo=searchCenter.GoodsSearchSearchGoodsGeo()
		GoodsSearchSearchGoodsGeo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsGeo.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsGeo.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}
		GoodsSearchSearchGoodsGeoRes = GoodsSearchSearchGoodsGeo.excute()
		assert GoodsSearchSearchGoodsGeoRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_OtoManageSearch_testConn(self):
		"""
		商品搜索引擎查询-oto运营管理查询
		"""
		OtoManageSearch=searchCenter.OtoManageSearch()
		OtoManageSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		OtoManageSearch.changeEnv("turboradio.cn")
		OtoManageSearch.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}
		OtoManageSearchRes = OtoManageSearch.excute()
		assert OtoManageSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchCorrectSearchContent_testConn(self):
		"""
		商品搜索词修正
		"""
		GoodsSearchCorrectSearchContent=searchCenter.GoodsSearchCorrectSearchContent()
		GoodsSearchCorrectSearchContent.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchCorrectSearchContent.changeEnv("turboradio.cn")
		GoodsSearchCorrectSearchContent.data = {"searchContent":"生物疝补骗"}
		GoodsSearchCorrectSearchContentRes = GoodsSearchCorrectSearchContent.excute()
		assert GoodsSearchCorrectSearchContentRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_QueryGoodsQueryGoodsBaseInfo_testConn(self):
		"""
		查询商品价格和销量
		"""
		QueryGoodsQueryGoodsBaseInfo=searchCenter.QueryGoodsQueryGoodsBaseInfo()
		QueryGoodsQueryGoodsBaseInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		QueryGoodsQueryGoodsBaseInfo.changeEnv("turboradio.cn")
		QueryGoodsQueryGoodsBaseInfo.data = {"sourceType":"1","queryGoodsBaseInfoDtoList":[{"merchantId":"649","storeId":"56920","goodsInternalId":"600839"},{"merchantId":"649","storeId":"56920","goodsInternalId":"LS5533"}]}
		QueryGoodsQueryGoodsBaseInfoRes = QueryGoodsQueryGoodsBaseInfo.excute()
		assert QueryGoodsQueryGoodsBaseInfoRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_SkuQuery_testConn(self):
		"""
		查询药品信息列表
		"""
		SkuQuery=searchCenter.SkuQuery()
		SkuQuery.headers = {"Content-Type": "application/json;charset=UTF-8"}
		SkuQuery.changeEnv("turboradio.cn")
		SkuQuery.data = {"page":1,"size":2,"merchantId":649,"storeId":56920}
		SkuQueryRes = SkuQuery.excute()
		assert SkuQueryRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_Sku_testConn(self):
		"""
		根据skuId查询药品基本信息
		"""
		Sku=searchCenter.Sku()
		Sku.headers = None
		Sku.changeEnv("turboradio.cn")
		Sku.params = {"None":"625-11953-2-211891"}
		SkuRes = Sku.excute()
		assert SkuRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_SkuSimple_testConn(self):
		"""
		根据skuId列表批量查询药品简单信息
		"""
		SkuSimple=searchCenter.SkuSimple()
		SkuSimple.headers = {"Content-Type": "application/json;charset=UTF-8"}
		SkuSimple.changeEnv("turboradio.cn")
		SkuSimple.data = {"ids":["649-56920-2-LS4516","649-56920-2-921138"]}
		SkuSimpleRes = SkuSimple.excute()
		assert SkuSimpleRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchUnify_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearchUnify=searchCenter.GoodsSearchSearchUnify()
		GoodsSearchSearchUnify.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchUnify.changeEnv("turboradio.cn")
		GoodsSearchSearchUnify.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}
		GoodsSearchSearchUnifyRes = GoodsSearchSearchUnify.excute()
		assert GoodsSearchSearchUnifyRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearch_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearch=searchCenter.GoodsSearchSearch()
		GoodsSearchSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearch.changeEnv("turboradio.cn")
		GoodsSearchSearch.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}
		GoodsSearchSearchRes = GoodsSearchSearch.excute()
		assert GoodsSearchSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchDtpGoods_testConn(self):
		"""
		查询dtp商品
		"""
		GoodsSearchSearchDtpGoods=searchCenter.GoodsSearchSearchDtpGoods()
		GoodsSearchSearchDtpGoods.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchDtpGoods.changeEnv("turboradio.cn")
		GoodsSearchSearchDtpGoods.data = {"searchContent":"玉屏风颗粒 宫瘤宁胶囊","categoryInfo":"","wordOperator":0,"searchPrescription":1,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":null,"longitude":null,"distance":null,"isAccurate":1,"storeNum":10,"searchSource":"O2O"}
		GoodsSearchSearchDtpGoodsRes = GoodsSearchSearchDtpGoods.excute()
		assert GoodsSearchSearchDtpGoodsRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCodes_testConn(self):
		"""
		根据多个条码基于地理位置搜索
		"""
		GoodsSearchSearchGoodsByTradeCodes=searchCenter.GoodsSearchSearchGoodsByTradeCodes()
		GoodsSearchSearchGoodsByTradeCodes.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCodes.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCodes.data = {"tradeCodes":["6921575620230"],"goodsNum":10,"latitude":31.972033,"longitude":118.777545,"searchSource":"O2O","merchantId":"","storeId":"","business":"nice_drug","member":{"memberId":15967187,"sessionId":"dkahgaj;ld;afjaha","page":1}}
		GoodsSearchSearchGoodsByTradeCodesRes = GoodsSearchSearchGoodsByTradeCodes.excute()
		assert GoodsSearchSearchGoodsByTradeCodesRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterExist_testConn(self):
		"""
		判断联想词是否存在
		"""
		WordSuggesterExist=searchCenter.WordSuggesterExist()
		WordSuggesterExist.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterExist.changeEnv("turboradio.cn")
		WordSuggesterExist.data = {"searchContent": "感冒","searchSource": "O2O","business": "nice_drug","member" : { "memberId" : 15967187, "sessionId" : "ghfjkhhjfhft","page" : 1}}
		WordSuggesterExistRes = WordSuggesterExist.excute()
		assert WordSuggesterExistRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSearchGoodsAll_testConn(self):
		"""
		福利严选搜索查询
		"""
		WelfareGoodsSearchGoodsAll=searchCenter.WelfareGoodsSearchGoodsAll()
		WelfareGoodsSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSearchGoodsAll.changeEnv("turboradio.cn")
		WelfareGoodsSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"channels":[7,8]}
		WelfareGoodsSearchGoodsAllRes = WelfareGoodsSearchGoodsAll.excute()
		assert WelfareGoodsSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSuggester_testConn(self):
		"""
		福利严选联想词搜索
		"""
		WelfareGoodsSuggester=searchCenter.WelfareGoodsSuggester()
		WelfareGoodsSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSuggester.changeEnv("turboradio.cn")
		WelfareGoodsSuggester.data = {"searchContent":"洗衣液","channels":[7,8]}
		WelfareGoodsSuggesterRes = WelfareGoodsSuggester.excute()
		assert WelfareGoodsSuggesterRes.text.__contains__("\"errno\":\"0\"")
import ApiLib.searchCenter.searchCenterApi as searchCenter


class Test_SearchCenterAutoCaseRun:

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterSuggester_testConn(self):
		"""
		查询商品
		"""
		WordSuggesterSuggester=searchCenter.WordSuggesterSuggester()
		WordSuggesterSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterSuggester.changeEnv("turboradio.cn")
		WordSuggesterSuggester.data = {"searchContent":"感冒"}
		WordSuggesterSuggesterRes = WordSuggesterSuggester.excute()
		assert WordSuggesterSuggesterRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsAll_testConn(self):
		"""
		商品搜索引擎查询-全国搜索
		"""
		GoodsSearchSearchGoodsAll=searchCenter.GoodsSearchSearchGoodsAll()
		GoodsSearchSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsAll.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsAll.data = {
    "searchContent": "参苏补肾胶囊",
    "merchantId":"663",
    "sortField" : 0,
    "sortType": 0,
    "page" : 1,
    "limit": 10,
    "latitude" : 31.974003,
    "longitude" : 118.781429,
    "provinceCodes" : null,
    "cityCodes" : null,
 "searchSource": "O2O",
 "showOffShelf" : 1,
    "business": "nice_drug",
    "member" : {
        "memberId" : 15967187,
        "sessionId" : "5748342542397602",
        "page" : 1
    }
}
		GoodsSearchSearchGoodsAllRes = GoodsSearchSearchGoodsAll.excute()
		assert GoodsSearchSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCode_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsByTradeCode=searchCenter.GoodsSearchSearchGoodsByTradeCode()
		GoodsSearchSearchGoodsByTradeCode.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCode.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCode.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}
		GoodsSearchSearchGoodsByTradeCodeRes = GoodsSearchSearchGoodsByTradeCode.excute()
		assert GoodsSearchSearchGoodsByTradeCodeRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsGeo_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsGeo=searchCenter.GoodsSearchSearchGoodsGeo()
		GoodsSearchSearchGoodsGeo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsGeo.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsGeo.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}
		GoodsSearchSearchGoodsGeoRes = GoodsSearchSearchGoodsGeo.excute()
		assert GoodsSearchSearchGoodsGeoRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_OtoManageSearch_testConn(self):
		"""
		商品搜索引擎查询-oto运营管理查询
		"""
		OtoManageSearch=searchCenter.OtoManageSearch()
		OtoManageSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		OtoManageSearch.changeEnv("turboradio.cn")
		OtoManageSearch.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}
		OtoManageSearchRes = OtoManageSearch.excute()
		assert OtoManageSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchUnify_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearchUnify=searchCenter.GoodsSearchSearchUnify()
		GoodsSearchSearchUnify.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchUnify.changeEnv("turboradio.cn")
		GoodsSearchSearchUnify.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}
		GoodsSearchSearchUnifyRes = GoodsSearchSearchUnify.excute()
		assert GoodsSearchSearchUnifyRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearch_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearch=searchCenter.GoodsSearchSearch()
		GoodsSearchSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearch.changeEnv("turboradio.cn")
		GoodsSearchSearch.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}
		GoodsSearchSearchRes = GoodsSearchSearch.excute()
		assert GoodsSearchSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchDtpGoods_testConn(self):
		"""
		查询dtp商品
		"""
		GoodsSearchSearchDtpGoods=searchCenter.GoodsSearchSearchDtpGoods()
		GoodsSearchSearchDtpGoods.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchDtpGoods.changeEnv("turboradio.cn")
		GoodsSearchSearchDtpGoods.data = {"searchContent":"玉屏风颗粒 宫瘤宁胶囊","categoryInfo":"","wordOperator":0,"searchPrescription":1,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":null,"longitude":null,"distance":null,"isAccurate":1,"storeNum":10,"searchSource":"O2O"}
		GoodsSearchSearchDtpGoodsRes = GoodsSearchSearchDtpGoods.excute()
		assert GoodsSearchSearchDtpGoodsRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCodes_testConn(self):
		"""
		根据多个条码基于地理位置搜索
		"""
		GoodsSearchSearchGoodsByTradeCodes=searchCenter.GoodsSearchSearchGoodsByTradeCodes()
		GoodsSearchSearchGoodsByTradeCodes.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCodes.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCodes.data = {"tradeCodes":["6921575620230"],"goodsNum":10,"latitude":31.972033,"longitude":118.777545,"searchSource":"O2O","merchantId":"","storeId":"","business":"nice_drug","member":{"memberId":15967187,"sessionId":"dkahgaj;ld;afjaha","page":1}}
		GoodsSearchSearchGoodsByTradeCodesRes = GoodsSearchSearchGoodsByTradeCodes.excute()
		assert GoodsSearchSearchGoodsByTradeCodesRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterExist_testConn(self):
		"""
		判断联想词是否存在
		"""
		WordSuggesterExist=searchCenter.WordSuggesterExist()
		WordSuggesterExist.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterExist.changeEnv("turboradio.cn")
		WordSuggesterExist.data = {"searchContent": "感冒","searchSource": "O2O","business": "nice_drug","member" : { "memberId" : 15967187, "sessionId" : "ghfjkhhjfhft","page" : 1}}
		WordSuggesterExistRes = WordSuggesterExist.excute()
		assert WordSuggesterExistRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSearchGoodsAll_testConn(self):
		"""
		福利严选搜索查询
		"""
		WelfareGoodsSearchGoodsAll=searchCenter.WelfareGoodsSearchGoodsAll()
		WelfareGoodsSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSearchGoodsAll.changeEnv("turboradio.cn")
		WelfareGoodsSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"channels":[7,8]}
		WelfareGoodsSearchGoodsAllRes = WelfareGoodsSearchGoodsAll.excute()
		assert WelfareGoodsSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSuggester_testConn(self):
		"""
		福利严选联想词搜索
		"""
		WelfareGoodsSuggester=searchCenter.WelfareGoodsSuggester()
		WelfareGoodsSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSuggester.changeEnv("turboradio.cn")
		WelfareGoodsSuggester.data = {"searchContent":"洗衣液","channels":[7,8]}
		WelfareGoodsSuggesterRes = WelfareGoodsSuggester.excute()
		assert WelfareGoodsSuggesterRes.text.__contains__("\"errno\":0")
import ApiLib.searchCenter.searchCenterApi as searchCenter


class Test_SearchCenterAutoCaseRun:

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterSuggester_testConn(self):
		"""
		查询商品
		"""
		WordSuggesterSuggester=searchCenter.WordSuggesterSuggester()
		WordSuggesterSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterSuggester.changeEnv("turboradio.cn")
		WordSuggesterSuggester.data = {"searchContent":"感冒"}
		WordSuggesterSuggesterRes = WordSuggesterSuggester.excute()
		assert WordSuggesterSuggesterRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsAll_testConn(self):
		"""
		商品搜索引擎查询-全国搜索
		"""
		GoodsSearchSearchGoodsAll=searchCenter.GoodsSearchSearchGoodsAll()
		GoodsSearchSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsAll.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsAll.data = {
    "searchContent": "参苏补肾胶囊",
    "merchantId":"663",
    "sortField" : 0,
    "sortType": 0,
    "page" : 1,
    "limit": 10,
    "latitude" : 31.974003,
    "longitude" : 118.781429,
    "provinceCodes" : None,
    "cityCodes" : None,
 "searchSource": "O2O",
 "showOffShelf" : 1,
    "business": "nice_drug",
    "member" : {
        "memberId" : 15967187,
        "sessionId" : "5748342542397602",
        "page" : 1
    }
}
		GoodsSearchSearchGoodsAllRes = GoodsSearchSearchGoodsAll.excute()
		assert GoodsSearchSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCode_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsByTradeCode=searchCenter.GoodsSearchSearchGoodsByTradeCode()
		GoodsSearchSearchGoodsByTradeCode.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCode.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCode.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}
		GoodsSearchSearchGoodsByTradeCodeRes = GoodsSearchSearchGoodsByTradeCode.excute()
		assert GoodsSearchSearchGoodsByTradeCodeRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsGeo_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsGeo=searchCenter.GoodsSearchSearchGoodsGeo()
		GoodsSearchSearchGoodsGeo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsGeo.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsGeo.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}
		GoodsSearchSearchGoodsGeoRes = GoodsSearchSearchGoodsGeo.excute()
		assert GoodsSearchSearchGoodsGeoRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_OtoManageSearch_testConn(self):
		"""
		商品搜索引擎查询-oto运营管理查询
		"""
		OtoManageSearch=searchCenter.OtoManageSearch()
		OtoManageSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		OtoManageSearch.changeEnv("turboradio.cn")
		OtoManageSearch.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}
		OtoManageSearchRes = OtoManageSearch.excute()
		assert OtoManageSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchUnify_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearchUnify=searchCenter.GoodsSearchSearchUnify()
		GoodsSearchSearchUnify.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchUnify.changeEnv("turboradio.cn")
		GoodsSearchSearchUnify.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}
		GoodsSearchSearchUnifyRes = GoodsSearchSearchUnify.excute()
		assert GoodsSearchSearchUnifyRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearch_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearch=searchCenter.GoodsSearchSearch()
		GoodsSearchSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearch.changeEnv("turboradio.cn")
		GoodsSearchSearch.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}
		GoodsSearchSearchRes = GoodsSearchSearch.excute()
		assert GoodsSearchSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchDtpGoods_testConn(self):
		"""
		查询dtp商品
		"""
		GoodsSearchSearchDtpGoods=searchCenter.GoodsSearchSearchDtpGoods()
		GoodsSearchSearchDtpGoods.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchDtpGoods.changeEnv("turboradio.cn")
		GoodsSearchSearchDtpGoods.data = {"searchContent":"玉屏风颗粒 宫瘤宁胶囊","categoryInfo":"","wordOperator":0,"searchPrescription":1,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":None,"longitude":None,"distance":None,"isAccurate":1,"storeNum":10,"searchSource":"O2O"}
		GoodsSearchSearchDtpGoodsRes = GoodsSearchSearchDtpGoods.excute()
		assert GoodsSearchSearchDtpGoodsRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCodes_testConn(self):
		"""
		根据多个条码基于地理位置搜索
		"""
		GoodsSearchSearchGoodsByTradeCodes=searchCenter.GoodsSearchSearchGoodsByTradeCodes()
		GoodsSearchSearchGoodsByTradeCodes.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCodes.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCodes.data = {"tradeCodes":["6921575620230"],"goodsNum":10,"latitude":31.972033,"longitude":118.777545,"searchSource":"O2O","merchantId":"","storeId":"","business":"nice_drug","member":{"memberId":15967187,"sessionId":"dkahgaj;ld;afjaha","page":1}}
		GoodsSearchSearchGoodsByTradeCodesRes = GoodsSearchSearchGoodsByTradeCodes.excute()
		assert GoodsSearchSearchGoodsByTradeCodesRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterExist_testConn(self):
		"""
		判断联想词是否存在
		"""
		WordSuggesterExist=searchCenter.WordSuggesterExist()
		WordSuggesterExist.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterExist.changeEnv("turboradio.cn")
		WordSuggesterExist.data = {"searchContent": "感冒","searchSource": "O2O","business": "nice_drug","member" : { "memberId" : 15967187, "sessionId" : "ghfjkhhjfhft","page" : 1}}
		WordSuggesterExistRes = WordSuggesterExist.excute()
		assert WordSuggesterExistRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSearchGoodsAll_testConn(self):
		"""
		福利严选搜索查询
		"""
		WelfareGoodsSearchGoodsAll=searchCenter.WelfareGoodsSearchGoodsAll()
		WelfareGoodsSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSearchGoodsAll.changeEnv("turboradio.cn")
		WelfareGoodsSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"channels":[7,8]}
		WelfareGoodsSearchGoodsAllRes = WelfareGoodsSearchGoodsAll.excute()
		assert WelfareGoodsSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSuggester_testConn(self):
		"""
		福利严选联想词搜索
		"""
		WelfareGoodsSuggester=searchCenter.WelfareGoodsSuggester()
		WelfareGoodsSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSuggester.changeEnv("turboradio.cn")
		WelfareGoodsSuggester.data = {"searchContent":"洗衣液","channels":[7,8]}
		WelfareGoodsSuggesterRes = WelfareGoodsSuggester.excute()
		assert WelfareGoodsSuggesterRes.text.__contains__("\"errno\":0")
import ApiLib.searchCenter.searchCenterApi as searchCenter


class Test_SearchCenterAutoCaseRun:

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterSuggester_testConn(self):
		"""
		查询商品
		"""
		WordSuggesterSuggester=searchCenter.WordSuggesterSuggester()
		WordSuggesterSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterSuggester.changeEnv("turboradio.cn")
		WordSuggesterSuggester.data = {"searchContent":"感冒"}
		WordSuggesterSuggesterRes = WordSuggesterSuggester.excute()
		assert WordSuggesterSuggesterRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsAll_testConn(self):
		"""
		商品搜索引擎查询-全国搜索
		"""
		GoodsSearchSearchGoodsAll=searchCenter.GoodsSearchSearchGoodsAll()
		GoodsSearchSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsAll.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsAll.data = {
    "searchContent": "参苏补肾胶囊",
    "merchantId":"663",
    "sortField" : 0,
    "sortType": 0,
    "page" : 1,
    "limit": 10,
    "latitude" : 31.974003,
    "longitude" : 118.781429,
    "provinceCodes" : None,
    "cityCodes" : None,
 "searchSource": "O2O",
 "showOffShelf" : 1,
    "business": "nice_drug",
    "member" : {
        "memberId" : 15967187,
        "sessionId" : "5748342542397602",
        "page" : 1
    }
}
		GoodsSearchSearchGoodsAllRes = GoodsSearchSearchGoodsAll.excute()
		assert GoodsSearchSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCode_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsByTradeCode=searchCenter.GoodsSearchSearchGoodsByTradeCode()
		GoodsSearchSearchGoodsByTradeCode.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCode.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCode.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}
		GoodsSearchSearchGoodsByTradeCodeRes = GoodsSearchSearchGoodsByTradeCode.excute()
		assert GoodsSearchSearchGoodsByTradeCodeRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsGeo_testConn(self):
		"""
		商品搜索引擎查询-根据条码基于地理位置搜索全国商品
		"""
		GoodsSearchSearchGoodsGeo=searchCenter.GoodsSearchSearchGoodsGeo()
		GoodsSearchSearchGoodsGeo.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsGeo.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsGeo.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}
		GoodsSearchSearchGoodsGeoRes = GoodsSearchSearchGoodsGeo.excute()
		assert GoodsSearchSearchGoodsGeoRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_OtoManageSearch_testConn(self):
		"""
		商品搜索引擎查询-oto运营管理查询
		"""
		OtoManageSearch=searchCenter.OtoManageSearch()
		OtoManageSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		OtoManageSearch.changeEnv("turboradio.cn")
		OtoManageSearch.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}
		OtoManageSearchRes = OtoManageSearch.excute()
		assert OtoManageSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchUnify_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearchUnify=searchCenter.GoodsSearchSearchUnify()
		GoodsSearchSearchUnify.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchUnify.changeEnv("turboradio.cn")
		GoodsSearchSearchUnify.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}
		GoodsSearchSearchUnifyRes = GoodsSearchSearchUnify.excute()
		assert GoodsSearchSearchUnifyRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearch_testConn(self):
		"""
		查询商品
		"""
		GoodsSearchSearch=searchCenter.GoodsSearchSearch()
		GoodsSearchSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearch.changeEnv("turboradio.cn")
		GoodsSearchSearch.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}
		GoodsSearchSearchRes = GoodsSearchSearch.excute()
		assert GoodsSearchSearchRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchDtpGoods_testConn(self):
		"""
		查询dtp商品
		"""
		GoodsSearchSearchDtpGoods=searchCenter.GoodsSearchSearchDtpGoods()
		GoodsSearchSearchDtpGoods.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchDtpGoods.changeEnv("turboradio.cn")
		GoodsSearchSearchDtpGoods.data = {"searchContent":"玉屏风颗粒 宫瘤宁胶囊","categoryInfo":"","wordOperator":0,"searchPrescription":1,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":None,"longitude":None,"distance":None,"isAccurate":1,"storeNum":10,"searchSource":"O2O"}
		GoodsSearchSearchDtpGoodsRes = GoodsSearchSearchDtpGoods.excute()
		assert GoodsSearchSearchDtpGoodsRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_GoodsSearchSearchGoodsByTradeCodes_testConn(self):
		"""
		根据多个条码基于地理位置搜索
		"""
		GoodsSearchSearchGoodsByTradeCodes=searchCenter.GoodsSearchSearchGoodsByTradeCodes()
		GoodsSearchSearchGoodsByTradeCodes.headers = {"Content-Type": "application/json;charset=UTF-8"}
		GoodsSearchSearchGoodsByTradeCodes.changeEnv("turboradio.cn")
		GoodsSearchSearchGoodsByTradeCodes.data = {"tradeCodes":["6921575620230"],"goodsNum":10,"latitude":31.972033,"longitude":118.777545,"searchSource":"O2O","merchantId":"","storeId":"","business":"nice_drug","member":{"memberId":15967187,"sessionId":"dkahgaj;ld;afjaha","page":1}}
		GoodsSearchSearchGoodsByTradeCodesRes = GoodsSearchSearchGoodsByTradeCodes.excute()
		assert GoodsSearchSearchGoodsByTradeCodesRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WordSuggesterExist_testConn(self):
		"""
		判断联想词是否存在
		"""
		WordSuggesterExist=searchCenter.WordSuggesterExist()
		WordSuggesterExist.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WordSuggesterExist.changeEnv("turboradio.cn")
		WordSuggesterExist.data = {"searchContent": "感冒","searchSource": "O2O","business": "nice_drug","member" : { "memberId" : 15967187, "sessionId" : "ghfjkhhjfhft","page" : 1}}
		WordSuggesterExistRes = WordSuggesterExist.excute()
		assert WordSuggesterExistRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSearchGoodsAll_testConn(self):
		"""
		福利严选搜索查询
		"""
		WelfareGoodsSearchGoodsAll=searchCenter.WelfareGoodsSearchGoodsAll()
		WelfareGoodsSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSearchGoodsAll.changeEnv("turboradio.cn")
		WelfareGoodsSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"channels":[7,8]}
		WelfareGoodsSearchGoodsAllRes = WelfareGoodsSearchGoodsAll.excute()
		assert WelfareGoodsSearchGoodsAllRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("SearchCenterAutoCaseRun")
	@allure.severity("normal")
	def test_WelfareGoodsSuggester_testConn(self):
		"""
		福利严选联想词搜索
		"""
		WelfareGoodsSuggester=searchCenter.WelfareGoodsSuggester()
		WelfareGoodsSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
		WelfareGoodsSuggester.changeEnv("turboradio.cn")
		WelfareGoodsSuggester.data = {"searchContent":"洗衣液","channels":[7,8]}
		WelfareGoodsSuggesterRes = WelfareGoodsSuggester.excute()
		assert WelfareGoodsSuggesterRes.text.__contains__("\"errno\":0")
