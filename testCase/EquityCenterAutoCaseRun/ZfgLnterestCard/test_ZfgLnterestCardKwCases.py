# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

Authorization_1 = "1"
token_2 = "2"


class Test_ZfgLnterestCard:

    @allure.feature("权益中心-非合并次卡领取激活-电子码领取方式-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0001(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml后台登录手机号
        mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobile")
        # 读取yaml初始化后台登录验证码
        UTsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateLoginCaptchaAll")
        # 打印sql到日志
        ckw.CommonKeyWord().Print_ToLog("sql:", UTsql)
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # Utsql执行
        UpdateCaptcha = ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", UTsql)
        # 打印修改结果到日志
        ckw.CommonKeyWord().Print_ToLog("SQL修改结果:", UpdateCaptcha)
        # 读取yaml修改后台登录验证码
        Upsql = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "updateLoginCaptcha")
        # 打印修改SQL到日志
        ckw.CommonKeyWord().Print_ToLog("修改后台登录验证码SQL：", Upsql)
        # 修改后台验证码SQL执行
        updatesql = ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_ALL", Upsql)
        # 打印后台验证码修改结果到日志
        ckw.CommonKeyWord().Print_ToLog("SQL修改结果:", updatesql)
        # 读取yaml后台登录验证码
        logincaptcha = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "LoginCaptcha")
        # 打印后台登录验证码到日志
        ckw.CommonKeyWord().Print_ToLog("后台登录验证码：", logincaptcha)
        # 运营中心后台登录获取token
        ddmodbilelogin = bkw.authApi_DdMobilelogin(
            {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
             "data": {"mobile": mobile, "code": logincaptcha}, "env": envt}, "dict")
        # 运营中心后台登录token提取
        token_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddmodbilelogin, [["data"]])
        # 运营中心后台登录token提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心后台登录token:", token_1)
        # 运营中心获取Authorization
        ddlogin = bkw.authApi_Ddlogin(
            {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": token_1, "env": envt},
            "dict")
        # 运营中心Authorization提取
        global Authorization_1
        Authorization_1 = ckw.CommonKeyWord().Json_GetJsonValue(ddlogin, [["data", "token"]])
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_1")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_1, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "3", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 读取yaml公众号登录验证码
        LogintCaptchas_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "LogintCaptchas")
        # 打印公众号登录验证到日志
        ckw.CommonKeyWord().Print_ToLog(LogintCaptchas_1)
        # 造公众号登录验证码
        ckw.CommonKeyWord().Db_ConfRedisSet("test_redis", "verifyCode_valid_18923425589", LogintCaptchas_1)
        # 公众号登录
        Loginlogin = bkw.authApi_LoginLogin({"header": {"Content-Type": "application/json"}, "parma": {},
                                             "data": {"mobile": mobiles, "code": LogintCaptchas_1}, "env": envt},
                                            "dict")
        # 提取公众号token
        global token_2
        token_2 = ckw.CommonKeyWord().Json_GetJsonValue(Loginlogin, [["data", "token"]])
        # 打印提取公众号token到日志
        ckw.CommonKeyWord().Print_ToLog("公众号token:", token_2)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_1")
        # 电子码领取权益提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 权益次卡领取信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 权益次卡领取激活
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 电子码重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-雇主清单领取方式-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0002(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_2")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": "陈星", "mobile": mobiles, "verifyName": "陈星",
                                   "verifyMobile": mobiles, "verifyIdCard": "110101199003079139",
                                   "verifyKeyword1": None, "verifyKeyword2": None, "verifyKeyword3": None,
                                   "merchantId": "7", "projectId": projectId_1, "groupId": groupId_2,
                                   "customerId": None, "nominalValue": None, "nominalTimes": "2",
                                   "oneTimeValue": "100.00", "idCardType": "1"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_2")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取公众号账户实名认证信息
        condition = bkw.thePublicApi_VProjectUserCondition(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {
                "type": "odx_dWxZnpesie_kDj-hNvvP2YiJpzxlx3O4bc3FWE5mpfBnWZEggCwIqF1BsTNpZ7Ni2m8BmsAk4MQG86ITxRsTIK24GcZpkdELWpEzQTRzIMsq11PAINVUrc37dMpAkGpCpahqhVZNoqhBeMWKr-16sncBiyF-ed-dTnNNWpDGh0HhSWrQjXq2rdZEE0g27rf3ZZ4rjdriO46MRzr1cTo7SV-9Gzn8cfVYmVACk_B7oyc6lT2DfYKTp4tee1nYZbAShL-nK3g12iblFQNoeR9Kq6PMpwBKtUtKpM0volhGtWzBAiJ7d-tXbB6tv0ojeA",
                "channel": channel}, "env": envt}, "dict")
        # 提取username
        userName = ckw.CommonKeyWord().Json_GetJsonValue(condition, [["data", "body", "userName"]])
        # 提取userIDcard
        useridcard = ckw.CommonKeyWord().Json_GetJsonValue(condition, [["data", "body", "userIdCard"]])
        # 打印提取的username到日志
        ckw.CommonKeyWord().Print_ToLog("领取用户的姓名：", userName)
        # 打印提取的userIDcard到日志
        ckw.CommonKeyWord().Print_ToLog("领取用户的身份证号码：", useridcard)
        # 雇主清单权益领取提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {},
             "data": {"mobile": mobiles, "name": userName, "idCardType": "1", "idCard": useridcard, "channel": channel},
             "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-链接二维码-一码一权益-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0003(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_3")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_3")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-链接二维码-通用码-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0004(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_4")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_3")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserGroup(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"groupId": "zLkkaAm7g5ouJCILiz2BJgjcxXY", "channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-实体卡领取激活-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0005(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_5")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_4")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-手机预分配领取激活-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0006(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_6")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_5")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 领取权益手机号提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"mobile": mobiles, "channel": channel}, "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-驻店宝指定手机号领取激活-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0007(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_7")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "20.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_6")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 领取权益手机号提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"mobile": mobiles, "channel": channel}, "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-驻店宝链接二维码领取激活-重复激活场景")
    @allure.severity("blocker")
    def test_zfg_0008(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_8")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "20.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_6")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 领取权益手机号提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 重复提交激活
        Risres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
        # 读取权益重复激活断言
        RepeatedSubmissionOfRights = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RepeatedSubmissionOfRights")
        # 打印权益重复激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RepeatedSubmissionOfRights)
        # 打印权益重复激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Risres)
        # 权益重复激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Risres, RepeatedSubmissionOfRights)

    @allure.feature("权益中心-非合并次卡领取激活-电子码领取方式-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0009(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_1")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_1, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "3", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_1")
        # 电子码领取权益提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 权益次卡领取信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 权益次卡领取激活
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-雇主清单领取方式-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0010(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_2")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": "陈星", "mobile": mobiles, "verifyName": "陈星",
                                   "verifyMobile": mobiles, "verifyIdCard": "110101199003079139",
                                   "verifyKeyword1": None, "verifyKeyword2": None, "verifyKeyword3": None,
                                   "merchantId": "7", "projectId": projectId_1, "groupId": groupId_2,
                                   "customerId": None, "nominalValue": None, "nominalTimes": "2",
                                   "oneTimeValue": "100.00", "idCardType": "1"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_2")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取公众号账户实名认证信息
        condition = bkw.thePublicApi_VProjectUserCondition(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {
                "type": "odx_dWxZnpesie_kDj-hNvvP2YiJpzxlx3O4bc3FWE5mpfBnWZEggCwIqF1BsTNpZ7Ni2m8BmsAk4MQG86ITxRsTIK24GcZpkdELWpEzQTRzIMsq11PAINVUrc37dMpAkGpCpahqhVZNoqhBeMWKr-16sncBiyF-ed-dTnNNWpDGh0HhSWrQjXq2rdZEE0g27rf3ZZ4rjdriO46MRzr1cTo7SV-9Gzn8cfVYmVACk_B7oyc6lT2DfYKTp4tee1nYZbAShL-nK3g12iblFQNoeR9Kq6PMpwBKtUtKpM0volhGtWzBAiJ7d-tXbB6tv0ojeA",
                "channel": channel}, "env": envt}, "dict")
        # 提取username
        userName = ckw.CommonKeyWord().Json_GetJsonValue(condition, [["data", "body", "userName"]])
        # 提取userIDcard
        useridcard = ckw.CommonKeyWord().Json_GetJsonValue(condition, [["data", "body", "userIdCard"]])
        # 打印提取的username到日志
        ckw.CommonKeyWord().Print_ToLog("领取用户的姓名：", userName)
        # 打印提取的userIDcard到日志
        ckw.CommonKeyWord().Print_ToLog("领取用户的身份证号码：", useridcard)
        # 雇主清单权益领取提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {},
             "data": {"mobile": mobiles, "name": userName, "idCardType": "1", "idCard": useridcard, "channel": channel},
             "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-链接二维码-一码一权益-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0011(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_3")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_3")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-链接二维码-通用码-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0012(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_4")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_3")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserGroup(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"groupId": "zLkkaAm7g5ouJCILiz2BJgjcxXY", "channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-实体卡领取激活-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0013(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_5")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_4")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-手机预分配领取激活-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0014(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_6")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "100.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_5")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 领取权益手机号提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"mobile": mobiles, "channel": channel}, "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-驻店宝指定手机号领取激活-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0015(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_7")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "20.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_6")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 领取权益手机号提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"mobile": mobiles, "channel": channel}, "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)

    @allure.feature("权益中心-非合并次卡领取激活-驻店宝链接二维码领取激活-正常激活场景")
    @allure.severity("blocker")
    def test_zfg_0016(self):
        # 读取yaml文件
        yamlfile = ckw.CommonKeyWord().Yaml_Read(
            "TestFile/FuGguang/ZfgLnterestCard.yaml")
        # 读取yaml测试环境域名
        envt = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "envt")
        # 打印域名到控制台
        ckw.CommonKeyWord().Print_ToControl("环境域名：", envt)
        # 打印域名到日志
        ckw.CommonKeyWord().Print_ToLog("环境域名：", envt)
        # 运营中心Authorization提取打印到日志
        ckw.CommonKeyWord().Print_ToLog("运营中心Authorization:", Authorization_1)
        # 读取yaml权益领取账户手机号码
        mobiles = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "mobiles")
        # 读取yaml权益项目ID
        projectId_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "projectId_1")
        # 读取yaml权益分组ID
        groupId_2 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "groupId_8")
        # 权益中心生成权益卡
        redeemadd = bkw.equityCenterApi_RedeemAdd(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + Authorization_1},
             "parma": {}, "data": {"cdKey": None, "userId": None, "name": None, "mobile": mobiles, "verifyName": None,
                                   "verifyMobile": mobiles, "verifyIdCard": None, "verifyKeyword1": None,
                                   "verifyKeyword2": None, "verifyKeyword3": None, "merchantId": "7",
                                   "projectId": projectId_1, "groupId": groupId_2, "customerId": None,
                                   "nominalValue": None, "nominalTimes": "2", "oneTimeValue": "20.00",
                                   "idCardType": "01"}, "env": envt}, "dict")
        # 提取权益中心权益电子兑换码
        cdkey = ckw.CommonKeyWord().Json_GetJsonValue(redeemadd, [["data", "verify", "cdKey"]])
        # 打印提取权益中心权益电子兑换码到日志
        ckw.CommonKeyWord().Print_ToLog("电子权益兑换码：", cdkey)
        # 获取公众号个人信息
        vmemberdetail = bkw.thePublicApi_VMemberDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Token " + token_2},
             "parma": {}, "data": {}, "env": envt}, "dict")
        # 提取用户公众号openid
        openid = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "openid"]])
        # 提取用户公众号account
        account = ckw.CommonKeyWord().Json_GetJsonValue(vmemberdetail, [["data", "account"]])
        # 打印提取用户公众号openid到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的openid:", openid)
        # 打印提取用户公众号account到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取权益用户的account:", account)
        # 读取yaml权益领取方式配置
        channel = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "channel_6")
        # 打印读取领取方式到日志
        ckw.CommonKeyWord().Print_ToLog("当前领取方式：", channel)
        # 领取权益手机号提交
        bkw.thePublicApi_VProjectUserCheck(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"cdKey": cdkey, "channel": channel,"sourceType":"wx"}, "env": envt}, "dict")
        # 获取当前权益信息
        bkw.thePublicApi_VProjectUserDetail(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提交激活权益
        Rigres = bkw.thePublicApi_VEquityNewActivate(
            {"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token_2},
             "parma": {}, "data": {"channel": channel}, "env": envt}, "dict")
        # 提取激活成功errno
        Reserrno = ckw.CommonKeyWord().Json_GetJsonValue(Rigres, [["errno"]])
        # 读取权益激活断言
        RightsActivation_1 = ckw.CommonKeyWord().Yaml_GetByKey(yamlfile, "RightsActivation")
        # 打印权益激活断言到日志
        ckw.CommonKeyWord().Print_ToLog("读取的断言预置：", RightsActivation_1)
        # 打印权益激活json到日志
        ckw.CommonKeyWord().Print_ToLog("提取的激活出参：", Reserrno)
        # 权益激活断言执行
        assert ckw.CommonKeyWord().Assert_ObjAndObj(Reserrno, RightsActivation_1)
