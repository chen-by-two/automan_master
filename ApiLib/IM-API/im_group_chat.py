# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


# 查寻IM账号
class IM_account(httpHandler):
    def __init__(self):
        super(IM_account, self).__init__()
        self.host = "http://immid-ser-js.uniondrug.net"
        self.path = "/im/chat/imAccount"
        self.headers = {""}
        self.params = None
        self.data = {"sysCode": "dstoremember", "sysFlag": "16236619_c"}

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "查询im账号")
        return self.response


# 自定义消息-发送优惠卷信息
class IM_couponMsg(httpHandler):
    def __init__(self):
        super(IM_couponMsg, self).__init__()
        self.host = "http://immid-ser-js.uniondrug.net"
        self.path = "/im/sysMsg/couponMsg"
        self.headers = {}
        self.params = None
        self.data = dict(errno="0", error="SUCCESS", dataType="OBJECT", data={
            "errno": "0",
            "error": "SUCCESS",
            "dataType": "OBJECT",
            "data": "null"
        })

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "发送优惠卷信息")
        return self.response


# 轮询查询在线状态
class IM_pollIsOnline(httpHandler):
    def __init__(self):
        super(IM_pollIsOnline, self).__init__()
        self.host = "http://immid-ser-js.uniondrug.net"
        self.path = "/im/offline/pollIsOnline"
        self.headers = {}
        self.params = None
        self.data = dict(sysCode="healthtreasure", roomId="healthtreasure_15968231_4022502", sender="15968231",
                         senderRole="healthtreasurehtd", receiver="4022502", receiverRole="healthtreasurehtu")

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "轮询查询在线状态")
        return self.response


# IM会话框数据初始化
class IM_imInit(httpHandler):
    def __init__(self):
        super(IM_imInit, self).__init__()
        self.host = "http://immid-ser-js.uniondrug.net"
        self.path = "/im/user/imInit"
        self.headers = {}
        self.params = None
        self.data = dict(fromAcct="1b71a29459ac472fa81a2d49333et", toAcct="2936181304", scene="team")

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "IM会话框数据初始化")
        return self.response


# 医生列表
class IM_updateUser(httpHandler):
    def __init__(self):
        super(IM_updateUser, self).__init__()
        self.host = "http://immid-ser-js.uniondrug.net"
        self.path = "/im/user/updateUser"
        self.headers = {}
        self.params = None
        self.data = dict(acctId="16666154cdee4053b0fcd922587br", longitude="12.46", latitude="12.46")

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "医生列表")
        return self.response


# 修改IM账号
class IM_addFriendTo(httpHandler):
    def __init__(self):
        super(IM_addFriendTo, self).__init__()
        self.host = "http://immid-ser-js.uniondrug.net"
        self.path = "/im/user/addFriendTo"
        self.headers = {}
        self.params = None
        self.data = dict(type="1", sysCode="commission", sysFlagFrom="2", sysFlagTo="1", environment="t")

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "修改IM账号")
        return self.response


# 查询列表
class RenewCart(httpHandler):
    def __init__(self):
        super(RenewCart, self).__init__()
        self.host = "http://immid-ser-js.turboradio.cn"
        self.path = "/im/chat/currencyNewList"
        self.headers = {}
        self.params = None
        self.data = dict(recordMemberList=[
            {
                "sysFlag": "15961141_a",
                "sysCode": "advisor"
            }
        ], hasGroup="false", hasSingle="true", isInvisible="false")

    def changeEnv(self, env_gs1):
        self.host = self.host.replace("uniondrug.net", env_gs1)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "查询列表")
        return self.response
