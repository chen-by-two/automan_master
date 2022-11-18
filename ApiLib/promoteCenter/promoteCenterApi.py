# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class PromoteSchemeAdd(httpHandler):
	def __init__(self):
		super(PromoteSchemeAdd, self).__init__()
		self.host = "http://gw.turboradio.cn"
		self.path = "/mng-promote/promote/scheme/add"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer b71b1be5-ff1f-4c33-9853-354290682eef"}
		self.params = None
		self.data = {"memberId":"228","mobile":"15250989839","name":"徐芬","schemeInfo":{"partnerLimit":1,"schemeName":"lucky测试专用","gmtEffectedStart":"2020-12-07 00:00:00","gmtEffectedEnd":"2022-12-06 23:59:59","cardName":"lucky测试专用","cardDescription":"lucky测试专用","schemePrompt":"lucky测试专用","startDay":-1,"duration":-1,"tagId":36,"status":None,"statusText":"","schemeId":"","projectName":"","tagName":"","goodsLimit":None},"payRule":{"payType":2,"fullAmount":0,"deductAmount":0,"discount":10,"convertType":1,"convertAmount":0,"maxAmount":9999,"serviceId":"20106","pushBackRate":"-1","pushBackRateStatus":2,"convertTypeText":"","serviceName":"","cardLimit":9999,"isOpen":None},"giftRule":{"status":1,"transactionType":1,"mergeStatus":0,"fullAmount":0,"payChannelType":11,"giftType":None,"giftProductType":1,"giftAmount":0,"giftDiscount":0,"stackNo":0,"giftQuantity":1,"giftProductId":None,"giftGroupId":None,"giftTypeText":None,"giftGroupName":None,"giftProjectName":None},"partnerInfo":[{"partnerId":"578","partnerName":"产品测试(商户简称)","selected":""}],"bankInfo":[],"blackChannelTypeList":[]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	营销中心创建营销方案")
		return self.response


class PromoteSendcard(httpHandler):
	def __init__(self):
		super(PromoteSendcard, self).__init__()
		self.host = "http://admincustomercenter."
		self.path = "backend.turboradio.cn/promote/sendcard"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer b71b1be5-ff1f-4c33-9853-354290682eef"}
		self.params = None
		self.data = {"memberId":"228","schemeId":"20210303201224470067","cardNum":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	客服中心发营销卡")
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


class CardSendCard(httpHandler):
	def __init__(self):
		super(CardSendCard, self).__init__()
		self.host = "http://java.promotecenter.service.turboradio.cnhttp://java.promotecenter.service.turboradio.cn"
		self.path = "/card/sendCard"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "memberId": 228,
    "schemeId": "20220428110246988156",
    "merchantId": 578,
    "merchantName": "louie.cruickshank",
    "source": "12it81",
    "requestNo": "xv123eysz"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据方案创建卡")
		return self.response


class TrialQueryActivity(httpHandler):
	def __init__(self):
		super(TrialQueryActivity, self).__init__()
		self.host = "http://java.promotecenter.service.turboradio.cn/trial"
		self.path = "/trial/queryActivity"
		self.headers = {"Content-Type":"application/json;charset=UTF-8","Authorization":"Bearer 3b7d40e6-8879-4b54-8cb0-c23b5a3a2f5c"}
		self.params = None
		self.data = {
    "memberId": 228,
    "channelType": "1",
    "merchantId": 578,
    "storeId": 4123,
    "goodsList": [
        {
            "itemUuid": "31329d19-e604-475f-b052-28215369d7ba",
            "goodsAmount": 27,
            "goodsNumber": 807,
            "skuNo": "uww67h",
            "goodsBarCode": "93903",
            "goodsType": "vf6a9k",
            "activityList": [
                {
                    "activityId": "72",
                    "activityName": "louie.cruickshank",
                    "numberLimit": 10,
                    "deductGoodsNumber": 523,
                    "isAvailable": 507,
                    "requestNo": "uonczh",
                    "activityType": "g43nb7",
                    "merchantActivityAmount": 711,
                    "itemUuid": "31329d19-e604-475f-b052-28215369d7ba"
                }
            ],
            "internalCode": "93903",
            "goodsName": "louie.cruickshank",
            "buyGifts": "pnl5rv"
        }
    ],
    "requestNo": "0utfzy"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询营销所有商家活动入口")
		return self.response


class CcardQueryCardDetail(httpHandler):
	def __init__(self):
		super(CcardQueryCardDetail, self).__init__()
		self.host = "http://java.promotecenter.service.turboradio.cn"
		self.path = "/card/queryCardDetail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "cardId": "24e05c0c97dc4d3ea0e3",
    "partnerId": 578
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据卡片ID查询卡片详情入口")
		return self.response


class CardQueryCardAmount(httpHandler):
	def __init__(self):
		super(CardQueryCardAmount, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/card/queryCardAmount"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
    "memberId": 228,
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
		self.logger.info(self.path +"	done" + "	查询用户卡片总额")
		return self.response


class OutSchemeDetailInfo(httpHandler):
	def __init__(self):
		super(OutSchemeDetailInfo, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/outScheme/detailInfo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"schemeId":"20201217135933272905"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询方案详情 包含连锁")
		return self.response



	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	批量查询卡详情")
		return self.response


class CardBatchQuery(httpHandler):
	def __init__(self):
		super(CardBatchQuery, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/card/batchQuery"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"cardList":[{"memberId":228,"cardId":"8a2b1009515847d1a0fc","cardType":"1","status":1,"cardLimit":1000,"cardBalance":975.88,"changedAmount":5,"couponId":"8a2b1009515847d1a0fc"}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	批量查询卡详情")
		return self.response


class OutSchemeDetailList(httpHandler):
	def __init__(self):
		super(OutSchemeDetailList, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/outScheme/detailList"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"schemeIdList":["20201217135933272905","20201125163905818722","20201105140303126980"]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询方案列表详情")
		return self.response


class CardQueryProjectInfo(httpHandler):
	def __init__(self):
		super(CardQueryProjectInfo, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/card/queryProjectInfo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"couponId":"164923085729500016"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	风控中心通过券id查询项目")
		return self.response


class CouponQuerySchemeInfo(httpHandler):
	def __init__(self):
		super(CouponQuerySchemeInfo, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/coupon/querySchemeInfo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"couponList":["164691929914300011","164691842655700016"]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	客服系统通过券列表调用营销中心查询方案提示")
		return self.response


class InfoCheckGoods(httpHandler):
	def __init__(self):
		super(InfoCheckGoods, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/info/checkGoods"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"goodsBarCode":"6953395504766","cardId":"5db5cba76b274aeeb54d","memberId":228}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	检查商品是否可以在此优惠权益内可用")
		return self.response


class OutSchemeQuerySchemeAndTag(httpHandler):
	def __init__(self):
		super(OutSchemeQuerySchemeAndTag, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/outScheme/querySchemeAndTag"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"couponIds":["164691929914300011","164691842655700016"]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	券ID批量查询方案ID和标签ID")
		return self.response


class CardQueryGiftDetail(httpHandler):
	def __init__(self):
		super(CardQueryGiftDetail, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/card/queryGiftDetail"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"orderNo":"92031011603301080188"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过主订单号查询赠送权益入口")
		return self.response


class LockLockCard(httpHandler):
	def __init__(self):
		super(LockLockCard, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/lock/lockCard"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"orderNo":"92031001603301020134","lockList":[{"couponId":"164691929914300011","memberId":228}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	锁定卡入口")
		return self.response


class OutSchemeSchemeInfo(httpHandler):
	def __init__(self):
		super(OutSchemeSchemeInfo, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/outScheme/schemeInfo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"schemeId":"20201217135933272905"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询方案详情 ，返回可用连锁信息")
		return self.response


class OutSchemeSchemeAndRule(httpHandler):
	def __init__(self):
		super(OutSchemeSchemeAndRule, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/outScheme/schemeAndRule"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"schemeId":"20201217135933272905"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询方案详情和规则详情")
		return self.response


class TrialActivityTrial(httpHandler):
	def __init__(self):
		super(TrialActivityTrial, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/trial/activityTrial"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"merchantId":578,"goodsList":[{"goodsAmount":200,"isMember":0,"drugType":0,"goodsBarCode":"6900966688219","goodsType":"1","merchantActivity":{"activityId":"20220620182024938696","activityName":"lucky单品促销","activityType":"3","requestNo":"cf3764e85f96482"},"goodsNumber":2,"buyGifts":"0","internalCode":"1000773","itemUuid":"c44c87e10c8dc4f3f91d306799191184"}],"channelType":"1","requestNo":"62b04b16d3f1a","memberId":228}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	超级会员日和单品促销活动试算入口")
		return self.response


class CardBatchMerchantQuery(httpHandler):
	def __init__(self):
		super(CardBatchMerchantQuery, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/card/batchMerchantQuery"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":228,"merchantId":578,"schemeId":20201217135933272905,"cardType":1," tagList":[64,243,81,297]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	根据连锁id和memberid查询用户下的可用卡")
		return self.response


class DeductCouponDeductPayBackNotice(httpHandler):
	def __init__(self):
		super(DeductCouponDeductPayBackNotice, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/deductCoupon/deductPayBackNotice"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"requestNo":2022062101401998931,"payNoticeList":[{"memberId":16233352,"bankCode":"","orderAmount":0,"equityAmount":34,"couponId":165579377299000010,"orderNo":92062101603586801331,"mobile":17321214316}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	抵扣券核销入口")
		return self.response


class DeductCouponVerification(httpHandler):
	def __init__(self):
		super(DeductCouponVerification, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/deductCoupon/verification"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"activityList":[{"activityAmount":115.00,"activityId":"20220401163034122281","activityType":"3","requestNo":"f99a9d02e3ba484","merchantIdList":[555]}],"isErp":"0"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	批量验证抵扣券入口")
		return self.response


class OutRateQueryRate(httpHandler):
	def __init__(self):
		super(OutRateQueryRate, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/outRate/queryRate"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"allCashFlag":1,"channelType":1,"goodsInfos":[{"activityType":0,"giftGoodsFlag":False,"goodsBarCode":"6920040530227","goodsType":1,"internalCode":"21522","itemId":9916315,"skuNo":"139092-21522"}],"memberId":"1247070","merchantId":"139092","orderBizType":-1,"orderMethod":14,"orderNo":"92062811603633470164","orderTime":1656386655000}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	订单商品扣率查询")
		return self.response


class DeductCouponCouponTrialForOrder(httpHandler):
	def __init__(self):
		super(DeductCouponCouponTrialForOrder, self).__init__()
		self.host = "http://java.promotecenter.service.uniondrug.net"
		self.path = "/deductCoupon/couponTrialForOrder"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":228,"channelType":1,"partnerId":139092,"requestNo":"5375ef9c6a6e8429d4e01371da0a519d","goodsList":[{"itemUuid":"024b6a9f-1117-463f-9c54-170a866bf87a","goodsAmount":0.26,"goodsNumber":1,"skuNo":"139092-66404","goodsBarCode":6953395504766,"goodsType":1,"isActivity":0}],"storeId":139094}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	优惠券批量试算")
		return self.response