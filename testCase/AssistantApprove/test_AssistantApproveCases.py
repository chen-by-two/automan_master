# -*- coding: utf-8 -*-
import pytest, os, allure
import KeyWordDriver.CommonKeyWord as ckw
import KeyWordDriver.BusinesskeyWord as bkw

class Test_Approve_case:

    @allure.feature("提交店员解冻审批")
    @allure.severity("blocker")
    def test_Assistant_Approve(self):
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/AssistantApprove/AssistantApprove.yaml")
        # 读取yaml里手机号
        mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "ApproveMobile")
        # 读取Yaml登录密码
        password = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "password")
        # 读取Yaml执行环节
        env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "env")
        # 登录获取token-调取接口
        loginRes = bkw.assistantappApi_UserLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
        "data": {"mobile": mobile, "code": password}, "env": env}, "dict")
        # 登录获取token-提取token
        global token
        token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
        # 登录获取userid-提取userid
        userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "id"]])
        # 打印token到控制台
        ckw.CommonKeyWord().Print_ToControl("token：", token)
        # 打印token到日志
        ckw.CommonKeyWord().Print_ToLog("token：", token)
        # token写入yaml文件
        ckw.CommonKeyWord().Yaml_Write_Any("./TestFile/AssistantApprove/token.yaml", "token", token)
        # 读取yaml文件
        yamlFile = ckw.CommonKeyWord().Yaml_Read("./TestFile/AssistantApprove/AssistantApprove.yaml")
        # 读取插入店员数据
        InsertAssistant = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "InsertAssistant")
        print(InsertAssistant)
        # 读取查询店员数据
        SelectAssistant = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "SelectAssistant")
        # 读取删除店员数据
        DeleteAssistant = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "DeleteAssistant")
        print(DeleteAssistant)
        # mysql执行任意sql-插入店员数据
        InsertAssistant = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_module_clerk", InsertAssistant)
        print(InsertAssistant)
        # mysql执行任意sql-查询店员数据
        SelectAssistant = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_module_clerk", SelectAssistant)
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("SelectAssistant：", SelectAssistant)
        # mysql执行任意sql-删除店员数据
        DeleteAssistant = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_module_clerk", DeleteAssistant)
        print(DeleteAssistant)

        # 读取更新店员状态sql
        UpdateSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "UpdateAssistantStatus")
        print(UpdateSql)
        # mysql执行任意sql-更新店员状态
        UpdateAssistant = ckw.CommonKeyWord().Db_SshConfMysqlExecute("DATABASE_RC_cn_uniondrug_module_clerk", UpdateSql)
        # 提交店员解冻审批-调取接口
        SubmitApproval = bkw.ApproveApi_UnfreezeAssistantSubmitApproval({"header": {"Content-Type": "application/json;charsetUTF-8", "Authorization": "Bearer " + token},
         "parma": {}, "data": {
    "assistants": [{
        "account": "15100001111",
        "status": "0",
        "partnerName": "沪宁大药房（简称）",
        "assistantId": "200003",
        "fullName": "张大大",
        "statusText": "已冻结",
        "storeName": "产品测试门店1-935（简称）"
    }],
    "approval": {
        "approveType": "2",
        "approveSettingId": "1",
        "applyName": "店员解冻",
        "processList": [{
            "operateType": "3",
            "processName": "大佬审批",
            "processType": "1",
            "processSettingId": "2558",
            "processUserList": [{
                "avatar": "https:\/\/ss2.bdstatic.com\/70cFvnSh_Q1YnxGkpoWK1HF6hhy\/it\/u=2834285391,2876082627&fm=26&gp=0.jpg",
                "mobile": "15380905486",
                "userId": "323",
                "userName": "张俊超02"
            }, {
                "avatar": "https:\/\/gimg2.baidu.com\/image_search\/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
                "mobile": "15651711729",
                "userId": "4186",
                "userName": "肖文瑶"
            }]
        }, {
            "operateType": "1",
            "processName": "抄送人",
            "processType": "2",
            "processSettingId": "2557",
            "processUserList": [{
                "avatar": "https:\/\/ss2.bdstatic.com\/70cFvnSh_Q1YnxGkpoWK1HF6hhy\/it\/u=2834285391,2876082627&fm=26&gp=0.jpg",
                "mobile": "15380905486",
                "userId": "323",
                "userName": "张俊超02"
            }, {
                "avatar": "https:\/\/gimg2.baidu.com\/image_search\/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
                "mobile": "15651711729",
                "userId": "4186",
                "userName": "肖文瑶"
            }]
        }]
    },
    "reason": "测测测测册测"
}, "env": env}, "dict")
        # 打印返回码到日志
        ckw.CommonKeyWord().Print_ToLog("SubmitApproval:", SubmitApproval)
        # 提取提交审批返回码
        SubmitApprovalErrorno = ckw.CommonKeyWord().Json_GetJsonValue(SubmitApproval, [["errno"]])
        # 打印到控制台
        ckw.CommonKeyWord().Print_ToControl("SubmitApproval：", SubmitApprovalErrorno)
        # 打印返回码到日志
        ckw.CommonKeyWord().Print_ToLog("SubmitApproval:", SubmitApprovalErrorno)
        # 如果返回值正确则取消息体数据，如果返回值错误则取报错信息
        if (SubmitApprovalErrorno == 0):
            # 提取提交审批返回
            SubmitApprovalData = ckw.CommonKeyWord().Json_GetJsonValue(SubmitApproval, [["data"]])
            # 打印到控制台
            ckw.CommonKeyWord().Print_ToControl("SubmitApproval：", SubmitApprovalData)
            # 打印返回到日志
            ckw.CommonKeyWord().Print_ToLog("SubmitApproval:", SubmitApprovalData)
        else:
            # 提取提交审批返回
            SubmitApprovalError = ckw.CommonKeyWord().Json_GetJsonValue(SubmitApproval, [["error"]])
            # 打印到控制台
            ckw.CommonKeyWord().Print_ToControl("SubmitApproval：", SubmitApprovalError)
            # 打印返回到日志
            ckw.CommonKeyWord().Print_ToLog("SubmitApproval:", SubmitApprovalError)
        # 读取yaml断言
        Errno = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile, "Errno")
        # 打印结果到日志
        ckw.CommonKeyWord().Print_ToLog("断言结果：", Errno)
        # 断言对比字典
        assert ckw.CommonKeyWord().Assert_ObjAndObj(SubmitApprovalErrorno, Errno)
        # 强制等待
        ckw.CommonKeyWord().Time_Sleep("1.0")
