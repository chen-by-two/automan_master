# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class UnfreezeAssistantSubmitApproval(httpHandler):
	def __init__(self):
		super(UnfreezeAssistantSubmitApproval, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/approvalAdd/approvalUnfreezeAssistant"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
	"assistants": [{
		"account": "15100001111",
		"status": "0",
		"partnerName": "沪宁大药房（简称）",
		"assistantId": "200003",
		"fullName": "张大大",
		"statusText": "已冻结",
		"storeName": "产品测试门店1-935（简称）"
	}],
	"approval": {
		"approveType": "2",
		"approveSettingId": "1",
		"applyName": "店员解冻",
		"processList": [{
			"operateType": "3",
			"processName": "大佬审批",
			"processType": "1",
			"processSettingId": "2558",
			"processUserList": [{
				"avatar": "https:\/\/ss2.bdstatic.com\/70cFvnSh_Q1YnxGkpoWK1HF6hhy\/it\/u=2834285391,2876082627&fm=26&gp=0.jpg",
				"mobile": "15380905486",
				"userId": "323",
				"userName": "张俊超02"
			}, {
				"avatar": "https:\/\/gimg2.baidu.com\/image_search\/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
				"mobile": "15651711729",
				"userId": "4186",
				"userName": "肖文瑶"
			}]
		}, {
			"operateType": "1",
			"processName": "抄送人",
			"processType": "2",
			"processSettingId": "2557",
			"processUserList": [{
				"avatar": "https:\/\/ss2.bdstatic.com\/70cFvnSh_Q1YnxGkpoWK1HF6hhy\/it\/u=2834285391,2876082627&fm=26&gp=0.jpg",
				"mobile": "15380905486",
				"userId": "323",
				"userName": "张俊超02"
			}, {
				"avatar": "https:\/\/gimg2.baidu.com\/image_search\/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
				"mobile": "15651711729",
				"userId": "4186",
				"userName": "肖文瑶"
			}]
		}]
	},
	"reason": "测测测测册测"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "店员解冻提交审批")
		return self.response

# class AdminTemplateSave(httpHandler):
# 	def __init__(self):
# 		super(AdminTemplateSave, self).__init__()
# 		self.host = "http://activity-news-backend.turboradio.cn"
# 		self.path = "/admin/template/save"
# 		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
# 		self.params = None
# 		self.data = {"id":"","type":"1","channel":"1","template_name":"测试新增模版0918","rules":"<p><span style=\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style=\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style=\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style=\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>","timeType":"1","times":"","release":"2","title":"药联健康给您发红包啦~","subtitle":"您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障","back_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png","button_icon":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png","play_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png","bottom_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png","share_img":"","share_icon":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png","explain":"","discount_img":"","pro_language":"药联健康给您发红包啦~","jump_url":"","OneRewardList":[{"reward_type":"2","scheme_type":"2","type":"2","udSchemeId":"xm202106301121282617","udSchemeName":"☆活动回归0630","amount":"14","rules":"活动回归0630","plan_type_id":"","rewardList":[]}]}
#
# 	def changeEnv(self,env):
# 		self.host = self.host.replace("turboradio.cn",env)
#
# 	def excute(self):
# 		if self.params != None:
# 			for k in self.params.keys():
# 				self.path = self.path+self.params[k]
# 		self.response = self.run(1)
# 		self.logger.info(self.path +"done" + "新增/编辑模版")
# 		return self.response