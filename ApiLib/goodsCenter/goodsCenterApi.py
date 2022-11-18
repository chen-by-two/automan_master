# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class SpuQuery(httpHandler):
	def __init__(self):
		super(SpuQuery, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/spu/query"
		self.headers = {"Content-Type":"application/json","Authorization":"Bearer ed9e5fd5-dd4a-4dba-80d0-3f861523a561"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":10}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	描述")
		return self.response


class UnifyproductDetails(httpHandler):
	def __init__(self):
		super(UnifyproductDetails, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "/unifyproduct/details"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"skuNo":"53219-5062011","channel":"8","channelId":0}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	统一交易商品详情拉取")
		return self.response


class UnifyproductBuyLimit(httpHandler):
	def __init__(self):
		super(UnifyproductBuyLimit, self).__init__()
		self.host = "https://wx.turboradio.cn"
		self.path = "unifyproduct/buyLimit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
		self.params = None
		self.data = {"memberId":15961742,"skuNo":"53219-5062011"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(0)
		self.logger.info(self.path +"\tdone" + "	统一交易商品风控")
		return self.response


class insertStandardGoods(httpHandler):
	def __init__(self):
		super(insertStandardGoods, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/standardGoods/insertStandardGoods"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"spuId":591527,"operator":"张丽军","goodsName":"张三autotest","tradeCode":"6912312312","specification":"1","retailPrice":"12","grossWeight":1,"originPlace":1,"brand":1,"weight":1,"volume":1,"id":"330772"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	编辑标准商品信息")
		return self.response


class StandardGoodsFindByPage(httpHandler):
	def __init__(self):
		super(StandardGoodsFindByPage, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/standardGoods/findByPage"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":10,"goodsName":"张三autotest"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询标准商品列表")
		return self.response


class updateManualYaozs(httpHandler):
	def __init__(self):
		super(updateManualYaozs, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/standardGoods/updateManualYaozs"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"standardGoodsManualYaozs":{"commonName":"张三autotest","enName":"zhangsanautotest","pinyinName":"zhangsanautotest","drugName":"张三autotest","approvalNumber":"5396120191101185034309630","specification":"必填","cureDisease":"必填","dosage":"必填"},"standardGoodsDosage":{},"id":"330772","operator":"张丽军"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	修改商品说明书")
		return self.response


class QueryManualYaozs(httpHandler):
	def __init__(self):
		super(QueryManualYaozs, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/standardGoods/queryManualYaozs?id=330772"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"standardGoodsManualYaozs":{"commonName":"张三autotest","enName":"zhangsanautotest","pinyinName":"zhangsanautotest","drugName":"张三autotest","approvalNumber":"5396120191101185034309630","specification":"必填","cureDisease":"必填","dosage":"必填"},"standardGoodsDosage":{},"id":"330772","operator":"张丽军"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	修改商品说明书")
		return self.response


class queryGcStandardGoods(httpHandler):
	def __init__(self):
		super(queryGcStandardGoods, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/standardGoods/queryGcStandardGoods"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"id":"330772"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询标准商品基本信息")
		return self.response


class GoodsSpuDetailsSave(httpHandler):
	def __init__(self):
		super(GoodsSpuDetailsSave, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/goodsSpuDetails/save"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"detailsCode":"a6cc046dc64c44a7875695e538cdbb0e","deleted":"0","title":"张三图文05104"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	编辑商品图文")
		return self.response


class GoodsSpuDetailsQuery(httpHandler):
	def __init__(self):
		super(GoodsSpuDetailsQuery, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/goodsSpuDetails/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"title":"张三图文05104","pageNum":"1","pageSize":"10"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询商品图文")
		return self.response


class querySku(httpHandler):
	def __init__(self):
		super(querySku, self).__init__()
		self.host = "http://java.goodscenter.mng.turboradio.cn"
		self.path = "/goods/querySku"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 36bf61a5-8600-4d37-b5c2-b330f12fc820"}
		self.params = None
		self.data = {"skuNo":"578-806894823071023104"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询SKU商品")
		return self.response


class CardQueryMyRecord(httpHandler):
	def __init__(self):
		super(CardQueryMyRecord, self).__init__()
		self.host = "http://java.promotecenter.service.turboradio.cn"
		self.path = "/card/queryMyRecord"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 3b7d40e6-8879-4b54-8cb0-c23b5a3a2f5c"}
		self.params = None
		self.data = {
    "memberId": 228,
    "cardType": "1",
    "status": 1,
    "tagList": [
        "49",
        "35",
        "169",
        "116",
        "165"
    ]
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询我的卡列表")
		return self.response