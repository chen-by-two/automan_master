# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class UnifyorderMemberEquityQuery(httpHandler):
    def __init__(self):
        super(UnifyorderMemberEquityQuery, self).__init__()
        self.host = "https://wx.turboradio.cn"
        self.path = "/unifyorder/member/equity/query"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
        self.params = None
        self.data = {"confirmNo": "ec85243842af7ab1b360ea0d1b7f6264"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易订单详情页拉取可用权益列表")
        return self.response


class UnifyorderConfirmEquityChange(httpHandler):
    def __init__(self):
        super(UnifyorderConfirmEquityChange, self).__init__()
        self.host = "https://wx.turboradio.cn"
        self.path = "/unifyorder/confirm/equity/change"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IjE1OTYxNzQyIiwid3hPcGVuaWQiOiJvZi1GWHc3LXl5WFlTYm1oWGVlejBCQ1Zrd3V3IiwidmVyc2lvbiI6eyJrZXkiOiJBVVRIX21vYmlsZV8xNTk2MTc0MiIsInZhbHVlIjoiNiJ9LCJpbmZvIjp7Im5hbWUiOiJcdTUyMThcdTY2MGFcdTcxMzYiLCJtb2JpbGUiOiIxNTAwNTE1MDAyMyJ9LCJjaGFubmVsIjp7InR5cGUiOiIiLCJvcGVuaWQiOiIiLCJkb2N0b3JPcGVuaWQiOiIiLCJwYXRpZW50T3BlbmlkIjoiIiwid2RPcGVuaWQiOiIiLCJ3ZEFjY291bnRJZCI6IiIsInF5T3BlbmlkIjoiIiwiYXNzaXN0YW50SWQiOjAsInN0b3JlSWQiOjAsIm1lcmNoYW50SWQiOjB9fQ.wgenNhRhqigAuqYq1t5z65045VprI3hyQ6lIIzf56bxwFBiKGzuHHWmGcEwOt4p-B1XkfwRBs0YhRxJEkCop7ylDGxqyxT_IAo9w7bJ3jHusXyRfNKKMFwZ99-HbZIKW9V38cK6vwc5O-kwKchQN6gyLURIEZ3TiusuoXVgoXegWrxq5Ju5gri5YqM6VjdnJ7Wbr8vZ924k4bqk3s2hF6Dn2rSQfq0N5KtnN_31lOLGe_-ySxgqpEn2pCgoNihqFrYwXo5Iz1PZpfZ_fH53LjsUgMNk78oZECItn1iUwjE0qIGOzCPwF3uKPrExTkPDNrADHQSvnj6b4w7Mxe4Ew0Q"}
        self.params = None
        self.data = {"id": 24413516, "equityNo": "1000680724125568", "equityName": "自付转权益", "equityStyle": 1,
                     "equityStyleText": "面额", "availableFrom": "2020-07-01 17:28:44",
                     "availableTo": "2120-07-01 23:59:59", "balanceValue": 1, "balanceTimes": 0, "oneTimeValue": 0,
                     "equityType": 1, "equityTypeText": "普通权益", "equityStatus": 1, "equityStatusText": "正常",
                     "memberId": 15961742, "merchantId": 7, "programId": 108, "nominalValue": 1, "usedValue": 0,
                     "lockedValue": 0, "availableValue": 1, "availableTimes": 0, "nominalTimes": 0, "usedTimes": 0,
                     "lockedTimes": 0, "recycleMoney": "0.00", "recycleTimes": 0,
                     "confirmNo": "ec85243842af7ab1b360ea0d1b7f6264"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易订单详情页选择权益")
        return self.response


class RedeemAdd(httpHandler):
    def __init__(self):
        super(RedeemAdd, self).__init__()
        self.host = "http://issue.equity.backend.turboradio.cn"
        self.path = "/redeem/add"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
        self.params = {}
        self.data = {"cdKey": None, "userId": None, "name": None, "mobile": "18923425589", "verifyName": None,
                     "verifyMobile": "18923425589", "verifyIdCard": None, "verifyKeyword1": None,
                     "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7", "projectId": "415989",
                     "groupId": "2875", "customerId": None, "nominalValue": None, "nominalTimes": "3",
                     "oneTimeValue": "1.00", "idCardType": "01"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	权益后台生成权益卡")
        return self.response


class RedeemDisable(httpHandler):
    def __init__(self):
        super(RedeemDisable, self).__init__()
        self.host = "http://issue.equity.backend.turboradio.cn"
        self.path = "/redeem/disable"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer ae8272f6-6080-458e-b83e-2c883ba07e0d"}
        self.params = {}
        self.data = {"userId": "14036604", "groupId": "3089"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	权益后台权益冻结")
        return self.response
