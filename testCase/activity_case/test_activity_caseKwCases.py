# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_activity_case:

	@allure.feature("活动后台-登录运营中心后台")
	@allure.severity("blocker")
	def test_activity_DdLogin_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileActivity")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 获取默认登录验证码123456-调取接口
		bkw.activityApi_SmsReset({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile},"env":env},"dict")
		# 手机号获取后台登录的token-调取接口
		DdMobilelogin = bkw.activityApi_DdMobilelogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code": "123456"},"env":env},"dict")
		# 获取登录后台的token-提取token
		logintoken = ckw.CommonKeyWord().Json_GetJsonValue(DdMobilelogin,[["data","token"]])
		# 登录运营中心后台-调取接口
		DdLogin = bkw.activityApi_DdLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"token":logintoken},"env":env},"dict")
		# 获取后台的token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(DdLogin,[["data","token"]])
		# 登录获取userid-提取userid
		workerId = ckw.CommonKeyWord().Json_GetJsonValue(DdLogin,[["data","workerId"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# token写入yaml文件
		ckw.CommonKeyWord().Yaml_Write_Any("./TestFile/activity/token.yaml","token",token)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-新增普通红包-福联社模版成功")
	@allure.severity("blocker")
	def test_activity_AdminTemplateSave_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 新增活动模版成功-调取接口
		AdminTemplateSave = bkw.activityApi_AdminTemplateSave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"id":"","type":"1","channel":"1","template_name":"普通红包FLS自动化","rules":"<p><span style\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>","timeType":"1","times":"","release":"2","title":"药联健康给您发红包啦~","subtitle":"您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障","back_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png","button_icon":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png","play_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png","bottom_img":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png","share_img":"","share_icon":"https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png","explain":"","discount_img":"","pro_language":"药联健康给您发红包啦~","jump_url":"","isRecheck":"0","commonRewardList":[{"reward_type":"5","scheme_type":"1","type":"2","udSchemeId":"","udSchemeName":"","amount":"","rules":"","plan_type_id":"","rewardList":[],"projectId":"4965","pileId":"4798"}]},"env":env},"dict")
		# 提取新增活动模版成功返回
		AdminTemplateSaveerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateSave,[["errno"]])
		# 提取新增活动模版id
		AdminTemplateid = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateSave,[["data","id"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateSaveerrno:",AdminTemplateSaveerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateSaveerrno:",AdminTemplateSaveerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateSaveerrno,Errno)
		# 模版id写入yaml文件
		ckw.CommonKeyWord().Yaml_Write("./TestFile/activity/info.yaml",token,"Templateid",AdminTemplateid)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-新增普通红包-福联社模版福联社商品为空")
	@allure.severity("blocker")
	def test_activity_AdminTemplateSave_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 新增活动模版成功-调取接口
		AdminTemplateSave = bkw.activityApi_AdminTemplateSave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": "",
    "type": "1",
    "channel": "1",
    "template_name": "普通红包福联社2603",
    "rules": "<p><span style\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>",
    "timeType": "2",
    "times": "3",
    "release": "2",
    "title": "药联健康给您发红包啦~",
    "subtitle": "您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障",
    "back_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png",
    "button_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png",
    "play_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png",
    "bottom_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png",
    "share_img": "",
    "share_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png",
    "explain": "",
    "discount_img": "",
    "pro_language": "药联健康给您发红包啦~",
    "jump_url": "",
    "isRecheck": "1",
    "commonRewardList": [
        {
            "reward_type": "5",
            "scheme_type": "1",
            "type": "2",
            "udSchemeId": "",
            "udSchemeName": "",
            "amount": "",
            "rules": "",
            "plan_type_id": "",
            "rewardList": [],
            "projectId": "",
            "pileId": "4797",
            "goodsName": "测试福实物商品222"
        }
    ]
},"env":env},"dict")
		# 提取新增活动模版成功返回
		AdminTemplateSaveerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateSave,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateSaveerrno:",AdminTemplateSaveerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateSaveerrno:",AdminTemplateSaveerrno)
		# 读取yaml断言
		fls_empty_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"fls_empty_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",fls_empty_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateSaveerrno,fls_empty_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-新增普通红包-福联社模版福联社采购批次为空")
	@allure.severity("blocker")
	def test_activity_AdminTemplateSave_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 新增活动模版成功-调取接口
		AdminTemplateSave = bkw.activityApi_AdminTemplateSave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": "",
    "type": "1",
    "channel": "1",
    "template_name": "普通红包FLS自动化",
    "rules": "<p><span style\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>",
    "timeType": "2",
    "times": "3",
    "release": "2",
    "title": "药联健康给您发红包啦~",
    "subtitle": "您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障",
    "back_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png",
    "button_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png",
    "play_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png",
    "bottom_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png",
    "share_img": "",
    "share_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png",
    "explain": "",
    "discount_img": "",
    "pro_language": "药联健康给您发红包啦~",
    "jump_url": "",
    "isRecheck": "1",
    "commonRewardList": [
        {
            "reward_type": "5",
            "scheme_type": "1",
            "type": "2",
            "udSchemeId": "",
            "udSchemeName": "",
            "amount": "",
            "rules": "",
            "plan_type_id": "",
            "rewardList": [],
            "projectId": "4965",
            "pileId": "",
            "goodsName": "测试福实物商品222"
        }
    ]
},"env":env},"dict")
		# 提取新增活动模版成功返回
		AdminTemplateSaveerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateSave,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateSaveerrno:",AdminTemplateSaveerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateSaveerrno:",AdminTemplateSaveerrno)
		# 读取yaml断言
		fls_empty_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"fls_empty_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",fls_empty_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateSaveerrno,fls_empty_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-编辑普通红包-福联社模版成功")
	@allure.severity("blocker")
	def test_activity_AdminTemplateEdit_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 读取Yaml执行sql
		find_reward_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"find_reward_id")
		# mysql执行任意sql-查询模版奖励id
		reward_id1 = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_activity",find_reward_id)
		# 从数据库提取模版奖励ld
		reward_id = ckw.CommonKeyWord().Json_GetJsonValue(reward_id1[0],[["id"]])
		# 编辑活动模版成功-调取接口
		AdminTemplateEdit = bkw.activityApi_AdminTemplateSave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": Templateid,
    "type": "1",
    "channel": "1",
    "release": "2",
    "template_name": "普通红包FLS自动化",
    "rules": "<p><span style\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>",
    "pro_language": "药联健康给您发红包啦~",
    "timeType": "1",
    "times": "",
    "title": "药联健康给您发红包啦~",
    "subtitle": "您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障",
    "back_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png",
    "play_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png",
    "button_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png",
    "jump_url": "",
    "share_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png",
    "bottom_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png",
    "insurerId": "0",
    "insurerName": "",
    "insurerLogo": "",
    "rewardInfo": [
        {
            "id": reward_id,
            "reward_type": "5",
            "productId": "0",
            "productName": "",
            "discount_name": "",
            "proportion": "0.00",
            "saleAmount": "0.00",
            "equity_name": "",
            "equityAmount": "0.00",
            "img": "",
            "plan_type_id": "0",
            "plan_type_name": "",
            "tem_ids": "0",
            "template_name": "",
            "type": "2",
            "udSchemeId": "",
            "scheme_type": "1",
            "udSchemeName": "",
            "amount": "0.00",
            "rules": "",
            "templateTimes": "",
            "guestConf": "",
            "userLimit": "0",
            "userLimitText": "",
            "sendType": "0",
            "sendTypeText": "",
            "ruleText": "",
            "qrcode": "",
            "extra": "0",
            "extraText": "",
            "extraAmount": "0",
            "projectId": "4965",
            "pileId": "4797",
            "goodsList": [
                {
                    "pileId": "4796",
                    "goodsName": "福联社实物商品测试1",
                    "singleEquityMoney": "30",
                    "equityNumber": "20",
                    "relationActivityCount": "0",
                    "isSelect": "false"
                },
                {
                    "pileId": "4797",
                    "goodsName": "测试福实物商品222",
                    "singleEquityMoney": "300",
                    "equityNumber": "3",
                    "relationActivityCount": "5",
                    "isSelect": "false"
                },
                {
                    "pileId": "4798",
                    "goodsName": "测试福规格2222",
                    "singleEquityMoney": "1000",
                    "equityNumber": "1",
                    "relationActivityCount": "2",
                    "isSelect": "true"
                }
            ],
            "goodsName": "测试福实物商品222"
        }
    ],
    "isRecheck": "1",
    "commonRewardList": [
        {
            "id": reward_id,
            "reward_type": "5",
            "productId": "0",
            "productName": "",
            "discount_name": "",
            "proportion": "0.00",
            "saleAmount": "0.00",
            "equity_name": "",
            "equityAmount": "0.00",
            "img": "",
            "plan_type_id": "0",
            "plan_type_name": "",
            "tem_ids": "0",
            "template_name": "",
            "type": "2",
            "udSchemeId": "",
            "scheme_type": "1",
            "udSchemeName": "",
            "amount": "0.00",
            "rules": "",
            "templateTimes": "",
            "guestConf": "",
            "userLimit": "0",
            "userLimitText": "",
            "sendType": "0",
            "sendTypeText": "",
            "ruleText": "",
            "qrcode": "",
            "extra": "0",
            "extraText": "",
            "extraAmount": "0",
            "projectId": "4965",
            "pileId": "4797",
            "goodsList": [
                {
                    "pileId": "4796",
                    "goodsName": "福联社实物商品测试1",
                    "singleEquityMoney": "30",
                    "equityNumber": "20",
                    "relationActivityCount": "0",
                    "isSelect": "false"
                },
                {
                    "pileId": "4797",
                    "goodsName": "测试福实物商品222",
                    "singleEquityMoney": "300",
                    "equityNumber": "3",
                    "relationActivityCount": "5",
                    "isSelect": "false"
                },
                {
                    "pileId": "4798",
                    "goodsName": "测试福规格2222",
                    "singleEquityMoney": "1000",
                    "equityNumber": "1",
                    "relationActivityCount": "2",
                    "isSelect": "true"
                }
            ],
            "goodsName": "测试福实物商品222"
        }
    ]
},"env":env},"dict")
		# 提取编辑活动模版成功返回
		AdminTemplateEditerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateEdit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateEditerrno:",AdminTemplateEditerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateEditerrno:",AdminTemplateEditerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateEditerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-编辑普通红包-福联社模版福联社商品为空")
	@allure.severity("blocker")
	def test_activity_AdminTemplateEdit_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 编辑活动模版成功-调取接口
		AdminTemplateEdit = bkw.activityApi_AdminTemplateSave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": Templateid,
    "type": "1",
    "channel": "1",
    "release": "2",
    "template_name": "普通红包FLS02",
    "rules": "<p><span style\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>",
    "pro_language": "药联健康给您发红包啦~",
    "timeType": "2",
    "times": "3,5",
    "title": "药联健康给您发红包啦~",
    "subtitle": "您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障",
    "back_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png",
    "play_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png",
    "button_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png",
    "jump_url": "",
    "share_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png",
    "bottom_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png",
    "insurerId": "0",
    "insurerName": "",
    "insurerLogo": "",
    "rewardInfo": [
        {
            "id": "528",
            "reward_type": "5",
            "productId": "0",
            "productName": "",
            "discount_name": "",
            "proportion": "0.00",
            "saleAmount": "0.00",
            "equity_name": "",
            "equityAmount": "0.00",
            "img": "",
            "plan_type_id": "0",
            "plan_type_name": "",
            "tem_ids": "0",
            "template_name": "",
            "type": "2",
            "udSchemeId": "",
            "scheme_type": "1",
            "udSchemeName": "",
            "amount": "0.00",
            "rules": "",
            "templateTimes": "",
            "guestConf": "",
            "userLimit": "0",
            "userLimitText": "",
            "sendType": "0",
            "sendTypeText": "",
            "ruleText": "",
            "qrcode": "",
            "extra": "0",
            "extraText": "",
            "extraAmount": "0",
            "projectId": "4966",
            "pileId": "4799",
            "goodsList": [
                {
                    "pileId": "4799",
                    "goodsName": "hjw营销卡1102",
                    "singleEquityMoney": "4",
                    "equityNumber": "20",
                    "relationActivityCount": "2",
                    "isSelect": "false"
                },
                {
                    "pileId": "4800",
                    "goodsName": "21.5万村医关爱保障金（1个月）",
                    "singleEquityMoney": "22",
                    "equityNumber": "15",
                    "relationActivityCount": "0",
                    "isSelect": "true"
                }
            ],
            "goodsName": "hjw营销卡1102"
        }
    ],
    "isRecheck": "1",
    "commonRewardList": [
        {
            "id": "528",
            "reward_type": "5",
            "productId": "0",
            "productName": "",
            "discount_name": "",
            "proportion": "0.00",
            "saleAmount": "0.00",
            "equity_name": "",
            "equityAmount": "0.00",
            "img": "",
            "plan_type_id": "0",
            "plan_type_name": "",
            "tem_ids": "0",
            "template_name": "",
            "type": "2",
            "udSchemeId": "",
            "scheme_type": "1",
            "udSchemeName": "",
            "amount": "0.00",
            "rules": "",
            "templateTimes": "",
            "guestConf": "",
            "userLimit": "0",
            "userLimitText": "",
            "sendType": "0",
            "sendTypeText": "",
            "ruleText": "",
            "qrcode": "",
            "extra": "0",
            "extraText": "",
            "extraAmount": "0",
            "projectId": "",
            "pileId": "4799",
            "goodsList": [
                {
                    "pileId": "4799",
                    "goodsName": "hjw营销卡1102",
                    "singleEquityMoney": "4",
                    "equityNumber": "20",
                    "relationActivityCount": "2",
                    "isSelect": "false"
                },
                {
                    "pileId": "4800",
                    "goodsName": "21.5万村医关爱保障金（1个月）",
                    "singleEquityMoney": "22",
                    "equityNumber": "15",
                    "relationActivityCount": "0",
                    "isSelect": "true"
                }
            ],
            "goodsName": "hjw营销卡1102"
        }
    ]
},"env":env},"dict")
		# 提取编辑活动模版成功返回
		AdminTemplateEditerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateEdit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateEditerrno:",AdminTemplateEditerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateEditerrno:",AdminTemplateEditerrno)
		# 读取yaml断言
		fls_empty_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"fls_empty_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",fls_empty_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateEditerrno,fls_empty_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-编辑普通红包-福联社模版福联社采购批次为空")
	@allure.severity("blocker")
	def test_activity_AdminTemplateEdit_003(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 编辑活动模版成功-调取接口
		AdminTemplateEdit = bkw.activityApi_AdminTemplateSave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": Templateid,
    "type": "1",
    "channel": "1",
    "release": "2",
    "template_name": "普通红包FLS02",
    "rules": "<p><span style\"color: rgb(17, 31, 44);\">1、通过本页面领取的价值100元药联权益，每人仅限领取3次；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">2、领取到账的权益仅限在指定合作门店使用；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">3、每次消费可抵扣订单金额的15%，抵扣金额从100元中扣除，直至扣完为止；</span></p><p><br></p><p><span style\"color: rgb(17, 31, 44);\">4、权益总额有限，先到先得，送完为止。（快快分享给亲朋好友领取吧！）</span></p>",
    "pro_language": "药联健康给您发红包啦~",
    "timeType": "2",
    "times": "3,5",
    "title": "药联健康给您发红包啦~",
    "subtitle": "您的健康是我们最大的心愿，药联为您和家人的健康多加一份保障",
    "back_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/98146e659f70bd2f44459360cbb33ac5.png",
    "play_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/702ee81e5e14d95834672acc65a07585.png",
    "button_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/5f0a80b5d32a89149774f3983a2e0262.png",
    "jump_url": "",
    "share_icon": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/64d35dcaf37e8c1f06162eaf8861f93f.png",
    "bottom_img": "https://uniondrug-ota.oss-cn-shanghai.aliyuncs.com/3dfdbf3baeb7a2992af8e7c510158cf4.png",
    "insurerId": "0",
    "insurerName": "",
    "insurerLogo": "",
    "rewardInfo": [
        {
            "id": "528",
            "reward_type": "5",
            "productId": "0",
            "productName": "",
            "discount_name": "",
            "proportion": "0.00",
            "saleAmount": "0.00",
            "equity_name": "",
            "equityAmount": "0.00",
            "img": "",
            "plan_type_id": "0",
            "plan_type_name": "",
            "tem_ids": "0",
            "template_name": "",
            "type": "2",
            "udSchemeId": "",
            "scheme_type": "1",
            "udSchemeName": "",
            "amount": "0.00",
            "rules": "",
            "templateTimes": "",
            "guestConf": "",
            "userLimit": "0",
            "userLimitText": "",
            "sendType": "0",
            "sendTypeText": "",
            "ruleText": "",
            "qrcode": "",
            "extra": "0",
            "extraText": "",
            "extraAmount": "0",
            "projectId": "4966",
            "pileId": "4799",
            "goodsList": [
                {
                    "pileId": "4799",
                    "goodsName": "hjw营销卡1102",
                    "singleEquityMoney": "4",
                    "equityNumber": "20",
                    "relationActivityCount": "2",
                    "isSelect": "false"
                },
                {
                    "pileId": "4800",
                    "goodsName": "21.5万村医关爱保障金（1个月）",
                    "singleEquityMoney": "22",
                    "equityNumber": "15",
                    "relationActivityCount": "0",
                    "isSelect": "true"
                }
            ],
            "goodsName": "hjw营销卡1102"
        }
    ],
    "isRecheck": "1",
    "commonRewardList": [
        {
            "id": "528",
            "reward_type": "5",
            "productId": "0",
            "productName": "",
            "discount_name": "",
            "proportion": "0.00",
            "saleAmount": "0.00",
            "equity_name": "",
            "equityAmount": "0.00",
            "img": "",
            "plan_type_id": "0",
            "plan_type_name": "",
            "tem_ids": "0",
            "template_name": "",
            "type": "2",
            "udSchemeId": "",
            "scheme_type": "1",
            "udSchemeName": "",
            "amount": "0.00",
            "rules": "",
            "templateTimes": "",
            "guestConf": "",
            "userLimit": "0",
            "userLimitText": "",
            "sendType": "0",
            "sendTypeText": "",
            "ruleText": "",
            "qrcode": "",
            "extra": "0",
            "extraText": "",
            "extraAmount": "0",
            "projectId": "4966",
            "pileId": "",
            "goodsList": [
                {
                    "pileId": "4799",
                    "goodsName": "hjw营销卡1102",
                    "singleEquityMoney": "4",
                    "equityNumber": "20",
                    "relationActivityCount": "2",
                    "isSelect": "false"
                },
                {
                    "pileId": "4800",
                    "goodsName": "21.5万村医关爱保障金（1个月）",
                    "singleEquityMoney": "22",
                    "equityNumber": "15",
                    "relationActivityCount": "0",
                    "isSelect": "true"
                }
            ],
            "goodsName": "hjw营销卡1102"
        }
    ]
},"env":env},"dict")
		# 提取编辑活动模版成功返回
		AdminTemplateEditerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateEdit,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateEditerrno:",AdminTemplateEditerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateEditerrno:",AdminTemplateEditerrno)
		# 读取yaml断言
		fls_empty_errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"fls_empty_errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",fls_empty_errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateEditerrno,fls_empty_errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-新建普通红包方案成功")
	@allure.severity("blocker")
	def test_activity_ActivitySave_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 新建活动方案成功-调取接口
		ActivitySave = bkw.activityApi_ActivitySave({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": "",
    "type": "1",
    "activity_name": "普通红包FLS方案自动化",
    "start_time": "2021-10-9 14:54:40",
    "end_time": "2025-11-30 14:54:40",
    "to_times": "",
    "merchants": [
        {
            "merchant_id": "760",
            "merchant_name": "国药控股国大药房（深圳）连锁有限公司",
            "referred": "深圳国大"
        }
    ],
    "activityScore": [
        {
            "max_point": "100.00",
            "min_point": "0.00",
            "template_id": Templateid,
            "template_name": "普通红包FLS自动化"
        }
    ],
    "shop_times": "0",
    "customer_times": "0",
    "shop_type": "0",
    "customer_type": "0",
    "times_id": "",
    "shop_is_limit": "0",
    "customer_is_limit": "0",
    "template_id": "",
    "template_name": ""
},"env":env},"dict")
		# 提取新建活动方案成功返回
		ActivitySaveerrno = ckw.CommonKeyWord().Json_GetJsonValue(ActivitySave,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("ActivitySaveerrno:",ActivitySaveerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("ActivitySaveerrno:",ActivitySaveerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(ActivitySaveerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-启用普通红包方案成功")
	@allure.severity("blocker")
	def test_activity_ActivitySave_002(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 读取yaml文件sql
		find_plan_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"find_plan_id")
		# mysql执行任意sql-查询方案id
		plan_id = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_activity",find_plan_id)
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",plan_id)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",plan_id)
		# 从数据库提取方案ld
		plan_id1 = ckw.CommonKeyWord().Json_GetJsonValue(plan_id[0],[["id"]])
		# 启用普通红包方案成功-调取接口
		ActivitySwitch = bkw.activityApi_ActivitySwitch({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "id": plan_id1,
    "is_disable": 1
},"env":env},"dict")
		# 提取启用普通红包方案成功返回
		ActivitySwitcherrno = ckw.CommonKeyWord().Json_GetJsonValue(ActivitySwitch,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("ActivitySwitcherrno:",ActivitySwitcherrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("ActivitySwitcherrno:",ActivitySwitcherrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(ActivitySwitcherrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动h5-领取普通红包成功")
	@allure.severity("blocker")
	def test_activity_SendRedeem_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 读取yaml文件sql
		find_plan_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"find_plan_id")
		# mysql执行任意sql-查询方案id
		plan_id = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_cn_uniondrug_activity",find_plan_id)
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",plan_id)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",plan_id)
		# 从数据库提取方案ld
		plan_id1 = ckw.CommonKeyWord().Json_GetJsonValue(plan_id[0],[["id"]])
		# 获取mermberid-调取接口
		MemberParse = bkw.activityApi_CommonMemberParse({"header":{},"parma":{},"data":{
    "activityId": plan_id1,
    "merchantId": "760",
    "memberFlag": "1"
},"env":env},"dict")
		# 提取mermberid
		Memberid = ckw.CommonKeyWord().Json_GetJsonValue(MemberParse,[["data","memberId"]])
		# 领取普通红包成功-调取接口
		SendRedeem = bkw.activityApi_Activity1RedOneSendRedeem({"header":{},"parma":{},"data":{
    "wxMemberId": "15963890",
    "memberId": Memberid,
    "openid": "of-FXw-T-M6uxrGUAQmHAjej_h1M",
    "mobile": "15380905486",
    "activityId": plan_id1,
    "templateId": Templateid
},"env":env},"dict")
		# 提取领取普通红包成功返回
		SendRedeemerrno = ckw.CommonKeyWord().Json_GetJsonValue(SendRedeem,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("SendRedeemerrno:",SendRedeemerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("SendRedeemerrno:",SendRedeemerrno)
		# token写入yaml文件追加写
		ckw.CommonKeyWord().Yaml_Write_Any_Add("./TestFile/activity/token.yaml","data",SendRedeemerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(SendRedeemerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("活动后台-删除活动模版成功")
	@allure.severity("blocker")
	def test_activity_AdminTemplateDel_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取yaml文件
		yamlFilei = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/info.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件sql
		find_template_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"find_template_id")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件Templateid
		Templateid = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilei,"Templateid")
		# 删除活动模版成功-调取接口
		AdminTemplateDel = bkw.activityApi_AdminTemplateDel({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"id":Templateid},"env":env},"dict")
		# 提取删除活动模版成功返回
		AdminTemplateDelerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminTemplateDel,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminTemplateDelerrno:",AdminTemplateDelerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminTemplateDelerrno:",AdminTemplateDelerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminTemplateDelerrno,Errno)
		# 读取yaml文件sql
		delete_plan_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"delete_plan_id")
		# mysql执行任意sql-删除活动方案
		ckw.CommonKeyWord().Db_ConfMysqlExecute("DATABASE_TEST_cn_uniondrug_activity",delete_plan_id)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("获取跑马灯弹幕用户数据")
	@allure.severity("blocker")
	def test_activity_ChainActivityPage_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 获取跑马灯弹幕用户数据-调取接口
		AdminChainActivityPage = bkw.activityApi_AdminChainActivityPage({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "page": "1",
    "limit": "10"
},"env":env},"dict")
		# 提取获取跑马灯弹幕用户数据成功返回
		AdminChainActivityPageerrno = ckw.CommonKeyWord().Json_GetJsonValue(AdminChainActivityPage,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("AdminChainActivityPageerrno:",AdminChainActivityPageerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("AdminChainActivityPageerrno:",AdminChainActivityPageerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(AdminChainActivityPageerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("聚合页首页")
	@allure.severity("blocker")
	def test_activity_CommonMerchantHome_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取Yaml-merchant_id
		merchant_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchant_id")
		# 读取yaml-store_id
		store_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"store_id")
		# 聚合页首页-调取接口
		CommonMerchantHome = bkw.activityApi_CommonMerchantHome({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
  "merchant_id":merchant_id,
  "storeMerchant_id":store_id,
  "page": "1",
  "limit": "10"
},"env":env},"dict")
		# 提取聚合页首页数据成功返回
		CommonMerchantHomeerrno = ckw.CommonKeyWord().Json_GetJsonValue(CommonMerchantHome,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CommonMerchantHomeerrno:",CommonMerchantHomeerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CommonMerchantHomeerrno:",CommonMerchantHomeerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CommonMerchantHomeerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("获取微信jssdk信息")
	@allure.severity("blocker")
	def test_activity_CommonModuleInfoWxConfig_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 获取微信jssdk信息-调取接口
		CommonModuleInfoWxConfig = bkw.activityApi_CommonModuleInfoWxConfig({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "appId": "",
    "timestamp": "",
    "nonceStr": "",
    "signature": "",
    "jsApiList": [
        ""
    ]
}
,"env":env},"dict")
		# 获取微信jssdk信息数据成功返回
		CommonModuleInfoWxConfigerrno = ckw.CommonKeyWord().Json_GetJsonValue(CommonModuleInfoWxConfig,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CommonModuleInfoWxConfigerrno:",CommonModuleInfoWxConfigerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CommonModuleInfoWxConfigerrno:",CommonModuleInfoWxConfigerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CommonModuleInfoWxConfigerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("查询连锁是否有可用普惠红包")
	@allure.severity("blocker")
	def test_activity_Activity6MerchantGetIds_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取yaml文件mobileActivity
		mobileActivity = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileActivity")
		# 读取Yaml-merchant_id
		merchant_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchant_id")
		# 查询连锁是否有可用普惠红包-调取接口
		Activity6MerchantGetIds = bkw.activityApi_Activity6MerchantGetIds({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{
    "ids": merchant_id,
    "mobile": mobileActivity
}
,"env":env},"dict")
		# 查询连锁是否有可用普惠红包成功返回
		Activity6MerchantGetIdserrno = ckw.CommonKeyWord().Json_GetJsonValue(Activity6MerchantGetIds,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Activity6MerchantGetIdserrno:",Activity6MerchantGetIdserrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Activity6MerchantGetIdserrno:",Activity6MerchantGetIdserrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(Activity6MerchantGetIdserrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")

	@allure.feature("公众号获取连锁活动")
	@allure.severity("blocker")
	def test_activity_CommonMerchantActivity_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/act_test.yaml")
		# 读取yaml文件
		yamlFilet = ckw.CommonKeyWord().Yaml_Read("./TestFile/activity/token.yaml")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 读取yaml文件token
		token = ckw.CommonKeyWord().Yaml_GetByKey(yamlFilet,"token")
		# 读取Yaml-merchant_id
		merchant_id = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"merchant_id")
		# 公众号获取连锁活动-调取接口
		CommonMerchantActivity = bkw.activityApi_CommonMerchantActivity({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{   "partnerOrganIds":merchant_id
}
,"env":env},"dict")
		# 公众号获取连锁活动成功返回
		CommonMerchantActivityerrno = ckw.CommonKeyWord().Json_GetJsonValue(CommonMerchantActivity,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("CommonMerchantActivityerrno:",CommonMerchantActivityerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("CommonMerchantActivityerrno:",CommonMerchantActivityerrno)
		# 读取yaml断言
		Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"Errno")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("断言结果：",Errno)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CommonMerchantActivityerrno,Errno)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")
