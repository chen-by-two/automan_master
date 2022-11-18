# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as ckw
import KeyWordDriver.BusinesskeyWord as bkw

# yamlFile = ckw.CommonKeyWord.Yaml_ReadNew("/Users/wowo/automan/TestFile/ZhuDengHu/zdh.yaml")
yamlFile = ckw.CommonKeyWord.Yaml_ReadNew("./TestFile/ZhuDengHu/zdh.yaml")
# 读取手机号码
mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
# 读取rc环境
env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
# 读取商品skuNos
skuNos = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo4")
# 读取yaml文件渠道
channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "channel")
#获取替代验证码
LogintCaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "LogintCaptcha")
#获取memberId
memberId=ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "memberId")

class Test_unifyOrderintegralPaid:
    @allure.feature("公众号登陆")
    @allure.severity("blocker")
    def test_drug_login(self):
        # 打开yaml文件
        # 造公众号登录验证码
        bkw.authApi_makeLoginCaptcha({"header": {"Content-Type": "application/json"},
                                      "parma": {},
                                      "data": {"operate": "set",
                                               "key": "verifyCode_valid_13813904992",
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
        return token
        ckw.CommonKeyWord().Print_ToControl("token：", token)
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
    @allure.feature("统一交易商品详情页屏蔽分享按钮")
    @allure.severity("blocker")
    def test_drug_confirm_judgeSkuNo(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：","用例2: 统一交易商品详情页屏蔽分享按钮")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易加入购物车")
    @allure.severity("blocker")
    def test_drug_unifycart_cart_add(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例002：统一交易加入购物车")

        UnifycartCartAddData = bkw.unifyOrderCenterApi_UnifycartCartAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                "channel": "7",
                "goodsNo": "171270-1006157343706054656",
                "commonName": "快照签名自动化测试商品\t",
                "quantity": 1,
                "salePrice": 10,
                "ttl": -1,
                "saleType": 2,
                "saleActivityId": None,
                "salerStoreId": "74596",
                "specName": "件"
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifycartCartAddData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifycartCartAddData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易默认地址")
    @allure.severity("blocker")
    def test_drug_unifyAdress_default(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例004：统一交易默认地址")

        UnifyAdressData = bkw.unifyOrderCenterApi_UnifyAddressDefault(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {}, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyAdressData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyAdressData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易购物车查询")
    @allure.severity("blocker")
    def test_drug_unifyCartQuery(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例005：统一交易购车查询")

        UnifyCartQueryData = bkw.unifyOrderCenterApi_UnifyCartQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"longitude":118.779749,"latitude":31.971816,"channel":"7"}, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyCartQueryData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyCartQueryData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易购买限制")
    @allure.severity("blocker")
    def test_drug_unifyproduct_buyLimit(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例006：统一交易购买限制")

        UnifyproductBuyLimitData = bkw.unifyOrderCenterApi_UnifyproductBuyLimit(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "memberId":memberId,"skuNoQries":[{"skuNo":skuNos,"quantity":1}]
             }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyproductBuyLimitData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyproductBuyLimitData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易购物车创建订单信息")
    @allure.severity("blocker")
    def test_drug_unifyorder_confirm_shopping_create (self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例007 ：统一交易购物车创建订单信息")
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 生成comfrimNo
        UnifyorderConfirmShoppingCreateData = bkw.unifyOrderCenterApi_UnifyorderConfirmShoppingCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "addressId": 103486,
                 "requestNo": timeStamp,
                 "skuNos": [{
                     "id": 16369,
                     "goodsNo": skuNos,
                     "quantity": "1",
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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("获取confirm详情")
    @allure.severity("blocker")
    def test_drug_unifyorder_confirm_detail(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例008：获取confirm详情")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易查询规则")
    @allure.severity("blocker")
    def test_drug_confirm_userRule_query(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例009：统一交易查询规则")

        UnifyorderConfirmUserRuleQueryData = bkw.unifyOrderCenterApi_UnifyorderConfirmUserRuleQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
                 "ruleTypes": [2, 3],
                "resources": [{
                    "resourceType": 3,
                    "details": [{
                        "resourceId": "",
                        "resourceValue": "0"
                    }]
                }, {
                    "resourceType": 4,
                    "details": [{
                        "resourceId": "",
                        "resourceValue": "10"
                    }]
                }],
                "totalAmount": 10,
                "channel": 7,
                "goodsList": [{
                    "merchantId": 171270,
                    "storeId": 171272,
                    "goodsType": 1,
                    "goodsAmount": 10,
                    "goodsNumber": 1,
                    "skuNo": skuNos,
                    "tradeCode": "",
                    "childList": []
                }
            ]
        }, "env": env},
            "dict")
        # 打印当前接口返回
        ckw.CommonKeyWord().Print_ToControl("data：", UnifyorderConfirmUserRuleQueryData)
        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UnifyorderConfirmUserRuleQueryData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取用户可用权益列表接口")
    @allure.severity("blocker")
    def test_drug_query_multi(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例010：统一交易获取用户可用权益列表接口")

        queryMulti = bkw.unifyOrderCenterApi_UnifyorderqueryMulti(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", queryMulti)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(queryMulti, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易用户优惠券列表查询")
    @allure.severity("blocker")
    def test_drug_member_coupon_query(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例011：统一交易用户优惠券列表查询")

        CouponQueryData = bkw.unifyOrderCenterApi_UnifyorderMemberCouponQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo": confirmNo}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", CouponQueryData)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(CouponQueryData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易校验身份")
    @allure.severity("blocker")
    def test_drug_confirm_userRole_containsIdentity(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例012：统一交易校验身份")

        UserRoleContainsIdentityData = bkw.unifyOrderCenterApi_UnifyorderConfirmUserRoleContainsIdentity(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"identityCode": 60}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", UserRoleContainsIdentityData)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(UserRoleContainsIdentityData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("订单详情页选择资源")
    @allure.severity("blocker")
    def test_drug_resourceChange(self):
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例013：订单详情页选择资源")
        # 切换使用权益
        resourceChangeData = bkw.unifyorderApi_UnifyorderConfirmResouceChange(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {
                "resourceIdList": ["913b9f2c6f8047518348"],
                "resourceType": 2,
                "balanceTimes": None,
                "oneTimeValue": 0,
                "balanceValue": 50000,
                "discountValue": 9.9,
                "rsourceName": "zdh快照签名专用自动化",
                "resourceDescription": "zdh快照签名专用自动化",
                "resourceCutOffDate": "2025-05-02 23:59:59",
                "nominalValue": 0,
                "type": 5,
                "checked": True,
                "confirmNo": confirmNo
}, "env": env}, "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("data：", resourceChangeData)

        # 提取接口返回errno
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(resourceChangeData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")

        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易创建订单接口")
    @allure.severity("blocker")
    def test_drug_order_create(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例014：统一交易创建订单接口")

        orderCreateData = bkw.unifyOrderCenterApi_UnifyorderOrdercreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
	"miniprogram": False,
	"confirmNo": confirmNo,
	"attachTOS": [{
		"ruleType": 2,
		"ruleId": 68,
		"name": "君子协议7",
		"attachId": 7,
		"url": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/uc2fbb4b53f87d4ba3b999d0088e8d6086.pdf",
		"type": 4
	}, {
		"ruleType": 2,
		"ruleId": 68,
		"name": "lucky专用协议",
		"attachId": 16,
		"url": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/ucc52b786aadea4e2eb59a7bd90f7e0f72.pdf",
		"type": 4
	}, {
		"type": 1,
		"name": "",
		"attachId": "",
		"url": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/uccb5f5b72a7224e31a1b8253a22aca4e4.jpeg",
		"ruleType": "2"
	}, {
		"type": 2,
		"name": "",
		"attachId": "",
		"url": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/ucab06993a5b734472a3843a01add7eef2.jpeg",
		"ruleType": "2"
	}, {
		"type": 3,
		"name": "",
		"attachId": "",
		"url": "https://uniondrug-release.oss-cn-shanghai.aliyuncs.com/dpsp/hl05e5kuqsfkaqlflmupls0nk6.png",
		"ruleType": "2"
	}, {
		"type": 5,
		"name": "",
		"attachId": "",
		"url": "",
		"ruleType": "3"
	}]
}, "env": env},"dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("orderCreateData：", orderCreateData)
        global orderNo
        orderNo = ckw.CommonKeyWord().Json_GetJsonValue(orderCreateData, [["data", "orderNo"]])
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(orderCreateData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易选择支付方式接口")
    @allure.severity("blocker")
    def test_drug_cashier_payModes(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例015：统一交易选择支付方式接口")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)
        #断言字段
        payAmount = ckw.CommonKeyWord().Json_GetJsonValue(cashierpayModesData, [["data","order", "payAmount"]])
        ckw.CommonKeyWord().Print_ToControl("微信直付：", cashierpayModesData)
        # #实付价格
        assert payAmount == "0.1"

    @allure.feature("统一交易创建支付流水")
    @allure.severity("blocker")
    def test_drug_cashier_create(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例016：统一交易创建支付流水")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易获取交易流水信息")
    @allure.severity("blocker")
    def test_drug_cashier_query(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例017：统一交易获取交易流水信息")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易支付回调")
    @allure.severity("blocker")
    def test_drug_notify_payment(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例018：统一交易支付回调")

        NotifyPaymentData = bkw.unifyOrderCenterApi_UnifyorderNotifyPaymentData(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
            "paymentNo": paymentNo,
            "accountId": 12,
            "methodCode": "CWXPAY",
            "openid": "oylyluITvd57Z5b9pu4SgHROHDiQ",
            "tradeType": None,
            "bankType": None,
            "totalFee": "0.01",
            "cashFee": "0.01",
            "transactionId": "4200001584202208086602896410",
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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易主订单查询")
    @allure.severity("blocker")
    def test_drug_orderMainQuery(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例019：统一交易主订单查询")

        orderQueryMainData = bkw.unifyOrderCenterApi_UnifyorderQueryMain(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
	"orderNo": orderNo,
	"includeList": ["attachDOList"]
}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("NotifyPaymentData：", orderQueryMainData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(orderQueryMainData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)

    @allure.feature("统一交易快照附件信息")
    @allure.severity("blocker")
    def test_drug_orderAttach(self):
        # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例020：统一交易快照附件信息")

        orderAttachData = bkw.unifyOrderCenterApi_UnifyorderAttach(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {
	"ruleType": "3",
	"type": "6",
	"orderNo": orderNo,
	"url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/frontend.wx/cftjl9n6gi8sp78319uuks3vab.png"
}, "env": env},
            "dict")
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("NotifyPaymentData：", orderAttachData)
        errno_post = ckw.CommonKeyWord().Json_GetJsonValue(orderAttachData, [["errno"]])
        # 读取yaml错误码
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)


    @allure.feature("统一交易获取子订单号")
    @allure.severity("blocker")
    def test_drug_query_original_main(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例021：统一交易获取子订单")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "errno")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)


    @allure.feature("订单仅退款")
    @allure.severity("blocker")
    def test_drug_order_cancel_sub(self):
            # 打印渠道到控制台
        ckw.CommonKeyWord().Print_ToControl("开始打印：", "用例022：统一交易仅退款")

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
        errno_yaml = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "err")
        assert ckw.CommonKeyWord().Assert_ObjAndObj(errno_yaml, errno_post)