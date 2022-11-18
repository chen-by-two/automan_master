# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as im1
import KeyWordDriver.BusinesskeyWord as im2

#path = 'TestFile/GongSheng/GsApp.Backend.yaml'
#yamlfile = im1.CommonKeyWord().Yaml_Read(path)

# 查寻IM账号
# 读取rc环境
#env = im1.CommonKeyWord().Yaml_GetByKey("env_rc")
class IM_acco:

    @allure.feature("查寻IM账号")
    @allure.severity("blocker")
    def IM_accountn(self):
        # 打开yaml文件
        im2.im_group_chat_IM_account({"header": {"Content-Type": "application/json"},
                                      "parma": {},
                                      "data": {"sysCode": "dstoremember", "sysFlag": "16236619_c"},
                                      },
                                    "dict")

    @allure.feature("自定义消息-发送优惠卷信息")
    @allure.severity("blocker")
    def IM_couponMsgn(self):
        # 打开yaml文件
        im2.im_group_chat_IM_couponMsg(dict(header={"Content-Type": "application/json"}, parma={},
                                          data=dict(errno="0", error="SUCCESS", dataType="OBJECT", data={
                                              "errno": "0",
                                              "error": "SUCCESS",
                                              "dataType": "OBJECT",
                                              "data": "null"
                                          })),
                                    "dict")

        @allure.feature("轮询查询在线状态")
        @allure.severity("blocker")
        def IM_pollIsOnlinen(self):
            # 打开yaml文件
            im2.im_group_chat_IM_pollIsOnline(dict(header={"Content-Type": "application/json"}, parma={},
                                                data=dict(sysCode="healthtreasure", roomId="healthtreasure_15968231_4022502", sender="15968231",
                         senderRole="healthtreasurehtd", receiver="4022502", receiverRole="healthtreasurehtu")),
                                           "dict")

        @allure.feature("IM会话框数据初始化")
        @allure.severity("blocker")
        def IM_imInitn(self):
            # 打开yaml文件
            im2.im_group_chat_IM_imInit(dict(header={"Content-Type": "application/json"}, parma={},
                                                   data=dict(fromAcct="1b71a29459ac472fa81a2d49333et", toAcct="2936181304", scene="team")),
                                              "dict")

        @allure.feature("医生列表")
        @allure.severity("blocker")
        def IM_updateUsern(self):
            # 打开yaml文件
            im2.im_group_chat_IM_updateUser(dict(header={"Content-Type": "application/json"}, parma={},
                                             data=dict(acctId="16666154cdee4053b0fcd922587br", longitude="12.46", latitude="12.46")),
                                        "dict")

        @allure.feature("修改IM账号")
        @allure.severity("blocker")
        def IM_addFriendTn(self):
            # 打开yaml文件
            im2.im_group_chat_IM_addFriendTo(dict(header={"Content-Type": "application/json"}, parma={},
                                                 data=dict(type="1", sysCode="commission", sysFlagFrom="2", sysFlagTo="1", environment="t")),
                                            "dict")

        @allure.feature("查询列表")
        @allure.severity("blocker")
        def RenewCartn(self):
            # 打开yaml文件
            im2.im_group_chat_RenewCart(dict(header={"Content-Type": "application/json"}, parma={},
                                                  data=dict(recordMemberList=[
            {
                "sysFlag": "15961141_a",
                "sysCode": "advisor"
            }
        ], hasGroup="false", hasSingle="true", isInvisible="false")),
                                             "dict")

