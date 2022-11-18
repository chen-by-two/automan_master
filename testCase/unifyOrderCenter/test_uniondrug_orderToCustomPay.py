import allure
import KeyWordDriver.CommonKeyWord as kc
import pytest
import KeyWordDriver.BusinesskeyWord as kb
@allure.feature("统一交易三方虚拟商品顾客自付下单")
@allure.severity("blocker")
def test_orderSelfPay():
    # yamlFile = kc.CommonKeyWord.Yaml_ReadNew("/Users/wowo/automan/TestFile/ZhuDengHu/zdh.yaml")
    yamlFile = kc.CommonKeyWord.Yaml_ReadNew("./TestFile/ZhuDengHu/zdh.yaml")
    mobile = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
    env = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
    skuNo = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo")
    # 获取替代验证码
    LogintCaptcha = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "LogintCaptcha")
    # 登录获取token-提取token
    # global token
    kb.authApi_makeLoginCaptcha({"header": {"Content-Type": "application/json"},
                                  "parma": {},
                                  "data": {"operate": "set",
                                           "key": "verifyCode_valid_13813904992",
                                           "data": LogintCaptcha},
                                  "env": env},
                                 "dict")
    # 打印渠道到控制台
    kc.CommonKeyWord().Print_ToControl("开始打印：", "公众号登陆")
    # 公众号登录
    Loginlogin = kb.authApi_LoginLogin({"header": {"Content-Type": "application/json"}, "parma": {},
                                         "data": {"mobile": mobile, "code": LogintCaptcha}, "env": env}, "dict")
    # 打印渠道到控制台
    kc.CommonKeyWord().Print_ToControl("登陆返回参数：", Loginlogin)
    # 公众号登录token提取鉴权
    token = kc.CommonKeyWord().Json_GetJsonValue(Loginlogin, [["data", "token"]])
    # 读取yaml文件token认证
    # 打印当前token认证
    kc.CommonKeyWord().Print_ToControl("token：", token)
    # token = kb.theRCPublic_login(mobile, env)
    # 获取时间戳
    timeStamp = kc.CommonKeyWord().Time_UnixTimestamp()
    confirmInfo = {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
                   "parma": {},
                   "data": {"skuNos": [skuNo],
                            "requestNo": timeStamp,
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
                            "showInsuredMember": None}, "env": env}
    # 创建确认单获取confirmNo-调取接口
    confCre = kb.unifyorderApi_UnifyorderConfirmCreateNew(confirmInfo, "dict")
    # 创建确认单获取confirmNo-提取confirmNo
    confirmNo = kc.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
    # 创建预订单
    orderData = {
        "header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
        "parma": {},
        "data": {"confirmNo": confirmNo}, "env": env}
    orderData = kb.unifyorderApi_UnifyorderOrdercreate(orderData, "dict")
    # 打印waterNo到控制台
    kc.CommonKeyWord().Print_ToControl("orderData：", orderData)
    # 打印waterNo到日志
    kc.CommonKeyWord().Print_ToLog("orderData：", orderData)
    # 提取主订单号
    mainOrderNo = kc.CommonKeyWord().Json_GetJsonValue(orderData, [["data", "orderNo"]])
    # 打印waterNo到控制台
    kc.CommonKeyWord().Print_ToControl("mainOrderNo：", mainOrderNo)
    # 打印waterNo到日志
    kc.CommonKeyWord().Print_ToLog("mainOrderNo：", mainOrderNo)
    # 创建微信支付接口
    kb.unifyorderApi_UnifyorderRcCashierCreate(
        {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
         "parma": {}, "data": {"orderNo": mainOrderNo, "payMode": "CWXPAY"}, "env": env}, "dict")
    # 获取支付单号和支付流水号
    paymentInfo = kb.unifyorderApi_UnifyorderRcPaymentNo(
        {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
         "parma": {}, "data": {"outTradeNo": mainOrderNo, "status": 0}, "env": env}, "dict")
    # 打印waterNo到日志
    kc.CommonKeyWord().Print_ToControl("paymentInfo",paymentInfo)
    #获取paymentBody
    paymentData = kc.CommonKeyWord().Json_GetJsonValue(paymentInfo, [["data","body"]])
    #获取paymentNo
    paymentNo=kc.CommonKeyWord().Json_GetJsonValue(paymentData[0],[["paymentNo"]])
    #获取支付流水号
    tradeNo = kc.CommonKeyWord().Json_GetJsonValue(paymentData[0],[["tradeNo"]])
    # 打印waterNo到控制台
    kc.CommonKeyWord().Print_ToControl("paymentNo：", paymentNo)
    # 打印waterNo到控制台
    kc.CommonKeyWord().Print_ToControl("tradeNo：", tradeNo)
    #三方支付回调
    notifyResult =kb.unifyOrderCenterApi_UnifyorderNotifyPaymentData(
        {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
         "parma": {}, "data": { "paymentNo":paymentNo,
            "accountId":12,
            "methodCode":"CWXPAY",
            "openid":"oRGmzs_tx73KsiBRL9gcXMbsa8do",
            "tradeType":None,
            "bankType":None,
            "totalFee":"0.01",
            "cashFee":"0.01",
            "transactionId":"220418124017114248",
            "outTradeNo":tradeNo,
            "timeEnd":"2022-04-18 15:13:47",
            "refundId":None,
            "outRefundNo":None,
            "tradeStatus":None,
            "refundAmount":None,
            "gmtRefund":None,
            "paymentType":"PD",
            "traceNo":None
            }, "env": env},
            "dict")
    # 打印到控制台
    kc.CommonKeyWord().Print_ToControl("notifyResult：", notifyResult)
    # 提取支付结果
    result = kc.CommonKeyWord().Json_GetJsonValue(notifyResult, [["success"]])
    # 提取支付结果
    tmp = kc.CommonKeyWord().Var_NewStr("True")
    # 提取支付结果
    assert kc.CommonKeyWord().Assert_ObjAndObj(str(result), tmp)
    # 校验支付结果
    checkRes = kb.unifyorderApi_UnifyorderRcCashierCheck(
        {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
         "parma": {}, "data": {"first": False, "orderNo": mainOrderNo}, "env": env}, "dict")
    # 提取支付结果
    result = kc.CommonKeyWord().Json_GetJsonValue(checkRes, [["success"]])
    # 提取支付结果
    tmp = kc.CommonKeyWord().Var_NewStr("True")
    # 提取支付结果
    assert kc.CommonKeyWord().Assert_ObjAndObj(str(result), tmp)

if __name__ == '__main__':
   pytest.main(["-vs","test_uniondrug_orderToCustomPay.py"])
