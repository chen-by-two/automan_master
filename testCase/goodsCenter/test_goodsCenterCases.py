# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.goodsCenter.goodsCenterApi as goodsCenter


class Test_goodsCenter:

	@allure.feature("goodsCenter")
	@allure.severity("blocker")
	def test_StandardGoodsFindByPage_test5(self):
		"""
		查询标准商品
		"""
		StandardGoodsFindByPage=goodsCenter.StandardGoodsFindByPage()
		StandardGoodsFindByPage.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		StandardGoodsFindByPage.changeEnv("turboradio.cn")
		StandardGoodsFindByPage.data = {"pageNum":1,"pageSize":10,"goodsName":"张三autotest"}
		StandardGoodsFindByPageRes = StandardGoodsFindByPage.excute()
		assert StandardGoodsFindByPageRes.text.__contains__("成功")

	@allure.feature("goodsCenter")
	@allure.severity("blocker")
	def test_SpuQuery_test7(self):
		"""
		查询spu
		"""
		SpuQuery=goodsCenter.SpuQuery()
		SpuQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		SpuQuery.changeEnv("turboradio.cn")
		SpuQuery.data = {"pageNum":1,"pageSize":10}
		SpuQueryRes = SpuQuery.excute()
		assert SpuQueryRes.text.__contains__("")

	@allure.feature("goodsCenter")
	@allure.severity("blocker")
	def test_queryGcStandardGoods_test8(self):
		"""
		查询标准商品基本信息
		"""
		queryGcStandardGoods=goodsCenter.queryGcStandardGoods()
		queryGcStandardGoods.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		queryGcStandardGoods.changeEnv("turboradio.cn")
		queryGcStandardGoods.data = {"id":"330772"}
		queryGcStandardGoodsRes = queryGcStandardGoods.excute()
		assert queryGcStandardGoodsRes.text.__contains__("")

	@allure.feature("goodsCenter")
	@allure.severity("blocker")
	def test_GoodsSpuDetailsSave_test9(self):
		"""
		编辑商品图文
		"""
		GoodsSpuDetailsSave=goodsCenter.GoodsSpuDetailsSave()
		GoodsSpuDetailsSave.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GoodsSpuDetailsSave.changeEnv("turboradio.cn")
		GoodsSpuDetailsSave.data = {"detailsCode":"a6cc046dc64c44a7875695e538cdbb0e","deleted":"0","title":"张三图文05104"}
		GoodsSpuDetailsSaveRes = GoodsSpuDetailsSave.excute()
		assert GoodsSpuDetailsSaveRes.text.__contains__("")

	@allure.feature("goodsCenter")
	@allure.severity("blocker")
	def test_GoodsSpuDetailsQuery_test10(self):
		"""
		查询商品图文
		"""
		GoodsSpuDetailsQuery=goodsCenter.GoodsSpuDetailsQuery()
		GoodsSpuDetailsQuery.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		GoodsSpuDetailsQuery.changeEnv("turboradio.cn")
		GoodsSpuDetailsQuery.data = {"title":"张三图文05104","pageNum":"1","pageSize":"10"}
		GoodsSpuDetailsQueryRes = GoodsSpuDetailsQuery.excute()
		assert GoodsSpuDetailsQueryRes.text.__contains__("")
