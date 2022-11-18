# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

token = "1"


class Test_Unify:

    @allure.feature("统一交易页登录")
    @allure.severity("blocker")
    def test_unifyLogin(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取yaml里手机号
        mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 登录获取token-提取token
        global token
        token = bkw.thePublic_login(mobile,env)
        # 打印token到控制台
        ckw.CommonKeyWord().Print_ToControl("token：", token)
        # 打印token到日志
        ckw.CommonKeyWord().Print_ToLog("token：", token)

    @allure.feature("统一交易页获取商品信息")
    @allure.severity("blocker")
    def test_unifyGetProductInfo(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo1")
        # 商品详情页获取waterNo-调取接口
        prdDetRes = bkw.unifyorderApi_UnifyproductDetails(
            {"header": {}, "parma": {}, "data": {"skuNo": skuNo, "channel": "8", "channelId": 0}, "env": env}, "dict")
        # 商品详情页获取waterNo-提取waterNo
        waterNo = ckw.CommonKeyWord().Json_GetJsonValue(prdDetRes, [["data", "waterNo"]])
        # 打印waterNo到控制台
        ckw.CommonKeyWord().Print_ToControl("waterNo：", waterNo)
        # 打印waterNo到日志
        ckw.CommonKeyWord().Print_ToLog("waterNo：", waterNo)

    @allure.feature("统一交易创建确认单")
    @allure.severity("blocker")
    def test_UnifyCreateConfirm(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取yaml里手机号
        mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo1")
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 创建确认单获取confirmNo-调取接口
        confCre = bkw.unifyorderApi_UnifyorderConfirmCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"skuNos": [skuNo], "requestNo": timeStamp, "channel": "7", "saleMerchantId": "539",
                                   "saleStoreId": "74596", "assistantId": 0, "shareMemberId": 0, "commissionNo": "",
                                   "partnerMerchantId": 131389, "partnerOpenId": "81091692a7c9c85dd987c161f05e",
                                   "channelId": "0", "orderSource": 0}, "env": env}, "dict")
        # 创建确认单获取confirmNo-提取confirmNo
        confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
        # 打印confirmNo到控制台
        ckw.CommonKeyWord().Print_ToControl("confirmNo：", confirmNo)
        # 打印confirmNo到日志
        ckw.CommonKeyWord().Print_ToLog("confirmNo：", confirmNo)

    @allure.feature("统一交易获取权益")
    @allure.severity("blocker")
    def test_UnifyGetEquity(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo1")
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 创建确认单获取confirmNo-调取接口
        confCre = bkw.unifyorderApi_UnifyorderConfirmCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"skuNos": [skuNo], "requestNo": timeStamp, "channel": "7", "saleMerchantId": "539",
                                   "saleStoreId": "74596", "assistantId": 0, "shareMemberId": 0, "commissionNo": "",
                                   "partnerMerchantId": 131389, "partnerOpenId": "81091692a7c9c85dd987c161f05e",
                                   "channelId": "0", "orderSource": 0}, "env": env}, "dict")
        # 创建确认单获取confirmNo-提取confirmNo
        confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
        # 打印confirmNo到控制台
        ckw.CommonKeyWord().Print_ToControl("confirmNo：", confirmNo)
        # 打印confirmNo到日志
        ckw.CommonKeyWord().Print_ToLog("confirmNo：", confirmNo)
        # 获取可用权益-调取接口
        mebEquQue = bkw.unifyorderApi_UnifyorderMemberResourceQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")

    @allure.feature("统一交易权益下单")
    @allure.severity("blocker")
    def buganle_UnifyBuyProductByEquity(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo1")
        # 读取yaml里equityNo
        rsourceId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "rsourceId_equity")
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 创建确认单获取confirmNo-调取接口
        confCre = bkw.unifyorderApi_UnifyorderConfirmCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"skuNos": [skuNo], "requestNo": timeStamp, "channel": "7", "saleMerchantId": "539",
                                   "saleStoreId": "74596", "assistantId": 0, "shareMemberId": 0, "commissionNo": "",
                                   "partnerMerchantId": 131389, "partnerOpenId": "81091692a7c9c85dd987c161f05e",
                                   "channelId": "0", "orderSource": 0}, "env": env}, "dict")
        # 创建确认单获取confirmNo-提取confirmNo
        confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
        # 打印confirmNo到控制台
        ckw.CommonKeyWord().Print_ToControl("confirmNo：", confirmNo)
        # 打印confirmNo到日志
        ckw.CommonKeyWord().Print_ToLog("confirmNo：", confirmNo)
        # 获取可用权益-调取接口
        mebEquQue = bkw.unifyorderApi_UnifyorderMemberResourceQuery(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")
        # 获取可用权益-提取可用权益
        canUseEquity = ckw.CommonKeyWord().Json_GetJsonValue(mebEquQue, [["data", "canUseds"]])
        # 指定权益卡
        equityCard = bkw.getRsourceInfo_byCardNo(canUseEquity, rsourceId)
        # 打印权益卡到控制台
        ckw.CommonKeyWord().Print_ToControl("权益卡：", equityCard)
        # 打印权益卡到日志
        ckw.CommonKeyWord().Print_ToLog("权益卡：", equityCard)
        # 给权益卡增加confirmNo
        chgEqu = ckw.CommonKeyWord().Dict_ModifyByKey(equityCard, "confirmNo", confirmNo)
        ckw.CommonKeyWord().Print_ToLog(chgEqu)
        # 切换使用权益
        confEquChg = bkw.unifyorderApi_UnifyorderConfirmResouceChange(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": chgEqu, "env": env}, "dict")
        # 创建订单
        createRes = bkw.unifyorderApi_UnifyorderOrderCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")
        # 提取主订单号
        mainOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(createRes, [["data", "shipment", "mainOrderNo"]])
        # 支付
        bkw.orderCenterApi_UnifyorderCashierCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo, "payMode": "CWXPAY"}, "env": env}, "dict")
        # 检查支付结果
        checkRes = bkw.unifyorderApi_UnifyorderCashierCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"first": False, "orderNo": mainOrderNo}, "env": env}, "dict")
        # 提取支付结果
        result = ckw.CommonKeyWord().Json_GetJsonValue(checkRes, [["success"]])
        # 提取支付结果
        tmp = ckw.CommonKeyWord().Var_NewStr("True")
        # 提取支付结果
        assert ckw.CommonKeyWord().Assert_ObjAndObj(str(result), tmp)

    @allure.feature("统一交易积分下单")
    @allure.severity("blocker")
    def test_UnifyBuyProductByIntegral(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo_Allintegral")
        # 获取时间戳
        timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
        # 等一秒
        ckw.CommonKeyWord().Time_Sleep("1.0")
        # 创建确认单获取confirmNo-调取接口
        confCre = bkw.unifyorderApi_UnifyorderConfirmCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {},
             "data": {"skuNos": [skuNo], "requestNo": timeStamp, "channel": "7", "saleMerchantId": "539",
                      "saleStoreId": "74596", "assistantId": 0, "shareMemberId": 0, "commissionNo": "",
                      "partnerMerchantId": 131389, "partnerOpenId": "81091692a7c9c85dd987c161f05e",
                      "channelId": "0", "orderSource": 0}, "env": env}, "dict")
        # 创建确认单获取confirmNo-提取confirmNo
        confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
        # 打印confirmNo到控制台
        ckw.CommonKeyWord().Print_ToControl("confirmNo：", confirmNo)
        # 打印confirmNo到日志
        ckw.CommonKeyWord().Print_ToLog("confirmNo：", confirmNo)

        # 使用积分
        bkw.unifyorderApi_UnifyorderMemberIntegralUse(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")
        # 创建订单
        createRes = bkw.unifyorderApi_UnifyorderOrderCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")
        # 提取主订单号
        mainOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(createRes, [["data", "shipment", "mainOrderNo"]])
        # 支付
        bkw.orderCenterApi_UnifyorderCashierCreate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo, "payMode": "CWXPAY"}, "env": env}, "dict")
        # 检查支付结果
        checkRes = bkw.unifyorderApi_UnifyorderCashierCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"first": False, "orderNo": mainOrderNo}, "env": env}, "dict")
        # 提取支付结果
        result = ckw.CommonKeyWord().Json_GetJsonValue(checkRes, [["success"]])
        # 提取支付结果
        tmp = ckw.CommonKeyWord().Var_NewStr("True")
        # 提取支付结果
        assert ckw.CommonKeyWord().Assert_ObjAndObj(str(result), tmp)
    # @allure.feature("统一交易积分+营销卡下单")
    # @allure.severity("blocker")
    # def test_UnifyBuyProductByIntegralAndCard(self):
    #     # 读取yaml文件
    #     yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
    #     # 读取yaml里手机号
    #     mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
    #     # 读取Yaml执行环节
    #     env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
    #     # 读取yaml里skuNo
    #     skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo_integralandcard")
    #     cardProjectId = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "cardProject53")
    #     BACKTOKEN = bkw.adminBackend_login(mobile, env)
    #     # 打印backToken到控制台
    #     ckw.CommonKeyWord().Print_ToControl("backToken：", BACKTOKEN)
    #     # 打印confirmNo到日志
    #     ckw.CommonKeyWord().Print_ToLog("backToken：", BACKTOKEN)
    #     # 发卡
    #     bkw.customerCenterApi_PromoteSendcard({"header": {"Content-Type": "application/json;charset=UTF-8",
    #                                                       "Authorization": "Bearer " + BACKTOKEN}, "parma": {},
    #                                           "data": {"memberId": "15965017",
    #                                                     "schemeId": str(cardProjectId), "cardNum": 1},
    #                                           "env": env}, "dict")
    #     # 查卡

    #     cardRes = bkw.customerCenterApi_PromoteCardlist({"header": {"Content-Type": "application/json;charset=UTF-8",
    #                                                                 "Authorization": "Bearer " + BACKTOKEN},
    #                                                      "parma": {},
    #                                                      "data": {"page": 1, "limit": 10, "equityStatus": [],
    #                                                               "status": "1", "memberId": "15965017"},
    #                                                      "env": env}, "dict")
    #     # 提取刚发的卡
    #     cardlist = ckw.jsonTools.getJsonValue(cardRes, [["data", "body"]])
    #     cardId = ckw.jsonTools.getJsonValue(cardlist[0], [["cardId"]])

    #     ckw.CommonKeyWord().Print_ToLog("cardId：", cardId)

    #     # 获取时间戳
    #     timeStamp = ckw.CommonKeyWord().Time_UnixTimestamp()
    #     # 等一秒
    #     ckw.CommonKeyWord().Time_Sleep("1.0")
    #     # 创建确认单获取confirmNo-调取接口
    #     confCre = bkw.unifyorderApi_UnifyorderConfirmCreate(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {},
    #          "data": {"skuNos": [skuNo], "requestNo": timeStamp, "channel": "7", "saleMerchantId": "539",
    #                   "saleStoreId": "74596", "assistantId": 0, "shareMemberId": 0, "commissionNo": "",
    #                   "partnerMerchantId": 131389, "partnerOpenId": "81091692a7c9c85dd987c161f05e",
    #                   "channelId": "0", "orderSource": 0}, "env": env}, "dict")
    #     # 创建确认单获取confirmNo-提取confirmNo
    #     confirmNo = ckw.CommonKeyWord().Json_GetJsonValue(confCre, [["data", "confirmNo"]])
    #     # 打印confirmNo到控制台
    #     ckw.CommonKeyWord().Print_ToControl("confirmNo：", confirmNo)
    #     # 打印confirmNo到日志
    #     ckw.CommonKeyWord().Print_ToLog("confirmNo：", confirmNo)

    #     # 获取可用资源-调取接口
    #     mebEquQue = bkw.unifyorderApi_UnifyorderMemberResourceQuery(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")
    #     # 获取可用资源-提取可用
    #     canUseEquity = ckw.CommonKeyWord().Json_GetJsonValue(mebEquQue, [["data", "canUseds"]])

    #     # 指定营销卡
    #     card = bkw.getRsourceInfo_byCardNo(canUseEquity, cardId)
    #     # 打印营销卡到控制台
    #     ckw.CommonKeyWord().Print_ToControl("权益卡：", card)
    #     # 打印营销卡到日志
    #     ckw.CommonKeyWord().Print_ToLog("权益卡：", card)
    #     # 给营销卡增加confirmNo
    #     chgCard = ckw.CommonKeyWord().Dict_ModifyByKey(card, "confirmNo", confirmNo)
    #     ckw.CommonKeyWord().Print_ToLog(chgCard)
    #     # 切换使用权益
    #     confCardChg = bkw.unifyorderApi_UnifyorderConfirmResouceChange(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {}, "data": chgCard, "env": env}, "dict")
    #     # 使用积分
    #     bkw.unifyorderApi_UnifyorderMemberIntegralUse(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")

    #     # 创建订单
    #     createRes = bkw.unifyorderApi_UnifyorderOrderCreate(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {}, "data": {"confirmNo": confirmNo}, "env": env}, "dict")
    #     # 提取主订单号
    #     mainOrderNo = ckw.CommonKeyWord().Json_GetJsonValue(createRes, [["data", "shipment", "mainOrderNo"]])
    #     # 支付
    #     bkw.orderCenterApi_UnifyorderCashierCreate(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {}, "data": {"orderNo": mainOrderNo, "payMode": "CWXPAY"}, "env": env}, "dict")
    #     # 检查支付结果
    #     checkRes = bkw.unifyorderApi_UnifyorderCashierCheck(
    #         {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
    #          "parma": {}, "data": {"first": False, "orderNo": mainOrderNo}, "env": env}, "dict")
    #     # 提取支付结果
    #     result = ckw.CommonKeyWord().Json_GetJsonValue(checkRes, [["success"]])
    #     # 提取支付结果
    #     tmp = ckw.CommonKeyWord().Var_NewStr("True")
    #     # 提取支付结果
    #     # assert ckw.CommonKeyWord().Assert_ObjAndObj(str(result), tmp)


    @allure.feature("统一交易校验增值服务组包商品原价")
    @allure.severity("blocker")
    def test_unifyGetProductOriginPrice(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read("C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo_packageService")
        # 商品详情页获取waterNo-调取接口
        prdDetRes = bkw.unifyorderApi_UnifyproductDetails(
            {"header": {}, "parma": {}, "data": {"skuNo": skuNo, "channel": "8", "channelId": 0}, "env": env}, "dict")
        # 提取原价
        originPrice = ckw.CommonKeyWord().Json_GetJsonValue(prdDetRes, [["data", "originPrice"]])
        assert originPrice == 3

    @allure.feature("统一交易校验增值服务组包商品销售价")
    @allure.severity("blocker")
    def test_unifyGetProductSalePrice(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read("C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo_packageService")
        # 商品详情页获取waterNo-调取接口
        prdDetRes = bkw.unifyorderApi_UnifyproductDetails(
            {"header": {}, "parma": {}, "data": {"skuNo": skuNo, "channel": "8", "channelId": 0}, "env": env}, "dict")
        # 提取销售价
        salePrice = ckw.CommonKeyWord().Json_GetJsonValue(prdDetRes, [["data", "salePrice"]])
        assert salePrice == 6

    @allure.feature("统一交易校验增值服务组包商品子商品数量")
    @allure.severity("blocker")
    def test_unifyGetProductNum(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo_packageService")
        # 商品详情页获取waterNo-调取接口
        prdDetRes = bkw.unifyorderApi_UnifyproductDetails(
            {"header": {}, "parma": {}, "data": {"skuNo": skuNo, "channel": "8", "channelId": 0}, "env": env}, "dict")
        # 提取组包商品内子商品
        productServiceList = ckw.CommonKeyWord().Json_GetJsonValue(prdDetRes, [["data", "productServiceList"]])

        assert productServiceList.__len__() == 3

    @allure.feature("统一交易校验增值服务组包商品子商品原价")
    @allure.severity("blocker")
    def test_unifyGetProductChildPrice(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取yaml里skuNo
        skuNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "skuNo_packageService")
        # 商品详情页获取waterNo-调取接口
        prdDetRes = bkw.unifyorderApi_UnifyproductDetails(
            {"header": {}, "parma": {}, "data": {"skuNo": skuNo, "channel": "8", "channelId": 0}, "env": env}, "dict")
        # 提取组包商品内子商品
        productServiceList = ckw.CommonKeyWord().Json_GetJsonValue(prdDetRes, [["data", "productServiceList"]])
        res = True
        for p in productServiceList:
            price = ckw.CommonKeyWord().Json_GetJsonValue(p, [["price"]])
            ckw.CommonKeyWord().Print_ToLog(
                "skuNo:" + ckw.CommonKeyWord().Json_GetJsonValue(p, [["skuNo"]]) + "\tprice:" + str(price))
            if price != 2:
                res = False
                break
        assert res

    @allure.feature("统一交易校验历史订单详情校验使用的营销卡金额")
    @allure.severity("blocker")
    def test_unifyCheckOrderDetilCouponAmount(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取订单号
        mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mainOrderNo")
        #
        oo = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjE3NDIsInd4T3BlbmlkIjoib2YtRlh3Ny15eVhZU2JtaFhlZXowQkNWa3d1dyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjE3NDIiLCJ2YWx1ZSI6IjkifSwiaW5mbyI6eyJuYW1lIjoiXHU1MjE4XHU2NjBhXHU3MTM2IiwibW9iaWxlIjoiMTUwMDUxNTAwMjMifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.E6l5QhMaRlCVE0n2Ruq6b52vSIQat1tDub5ks308T0dbtaeWxKtny1JRbWtd8kcquFr-Bf3_wA4Wdr_MW2BoQUq3X_1VGUVVfyRZGWwlzvI70X5NK60UQxz6u1wi75FhuGpMdp3lktDxrGX1-tfJsNWpXIO8_kAQSyRtiXd-4vCPQkrqoh30HD3p881TYMU4qyHi6_FxuE9_CV1mQ0q5TtVfBW_znOi1dQb_l0EW4wDis6skEBCacnTSW0qZbeF8i92XBEr80M6Y9vw7L7mKAMrZIwXayo164cvBv32P19tieSdYhrFLmspIaAnKW_4lze0wjO81hgL_lJta3qYZ7A"
        orderDetil = bkw.unifyorderApi_UnifyorderOrderDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo}, "env": env}, "dict")
        couponAmount = ckw.CommonKeyWord().Json_GetJsonValue(orderDetil,[["data","couponAmount"]])
        assert True

    @allure.feature("统一交易校验历史订单详情校验使用的营销卡金额")
    @allure.severity("blocker")
    def test_unifyCheckOrderDetilCouponAmount(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取订单号
        mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mainOrderNo")
        #
        oo = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjE3NDIsInd4T3BlbmlkIjoib2YtRlh3Ny15eVhZU2JtaFhlZXowQkNWa3d1dyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjE3NDIiLCJ2YWx1ZSI6IjkifSwiaW5mbyI6eyJuYW1lIjoiXHU1MjE4XHU2NjBhXHU3MTM2IiwibW9iaWxlIjoiMTUwMDUxNTAwMjMifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.E6l5QhMaRlCVE0n2Ruq6b52vSIQat1tDub5ks308T0dbtaeWxKtny1JRbWtd8kcquFr-Bf3_wA4Wdr_MW2BoQUq3X_1VGUVVfyRZGWwlzvI70X5NK60UQxz6u1wi75FhuGpMdp3lktDxrGX1-tfJsNWpXIO8_kAQSyRtiXd-4vCPQkrqoh30HD3p881TYMU4qyHi6_FxuE9_CV1mQ0q5TtVfBW_znOi1dQb_l0EW4wDis6skEBCacnTSW0qZbeF8i92XBEr80M6Y9vw7L7mKAMrZIwXayo164cvBv32P19tieSdYhrFLmspIaAnKW_4lze0wjO81hgL_lJta3qYZ7A"
        orderDetil = bkw.unifyorderApi_UnifyorderOrderDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo}, "env": env}, "dict")
        couponAmount = ckw.CommonKeyWord().Json_GetJsonValue(orderDetil, [["data","couponAmount"]])
        assert True

    @allure.feature("统一交易校验历史订单详情校验使用的积分金额")
    @allure.severity("blocker")
    def test_unifyCheckOrderDetilCreditAmount(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取订单号
        mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mainOrderNo")
        #
        oo = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjE3NDIsInd4T3BlbmlkIjoib2YtRlh3Ny15eVhZU2JtaFhlZXowQkNWa3d1dyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjE3NDIiLCJ2YWx1ZSI6IjkifSwiaW5mbyI6eyJuYW1lIjoiXHU1MjE4XHU2NjBhXHU3MTM2IiwibW9iaWxlIjoiMTUwMDUxNTAwMjMifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.E6l5QhMaRlCVE0n2Ruq6b52vSIQat1tDub5ks308T0dbtaeWxKtny1JRbWtd8kcquFr-Bf3_wA4Wdr_MW2BoQUq3X_1VGUVVfyRZGWwlzvI70X5NK60UQxz6u1wi75FhuGpMdp3lktDxrGX1-tfJsNWpXIO8_kAQSyRtiXd-4vCPQkrqoh30HD3p881TYMU4qyHi6_FxuE9_CV1mQ0q5TtVfBW_znOi1dQb_l0EW4wDis6skEBCacnTSW0qZbeF8i92XBEr80M6Y9vw7L7mKAMrZIwXayo164cvBv32P19tieSdYhrFLmspIaAnKW_4lze0wjO81hgL_lJta3qYZ7A"
        orderDetil = bkw.unifyorderApi_UnifyorderOrderDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo}, "env": env}, "dict")
        creditAmount = ckw.CommonKeyWord().Json_GetJsonValue(orderDetil, [["data", "creditAmount"]])
        assert creditAmount == "12"

    @allure.feature("统一交易校验历史订单详情校验使用的自付金额")
    @allure.severity("blocker")
    def test_unifyCheckOrderDetilPayAmount(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取订单号
        mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mainOrderNo")
        #
        oo = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjE3NDIsInd4T3BlbmlkIjoib2YtRlh3Ny15eVhZU2JtaFhlZXowQkNWa3d1dyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjE3NDIiLCJ2YWx1ZSI6IjkifSwiaW5mbyI6eyJuYW1lIjoiXHU1MjE4XHU2NjBhXHU3MTM2IiwibW9iaWxlIjoiMTUwMDUxNTAwMjMifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.E6l5QhMaRlCVE0n2Ruq6b52vSIQat1tDub5ks308T0dbtaeWxKtny1JRbWtd8kcquFr-Bf3_wA4Wdr_MW2BoQUq3X_1VGUVVfyRZGWwlzvI70X5NK60UQxz6u1wi75FhuGpMdp3lktDxrGX1-tfJsNWpXIO8_kAQSyRtiXd-4vCPQkrqoh30HD3p881TYMU4qyHi6_FxuE9_CV1mQ0q5TtVfBW_znOi1dQb_l0EW4wDis6skEBCacnTSW0qZbeF8i92XBEr80M6Y9vw7L7mKAMrZIwXayo164cvBv32P19tieSdYhrFLmspIaAnKW_4lze0wjO81hgL_lJta3qYZ7A"
        orderDetil = bkw.unifyorderApi_UnifyorderOrderDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo}, "env": env}, "dict")
        payAmount = ckw.CommonKeyWord().Json_GetJsonValue(orderDetil, [["data", "payAmount"]])
        assert payAmount == "96"

    @allure.feature("统一交易校验历史订单详情校验原价")
    @allure.severity("blocker")
    def test_unifyCheckOrderDetilUnitPrice(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取订单号
        mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mainOrderNo")
        #
        oo = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjE3NDIsInd4T3BlbmlkIjoib2YtRlh3Ny15eVhZU2JtaFhlZXowQkNWa3d1dyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjE3NDIiLCJ2YWx1ZSI6IjkifSwiaW5mbyI6eyJuYW1lIjoiXHU1MjE4XHU2NjBhXHU3MTM2IiwibW9iaWxlIjoiMTUwMDUxNTAwMjMifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.E6l5QhMaRlCVE0n2Ruq6b52vSIQat1tDub5ks308T0dbtaeWxKtny1JRbWtd8kcquFr-Bf3_wA4Wdr_MW2BoQUq3X_1VGUVVfyRZGWwlzvI70X5NK60UQxz6u1wi75FhuGpMdp3lktDxrGX1-tfJsNWpXIO8_kAQSyRtiXd-4vCPQkrqoh30HD3p881TYMU4qyHi6_FxuE9_CV1mQ0q5TtVfBW_znOi1dQb_l0EW4wDis6skEBCacnTSW0qZbeF8i92XBEr80M6Y9vw7L7mKAMrZIwXayo164cvBv32P19tieSdYhrFLmspIaAnKW_4lze0wjO81hgL_lJta3qYZ7A"
        orderDetil = bkw.unifyorderApi_UnifyorderOrderDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo}, "env": env}, "dict")
        unitPrice = ckw.CommonKeyWord().Json_GetJsonValue(orderDetil, [["data", "items",]])
        unitPrice = ckw.CommonKeyWord().Json_GetJsonValue(unitPrice[0],[["unitPrice"]])
        assert unitPrice == 111

    @allure.feature("统一交易校验历史订单详情校验收货人姓名")
    @allure.severity("blocker")
    def test_unifyCheckOrderDetilRecipientName(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # yamlFile = ckw.CommonKeyWord().Yaml_Read(
        #     "C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 读取订单号
        mainOrderNo = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mainOrderNo")
        #
        # oo = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjE3NDIsInd4T3BlbmlkIjoib2YtRlh3Ny15eVhZU2JtaFhlZXowQkNWa3d1dyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjE3NDIiLCJ2YWx1ZSI6IjkifSwiaW5mbyI6eyJuYW1lIjoiXHU1MjE4XHU2NjBhXHU3MTM2IiwibW9iaWxlIjoiMTUwMDUxNTAwMjMifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.E6l5QhMaRlCVE0n2Ruq6b52vSIQat1tDub5ks308T0dbtaeWxKtny1JRbWtd8kcquFr-Bf3_wA4Wdr_MW2BoQUq3X_1VGUVVfyRZGWwlzvI70X5NK60UQxz6u1wi75FhuGpMdp3lktDxrGX1-tfJsNWpXIO8_kAQSyRtiXd-4vCPQkrqoh30HD3p881TYMU4qyHi6_FxuE9_CV1mQ0q5TtVfBW_znOi1dQb_l0EW4wDis6skEBCacnTSW0qZbeF8i92XBEr80M6Y9vw7L7mKAMrZIwXayo164cvBv32P19tieSdYhrFLmspIaAnKW_4lze0wjO81hgL_lJta3qYZ7A"
        orderDetil = bkw.unifyorderApi_UnifyorderOrderDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
             "parma": {}, "data": {"orderNo": mainOrderNo}, "env": env}, "dict")
        recipientName = ckw.CommonKeyWord().Json_GetJsonValue(orderDetil, [["data", "shipment","recipientName"]])
        assert recipientName == "刘昊然"
if __name__ == '__main__':
    pytest.main(["TestFile/HaoRanOnly/lhrtest.yaml","-s"])