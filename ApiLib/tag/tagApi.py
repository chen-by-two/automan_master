# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class UserPackageBaseCreate(httpHandler):
	def __init__(self):
		super(UserPackageBaseCreate, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/user/package/base/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"clauseType":"IS","tagId":"XB","tagValue":"男"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	基础人群包（一级）创建接口")
		return self.response


class UserPackageHighlevelCreate(httpHandler):
	def __init__(self):
		super(UserPackageHighlevelCreate, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/user/package/highlevel/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"packageIds":[1,3,5],"relationType":"AND"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	高层级人群包创建接口")
		return self.response


class UserPackageUsersGet(httpHandler):
	def __init__(self):
		super(UserPackageUsersGet, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/user/package/users/get"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"packageId":2,"page":1,"size":1000}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	根据人群包分页查询用户id接口")
		return self.response


class MemberWideInsertMemberPackage(httpHandler):
	def __init__(self):
		super(MemberWideInsertMemberPackage, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/memberWide/insertMemberPackage"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"conditions":[{"conditionType":1,"valueType":1,"values":["1","2"],"fieldType":1},{"conditionType":2,"valueType":2,"values":["1993"],"fieldType":1},{"conditionType":2,"valueType":3,"values":["1995"],"fieldType":1},{"conditionType":3,"valueType":1,"values":["110000","130000"],"fieldType":1},{"conditionType":4,"valueType":1,"values":["130200","130700"],"fieldType":1}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	新增用户宽表基础人群包接口")
		return self.response


class OrderWideInsertOrderPackage(httpHandler):
	def __init__(self):
		super(OrderWideInsertOrderPackage, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/orderWide/insertOrderPackage"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"conditions":[{"conditionType":1,"valueType":2,"values":["2020-05-06 12:12:12"],"fieldType":1},{"conditionType":1,"valueType":3,"values":["2020-05-07 12:12:12"],"fieldType":1},{"conditionType":2,"valueType":2,"values":["0"],"fieldType":2},{"conditionType":2,"valueType":3,"values":["18"],"fieldType":2}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	新增交易宽表基础人群包接口")
		return self.response


class UserPackageDelete(httpHandler):
	def __init__(self):
		super(UserPackageDelete, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/user/package/delete"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"id" : 2}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	删除人群包接口")
		return self.response


class UserPackageListMember(httpHandler):
	def __init__(self):
		super(UserPackageListMember, self).__init__()
		self.host = "http://java.tag.service.turboradio.cn"
		self.path = "/user/package/listMember"
		self.headers = {"Content-Type": "application/json;charset=UTF-8"}
		self.params = None
		self.data = {"ids":[1,2,3]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"\tdone" + "	查询覆盖人数、数据时间接口")
		return self.response
