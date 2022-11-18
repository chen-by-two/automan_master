# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class StagnationUserStatistic(httpHandler):
	def __init__(self):
		super(StagnationUserStatistic, self).__init__()
		self.host = "https://wxapi.turboradio.cn"
		self.path = "/stagnation/user/statistic"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjEyNzcsInd4T3BlbmlkIjoib2YtRlh3MWZ0RUVNVmZhQWFXUE5ydlM1YjRNWSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjEyNzciLCJ2YWx1ZSI6IjMifSwiaW5mbyI6eyJuYW1lIjoiIiwibW9iaWxlIjoiMTgwMjE3MjI2NTIifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.mTvpFDffNwH_FQKY4JYrFGAomcmGoeTkh5K5iPd854QZJdw82iMR6UhZSBeVHl_GpMXgGSZZSmbvAI6NDBUEYdM3d3ILSNzVhV3boyveRVX6oh13mxgUQbjw6apLiH-Whaa89Y2zZCL4lCpmZsbMPn-Z2u6Lx0P1ur5NtFRNFQi2xoFnaiWE7y_xXJnVnBEgZ1iR2UuJuqovBxuEqXDcyhmICNxdpMgzZh4QpaNDnUAsJdHzU7KW1MlamH9tyeiscVaDBytHTAgJUCH4tceIacHyZQJaahcqZveB9y_NKoz31KHmuIov8SwPokMkuw-sVS8VUbvQ6HqbMN70T43q7g"}
		self.params = None
		self.data = {"memberId": "15961277"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	个人中心统计数据")
		return self.response


class StagnationUserRecordPaging(httpHandler):
	def __init__(self):
		super(StagnationUserRecordPaging, self).__init__()
		self.host = "https://wxapi.turboradio.cn"
		self.path = "/stagnation/user/recordPaging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjcxODcsInd4T3BlbmlkIjoib2YtRlh3NXVLWU1oV0x4NFJWN3lNX3B4SVRmcyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjcxODciLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU4MDk2XHU2NTg3XHU3NDc2IiwibW9iaWxlIjoiMTU2NTE3MTE3MjkifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.rabiKn7QQ4451LNO3y2LoI2NOzsPthsPYRb-Hz2t_xMO7FiW0S4pOaG7x-KTvkTd67jCJ4OMfV9A0UP4P7DOtkj1zjO7UkHB8SItrft2LlFrLJacSzgtstMATBgy0VfEuU3we49vA-CwKU_qf3QNKlFAQP9wd_T7mAIhIhEh6pMM0Ui-HwvbJ7TmOWvKMA-IV1HI_1Hm7YPvFlfwkmXt10YAsBN9QTm6WaWeCgTnJ8bYZu77xISeYqumprnFOb6lOTtT0k30oO_t6Mrs8eT4OfeEaDCmC9iv5qH614lPJ_Ad4WJcE0S5SQwi8NM3NVE-zIv97IYA3VB4KZBXLdQ0Pw"}
		self.params = None
		self.data = {"memberId": "15967187","date": "","status": "1","equityNo": "","note": "","page": "1","limit": "10"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	发放记录查询")
		return self.response


class LoginImageCaptcha(httpHandler):
	def __init__(self):
		super(LoginImageCaptcha, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/imageCaptcha"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"15651711729"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	发送图形验证码")
		return self.response


class LoginSendCaptchaNew(httpHandler):
	def __init__(self):
		super(LoginSendCaptchaNew, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/sendCaptchaNew"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"15651711729","captcha":"2046"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	发送短信验证码")
		return self.response


class LoginLogin(httpHandler):
	def __init__(self):
		super(LoginLogin, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"15651711729","captcha":"807907"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过验证码登录")
		return self.response


class StagnationUserUserInfo(httpHandler):
	def __init__(self):
		super(StagnationUserUserInfo, self).__init__()
		self.host = "http://wxapi.turboradio.cn"
		self.path = "/stagnation/user/userInfo"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户信息查询")
		return self.response