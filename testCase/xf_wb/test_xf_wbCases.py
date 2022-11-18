# -*- coding: utf-8 -*-
import pytest,os,allure
import ApiLib.promoteCenter.promoteCenterApi as promoteCenter


class Test_xf_wb:

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CardQueryMyRecord_test1(self):
		"""
		查询我的卡列表
		"""
		CardQueryMyRecord=promoteCenter.CardQueryMyRecord()
		CardQueryMyRecord.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardQueryMyRecord.changeEnv("uniondrug.net")
		CardQueryMyRecord.data = {"memberId":228,"cardType":"1","status":1,"tagList":["49","35","169","116","165"]}
		CardQueryMyRecordRes = CardQueryMyRecord.excute()
		assert CardQueryMyRecordRes.text.__contains__("21595263016d47a782d8")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CcardQueryCardDetail_test2(self):
		"""
		根据卡片ID查询卡片详情入口
		"""
		CcardQueryCardDetail=promoteCenter.CcardQueryCardDetail()
		CcardQueryCardDetail.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CcardQueryCardDetail.changeEnv("uniondrug.net")
		CcardQueryCardDetail.data = {"cardId":"8a2b1009515847d1a0fc","partnerId":578}
		CcardQueryCardDetailRes = CcardQueryCardDetail.excute()
		assert CcardQueryCardDetailRes.text.__contains__("20220310211421443194")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CardQueryCardAmount_test3(self):
		"""
		查询用户卡片总额
		"""
		CardQueryCardAmount=promoteCenter.CardQueryCardAmount()
		CardQueryCardAmount.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardQueryCardAmount.changeEnv("uniondrug.net")
		CardQueryCardAmount.data = {"memberId":228,"tagList":["49","165"]}
		CardQueryCardAmountRes = CardQueryCardAmount.excute()
		assert CardQueryCardAmountRes.text.__contains__("OBJECT")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_OutSchemeDetailInfo_test4(self):
		"""
		查询方案详情 包含连锁
		"""
		OutSchemeDetailInfo=promoteCenter.OutSchemeDetailInfo()
		OutSchemeDetailInfo.headers = {"Content-Type":"application/json;charset=UTF-8"}
		OutSchemeDetailInfo.changeEnv("uniondrug.net")
		OutSchemeDetailInfo.data = {"schemeId":"20201217135933272905"}
		OutSchemeDetailInfoRes = OutSchemeDetailInfo.excute()
		assert OutSchemeDetailInfoRes.text.__contains__("20201217135933272905")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CardBatchQuery_test5(self):
		"""
		批量查询卡详情
		"""
		CardBatchQuery=promoteCenter.CardBatchQuery()
		CardBatchQuery.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardBatchQuery.changeEnv("uniondrug.net")
		CardBatchQuery.data = {"cardList":[{"memberId":228,"cardId":"8a2b1009515847d1a0fc","cardType":"1","status":1,"cardLimit":1000,"cardBalance":975.88,"changedAmount":5,"couponId":"8a2b1009515847d1a0fc"}]}
		CardBatchQueryRes = CardBatchQuery.excute()
		assert CardBatchQueryRes.text.__contains__("8a2b1009515847d1a0fc")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_OutSchemeDetailList_test6(self):
		"""
		查询方案列表详情
		"""
		OutSchemeDetailList=promoteCenter.OutSchemeDetailList()
		OutSchemeDetailList.headers = {"Content-Type":"application/json;charset=UTF-8"}
		OutSchemeDetailList.changeEnv("uniondrug.net")
		OutSchemeDetailList.data = {"schemeIdList":["20201217135933272905","20201125163905818722","20201105140303126980"]}
		OutSchemeDetailListRes = OutSchemeDetailList.excute()
		assert OutSchemeDetailListRes.text.__contains__("20201217135933272905")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CardQueryProjectInfo_test7(self):
		"""
		风控中心通过券id查询项目
		"""
		CardQueryProjectInfo=promoteCenter.CardQueryProjectInfo()
		CardQueryProjectInfo.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardQueryProjectInfo.changeEnv("uniondrug.net")
		CardQueryProjectInfo.data = {"couponId":"164923085729500016"}
		CardQueryProjectInfoRes = CardQueryProjectInfo.excute()
		assert CardQueryProjectInfoRes.text.__contains__("20220406135705548628")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CouponQuerySchemeInfo_test8(self):
		"""
		客服系统通过券列表调用营销中心查询方案提示
		"""
		CouponQuerySchemeInfo=promoteCenter.CouponQuerySchemeInfo()
		CouponQuerySchemeInfo.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CouponQuerySchemeInfo.changeEnv("uniondrug.net")
		CouponQuerySchemeInfo.data = {"couponList":["164691929914300011","164691842655700016"]}
		CouponQuerySchemeInfoRes = CouponQuerySchemeInfo.excute()
		assert CouponQuerySchemeInfoRes.text.__contains__("164691842655700016")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_InfoCheckGoods_test9(self):
		"""
		检查商品是否可以在此优惠权益内可用
		"""
		InfoCheckGoods=promoteCenter.InfoCheckGoods()
		InfoCheckGoods.headers = {"Content-Type":"application/json;charset=UTF-8"}
		InfoCheckGoods.changeEnv("uniondrug.net")
		InfoCheckGoods.data = {"goodsBarCode":"6953395504766","cardId":"5db5cba76b274aeeb54d","memberId":228}
		InfoCheckGoodsRes = InfoCheckGoods.excute()
		assert InfoCheckGoodsRes.text.__contains__("2")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_OutSchemeQuerySchemeAndTag_test10(self):
		"""
		券ID批量查询方案ID和标签ID
		"""
		OutSchemeQuerySchemeAndTag=promoteCenter.OutSchemeQuerySchemeAndTag()
		OutSchemeQuerySchemeAndTag.headers = {"Content-Type":"application/json;charset=UTF-8"}
		OutSchemeQuerySchemeAndTag.changeEnv("uniondrug.net")
		OutSchemeQuerySchemeAndTag.data = {"couponIds":["164691929914300011","164691842655700016"]}
		OutSchemeQuerySchemeAndTagRes = OutSchemeQuerySchemeAndTag.excute()
		assert OutSchemeQuerySchemeAndTagRes.text.__contains__("20220310211421443194")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CardQueryGiftDetail_test11(self):
		"""
		通过主订单号查询赠送权益入口
		"""
		CardQueryGiftDetail=promoteCenter.CardQueryGiftDetail()
		CardQueryGiftDetail.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardQueryGiftDetail.changeEnv("uniondrug.net")
		CardQueryGiftDetail.data = {"orderNo":"92031011603301080188"}
		CardQueryGiftDetailRes = CardQueryGiftDetail.excute()
		assert CardQueryGiftDetailRes.text.__contains__("此订单无赠送项目 ")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_LockLockCard_test12(self):
		"""
		锁定卡入口
		"""
		LockLockCard=promoteCenter.LockLockCard()
		LockLockCard.headers = {"Content-Type":"application/json;charset=UTF-8"}
		LockLockCard.changeEnv("uniondrug.net")
		LockLockCard.data = {"orderNo":"92031001603301020134","lockList":[{"couponId":"164691929914300011","memberId":228}]}
		LockLockCardRes = LockLockCard.excute()
		assert LockLockCardRes.text.__contains__("卡状态异常，不支持此次抵扣")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_OutSchemeSchemeInfo_test13(self):
		"""
		查询方案详情 ，返回可用连锁信息
		"""
		OutSchemeSchemeInfo=promoteCenter.OutSchemeSchemeInfo()
		OutSchemeSchemeInfo.headers = {"Content-Type":"application/json;charset=UTF-8"}
		OutSchemeSchemeInfo.changeEnv("uniondrug.net")
		OutSchemeSchemeInfo.data = {"schemeId":"20201217135933272905"}
		OutSchemeSchemeInfoRes = OutSchemeSchemeInfo.excute()
		assert OutSchemeSchemeInfoRes.text.__contains__("20201217135933272905")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_OutSchemeSchemeAndRule_test14(self):
		"""
		查询方案详情和规则详情
		"""
		OutSchemeSchemeAndRule=promoteCenter.OutSchemeSchemeAndRule()
		OutSchemeSchemeAndRule.headers = {"Content-Type":"application/json;charset=UTF-8"}
		OutSchemeSchemeAndRule.changeEnv("uniondrug.net")
		OutSchemeSchemeAndRule.data = {"schemeId":"20201217135933272905"}
		OutSchemeSchemeAndRuleRes = OutSchemeSchemeAndRule.excute()
		assert OutSchemeSchemeAndRuleRes.text.__contains__("lucky通用权益")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_TrialQueryActivity_test16(self):
		"""
		查询营销所有商家活动入口
		"""
		TrialQueryActivity=promoteCenter.TrialQueryActivity()
		TrialQueryActivity.headers = {"Content-Type":"application/json;charset=UTF-8"}
		TrialQueryActivity.changeEnv("uniondrug.net")
		TrialQueryActivity.data = {"orderSource":1,"merchantId":578,"goodsList":[{"goodsAmount":153.75,"goodsNumber":1,"goodsName":"小儿感冒退热糖浆","internalCode":"1001242","itemUuid":"1001242","goodsBarCode":"6933890700533","goodsType":"1"},{"goodsAmount":1679.53,"goodsNumber":1,"goodsName":"风热感冒颗粒","internalCode":"1008120","itemUuid":"1008120","goodsBarCode":"690323423434","goodsType":"1"},{"goodsAmount":48.01,"goodsNumber":1,"goodsName":"复方感冒灵片","internalCode":"1000340","itemUuid":"1000340","goodsBarCode":"6927771401932","goodsType":"1"},{"goodsAmount":200,"goodsNumber":1,"goodsName":"复方感冒灵颗粒","internalCode":"1000773","itemUuid":"1000773","goodsBarCode":"6900966688219","goodsType":"1"},{"goodsAmount":153.75,"goodsNumber":1,"goodsName":"复方感冒灵片","internalCode":"1001242","itemUuid":"1001242","goodsBarCode":"6933890700559","goodsType":"1"},{"goodsAmount":2000,"goodsNumber":1,"goodsName":"感冒灵胶囊","internalCode":"1001973","itemUuid":"1001973","goodsBarCode":"6901339924569","goodsType":"1"},{"goodsAmount":1567.9,"goodsNumber":1,"goodsName":"小儿感冒颗粒","internalCode":"1002549","itemUuid":"1002549","goodsBarCode":"6928476702027","goodsType":"1"},{"goodsAmount":1706.81,"goodsNumber":1,"goodsName":"感冒清热颗粒","internalCode":"1005951","itemUuid":"1005951","goodsBarCode":"6926247830900","goodsType":"1"},{"goodsAmount":27.66,"goodsNumber":1,"goodsName":"风寒感冒颗粒","internalCode":"1007333","itemUuid":"1007333","goodsBarCode":"6936795700518","goodsType":"1"},{"goodsAmount":1559.38,"goodsNumber":1,"goodsName":"风热感冒颗粒","internalCode":"1008121","itemUuid":"1008121","goodsBarCode":"6901070385490","goodsType":"1"},{"goodsAmount":485.73,"goodsNumber":1,"goodsName":"四季感冒片","internalCode":"1008202","itemUuid":"1008202","goodsBarCode":"6926686603530","goodsType":"1"}],"channelType":"1","requestNo":"62b04aa982f28","memberId":228}
		TrialQueryActivityRes = TrialQueryActivity.excute()
		assert TrialQueryActivityRes.text.__contains__("1")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_TrialActivityTrial_test17(self):
		"""
		超级会员日和单品促销活动试算入口
		"""
		TrialActivityTrial=promoteCenter.TrialActivityTrial()
		TrialActivityTrial.headers = {"Content-Type":"application/json;charset=UTF-8"}
		TrialActivityTrial.changeEnv("uniondrug.net")
		TrialActivityTrial.data = {"merchantId":578,"goodsList":[{"goodsAmount":200,"isMember":0,"drugType":0,"goodsBarCode":"6900966688219","goodsType":"1","merchantActivity":{"activityId":"20220620182024938696","activityName":"lucky单品促销","activityType":"3","requestNo":"cf3764e85f96482"},"goodsNumber":2,"buyGifts":"0","internalCode":"1000773","itemUuid":"c44c87e10c8dc4f3f91d306799191184"}],"channelType":"1","requestNo":"62b04b16d3f1a","memberId":228}
		TrialActivityTrialRes = TrialActivityTrial.excute()
		assert TrialActivityTrialRes.text.__contains__("20220620182024938696")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_CardBatchMerchantQuery_test18(self):
		"""
		根据连锁id和memberid查询用户下的可用卡
		"""
		CardBatchMerchantQuery=promoteCenter.CardBatchMerchantQuery()
		CardBatchMerchantQuery.headers = {"Content-Type":"application/json;charset=UTF-8"}
		CardBatchMerchantQuery.changeEnv("uniondrug.net")
		CardBatchMerchantQuery.data = {"memberId":228,"merchantId":578,"schemeId":20201217135933272905,"cardType":1," tagList":[64,243,81,297]}
		CardBatchMerchantQueryRes = CardBatchMerchantQuery.excute()
		assert CardBatchMerchantQueryRes.text.__contains__("20201217135933272905")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_DeductCouponDeductPayBackNotice_test19(self):
		"""
		抵扣券核销入口
		"""
		DeductCouponDeductPayBackNotice=promoteCenter.DeductCouponDeductPayBackNotice()
		DeductCouponDeductPayBackNotice.headers = {"Content-Type":"application/json;charset=UTF-8"}
		DeductCouponDeductPayBackNotice.changeEnv("uniondrug.net")
		DeductCouponDeductPayBackNotice.data = {"requestNo":2022062101401998931,"payNoticeList":[{"memberId":16233352,"bankCode":"","orderAmount":0,"equityAmount":34,"couponId":165579377299000010,"cardId":None,"cardType":None,"status":None,"orderNo":92062101603586801331,"mobile":17321214316," cardLimit":None,"cardBalance":None,"changedAmount":None}]}
		DeductCouponDeductPayBackNoticeRes = DeductCouponDeductPayBackNotice.excute()
		assert DeductCouponDeductPayBackNoticeRes.text.__contains__("卡状态异常，不支持此次抵扣")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_DeductCouponVerification_test20(self):
		"""
		批量验证抵扣券入口
		"""
		DeductCouponVerification=promoteCenter.DeductCouponVerification()
		DeductCouponVerification.headers = {"Content-Type":"application/json;charset=UTF-8"}
		DeductCouponVerification.changeEnv("uniondrug.net")
		DeductCouponVerification.data = {"activityList":[{"activityAmount":115.00,"activityId":"20220401163034122281","activityType":"3","requestNo":"f99a9d02e3ba484","merchantIdList":[555]}],"isErp":"0"}
		DeductCouponVerificationRes = DeductCouponVerification.excute()
		assert DeductCouponVerificationRes.text.__contains__("20220401163034122281")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_OutRateQueryRate_test21(self):
		"""
		订单商品扣率查询
		"""
		OutRateQueryRate=promoteCenter.OutRateQueryRate()
		OutRateQueryRate.headers = {"Content-Type":"application/json;charset=UTF-8"}
		OutRateQueryRate.changeEnv("uniondrug.net")
		OutRateQueryRate.data = {"allCashFlag":1,"channelType":1,"goodsInfos":[{"activityType":0,"giftGoodsFlag":False,"goodsBarCode":"6920040530227","goodsType":1,"internalCode":"21522","itemId":9916315,"skuNo":"139092-21522"}],"memberId":"1247070","merchantId":"139092","orderBizType":-1,"orderMethod":14,"orderNo":"92062811603633470164","orderTime":1656386655000}
		OutRateQueryRateRes = OutRateQueryRate.excute()
		assert OutRateQueryRateRes.text.__contains__("139092")

	@allure.feature("xf_wb")
	@allure.severity("blocker")
	def test_DeductCouponCouponTrialForOrder_test22(self):
		"""
		优惠券批量试算
		"""
		DeductCouponCouponTrialForOrder=promoteCenter.DeductCouponCouponTrialForOrder()
		DeductCouponCouponTrialForOrder.headers = {"Content-Type":"application/json;charset=UTF-8"}
		DeductCouponCouponTrialForOrder.changeEnv("uniondrug.net")
		DeductCouponCouponTrialForOrder.data = {"memberId":228,"channelType":1,"partnerId":139092,"requestNo":"5375ef9c6a6e8429d4e01371da0a519d","goodsList":[{"itemUuid":"024b6a9f-1117-463f-9c54-170a866bf87a","goodsAmount":0.26,"goodsNumber":1,"skuNo":"139092-66404","goodsBarCode":6953395504766,"goodsType":1,"isActivity":0}],"storeId":139094}
		DeductCouponCouponTrialForOrderRes = DeductCouponCouponTrialForOrder.excute()
		assert DeductCouponCouponTrialForOrderRes.text.__contains__("d2e70d55a94e41a5a373")
