# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class queryPoolClaimAmount(httpHandler):
    def __init__(self):
        super(queryPoolClaimAmount, self).__init__()
        self.host = "http://jm-insure.turboradio.cn"
        self.path = "/insure/queryPoolClaimAmount"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"latitude": 1, "startDate": "2022-04-07", "endDate": "2022-04-20", "directPay": 1,
                     "medicalDeviced": 0, "drugType": 0, "insureCompanyId": 7}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	查询订单模式直赔流量池")
        return self.response


class listFeeBill(httpHandler):
    def __init__(self):
        super(listFeeBill, self).__init__()
        self.host = "http://jm-insure.turboradio.cn"
        self.path = "/policyProcedures/listFeeBill"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"policyIds": [2312, 2311]}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	查询保单手续费")
        return self.response


class getByProjectId(httpHandler):
    def __init__(self):
        super(getByProjectId, self).__init__()
        self.host = "http://jm-insure.turboradio.cn"
        self.path = "/policy/getByProjectId"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"projectId": 576}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	根据项目id查询保单详情")
        return self.response


class InfoPaging(httpHandler):
    def __init__(self):
        super(InfoPaging, self).__init__()
        self.host = "http://jm-insure.turboradio.cn"
        self.path = "/policy/infoPaging"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {
            "insurerId": 7,
            "policyNo": "uccyrv",
            "policyType": 2,
            "insureMethod": 1,
            "claimMethod": 1,
            "startTime": "2022-05-20 00:00:00"

        }

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	获取保单的服务费和保费计划")
        return self.response


class dataCheck(httpHandler):
    def __init__(self):
        super(dataCheck, self).__init__()
        self.host = "http://jm-insure.turboradio.cn"
        self.path = "/batch/dataCheck"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"billNo": "BN202112231635322870799588076054", "sumClaim": 65.43, "totalNum": 2}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	批次报案总额校验")
        return self.response


class getByInsurerIdAndPolicyNo(httpHandler):
    def __init__(self):
        super(getByInsurerIdAndPolicyNo, self).__init__()
        self.host = "http://jm-insure.turboradio.cn"
        self.path = "/policy/getByInsurerIdAndPolicyNo"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"insurerId": 240371, "policyNo": "531312214400000000900"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	根据保司id、保单号 获取保单详情")
        return self.response


class mbsOrderClearing(httpHandler):
    def __init__(self):
        super(mbsOrderClearing, self).__init__()
        self.host = "http://jm-insure.uniondrug.net"
        self.path = "/mbs/order/clearing"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"insurerId": 240371, "policyNo": "531312214400000000900"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	mbs-商品清算入投保理赔")
        return self.response


class mbsGoodsReplace(httpHandler):
    def __init__(self):
        super(mbsGoodsReplace, self).__init__()
        self.host = "http://jm-insure.uniondrug.net"
        self.path = "/mbs/goods/replace"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"insurerId": 240371, "policyNo": "531312214400000000900"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	mbs-商品替换入投保理赔")
        return self.response


class mbsOrderAttach(httpHandler):
    def __init__(self):
        super(mbsOrderAttach, self).__init__()
        self.host = "http://jm-insure.uniondrug.net"
        self.path = "/mbs/order/attach"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"insurerId": 240371, "policyNo": "531312214400000000900"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	订单理赔材料")
        return self.response


class mbsClaimSattleClaim(httpHandler):
    def __init__(self):
        super(mbsClaimSattleClaim, self).__init__()
        self.host = "http://jm-insure.uniondrug.net"
        self.path = "/mbs/claim/sattleClaim"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"statementNo":"DS20220628100002","orderNo":"92061611603549650106","endDate":"2022-06-16","startDate":"2022-06-16"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "	done" + "	直付订单理赔")
        return self.response