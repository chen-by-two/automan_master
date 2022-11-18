# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


# 采用用户名/密码登录商家服务平台
class PasswordLogin(httpHandler):
	def __init__(self):
		super(PasswordLogin, self).__init__()
		self.host = "https://business-center-backend.turboradio.cn"
		self.path = "/user/login"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"mobile":"15256908297","password":"123456"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	商家服务平台通过密码登录--老接口")
		return self.response


# 采用用户名/密码登录商家服务平台
class SmsLogin(httpHandler):
	def __init__(self):
		super(SmsLogin, self).__init__()
		self.host = "https://m.uniondrug.net"
		self.path = "/user/smsLogin"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"account": "15256908297", "type": 2, "credentials": "123456", "tenantId": 3}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	商家服务平台通过密码登录")
		return self.response


# 数据库查询，获取手机验证码进行登录
class DdMobilelogin(httpHandler):
	def __init__(self):
		super(DdMobilelogin, self).__init__()
		self.host = "https://pm-fin-shares.turboradio.cn"
		self.path = "/auth/login"
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
		self.logger.info(self.path +"\tdone" + "	财务共享平台登录")
		return self.response


class Ddlogin(httpHandler):
	def __init__(self):
		super(Ddlogin, self).__init__()
		self.host = "https://pm-fin-shares.turboradio.cn"
		self.path = "/auth/login"
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
		self.logger.info(self.path +"\tdone" + "	财务共享平台获取Authorization")
		return self.response


