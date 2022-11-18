import pytest
import allure
import KeyWordDriver.CommonKeyWord as kc
import pytest
import KeyWordDriver.BusinesskeyWord as kb
class Test_OrderTransaction:
    #获取yaml公共信息
    global yamlFile
    global mobile
    global env
    global skuNo
    token = "1"
    # yamlFile = kc.CommonKeyWord.Yaml_ReadNew("/Users/wowo/automan/TestFile/ZhuDengHu/zdh.yaml")
    yamlFile = kc.CommonKeyWord.Yaml_ReadNew("./TestFile/ZhuDengHu/zdh.yaml")
    mobile = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
    env = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
    skuNo = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo")

    #公众号登录
    @allure.feature("获取token统一交易页登录")
    @allure.severity("blocker")
    def test_userLogion(self):
        # 登录获取token-提取token
        global token
        token = kb.theRCPublic_login(mobile, env)
        print(token)
        # 打印token到控制台
        kc.CommonKeyWord().Print_ToControl("token：", token)
        # 打印token到日志
        kc.CommonKeyWord().Print_ToLog("token：", token)
        # 获取替代验证码
        # LogintCaptcha = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "LogintCaptcha")
        # global token
        # kb.authApi_makeLoginCaptcha({"header": {"Content-Type": "application/json"},
        #                              "parma": {},
        #                              "data": {"operate": "set",
        #                                       "key": "verifyCode_valid_13813904992",
        #                                       "data": LogintCaptcha},
        #                              "env": env},
        #                             "dict")
        # # 打印渠道到控制台
        # kc.CommonKeyWord().Print_ToControl("开始打印：", "公众号登陆")
        # # 公众号登录
        # Loginlogin = kb.authApi_LoginLogin({"header": {"Content-Type": "application/json"}, "parma": {},
        #                                     "data": {"mobile": mobile, "code": LogintCaptcha}, "env": env}, "dict")
        # # 打印渠道到控制台
        # kc.CommonKeyWord().Print_ToControl("登陆返回参数：", Loginlogin)
        # # 公众号登录token提取鉴权
        # token = kc.CommonKeyWord().Json_GetJsonValue(Loginlogin, [["data", "token"]])
        # # 读取yaml文件token认证
        # # 打印当前token认证
        # kc.CommonKeyWord().Print_ToControl("token：", token)
        # token = kb.theRCPublic_login(mobile, env)

    @allure.feature("获取统一交易商品信息")
    @allure.severity("blocker")
    def test_getGoodsInfo(self):
        #获取商品详情信息
        goodsInfo =  kb.unifyorderApi_UnifyproductDetails(
            {"header": {}, "parma": {}, "data": {"skuNo": skuNo, "channel": "7", "channelId": 0}, "env": env}, "dict")
        #流水号
        waterNo = kc.CommonKeyWord.Json_GetJsonValue(self,goodsInfo, [["data", "waterNo"]])
        # 打印waterNo到控制台
        kc.CommonKeyWord().Print_ToControl("waterNo：", waterNo)
        # 打印waterNo到日志
        kc.CommonKeyWord().Print_ToLog("waterNo：", waterNo)

    @allure.feature("统一交易创建确认单")
    @allure.severity("blocker")
    def test_createOrderConfirm(self):
        confirmInfo = {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
                 "parma": {},
                 "data": {"skuNos": [skuNo],
	"requestNo": "1648015394657",
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
        # 打印confirmNo到控制台
        kc.CommonKeyWord().Print_ToControl("confirmNo：", confirmNo)
        # 打印confirmNo到日志
        kc.CommonKeyWord().Print_ToLog("confirmNo：", confirmNo)
        queryMulti=kb.unifyorderApi_UnifyorderApi_UnifyorderqueryMulti({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
             "data": {"confirmNo":confirmNo}, "env": env}, "dict")
        # 打印到控制台
        kc.CommonKeyWord().Print_ToControl("queryMulti：", queryMulti)
        # 打印当前comfirm接口返回
        kc.CommonKeyWord().Print_ToLog("queryMulti：", queryMulti)

    @allure.feature("统一交易使用权益卡")
    @allure.severity("blocker")
    def test_changeResource(self):
        resourceId = kc.CommonKeyWord().Yaml_GetByKey(yamlFile, "resourceId")
        # 打印到控制台
        kc.CommonKeyWord().Print_ToControl("resourceId：", resourceId)
        confirmInfo = {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
                       "parma": {},
                       "data": {"skuNos": [skuNo],
                                "requestNo": "1648015394657",
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
        #global confirmNo
        confirmNo = kc.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
        # 打印confirmNo到控制台
        checkOrderRecouce = {
            "header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
            "parma": {},
            "data": {"resourceIdList": [resourceId],
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
                    "confirmNo": confirmNo},
                    "env": env}
        queryResourceId = kb.unifyorderApi_UnifyorderqueryChangeResourceId(checkOrderRecouce, "dict")
        kc.CommonKeyWord().Print_ToControl("资源查询queryResourceId：", queryResourceId)
        kc.CommonKeyWord().Print_ToLog("资源查询queryResourceId：", queryResourceId)
        #创建预订单
        orderData = {
            "header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
            "parma": {},
            "data": {"confirmNo": confirmNo}, "env": env}
        orderData = kb.unifyorderApi_UnifyorderOrdercreate(orderData, "dict")
        kc.CommonKeyWord().Print_ToControl("创建订单信息：", orderData)
        kc.CommonKeyWord().Print_ToLog("创建订单信息", orderData)
        orderNo = kc.CommonKeyWord().Json_GetJsonValue(orderData, [["data", "orderNo"]])
        kc.CommonKeyWord().Print_ToControl("订单号：", orderNo)
        kc.CommonKeyWord().Print_ToLog("订单号", orderNo)
        payModesData = kb.unifyorderApi_UnifyorderPayModes(
        {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": token}, "parma": {},
         "data": {"miniprogram": False,
                  "orderNo": orderNo,
                  "supportAppPay": False
                  }, "env": env}, "dict")
        # 打印到控制台
        kc.CommonKeyWord().Print_ToControl("payModesData：", payModesData)
        kc.CommonKeyWord().Print_ToLog("payModesData：", payModesData)
        #提取价格
        unitPrice = kc.CommonKeyWord().Json_GetJsonValue(payModesData, [["data", "order", "directAmount"]])
        #提取商品数量
        quantity = kc.CommonKeyWord().Json_GetJsonValue(payModesData, [["data", "order", "goodsCount"]])
        # 提取支付结果
        result = kc.CommonKeyWord().Json_GetJsonValue(payModesData, [["success"]])
        # 提取支付结果
        price = kc.CommonKeyWord().Var_NewStr("3.42")
        singlequantity= kc.CommonKeyWord().Var_NewStr("1")
        tmp = kc.CommonKeyWord().Var_NewStr("True")
        # 提取支付结果
        assert kc.CommonKeyWord().Assert_ObjAndObj(str(unitPrice), price)
        assert kc.CommonKeyWord().Assert_ObjAndObj(str(quantity), singlequantity)
        assert kc.CommonKeyWord().Assert_ObjAndObj(str(result), tmp)

if __name__ == '__main__':
   pytest.main(["-vs","test_uniondrug_order.py"])



