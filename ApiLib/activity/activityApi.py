# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class AdminTemplateSave(httpHandler):
	def __init__(self):
		super(AdminTemplateSave, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/admin/template/save"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {"id":"","type":"1","channel":"1","template_name":"测试新增模版0918","rules":"<p><span style=\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style=\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style=\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style=\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>","timeType":"1","times":"","release":"2","title":"药联健康给您发红包啦~","subtitle":"您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障","back_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png","button_icon":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png","play_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png","bottom_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png","share_img":"","share_icon":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png","explain":"","discount_img":"","pro_language":"药联健康给您发红包啦~","jump_url":"","OneRewardList":[{"reward_type":"2","scheme_type":"2","type":"2","udSchemeId":"xm202106301121282617","udSchemeName":"☆活动回归0630","amount":"14","rules":"活动回归0630","plan_type_id":"","rewardList":[]}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "新增/编辑模版")
		return self.response


class AdminTemplatePurchaseGoodsList(httpHandler):
	def __init__(self):
		super(AdminTemplatePurchaseGoodsList, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/admin/template/purchaseGoodsList"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "purchaseProjectId": "4967",
    "activityType": "1"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询福联社项目")
		return self.response


class DdLogin(httpHandler):
	def __init__(self):
		super(DdLogin, self).__init__()
		self.host = "http://uncenter.backend.turboradio.cn"
		self.path = "/dd/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1bmlvbmRydWcuYXV0aCIsImF1ZCI6InVuaW9uZHJ1Zy51bmNlbnRlciIsImlhdCI6MTYzMjQ2OTI5NSwibmJmIjoxNjMyNDY5Mjk1LCJleHAiOjE2MzI0NzY0OTUsInVzZXIiOnsibW9iaWxlIjoiMTUzODA5MDU0ODYifX0.gYtI8WvCpqBVX8VzKk__eZKVtE-l48l1_Gc5DItxjY4"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	钉钉登录运营中心后台")
		return self.response


class DdMobilelogin(httpHandler):
	def __init__(self):
		super(DdMobilelogin, self).__init__()
		self.host = "http://uncenter.backend.turboradio.cn"
		self.path = "/dd/mobilelogin"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {"mobile":"15380905486","code":"123456"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	手机号登录获取登录后台token")
		return self.response


class SmsReset(httpHandler):
	def __init__(self):
		super(SmsReset, self).__init__()
		self.host = "http://ai.backend.turboradio.cn"
		self.path = "/sms/reset"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "mobile": "15380905486"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取默认登录验证码123456")
		return self.response


class AdminTemplateDel(httpHandler):
	def __init__(self):
		super(AdminTemplateDel, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/admin/template/del"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {"id":"472"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	删除模版")
		return self.response


class ActivitySave(httpHandler):
	def __init__(self):
		super(ActivitySave, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/activity/save"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "id": "",
    "type": "1",
    "activity_name": "普通红包方案100902",
    "start_time": "2021-10-9 14:54:40",
    "end_time": "2021-11-30 14:54:40",
    "to_times": "",
    "merchants": [
        {
            "merchant_id": "760",
            "merchant_name": "国药控股国大药房（深圳）连锁有限公司",
            "referred": "深圳国大"
        }
    ],
    "activityScore": [
        {
            "max_point": "100.00",
            "min_point": "0.00",
            "template_id": "491",
            "template_name": "普通红包福联社2603"
        }
    ],
    "shop_times": "0",
    "customer_times": "0",
    "shop_type": "0",
    "customer_type": "0",
    "times_id": "",
    "shop_is_limit": "0",
    "customer_is_limit": "0",
    "template_id": "",
    "template_name": ""
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	新建方案")
		return self.response


class ActivitySwitch(httpHandler):
	def __init__(self):
		super(ActivitySwitch, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/activity/switch"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "id": "382",
    "is_disable": 1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	启用方案")
		return self.response


class Activity1RedOneSendRedeem(httpHandler):
	def __init__(self):
		super(Activity1RedOneSendRedeem, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/Activity1/RedOne/sendRedeem"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "wxMemberId": "15963890",
    "memberId": "1639",
    "openid": "of-FXw-T-M6uxrGUAQmHAjej_h1M",
    "mobile": "15380905486",
    "activityId": "51",
    "templateId": "491"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	领取普通红包")
		return self.response


class CommonMemberParse(httpHandler):
	def __init__(self):
		super(CommonMemberParse, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/common/member/parse"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "activityId": "377",
    "merchantId": "760",
    "memberFlag": "1"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取普通红包memberid")
		return self.response



class AdminChainActivityPage(httpHandler):
	def __init__(self):
		super(AdminChainActivityPage, self).__init__()
		self.host = "http://activity-news-backend.uniondrug.net"
		self.path = "/admin/ChainActivity/page"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "page": "1",
    "limit": "10"
}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取跑马灯弹幕用户数据")
		return self.response


class CommonMerchantHome(httpHandler):
	def __init__(self):
		super(CommonMerchantHome, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/common/merchant/home"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "merchant_id": "578",
    "storeMerchant_id": "4123",
    "page": "1",
    "limit": "10"
}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	聚合页首页")
		return self.response


class CommonModuleInfoWxConfig(httpHandler):
	def __init__(self):
		super(CommonModuleInfoWxConfig, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/common/moduleInfo/wxConfig"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "appId": "",
    "timestamp": "",
    "nonceStr": "",
    "signature": "",
    "jsApiList": [
        ""
    ]
}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取微信jssdk信息")
		return self.response


class Activity6MerchantGetIds(httpHandler):
	def __init__(self):
		super(Activity6MerchantGetIds, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/Activity6/merchant/getIds"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "ids": "578",
    "mobile": "15150578643"
}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询连锁是否有可用普惠红包")
		return self.response


class CommonMerchantActivity(httpHandler):
	def __init__(self):
		super(CommonMerchantActivity, self).__init__()
		self.host = "http://activity-news-backend.turboradio.cn"
		self.path = "/common/merchant/activity"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "partnerOrganIds": "635"
}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	公众号获取连锁活动")
		return self.response