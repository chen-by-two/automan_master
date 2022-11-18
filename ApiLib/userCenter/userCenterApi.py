from Common.HttpHandler import httpHandler



class UserCardAdd(httpHandler):
	def __init__(self):
		super(UserCardAdd, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/add"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"typeId":1,"cardNo":" 110101192801012439 ","cardName":"张小君","address":"江苏省南京市雨花台区金证科技园2栋","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","images":"652423567","authWay":"11"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	身份证实名认证接口")
		return self.response


class V2ApiOrgAdd(httpHandler):
	def __init__(self):
		super(V2ApiOrgAdd, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/org/add"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
 "memberId":6261,
 "merchantId":7791,
 "merchantType":1,
 "merchantName":"merchantName",
 "merchantShortName":"merchantShortName",
 "orgId":9071,
 "orgName":"orgName",
 "jobNo":"jobNo",
 "remark":"remark",
 "orgResource":18
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	添加组织")
		return self.response


class V2ApiOrgQueryBy(httpHandler):
	def __init__(self):
		super(V2ApiOrgQueryBy, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/org/queryBy"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
 "memberId":6261,
 "orgId":-1,
"merchantType":20
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询组织")
		return self.response


class V2ApiOrgRemove(httpHandler):
	def __init__(self):
		super(V2ApiOrgRemove, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/org/remove"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
 "memberId":6261,
 "orgId":9071
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	删除组织")
		return self.response


class V2ApiUserCardAddByNo(httpHandler):
	def __init__(self):
		super(V2ApiUserCardAddByNo, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/addByNo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {
	"memberId":15965321,
	"typeId":4,
	"cardNo":"ysz1022t",
	"cardName":"李若然·",
	"gmtExpiryStart":"2020-09-02 10:22:05",
	"gmtExpiryEnd":"2021-11-11 10:22:05",
	"imageFront":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/53b3c8a6ff4a4bb1a479fa4201192cf9.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=R25lYF2f3SWU9qXhq%2FKKwJjNkvw%3D",
	"imageBack":"http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/d2dbbeb79671425eaea2b155e1fa83bb.png?Expires=4102416000&OSSAccessKeyId=LTAIixbWNsbuXaBc&Signature=pPjRFueq1Q1ZEgu2Z2fxFur9gwk%3D",
	"authWay":1,
    "approveStatus":1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	职业认证接口")
		return self.response


class MngTaskUpdate(httpHandler):
	def __init__(self):
		super(MngTaskUpdate, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/add"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"typeId":1,"cardNo":"530111197410022174","cardName":"杨琼仙","gmtExpiryStart":"2021-1-26 09:17:45","gmtExpiryEnd":"2029-12-16 09:17:45","imageFront":"2mublb8888","imageBack":"1n0to9","authWay":7}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	修改成长任务接口")
		return self.response


class UserBasicQuery(httpHandler):
	def __init__(self):
		super(UserBasicQuery, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userBasic/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"id":15965194,"account":"18761600404"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询用户基本信息")
		return self.response


class UserCardGetById(httpHandler):
	def __init__(self):
		super(UserCardGetById, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/getById"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"typeId":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过memberId查询实名认证信息")
		return self.response


class UserThirdQuery(httpHandler):
	def __init__(self):
		super(UserThirdQuery, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userThird/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"oauthType":1,"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询第三方平台授权")
		return self.response


class UserMajorQueryBy(httpHandler):
	def __init__(self):
		super(UserMajorQueryBy, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userMajor/queryBy"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"account":"18761600404"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过memberId和account查询")
		return self.response


class UserMajorQueryByOpenId(httpHandler):
	def __init__(self):
		super(UserMajorQueryByOpenId, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userMajor/queryByOpenId"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"openId":"of-FXw49rVufE5YKTEKOx_tJx6Cc","oauthType":6}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过openid查询")
		return self.response


class UserBasicBatchByIds(httpHandler):
	def __init__(self):
		super(UserBasicBatchByIds, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userBasic/batchByIds"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberIds":[15965194]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	批量查看用户详情")
		return self.response


class UserCardGetReal(httpHandler):
	def __init__(self):
		super(UserCardGetReal, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/getReal"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过memberID查询实名证件")
		return self.response


class UserAddressPage(httpHandler):
	def __init__(self):
		super(UserAddressPage, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userAddress/page"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":10,"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	分页查询用户收货地址列表")
		return self.response


class UserRoleGetOne(httpHandler):
	def __init__(self):
		super(UserRoleGetOne, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userRole/getOne"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"codeList":[645,556]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询用户组织")
		return self.response


class UserBasicAddOrQuery(httpHandler):
	def __init__(self):
		super(UserBasicAddOrQuery, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userBasic/addOrQuery"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"account":"18762189000","credentials":"mobk9q","staCode":0,"nickName":"meryl.bauch","usedName":"思淼.叶","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"炫明.刘@gmail.com","mobile":"15880518621","img":"ml4e9k","udCard":"vi2xqh","balance":871,"province":"ygluvy","provinceCode":"11784","city":"ifrmbn","cityCode":"11784","region":"a73soh","regionCode":"11784","memberSource":9}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	添加用户已存在则查询用户")
		return self.response


class UserRuleQuery(httpHandler):
	def __init__(self):
		super(UserRuleQuery, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userRule/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"ruleTypes":[2,1,3],"resources":[{"resourceType":1,"details":[{"resourceId":"489","resourceValue":""}]}]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询用户签名规则")
		return self.response


class UserInfoGetRealByCarNo(httpHandler):
	def __init__(self):
		super(UserInfoGetRealByCarNo, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userInfo/getRealByCarNo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"cardNo":"530111197410022174"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过证件号码查询实名的用户信息")
		return self.response


class UserGuardianQuery(httpHandler):
	def __init__(self):
		super(UserGuardianQuery, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userGuardian/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询监护人信息")
		return self.response


class UserMajorBatchByMemberIds(httpHandler):
	def __init__(self):
		super(UserMajorBatchByMemberIds, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userMajor/batchByMemberIds"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberIds":[15965194]}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过memberId批量查询用户信息")
		return self.response


class UserTagContainsTagValuesBatch(httpHandler):
	def __init__(self):
		super(UserTagContainsTagValuesBatch, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userTag/containsTagValuesBatch"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberIds":[12,15,17,19,21,22,23,25,28,30,31],"tagId":"071AC4E0"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	批量判断标签下所有值是否包含用户")
		return self.response


class UserAddressPageGet(httpHandler):
	def __init__(self):
		super(UserAddressPageGet, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userAddress/get"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"id":29433}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询用户收货地址")
		return self.response


class UserCardBatchByIds(httpHandler):
	def __init__(self):
		super(UserCardBatchByIds, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/batchByIds"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberIds":[15965194],"typeId":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过memberId集合批量查询用户实名信息")
		return self.response


class UserPage(httpHandler):
	def __init__(self):
		super(UserPage, self).__init__()
		self.host = "http://user-biz-js.turboradio.cn"
		self.path = "/user/page"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"page":1,"limit":10,"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	分页查询用户服务资格")
		return self.response


class UserCardGetRealInfo(httpHandler):
	def __init__(self):
		super(UserCardGetRealInfo, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/getRealInfo"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过memberId查询实名证件")
		return self.response


class UserThirdPage(httpHandler):
	def __init__(self):
		super(UserThirdPage, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userThird/page"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"pageNum":1,"pageSize":10,"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	分页查询第三方平台授权列表")
		return self.response


class UserFamilyQueryByMemberId(httpHandler):
	def __init__(self):
		super(UserFamilyQueryByMemberId, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userFamily/queryByMemberId"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	通过用户ID查询家庭关系列表")
		return self.response


class UserRuleQueryGetSign(httpHandler):
	def __init__(self):
		super(UserRuleQueryGetSign, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userRule/getSign"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询用户签名规则")
		return self.response


class UserThirdBind(httpHandler):
	def __init__(self):
		super(UserThirdBind, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userThird/bind"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"oauthName":"张小三","oauthType":13,"appId":"52","openId":"52","openId2":"xwdj08","unionId":"52"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	绑定第三方平台授权")
		return self.response


class UserAddressAdd(httpHandler):
	def __init__(self):
		super(UserAddressAdd, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userAddress/add"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"tag":"wpbnur","consigneeName":"赵五","mobile":"18761600404","province":"5543","provinceCode":"65120","city":"wypgpc","cityCode":"65120","region":"japb8g","regionCode":"65120","street":"23423424","fullAddress":"234242","locationType":"i9hsin","longitude":"ep680y","latitude":"kjw1cm","landmark":"2342424242","isDefault":0,"staCode":1}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	添加收货地址")
		return self.response


class UserRoleContainsIdentity(httpHandler):
	def __init__(self):
		super(UserRoleContainsIdentity, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userRole/containsIdentity"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"identityCode":0}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	校验用户身份")
		return self.response


class UserAddressGetDefault(httpHandler):
	def __init__(self):
		super(UserAddressGetDefault, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userAddress/getDefault"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	获取默认地址")
		return self.response


class UserBasicUpdate(httpHandler):
	def __init__(self):
		super(UserBasicUpdate, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userBasic/update"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"id":15965194,"account":"18761600404","staCode":0,"nickName":"33333333","usedName":"徐芬芬","gender":"01","birthdayPrefix":1,"birthday":"2021-03-02 13:34:44","email":"22xh2e34fv@gmail.com","mobile":"18761600404","img":"1mxdx2","udCard":"39barj","balance":751,"province":"3ygwci","provinceCode":"11784","city":"iru6cw","cityCode":"11784","region":"nrspde","regionCode":"11784"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	编辑用户基本信息")
		return self.response


class UserCardCheck(httpHandler):
	def __init__(self):
		super(UserCardCheck, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/userCard/check"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"cardName":"张丽军","cardNo":"210423199308061827"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	校验大陆身份证")
		return self.response


class PromoteUpdate(httpHandler):
	def __init__(self):
		super(PromoteUpdate, self).__init__()
		self.host = "http://java.uc.resource.turboradio.cn"
		self.path = "/user/mbs/promote/update"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15965194","cardId":"1d646eca76a5403d8e0b","status":"1","cardType":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	优惠权益mbs消费接口")
		return self.response


class MbsLogin(httpHandler):
	def __init__(self):
		super(MbsLogin, self).__init__()
		self.host = "http://java.uc.resource.turboradio.cn"
		self.path = "/user/mbs/login"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"topicName":"auth","topicTag":"userFirstLoginDaily"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户登录mbs")
		return self.response


class EquityUpdate(httpHandler):
	def __init__(self):
		super(EquityUpdate, self).__init__()
		self.host = "http://java.uc.resource.turboradio.cn"
		self.path = "/user/mbs/equity/update"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15965194","equityId":"112467791132769","equityStatus":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	权益mbs消费接口")
		return self.response


class GuaranteeUpdate(httpHandler):
	def __init__(self):
		super(GuaranteeUpdate, self).__init__()
		self.host = "http://java.uc.resource.turboradio.cn"
		self.path = "/user/mbs/guarantee/update"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15965194","guaranteeId":"112467791132769","guaranteeStatus":"1","guaranteeType":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	保障mbs消费接口")
		return self.response


class GiftUpdate(httpHandler):
	def __init__(self):
		super(GiftUpdate, self).__init__()
		self.host = "http://java.uc.resource.turboradio.cn"
		self.path = "/user/mbs/gift/update"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15965194","recordId":"1129","state":"1"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	增值礼包mbs消费接口")
		return self.response


class ResourceQuery(httpHandler):
	def __init__(self):
		super(ResourceQuery, self).__init__()
		self.host = "http://java.uc.resource.turboradio.cn"
		self.path = "/user/resource/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":15965194,"sort":0,"couponType":2}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	用户资源混合查询")
		return self.response


class SubsidyQuery(httpHandler):
	def __init__(self):
		super(SubsidyQuery, self).__init__()
		self.host = "http://cios-subsidy-js.turboradio.cn"
		self.path = "/subsidy/query"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"orderNo":"82072801655625370102","channel":1,"merchantId":635,"resources":[{"resourceType":1,"resourceId":""}],"gmtOrdered":"2022-07-28 15:52:00"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询商家补贴方案")
		return self.response


class SubsidyGetById(httpHandler):
	def __init__(self):
		super(SubsidyGetById, self).__init__()
		self.host = "http://cios-subsidy-js.turboradio.cn"
		self.path = "/subsidy/getById"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"id":89}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	查询方案详情")
		return self.response


class MemberReal(httpHandler):
	def __init__(self):
		super(MemberReal, self).__init__()
		self.host = "http://vip-srv-js.turboradio.cn"
		self.path = "/mbs/member/real"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15965194"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	会员")
		return self.response


class DataTimePage(httpHandler):
	def __init__(self):
		super(DataTimePage, self).__init__()
		self.host = "http://java.user.service.turboradio.cn"
		self.path = "/v2/api/data/time/page"
		self.headers = {"Content-Type":"application/json;charset=UTF-8"}
		self.params = None
		self.data = {"memberId":"15965194"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	DataTimePage")
		return self.response