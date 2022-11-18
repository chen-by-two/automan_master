# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

BACKTOKEN = "1"


class Test_OrderBackend:

    @allure.feature("订单默认查询")
    @allure.severity("blocker")
    def test_baseSearch(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/lhrtest.yaml")
        # 读取yaml里手机号
        mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "mobileOrder")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        global BACKTOKEN
        BACKTOKEN = bkw.adminBackend_login(mobile, env)
        # 默认查询
        res = bkw.orderCenterApi_MngOrderOrderMngPaging({"header": {"Content-Type": "application/json;charset=UTF-8",
                                                                    "Authorization": "Bearer " + BACKTOKEN},
                                                         "parma": {},
                                                         "data": {"page": 1, "limit": 10},
                                                         "env": env}, "text")
        assert res.__contains__("请求成功")


