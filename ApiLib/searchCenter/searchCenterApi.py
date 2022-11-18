# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class WordSuggesterSuggester(httpHandler):
	def __init__(self):
		super(WordSuggesterSuggester, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/wordSuggester/suggester"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"感冒"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询商品")
		return self.response


class GoodsSearchSearchGoodsAll(httpHandler):
	def __init__(self):
		super(GoodsSearchSearchGoodsAll, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/searchGoodsAll"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"provinceCodes":["123","234"],"cityCode":["1234","2345"]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	商品搜索引擎查询-全国搜索")
		return self.response


class GoodsSearchSearchGoodsByTradeCode(httpHandler):
	def __init__(self):
		super(GoodsSearchSearchGoodsByTradeCode, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/searchGoodsByTradeCode"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"tradeCode":"6902401920083","goodsNum":10,"latitude":12,"longitude":12}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	商品搜索引擎查询-根据条码基于地理位置搜索全国商品")
		return self.response


class GoodsSearchSearchGoodsGeo(httpHandler):
	def __init__(self):
		super(GoodsSearchSearchGoodsGeo, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/searchGoodsGeo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":12,"longitude":12,"distance":3,"isAccurate":1,"storeNum":10}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询商品价格和销量")
		return self.response


class OtoManageSearch(httpHandler):
	def __init__(self):
		super(OtoManageSearch, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/otoManage/search"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"merchantId":"95852","provinceCode":"430000","cityCode":"430100","areaCode":"430102","storeIds":["20000001","20000002"],"commonName":"感冒","approvalNumber":"1234","isPrescription":0,"isUniondrugOffShelf":1,"tradeCode":"90085","goodsInternalId":"90241","page":1,"limit":10}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	商品搜索引擎查询-oto运营管理查询")
		return self.response


class GoodsSearchCorrectSearchContent(httpHandler):
	def __init__(self):
		super(GoodsSearchCorrectSearchContent, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/correctSearchContent"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"生物疝补骗"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	商品搜索词修正")
		return self.response


class QueryGoodsQueryGoodsBaseInfo(httpHandler):
	def __init__(self):
		super(QueryGoodsQueryGoodsBaseInfo, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/queryGoods/queryGoodsBaseInfo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"sourceType":"1","queryGoodsBaseInfoDtoList":[{"merchantId":"649","storeId":"56920","goodsInternalId":"600839"},{"merchantId":"649","storeId":"56920","goodsInternalId":"LS5533"}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询商品价格和销量")
		return self.response


class SkuQuery(httpHandler):
	def __init__(self):
		super(SkuQuery, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/sku/query"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"page":1,"size":2,"merchantId":649,"storeId":56920}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询药品信息列表")
		return self.response


class Sku(httpHandler):
	def __init__(self):
		super(Sku, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/sku/"
		self.headers = None
		self.params = {"None":"625-11953-2-211891"}
		self.data = None

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(0)
		self.logger.info(self.path +"\tdone" + "	根据skuId查询药品基本信息")
		return self.response


class SkuSimple(httpHandler):
	def __init__(self):
		super(SkuSimple, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/sku/simple"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"ids":["649-56920-2-LS4516","649-56920-2-921138"]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	根据skuId列表批量查询药品简单信息")
		return self.response


class GoodsSearchSearchUnify(httpHandler):
	def __init__(self):
		super(GoodsSearchSearchUnify, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/searchUnify"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"","categoryInfo":"Z X","wordOperator":1,"searchPrescription":0,"sortField":1,"sortType":2,"queryStoreList":[{"merchantId":"10000001","storeId":"20000001"},{"merchantId":"10000002","storeId":"20000002"}],"page":1,"limit":10,"isAccurate":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询商品")
		return self.response


class GoodsSearchSearch(httpHandler):
	def __init__(self):
		super(GoodsSearchSearch, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/search"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"","merchantId":"","storeId":"","categoryInfo":"Z X","sourceType":"2","wordOperator":1,"excludeGoodsId":"1234","searchPrescription":0,"sortField":1,"sortType":2,"page":1,"limit":10}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询商品")
		return self.response


class GoodsSearchSearchDtpGoods(httpHandler):
	def __init__(self):
		super(GoodsSearchSearchDtpGoods, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/searchDtpGoods"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"玉屏风颗粒 宫瘤宁胶囊","categoryInfo":"","wordOperator":0,"searchPrescription":1,"sortField":1,"sortType":2,"page":1,"limit":10,"latitude":None,"longitude":None,"distance":None,"isAccurate":1,"storeNum":10,"searchSource":"O2O"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	搜索DTP药品")
		return self.response


class GoodsSearchSearchGoodsByTradeCodes(httpHandler):
	def __init__(self):
		super(GoodsSearchSearchGoodsByTradeCodes, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/goodsSearch/searchGoodsByTradeCodes"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"tradeCodes":["6921575620230"],"goodsNum":10,"latitude":31.972033,"longitude":118.777545,"searchSource":"O2O","merchantId":"","storeId":"","business":"nice_drug","member":{"memberId":15967187,"sessionId":"dkahgaj;ld;afjaha","page":1}}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据多个条码基于地理位置搜索")
		return self.response


class WordSuggesterExist(httpHandler):
	def __init__(self):
		super(WordSuggesterExist, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/wordSuggester/exist"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent": "感冒","searchSource": "O2O","business": "nice_drug","member" : { "memberId" : 15967187, "sessionId" : "ghfjkhhjfhft","page" : 1}}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	判断联想词是否存在")
		return self.response


class WelfareGoodsSearchGoodsAll(httpHandler):
	def __init__(self):
		super(WelfareGoodsSearchGoodsAll, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/welfareGoods/searchGoodsAll"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"","sortField":1,"sortType":2,"page":1,"limit":10,"channels":[7,8]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	福利严选搜索查询")
		return self.response


class WelfareGoodsSuggester(httpHandler):
	def __init__(self):
		super(WelfareGoodsSuggester, self).__init__()
		self.host = "http://data.search.turboradio.cn"
		self.path = "/welfareGoods/suggester"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"searchContent":"洗衣液","channels":[7,8]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	福利严选联想词搜索")
		return self.response