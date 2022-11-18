# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class LoginSendCaptcha(httpHandler):
	def __init__(self):
		super(LoginSendCaptcha, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/sendCaptcha"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"15005150023"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	发送验证码")
		return self.response


class LoginLogin(httpHandler):
	def __init__(self):
		super(LoginLogin, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"15005150023","code":"758808"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	通过验证码登录")
		return self.response


class SmsSend(httpHandler):
	def __init__(self):
		super(SmsSend, self).__init__()
		self.host = "http://uncenter.backend.turboradio.cn"
		self.path = "/sms/send"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"13262567886"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	运营中心后台验证码获取")
		return self.response


class DdMobilelogin(httpHandler):
	def __init__(self):
		super(DdMobilelogin, self).__init__()
		self.host = "http://uncenter.backend.turboradio.cn"
		self.path = "/dd/mobilelogin"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"13262567886","code":690274}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	运营中心后台登录")
		return self.response


class Ddlogin(httpHandler):
	def __init__(self):
		super(Ddlogin, self).__init__()
		self.host = "http://uncenter.backend.turboradio.cn"
		self.path = "/dd/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1bmlvbmRydWcuYXV0aCIsImF1ZCI6InVuaW9uZHJ1Zy51bmNlbnRlciIsImlhdCI6MTU5OTYxODY0NSwibmJmIjoxNTk5NjE4NjQ1LCJleHAiOjE1OTk2MjU4NDUsInVzZXIiOnsibW9iaWxlIjoiMTMyNjI1Njc4ODYifX0.Tmkduk2vRJZd7RvJogmQHB2kdqpqAXknpFfcmmYzXOc"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	运营中心获取Authorization")
		return self.response


class ThePublicLoginSendCaptcha(httpHandler):
	def __init__(self):
		super(ThePublicLoginSendCaptcha, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/sendCaptcha"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"18923425589"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	公众号验证码发送接口")
		return self.response


class ThePublicLoginLogin(httpHandler):
	def __init__(self):
		super(ThePublicLoginLogin, self).__init__()
		self.host = "https://auth-backend.turboradio.cn"
		self.path = "/login/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"18923425589","code":"919136","channel":{"type":"wechat","openid":"jTcu+kAfgxtzPrgVMgGtilKR5tIahkXZpdpWnMXuCbVf1rS/9EGU7NB0puGdD+6JXNRRumvOPi1z4PwGivZG8vLoJ+1sKDgWzDmL9XQ1WU1qQVWpJj+vaTlXqEIgPq3Q/KSbW2jv7LbimexGOuY2BDJHZkylL/NamkCnsUByCKOcowijm6On3H17b6+mwAquRrGfffqNh7HHb91EHRId+tO04eOtlZWfNpR9VTFVeLhD2Kl8Dzx8zSR7Po9Ogh93oDSsLN+1xgZXxJC0CClIspS3MAo2WfQPVICRXDpls/ZaCmSpeD5PKP+bz2/Udn/HTa4MAcHHaqR43ixm8IFrJQ==","encryptOpenid":"jTcu+kAfgxtzPrgVMgGtilKR5tIahkXZpdpWnMXuCbVf1rS/9EGU7NB0puGdD+6JXNRRumvOPi1z4PwGivZG8vLoJ+1sKDgWzDmL9XQ1WU1qQVWpJj+vaTlXqEIgPq3Q/KSbW2jv7LbimexGOuY2BDJHZkylL/NamkCnsUByCKOcowijm6On3H17b6+mwAquRrGfffqNh7HHb91EHRId+tO04eOtlZWfNpR9VTFVeLhD2Kl8Dzx8zSR7Po9Ogh93oDSsLN+1xgZXxJC0CClIspS3MAo2WfQPVICRXDpls/ZaCmSpeD5PKP+bz2/Udn/HTa4MAcHHaqR43ixm8IFrJQ==","img":"http://thirdwx.qlogo.cn/mmopen/vwLEibamy4gOCUR45zJIqN3ycggsGwZ3ZpIDHqPDwyGdSjictldZfYjztlXDo47ThEYEpoESqGBRtCTmvtJK5ly80m3YnTOJKV/132","nickname":"Regret","sex":"1"}}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	公众号登录")
		return self.response
class makeLoginCaptcha(httpHandler):
	def __init__(self):
		super(makeLoginCaptcha, self).__init__()
		self.host = "http://msg.backend.uniondrug.net"
		self.path = "/extTemplate/operate"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {
  "operate":"set",
  "key":"verifyCode_valid_13372038701",
  "data":"123456"
}

	def changeEnv(self,env):
		self.host = self.host.replace("uniondrug.net",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	验证码制造成功")
		return self.response

