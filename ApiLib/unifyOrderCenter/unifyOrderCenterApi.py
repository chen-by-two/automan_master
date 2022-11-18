# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler
class UnifyorderGetConfirmNo(httpHandler):
    def __init__(self):
        super(UnifyorderGetConfirmNo, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/create"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}

        self.data = {
            "skuNos": ["539-948992584087240704"],
            "requestNo": "1646299402738",
            "channel": "7",
            "saleMerchantId": "539",
            "saleStoreId": "74596",
            "assistantId": 0,
            "shareMemberId": 0,
            "commissionNo": "",
            "partnerMerchantId": 0,
            "partnerOpenId": 0,
            "channelId": "0",
            "orderSource": 0,
            "orderMethod": "3",
            "tid": "",
            "quantity": "1",
            "showInsuredMember": None
                }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易获取ConfirmNo接口")
        return self.response





class UnifyorderqueryMulti(httpHandler):
    def __init__(self):
        super(UnifyorderqueryMulti, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/member/resource/query/multi"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}

        self.data = {
                "confirmNo": "03d63a49ce4668cd10aaeb8efe5b2486"
                    }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易获取用户可用权益列表接口")
        return self.response


class UnifyorderResoucechange(httpHandler):
    def __init__(self):
        super(UnifyorderResoucechange, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/resouce/change"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}

        self.data = {
            "resourceIdList": ["23426377", "23426396", "23426415", "23426417", "23426483"],
            "resourceType": 1,
            "balanceTimes": None,
            "oneTimeValue": 0,
            "balanceValue": None,
            "rsourceName": "权益固定面额",
            "resourceDescription": None,
            "resourceCutOffDate": "2023-01-29 23:59:59",
            "nominalValue": 0,
            "type": 3,
            "checked": None,
            "confirmNo": "03d63a49ce4668cd10aaeb8efe5b2486"
            }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易获取选择要用的资源接口")
        return self.response



class UnifyorderOrdercreate(httpHandler):
    def __init__(self):
        super(UnifyorderOrdercreate, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/order/create"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}

        self.data ={
            "miniprogram": None,
            "confirmNo": "03d63a49ce4668cd10aaeb8efe5b2486",
            "attachTOS": [{
                "type": 1,
                "name": "",
                "attachId": "",
                "url": "",
                "ruleType": "2"
            },
            {
                "type": 2,
                "name": "",
                "attachId": "",
                "url": "",
                "ruleType": "2"
            },
            {
                "type": 3,
                "name": "",
                "attachId": "",
                "url": "",
                "ruleType": "2"
            }]
            }
    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易创建订单接口")
        return self.response



class UnifyorderCashierpayModes(httpHandler):
    def __init__(self):
        super(UnifyorderCashierpayModes, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/cashier/payModes"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "miniprogram": None,
            "orderNo": "92030301603287940777",
            "supportAppPay": None
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	统一交易选择支付方式接口")
        return self.response

class UnifyorderCashiercreate(httpHandler):
    def __init__(self):
        super(UnifyorderCashiercreate, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/cashier/create"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "orderNo": "92041801603400060700",
            "payMode": "CWXPAY",
            "callback": "https://wx.uniondrug.net/dealnj/paySuccess?orderNo=92041801603400060700&usenow="
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易创建支付流水")
        return self.response


class UnifyorderCashierquery(httpHandler):
    def __init__(self):
        super(UnifyorderCashierquery, self).__init__()
        self.host = "http://java.pmc.cashier.uniondrug.net"
        self.path = "/cashier/queryCashierAllByOutTradeNo"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "outTradeNo": "82041801641488331705",
            "status": 0
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易获取交易流水信息")
        return self.response


class UnifyorderNotifyPayment(httpHandler):
    def __init__(self):
        super(UnifyorderNotifyPayment, self).__init__()
        self.host = "http://java.pmc.cashier.uniondrug.net"
        self.path = "/notify/payment"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "paymentNo": "2022042101345152815",
            "accountId": 12,
            "methodCode": "CWXPAY",
            "openid": "oRGmzs_tx73KsiBRL9gcXMbsa8do",
            "tradeType": None,
            "bankType": None,
            "totalFee": "0.01",
            "cashFee": "0.01",
            "transactionId": "220418124017114248",
            "outTradeNo": "100192042101603410720715",
            "timeEnd": "2022-04-18 15:13:47",
            "refundId": None,
            "outRefundNo": None,
            "tradeStatus": None,
            "refundAmount": None,
            "gmtRefund": None,
            "paymentType": "PD",
            "traceNo": None
}

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易支付回调")
        return self.response

class UnifyorderQueryMain(httpHandler):
    def __init__(self):
        super(UnifyorderQueryMain, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/order/query/main"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
	"orderNo": "92062201603592220726",
	"includeList": ["attachDOList"]
}

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易查询主订单接口")
        return self.response

class UnifyorderAttach(httpHandler):
    def __init__(self):
        super(UnifyorderAttach, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/order/attach/append"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
	"ruleType": "3",
	"type": "6",
	"orderNo": "92062201603592220726",
	"url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/cftjl9n6gi8sp78319uuks3vab.png"
}

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易快照附件信息")
        return self.response

class UnifyorderQueryOriginalMain(httpHandler):
    def __init__(self):
        super(UnifyorderQueryOriginalMain, self).__init__()
        self.host = "http://java.order.query.uniondrug.net"
        self.path = "/order/query/original/main"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.data = {
            "orderNo": "92062101603583380747",
            "viewAll": True
                }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易查询子订单号")
        return self.response

class UnifyorderOrderCancelSub(httpHandler):
    def __init__(self):
        super(UnifyorderOrderCancelSub, self).__init__()
        self.host = "http://java.order.uniondrug.net"
        self.path = "/order/cancel/sub"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.data = {
                "orderNo": "92061511603543670781",
                "type": None,
                "refundReasonType": 14,
                "refundReason": "自动化测试"
                }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易退单")
        return self.response

class UnifyorderConfirmJudgeSkuNo(httpHandler):
    def __init__(self):
        super(UnifyorderConfirmJudgeSkuNo, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/judgeSkuNo"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "skuNo":"578-988810502337462272"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易商品详情页屏蔽分享按钮")
        return self.response

class UnifycartCartAdd(httpHandler):
    def __init__(self):
        super(UnifycartCartAdd, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifycart/cart/add"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "channel": "7",
            "goodsNo": "578-988810502337462272",
            "commonName": "实物商品-积分+自付",
            "quantity": 1,
            "salePrice": 20,
            "ttl": -1,
            "saleType": 2,
            "saleActivityId": None,
            "salerStoreId": "74596",
            "specName": "1"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易加入购物车")
        return self.response

class UnifycartCartCount(httpHandler):
    def __init__(self):
        super(UnifycartCartCount, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifycart/cart/count"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "channel": "7"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易购物车数量")
        return self.response

class UnifyproductBuyLimit(httpHandler):
    def __init__(self):
        super(UnifyproductBuyLimit, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyproduct/buyLimit"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "memberId":16234661,
            "skuNoQries": [
                {
                    "skuNo": "578-988810502337462272",
                    "quantity": 1
                }
            ]
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易购买限制")
        return self.response

class UnifyAddressDefault(httpHandler):
        def __init__(self):
            super(UnifyAddressDefault, self).__init__()
            self.host = "https://wx.uniondrug.net"
            self.path = "/unifyorder/address/default"
            self.headers = {"Content-Type": "application/json;charset=UTF-8",
                            "Authorization": ""}
            self.data = {
            }

        def changeEnv(self, env):
            self.host = self.host.replace("uniondrug.net", env)

        def excute(self):
            if self.params != None:
                for k in self.params.keys():
                    self.path = self.path + self.params[k]
            self.response = self.run(1)
            self.logger.info(self.path + "\tdone" + "   统一交易默认地址")
            return self.response

class UnifyCartQuery(httpHandler):
    def __init__(self):
        super(UnifyCartQuery, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifycart/cart/query"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "longitude": 118.779749, "latitude": 31.971816, "channel": "7"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易购物车查询")
        return self.response

class UnifyorderConfirmShoppingCreate (httpHandler):
    def __init__(self):
        super(UnifyorderConfirmShoppingCreate, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/shopping/create"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "addressId": 103517,
            "requestNo": 1655796015000,
            "skuNos": [
                {
                    "id": 14855,
                    "goodsNo": "578-988810502337462272",
                    "quantity": 1,
                    "channel": 7,
                    "saleMerchantId": 539,
                    "saleStoreId": 74596,
                    "orderSource": 0
                }
            ]
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易购物车创建订单信息")
        return self.response

class UnifyorderConfirmDetail (httpHandler):
    def __init__(self):
        super(UnifyorderConfirmDetail, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/detail"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "confirmNo": "5a3a2fa1c3824c62fb338a0a1f70980d"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   获取confirm详情")
        return self.response

class UnifyorderConfirmUserRuleQuery (httpHandler):
    def __init__(self):
        super(UnifyorderConfirmUserRuleQuery, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/userRule/query"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "ruleTypes": [
                2,
                3
            ],
            "resources": [
                {
                    "resourceType": 3,
                    "details": [
                        {
                            "resourceId": "",
                            "resourceValue": "10"
                        }
                    ]
                },
                {
                    "resourceType": 4,
                    "details": [
                        {
                            "resourceId": "",
                            "resourceValue": "20"
                        }
                    ]
                }
            ],
            "totalAmount": 20,
            "channel": 7,
            "goodsList": [
                {
                    "merchantId": 578,
                    "storeId": 4123,
                    "goodsType": 1,
                    "goodsAmount": 20,
                    "goodsNumber": 1,
                    "skuNo": "578-988810502337462272",
                    "tradeCode": "",
                    "childList": [

                    ]
                }
            ]
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易查询规则")
        return self.response

class UnifyorderMemberCouponQuery (httpHandler):
    def __init__(self):
        super(UnifyorderMemberCouponQuery, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/member/coupon/query"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "confirmNo": "5a3a2fa1c3824c62fb338a0a1f70980d"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易用户优惠券列表查询")
        return self.response

class UnifyorderConfirmUserRoleContainsIdentity (httpHandler):
    def __init__(self):
        super(UnifyorderConfirmUserRoleContainsIdentity, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/confirm/userRole/containsIdentity"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "identityCode": 60
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易校验身份")
        return self.response

class UnifyorderMemberIntegralUse (httpHandler):
    def __init__(self):
        super(UnifyorderMemberIntegralUse, self).__init__()
        self.host = "https://wx.uniondrug.net"
        self.path = "/unifyorder/member/integral/use"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": ""}
        self.data = {
            "confirmNo": "5a3a2fa1c3824c62fb338a0a1f70980d"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("uniondrug.net", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "   统一交易启用药联积分")
        return self.response