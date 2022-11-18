# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as ckw
import KeyWordDriver.BusinesskeyWord as bkw

# path = '/Users/uniondrug/PycharmProjects/automan/TestFile/wangj/unifyOrder_drug.yaml'
path = 'TestFile/wangj/unifyOrder_drug.yaml'
yamlfile = ckw.CommonKeyWord().Yaml_Read(path)
# 读取手机号码
mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile")
# 读取rc环境
env = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "env_rc")
# 读取商品skuNos
skuNos = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "skuNos")
# 读取yaml文件渠道
channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel")
# 获取资源id
sourceId3 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "sourceId3")
#获取替代验证码
LogintCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "LogintCaptcha")

class Test_unifyOrderEquityAndSelf_drug:

    @allure.feature("公众号登陆")
    @allure.severity("blocker")
    def test_drug_login(self):
        # 打开yaml文件
        # 造公众号登录验证码
        bkw.authApi_makeLoginCaptcha({"header": {"Content-Type": "application/json"},
                                      "parma": {},
                                      "data": {"operate": "set",
                                               "key": "verifyCode_valid_15950572929",
                                               "data": LogintCaptcha},
                                      "env": env},
                                    "dict")
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "公众号登陆")
        # 公众号登录
        Loginlogin = bkw.authApi_LoginLogin({"header": {"Content-Type": "application/json"}, "parma": {},
                                             "data": {"mobile": mobile, "code": LogintCaptcha}, "env": env}, "dict")
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("登陆返回参数：", Loginlogin)
        # 公众号登录token提取鉴权
        global token
        token = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin, [["data", "token"]])
        # 读取yaml文件token认证
        # 打印当前token认证
        ckw.CommonKeyWord().Print_ToControl("token：", token)

    @allure.feature("统一交易获取ConfirmNo接口")
    @allure.severity("blocker")
    def test_drug_confirm_create(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例001：统一交易获取ConfirmNo接口")

        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 生成comfrimNo
        comfirmNoData = bkw.unifyOrderCenterApi_UnifyorderGetConfirmNo(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"skuNos": [skuNos],
                      "requestNo": timeStamp,
                      "channel": channel,
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
                      "showInsuredMember": None}, "env": env},
            "dict")
        # 打印当前comfirm接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", comfirmNoData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(comfirmNoData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        ckw.CommonKeyWord().Print_ToControl("confirmNo接口data：", comfirmNoData)
        global confirmNo
        confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(comfirmNoData, [["data", "confirmNo"]])
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取用户可用权益列表接口")
    def test_drug_query_multi(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例002：统一交易获取用户可用权益列表接口")

        queryMulti = bkw.unifyOrderCenterApi_UnifyorderqueryMulti(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("queryMulti：", queryMulti)
        # 打印当前comfirm接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", queryMulti)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(queryMulti, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取选择要用的资源接口")
    def test_drug_resouce_change(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例003：统一交易获取选择要用的资源接口")

        resouceChangeData = bkw.unifyOrderCenterApi_UnifyorderResoucechange(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"resourceIdList": [sourceId3],
                      "resourceType": 1,
                      "balanceTimes": None,
                      "oneTimeValue": 0,
                      "balanceValue": None,
                      "rsourceName": "药联健康权益",
                      "resourceDescription": None,
                      "resourceCutOffDate": "2026-04-30 23:59:59",
                      "nominalValue": 0,
                      "type": 3,
                      "checked": True,
                      "confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("resouceChangeData：", resouceChangeData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(resouceChangeData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易创建订单接口")
    def test_drug_order_create(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例004：统一交易创建订单接口")

        orderCreateData = bkw.unifyOrderCenterApi_UnifyorderOrdercreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"miniprogram": False,
                      "confirmNo": confirmNo,
                      "attachTOS": [{
                          "type": 1,
                          "name": "",
                          "attachId": "",
                          "url": "",
                          "ruleType": "2"
                      }, {
                          "type": 2,
                          "name": "",
                          "attachId": "",
                          "url": "",
                          "ruleType": "2"
                      }, {
                          "type": 3,
                          "name": "",
                          "attachId": "",
                          "url": "",
                          "ruleType": "2"
                      }]}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("orderCreateData：", orderCreateData)
        global orderNo
        orderNo = ckw.CommonKeyWord().Json_GetJsonValue(orderCreateData, [["data", "orderNo"]])
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(orderCreateData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易选择支付方式接口")
    def test_drug_cashier_payModes(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例005：统一交易选择支付方式接口")

        cashierpayModesData = bkw.unifyOrderCenterApi_UnifyorderCashierpayModes(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"miniprogram": False,
                      "orderNo": orderNo,
                      "supportAppPay": False
                      }, "env": env},
            "dict")

        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("cashierpayModesData：", cashierpayModesData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(cashierpayModesData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)
        #断言字段
        directAmount = ckw.CommonKeyWord().Json_GetJsonValue(cashierpayModesData, [["data", "order", "directAmount"]])
        payAmount = ckw.CommonKeyWord().Json_GetJsonValue(cashierpayModesData, [["data","order", "payAmount"]])

        ckw.CommonKeyWord().Print_ToControl("权益支付价格：", directAmount)

        ckw.CommonKeyWord().Print_ToControl("微信直付：", cashierpayModesData)

        #实物商品价格
        assert directAmount == "5"
        # #实付价格
        assert payAmount == "5"

    @allure.feature("统一交易创建支付流水")
    @allure.severity("blocker")
    def test_drug_cashier_create(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例006：统一交易创建支付流水")

        cashierCreateData = bkw.unifyOrderCenterApi_UnifyorderCashiercreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"orderNo": orderNo,
                      "payMode": "CWXPAY",
                      "callback": "https://wx.uniondrug.net/dealnj/paySuccess?orderNo=" + orderNo + "&usenow="
                      }, "env": env},
            "dict")

        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("cashierCreateData：", cashierCreateData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(cashierCreateData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取交易流水信息")
    @allure.severity("blocker")
    def test_drug_cashier_query(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例007：统一交易获取交易流水信息")

        CashierqueryCashierData = bkw.unifyOrderCenterApi_UnifyorderCashierqueryCashier(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"outTradeNo": orderNo,
                      "status": 0
                      }, "env": env},
            "dict")


        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("CashierqueryCashierData：", CashierqueryCashierData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(CashierqueryCashierData, [["errno"]])

        global paymentNo
        global tradeNo
        #获取paymentNo
        paymentNoData = ckw.CommonKeyWord().Json_GetJsonValue(CashierqueryCashierData, [["data", "body"]])
        paymentNo = ckw.CommonKeyWord().Json_GetJsonValue(paymentNoData[0], [["paymentNo"]])
        # 打印
        ckw.CommonKeyWord().Print_ToControl("paymentNo：", paymentNo)
        #获取tradeNo
        tradeNoData = ckw.CommonKeyWord().Json_GetJsonValue(CashierqueryCashierData, [["data", "body"]])
        tradeNo = ckw.CommonKeyWord().Json_GetJsonValue(tradeNoData[0], [["tradeNo"]])
        # 打印
        ckw.CommonKeyWord().Print_ToControl("tradeNo：", tradeNo)

        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易支付回调")
    @allure.severity("blocker")
    def test_drug_notify_payment(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例008：统一交易支付回调")

        NotifyPaymentData = bkw.unifyOrderCenterApi_UnifyorderNotifyPaymentData(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "paymentNo": paymentNo,
                 "accountId": 12,
                 "methodCode": "CWXPAY",
                 "openid": "oRGmzs_tx73KsiBRL9gcXMbsa8do",
                 "tradeType": None,
                 "bankType": None,
                 "totalFee": "0.01",
                 "cashFee": "0.01",
                 "transactionId": "220418124017114248",
                 "outTradeNo": tradeNo,
                 "timeEnd": "2022-04-18 15:13:47",
                 "refundId": None,
                 "outRefundNo": None,
                 "tradeStatus": None,
                 "refundAmount": None,
                 "gmtRefund": None,
                 "paymentType": "PD",
                 "traceNo": None
            }, "env": env},
            "dict")

        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("NotifyPaymentData：", NotifyPaymentData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(NotifyPaymentData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取子订单号")
    @allure.severity("blocker")
    def test_drug_query_original_main(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例009：统一交易获取子订单")

        QueryOriginalMainData = bkw.unifyOrderCenterApi_UnifyorderQueryOriginalMain(
            {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
             "data": {"orderNo": orderNo,
                      "viewAll": True},
            "env": env},
            "dict")


        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("QueryOriginalMainData：", QueryOriginalMainData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(QueryOriginalMainData, [["errno"]])

        global suborderNo
        #获取paymentNo
        subOrderList = ckw.CommonKeyWord().Json_GetJsonValue(QueryOriginalMainData, [["data", "subOrderList"]])
        suborderNo = ckw.CommonKeyWord().Json_GetJsonValue(subOrderList[0], [["orderNo"]])
        # 打印
        ckw.CommonKeyWord().Print_ToControl("suborderNo：", suborderNo)

        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)


    @allure.feature("统一交易仅退款")
    @allure.severity("blocker")
    def test_drug_order_cancel_sub(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例010：统一交易仅退款")

        orderCancelSubData = bkw.unifyOrderCenterApi_UnifyorderOrderCancelSubData(
            {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
             "data": {
             "orderNo": suborderNo,
             "type": None,
             "refundReasonType": 14,
             "refundReason": "12345"
            }, "env": env},
            "dict")

        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("orderCancelSubData：", orderCancelSubData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(orderCancelSubData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "err")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)