# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 17:57
# @Author  : Haoran
import pytest, os, allure
import ApiLib.searchCenter.searchCenterApi as searchCenter


class Test_apiConn:


    @allure.feature("查询商品接口死活")
    @allure.severity("normal")
    def test_WordSuggesterSuggester_testConn(self):

        """
        连通性测试1
        """
        WordSuggesterSuggester = searchCenter.WordSuggesterSuggester()
        WordSuggesterSuggester.headers = {"Content-Type": "application/json;charset=UTF-8"}
        WordSuggesterSuggester.changeEnv("turboradio.cn")
        WordSuggesterSuggester.data = {"searchContent":"感冒"}
        WordSuggesterSuggesterRes = WordSuggesterSuggester.excute()
        assert WordSuggesterSuggesterRes.status_code == 200

    @allure.feature("商品搜索引擎查询-全国搜索接口死活")
    @allure.severity("normal")
    def test_GoodsSearchSearchGoodsAll_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchSearchGoodsAll = searchCenter.GoodsSearchSearchGoodsAll()
        GoodsSearchSearchGoodsAll.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchSearchGoodsAll.changeEnv("turboradio.cn")
        GoodsSearchSearchGoodsAll.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"provinceCodes":["123","234"],"cityCode":["1234","2345"]}
        GoodsSearchSearchGoodsAllRes = GoodsSearchSearchGoodsAll.excute()
        assert GoodsSearchSearchGoodsAllRes.status_code == 200

    @allure.feature("商品搜索引擎查询-根据条码基于地理位置搜索全国商品接口死活")
    @allure.severity("normal")
    def test_GoodsSearchSearchGoodsByTradeCode_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchSearchGoodsByTradeCode = searchCenter.GoodsSearchSearchGoodsByTradeCode()
        GoodsSearchSearchGoodsByTradeCode.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchSearchGoodsByTradeCode.changeEnv("turboradio.cn")
        GoodsSearchSearchGoodsByTradeCode.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}
        GoodsSearchSearchGoodsByTradeCodeRes = GoodsSearchSearchGoodsByTradeCode.excute()
        assert GoodsSearchSearchGoodsByTradeCodeRes.status_code == 200


    @allure.feature("查询商品价格和销量接口死活")
    @allure.severity("normal")
    def test_GoodsSearchSearchGoodsGeo_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchSearchGoodsGeo = searchCenter.GoodsSearchSearchGoodsGeo()
        GoodsSearchSearchGoodsGeo.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchSearchGoodsGeo.changeEnv("turboradio.cn")
        GoodsSearchSearchGoodsGeo.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}
        GoodsSearchSearchGoodsGeoRes = GoodsSearchSearchGoodsGeo.excute()
        assert GoodsSearchSearchGoodsGeoRes.status_code == 200

    @allure.feature("商品搜索引擎查询-oto运营管理查询接口死活")
    @allure.severity("normal")
    def test_OtoManageSearch_testConn(self):
        """
        连通性测试1
        """
        OtoManageSearch = searchCenter.OtoManageSearch()
        OtoManageSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
        OtoManageSearch.changeEnv("turboradio.cn")
        OtoManageSearch.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}
        OtoManageSearchRes = OtoManageSearch.excute()
        assert OtoManageSearchRes.status_code == 200

    @allure.feature("商品搜索词修正接口死活")
    @allure.severity("normal")
    def test_GoodsSearchCorrectSearchContent_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchCorrectSearchContent = searchCenter.GoodsSearchCorrectSearchContent()
        GoodsSearchCorrectSearchContent.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchCorrectSearchContent.changeEnv("turboradio.cn")
        GoodsSearchCorrectSearchContent.data = {"searchContent":"生物疝补骗"}
        GoodsSearchCorrectSearchContentRes = GoodsSearchCorrectSearchContent.excute()
        assert GoodsSearchCorrectSearchContentRes.status_code == 200

    @allure.feature("查询商品价格和销量接口死活")
    @allure.severity("normal")
    def test_QueryGoodsQueryGoodsBaseInfo_testConn(self):
        """
        连通性测试1
        """
        QueryGoodsQueryGoodsBaseInfo = searchCenter.QueryGoodsQueryGoodsBaseInfo()
        QueryGoodsQueryGoodsBaseInfo.headers = {"Content-Type": "application/json;charset=UTF-8"}
        QueryGoodsQueryGoodsBaseInfo.changeEnv("turboradio.cn")
        QueryGoodsQueryGoodsBaseInfo.data = {"sourceType":"1","queryGoodsBaseInfoDtoList":[{"merchantId":"649","storeId":"56920","goodsInternalId":"600839"},{"merchantId":"649","storeId":"56920","goodsInternalId":"LS5533"}]}
        QueryGoodsQueryGoodsBaseInfoRes = QueryGoodsQueryGoodsBaseInfo.excute()
        assert QueryGoodsQueryGoodsBaseInfoRes.status_code == 200

    @allure.feature("查询药品信息列表接口死活")
    @allure.severity("normal")
    def test_SkuQuery_testConn(self):
        """
        连通性测试1
        """
        SkuQuery = searchCenter.SkuQuery()
        SkuQuery.headers = {"Content-Type": "application/json;charset=UTF-8"}
        SkuQuery.changeEnv("turboradio.cn")
        SkuQuery.data = {"page":1,"size":2,"merchantId":649,"storeId":56920}
        SkuQueryRes = SkuQuery.excute()
        assert SkuQueryRes.status_code == 200

    @allure.feature("根据skuId查询药品基本信息接口死活")
    @allure.severity("normal")
    def test_Sku_testConn(self):
        """
        连通性测试1
        """
        Sku = searchCenter.Sku()
        Sku.headers = {"Content-Type": "application/json;charset=UTF-8"}
        Sku.changeEnv("turboradio.cn")
        Sku.params = {"None":"625-11953-2-211891"}
        SkuRes = Sku.excute()
        assert SkuRes.status_code == 200

    @allure.feature("根据skuId列表批量查询药品简单信息接口死活")
    @allure.severity("normal")
    def test_SkuSimple_testConn(self):
        """
        连通性测试1
        """
        SkuSimple = searchCenter.SkuSimple()
        SkuSimple.headers = {"Content-Type": "application/json;charset=UTF-8"}
        SkuSimple.changeEnv("turboradio.cn")
        SkuSimple.data = {"ids":["649-56920-2-LS4516","649-56920-2-921138"]}
        SkuSimpleRes = SkuSimple.excute()
        assert SkuSimpleRes.status_code == 200

    @allure.feature("查询商品接口死活")
    @allure.severity("normal")
    def test_GoodsSearchSearchUnify_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchSearchUnify = searchCenter.GoodsSearchSearchUnify()
        GoodsSearchSearchUnify.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchSearchUnify.changeEnv("turboradio.cn")
        GoodsSearchSearchUnify.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}
        GoodsSearchSearchUnifyRes = GoodsSearchSearchUnify.excute()
        assert GoodsSearchSearchUnifyRes.status_code == 200

    @allure.feature("查询商品接口死活")
    @allure.severity("normal")
    def test_GoodsSearchSearch_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchSearch = searchCenter.GoodsSearchSearch()
        GoodsSearchSearch.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchSearch.changeEnv("turboradio.cn")
        GoodsSearchSearch.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}
        GoodsSearchSearchRes = GoodsSearchSearch.excute()
        assert GoodsSearchSearchRes.status_code == 200

    @allure.feature("搜索DTP药品接口死活")
    @allure.severity("normal")
    def test_GoodsSearchSearchDtpGoods_testConn(self):
        """
        连通性测试1
        """
        GoodsSearchSearchDtpGoods = searchCenter.GoodsSearchSearchDtpGoods()
        GoodsSearchSearchDtpGoods.headers = {"Content-Type": "application/json;charset=UTF-8"}
        GoodsSearchSearchDtpGoods.changeEnv("turboradio.cn")
        GoodsSearchSearchDtpGoods.data = {"searchContent":"玉屏风颗粒 宫瘤宁胶囊","categoryInfo":"","wordOperator":0,"searchPrescription":1,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":None,"longitude":None,"distance":None,"isAccurate":1,"storeNum":10,"searchSource":"O2O"}
        GoodsSearchSearchDtpGoodsRes = GoodsSearchSearchDtpGoods.excute()
        assert GoodsSearchSearchDtpGoodsRes.status_code == 200