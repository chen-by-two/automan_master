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
skuNos = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "skuNos3")
# 读取yaml文件渠道
channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel")
#获取替代验证码
LogintCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "LogintCaptcha")

class Test_unifyOrderintegralselfPaid:

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
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
    @allure.feature("统一交易商品详情页屏蔽分享按钮")
    @allure.severity("blocker")
    def test_drug_confirm_judgeSkuNo(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例001：统一交易商品详情页屏蔽分享按钮")

        ConfirmJudgeSkuNoData = bkw.unifyOrderCenterApi_UnifyorderConfirmJudgeSkuNo(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "skuNo": skuNos
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", ConfirmJudgeSkuNoData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(ConfirmJudgeSkuNoData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易加入购物车")
    @allure.severity("blocker")
    def test_drug_unifycart_cart_add(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例002：统一交易加入购物车")

        UnifycartCartAddData = bkw.unifyOrderCenterApi_UnifycartCartAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                "channel": channel,
                "goodsNo": skuNos,
                "commonName": "实物商品-积分+自付",
                "quantity": 1,
                "salePrice": 20,
                "ttl": -1,
                "saleType": 2,
                "saleActivityId": None,
                "salerStoreId": "74596",
                "specName": "1"
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifycartCartAddData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifycartCartAddData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易购物车数量")
    @allure.severity("blocker")
    def test_drug_unifycart_cart_count(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例003：统一交易购物车数量")

        UnifycartCartCountData = bkw.unifyOrderCenterApi_UnifycartCartCount(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                "channel": channel
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifycartCartCountData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifycartCartCountData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易购买限制")
    @allure.severity("blocker")
    def test_drug_unifyproduct_buyLimit(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例004：统一交易购买限制")

        UnifyproductBuyLimitData = bkw.unifyOrderCenterApi_UnifyproductBuyLimit(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "memberId": 16234661,
                 "skuNoQries": [
                     {
                         "skuNo": skuNos,
                         "quantity": 1
                     }
                 ]
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyproductBuyLimitData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyproductBuyLimitData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易购物车创建订单信息")
    @allure.severity("blocker")
    def test_drug_unifyorder_confirm_shopping_create (self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例005：统一交易购物车创建订单信息")
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 生成comfrimNo
        UnifyorderConfirmShoppingCreateData = bkw.unifyOrderCenterApi_UnifyorderConfirmShoppingCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "addressId": 103517,
                 "requestNo": timeStamp,
                 "skuNos": [
                     {
                         "id": 14855,
                         "goodsNo": skuNos,
                         "quantity": 1,
                         "channel": channel,
                         "saleMerchantId": 539,
                         "saleStoreId": 74596,
                         "orderSource": 0
                     }
                 ]
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyorderConfirmShoppingCreateData)
        global confirmNo
        confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(UnifyorderConfirmShoppingCreateData, [["data", "confirmNo"]])
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyorderConfirmShoppingCreateData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("获取confirm详情")
    @allure.severity("blocker")
    def test_drug_unifyorder_confirm_detail(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例006：获取confirm详情")

        UnifyorderConfirmDetailData = bkw.unifyOrderCenterApi_UnifyorderConfirmDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "confirmNo": confirmNo
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyorderConfirmDetailData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyorderConfirmDetailData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易查询规则")
    @allure.severity("blocker")
    def test_drug_confirm_userRule_query(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例007：统一交易查询规则")

        UnifyorderConfirmUserRuleQueryData = bkw.unifyOrderCenterApi_UnifyorderConfirmUserRuleQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
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
                 "channel": channel,
                 "goodsList": [
                {
                    "merchantId": 578,
                    "storeId": 4123,
                    "goodsType": 1,
                    "goodsAmount": 20,
                    "goodsNumber": 1,
                    "skuNo": skuNos,
                    "tradeCode": "",
                    "childList": [

                    ]
                }
            ]
        }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyorderConfirmUserRuleQueryData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyorderConfirmUserRuleQueryData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取用户可用权益列表接口")
    @allure.severity("blocker")
    def test_drug_query_multi(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例008：统一交易获取用户可用权益列表接口")

        queryMulti = bkw.unifyOrderCenterApi_UnifyorderqueryMulti(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", queryMulti)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(queryMulti, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易用户优惠券列表查询")
    @allure.severity("blocker")
    def test_drug_member_coupon_query(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例009：统一交易用户优惠券列表查询")

        CouponQueryData = bkw.unifyOrderCenterApi_UnifyorderMemberCouponQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", CouponQueryData)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(CouponQueryData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易校验身份")
    @allure.severity("blocker")
    def test_drug_confirm_userRole_containsIdentity(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例010：统一交易校验身份")

        UserRoleContainsIdentityData = bkw.unifyOrderCenterApi_UnifyorderConfirmUserRoleContainsIdentity(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"identityCode": 60}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", UserRoleContainsIdentityData)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UserRoleContainsIdentityData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易启用药联积分")
    @allure.severity("blocker")
    def test_drug_confirm_userRole_containsIdentity(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例011：统一交易启用药联积分")

        IntegralUseData = bkw.unifyOrderCenterApi_UnifyorderMemberIntegralUse(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", IntegralUseData)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(IntegralUseData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易创建订单接口")
    @allure.severity("blocker")
    def test_drug_order_create(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例012：统一交易创建订单接口")

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
    @allure.severity("blocker")
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
        creditAmount = ckw.CommonKeyWord().Json_GetJsonValue(cashierpayModesData, [["data", "order", "creditAmount"]])
        payAmount = ckw.CommonKeyWord().Json_GetJsonValue(cashierpayModesData, [["data","order", "payAmount"]])

        ckw.CommonKeyWord().Print_ToControl("积分抵扣金额：", creditAmount)

        ckw.CommonKeyWord().Print_ToControl("微信直付：", cashierpayModesData)

        #实物商品价格
        assert creditAmount == "10"
        # #实付价格
        assert payAmount == "10"

    @allure.feature("统一交易创建支付流水")
    @allure.severity("blocker")
    def test_drug_cashier_create(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例013：统一交易创建支付流水")

        cashierCreateData = bkw.unifyOrderCenterApi_UnifyorderCashiercreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"orderNo":orderNo,
                      "payMode":"CWXPAY",
                      "callback":"https://wx.uniondrug.net/dealnj/paySuccess?orderNo=" + orderNo + "&usenow="
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
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例014：统一交易获取交易流水信息")

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
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例015：统一交易支付回调")

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
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例016：统一交易获取子订单")

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
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例018：统一交易仅退款")

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