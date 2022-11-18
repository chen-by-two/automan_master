# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class UserLogin(httpHandler):
    def __init__(self):
        super(UserLogin, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/user/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": "Bearer"}
        self.params = None
        self.data = {"code": "123456", "mobile": "15150578643"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	账号登录")
        return self.response


class CodeSend(httpHandler):
    def __init__(self):
        super(CodeSend, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/code/send"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": "Bearer"}
        self.params = None
        self.data = {"type": "login", "mobile": "15380905486"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	获取验证码")
        return self.response


class UserSmsLogin(httpHandler):
    def __init__(self):
        super(UserSmsLogin, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/user/sms/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {"code": "0047", "mobile": "15380905486"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	验证码登录")
        return self.response


class CustomerAdd(httpHandler):
    def __init__(self):
        super(CustomerAdd, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/customer/add"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {"tags": [{"tagId": "50", "tagName": "云联业务", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "49", "tagName": "自主报名", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "48", "tagName": "意向不明", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "47", "tagName": "意向签约", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "4", "tagName": "短期客户", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "3", "tagName": "长期客户", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "2", "tagName": "合作意愿弱", "is_select": 0, "customerId": "", "id": "", "sort": 0},
                              {"tagId": "1", "tagName": "合作意愿强", "is_select": 0, "customerId": "", "id": "",
                               "sort": 0}], "customerName": "南京艾小宝保险有限公司02", "customerType": 2,
                     "customerTypeText": "保司", "customerStatus": 0, "customerStatusText": "未签约", "level": 2,
                     "levelText": "省级分公司", "longitude": 118.778598, "latitude": 31.973037,
                     "address": "江苏省南京市雨花台区花神大道23号", "userId": "287", "customerId": "", "contacts": [
                {"contactName": "啦啦啦", "weixinUrl": "", "address": "", "sex": "1", "mobile": "15988663965",
                 "position": "测测测", "userId": "287", "customerId": ""}]}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	添加客户")
        return self.response


class CustomerPaging(httpHandler):
    def __init__(self):
        super(CustomerPaging, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/customer/paging"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {"userId": "287", "page": 1, "limit": 10}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	客户列表")
        return self.response


class CustomerInfo(httpHandler):
    def __init__(self):
        super(CustomerInfo, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/customer/info"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {"userId": "287", "customerId": "3213"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	客户详情")
        return self.response


class CustomerEdit(httpHandler):
    def __init__(self):
        super(CustomerEdit, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/customer/edit"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {
            "contacts": [{
                "contactId": "603",
                "customerId": "5787",
                "userId": "287",
                "contactName": "明年",
                "sex": "0",
                "sexText": "女",
                "mobile": "15233312221",
                "phone": "",
                "department": "",
                "position": "测测",
                "address": "",
                "houseNumber": "",
                "longitude": "0.000000",
                "latitude": "0.000000",
                "weixinUrl": "",
                "remark": "",
                "gmtCreated": "2020-10-26 11:13:59",
                "gmtUpdated": "2020-10-26 11:13:59"
            }],
            "images": [],
            "tags": [{
                "tagId": "50",
                "tagName": "云联业务",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "49",
                "tagName": "自主报名",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "48",
                "tagName": "意向不明",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "47",
                "tagName": "意向签约",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "4",
                "tagName": "短期客户",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "3",
                "tagName": "长期客户",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "2",
                "tagName": "合作意愿弱",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }, {
                "tagId": "1",
                "tagName": "合作意愿强",
                "is_select": 0,
                "customerId": "5787",
                "id": "",
                "sort": 0
            }],
            "pbmInfo": "",
            "chainInfo": "",
            "report": [],
            "statusText": "",
            "customerId": "5787",
            "userId": "287",
            "type": "1",
            "customerName": "飞龙大药房",
            "pinyin": "",
            "customerType": "4",
            "customerTypeText": "云联门店",
            "customerStatus": "0",
            "customerStatusText": "无意向未签约",
            "grade": "0",
            "gradeText": "未知",
            "mobile": "",
            "level": 1,
            "levelText": "总公司",
            "longitude": "0.000000",
            "latitude": "0.000000",
            "distance": "0",
            "address": "陕西省渭南市",
            "houseNumber": "",
            "zipCode": "",
            "fax": "",
            "remark": "",
            "organizationName": "",
            "cooperationCode": "",
            "organizationId": "0",
            "partnerId": "0",
            "gmtCreated": "2020-09-27 15:46:35",
            "gmtUpdated": "2020-10-26 11:16:09",
            "poolPartnerId": "201984",
            "applyId": "984",
            "applyStoreId": "0",
            "insuranceApplyId": "0",
            "topStatus": "0",
            "visitStatus": "1",
            "visitStatusText": ""
        }

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	编辑客户")
        return self.response


class CustomerDelete(httpHandler):
    def __init__(self):
        super(CustomerDelete, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/customer/delete"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {
            "customerId": "7159",
            "reasonId": "1",
            "other": ""
        }

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	删除客户")
        return self.response


class InspectCreate(httpHandler):
    def __init__(self):
        super(InspectCreate, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/inspect/create"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e1"}
        self.params = None
        self.data = {"address": "江苏省南京市雨花台区文竹路6号靠近金证南京科技园(装修中)", "map_lat": 31.971663, "trains": [],
                     "map_lon": 118.779486, "images": [{"type": "1",
                                                        "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/cr0rk1b4dnpo2mf03o4ssdne5c.jpg"},
                                                       {"type": "2",
                                                        "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/10eehcd9k3qnv8bu307qnsrh11.jpg"},
                                                       {"type": "2",
                                                        "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/fov3up8ve67806m4o4gr385bch.jpg"},
                                                       {"type": "3",
                                                        "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/r2oqr0ghkkdf71lqnd2l5kmrjk.jpg"},
                                                       {"type": "3",
                                                        "url": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/hqqjjkqlo0k7n52gp19enlrut3.jpg"}],
                     "storeId": "125756", "remark": "巡店自动化测试"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	新增巡店记录")
        return self.response


class VisitAddCommonVisit(httpHandler):
    def __init__(self):
        super(VisitAddCommonVisit, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/visit/addCommonVisit"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e2"}
        self.params = None
        self.data = {
            "userId": "306",
            "userName": "张大仙",
            "customerId": "7159",
            "customerName": "测试新增客户自动化",
            "visitType": "1",
            "content": "添加计划拜访",
            "visitDate": "2020-11-06"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	添加客户拜访")
        return self.response


class VisitArrivalVisit(httpHandler):
    def __init__(self):
        super(VisitArrivalVisit, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/visit/arrivalVisit"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e3"}
        self.params = None
        self.data = {
            "customer": {
                "contacts": [{
                    "contactId": "615",
                    "customerId": "7159",
                    "userId": "306",
                    "contactName": "张大仙",
                    "sex": "0",
                    "sexText": "女",
                    "mobile": "15233331112",
                    "phone": "",
                    "department": "",
                    "position": "测测测",
                    "address": "",
                    "houseNumber": "",
                    "longitude": "0.000000",
                    "latitude": "0.000000",
                    "weixinUrl": "",
                    "remark": "",
                    "gmtCreated": "2020-11-06 15:27:43",
                    "gmtUpdated": "2020-11-06 15:27:43"
                }],
                "images": [],
                "tags": [{
                    "tagName": "云联业务",
                    "id": "5416",
                    "customerId": "7159",
                    "tagId": "50",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "自主报名",
                    "id": "5417",
                    "customerId": "7159",
                    "tagId": "49",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "意向不明",
                    "id": "5418",
                    "customerId": "7159",
                    "tagId": "48",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "意向签约",
                    "id": "5419",
                    "customerId": "7159",
                    "tagId": "47",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "短期客户",
                    "id": "5420",
                    "customerId": "7159",
                    "tagId": "4",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "长期客户",
                    "id": "5421",
                    "customerId": "7159",
                    "tagId": "3",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "合作意愿弱",
                    "id": "5422",
                    "customerId": "7159",
                    "tagId": "2",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "合作意愿强",
                    "id": "5423",
                    "customerId": "7159",
                    "tagId": "1",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }],
                "pbmInfo": "",
                "chainInfo": "",
                "report": [],
                "statusText": "",
                "customerId": "7159",
                "userId": "306",
                "type": "1",
                "customerName": "测试新增客户自动化",
                "pinyin": "测试新增客户自动化",
                "customerType": "1",
                "customerTypeText": "连锁药店",
                "customerStatus": "3",
                "customerStatusText": "有意向未签约",
                "grade": "0",
                "gradeText": "未知",
                "mobile": "",
                "level": "2",
                "levelText": "省级分公司",
                "longitude": "118.779335",
                "latitude": "31.971964",
                "distance": "0",
                "address": "江苏省南京市雨花台区凤信路6号金证南京科技园2号楼中梁地产集团财务共享服务中心",
                "houseNumber": "",
                "zipCode": "",
                "fax": "",
                "remark": "",
                "organizationName": "",
                "cooperationCode": "",
                "organizationId": "0",
                "partnerId": "0",
                "gmtCreated": "2020-11-06 15:27:42",
                "gmtUpdated": "2020-11-06 15:27:42",
                "poolPartnerId": "0",
                "applyId": "0",
                "applyStoreId": "0",
                "insuranceApplyId": "0",
                "topStatus": "0",
                "visitStatus": "0",
                "visitStatusText": ""
            },
            "subCustomer": {
                "contacts": [],
                "images": [],
                "tags": [],
                "pbmInfo": {
                    "pbmNum": "0",
                    "notPbmNum": "0"
                },
                "chainInfo": {
                    "store_count_of_partner": "0",
                    "assistant_count_of_partner": "0",
                    "fund_pool": "0"
                },
                "report": [],
                "statusText": "",
                "customerId": "0",
                "userId": "0",
                "type": "0",
                "customerName": "",
                "pinyin": "",
                "customerType": "0",
                "customerTypeText": "",
                "customerStatus": "0",
                "customerStatusText": "",
                "grade": "0",
                "gradeText": "",
                "mobile": "",
                "level": "0",
                "levelText": "",
                "longitude": "",
                "latitude": "",
                "distance": "0",
                "address": "",
                "houseNumber": "",
                "zipCode": "",
                "fax": "",
                "remark": "",
                "organizationName": "",
                "cooperationCode": "",
                "organizationId": "0",
                "partnerId": "0",
                "gmtCreated": "",
                "gmtUpdated": "",
                "poolPartnerId": "0",
                "applyId": "0",
                "applyStoreId": "0",
                "insuranceApplyId": "0",
                "topStatus": "0",
                "visitStatus": "0",
                "visitStatusText": ""
            },
            "images": [],
            "users": {
                "v4Role": "",
                "id": "306",
                "account": "18099990000",
                "member_id": "15961232",
                "full_name": "张大仙",
                "role": "0",
                "status": "1",
                "created_at": "2020-03-11 01:09:59",
                "updated_at": "2020-11-06 15:26:20",
                "last_login_at": "2020-11-06 15:26:20",
                "head_img": "",
                "app_version": "",
                "superuser": "0",
                "superior": "0",
                "role_id": "0"
            },
            "name": "",
            "userName": "张大仙",
            "isDataComplete": "1",
            "partnerId": "0",
            "visitId": "1331",
            "customerId": "7159",
            "userId": "306",
            "content": "添加计划拜访",
            "visitType": "1",
            "visitTypeText": "常规拜访",
            "visitDate": "2020-11-06",
            "visitStatus": "1",
            "visitStatusText": "计划拜访",
            "arrivalTime": "2020-11-06 15:39:01",
            "departureTime": "",
            "summary": "",
            "description": "",
            "address": "",
            "longitude": "0.000000",
            "latitude": "0.000000",
            "overDistance": 0,
            "gmtCreated": "2020-11-06 15:33:26",
            "gmtUpdated": "2020-11-06 15:39:01",
            "isTempCustomerVisit": "0",
            "comment": "",
            "customerName": "测试新增客户自动化",
            "subCustomerName": ""
        }

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	客户拜访到总部")
        return self.response


class VisitVisitComplete(httpHandler):
    def __init__(self):
        super(VisitVisitComplete, self).__init__()
        self.host = "http://assistant.backend.turboradio.cn"
        self.path = "/visit/visitComplete"
        self.headers = {"Content-Type": "application/json;charset=UTF-8",
                        "Authorization": "Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
        self.params = None
        self.data = {
            "customer": {
                "contacts": [{
                    "contactId": "615",
                    "customerId": "7159",
                    "userId": "306",
                    "contactName": "张大仙",
                    "sex": "0",
                    "sexText": "女",
                    "mobile": "15233331112",
                    "phone": "",
                    "department": "",
                    "position": "测测测",
                    "address": "",
                    "houseNumber": "",
                    "longitude": "0.000000",
                    "latitude": "0.000000",
                    "weixinUrl": "",
                    "remark": "",
                    "gmtCreated": "2020-11-06 15:27:43",
                    "gmtUpdated": "2020-11-06 15:27:43"
                }],
                "images": [],
                "tags": [{
                    "tagName": "云联业务",
                    "id": "5416",
                    "customerId": "7159",
                    "tagId": "50",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "自主报名",
                    "id": "5417",
                    "customerId": "7159",
                    "tagId": "49",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "意向不明",
                    "id": "5418",
                    "customerId": "7159",
                    "tagId": "48",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "意向签约",
                    "id": "5419",
                    "customerId": "7159",
                    "tagId": "47",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "短期客户",
                    "id": "5420",
                    "customerId": "7159",
                    "tagId": "4",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "长期客户",
                    "id": "5421",
                    "customerId": "7159",
                    "tagId": "3",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "合作意愿弱",
                    "id": "5422",
                    "customerId": "7159",
                    "tagId": "2",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }, {
                    "tagName": "合作意愿强",
                    "id": "5423",
                    "customerId": "7159",
                    "tagId": "1",
                    "sort": "0",
                    "is_select": "0",
                    "selectText": "未选中"
                }],
                "pbmInfo": "",
                "chainInfo": "",
                "report": [],
                "statusText": "",
                "customerId": "7159",
                "userId": "306",
                "type": "1",
                "customerName": "测试新增客户自动化",
                "pinyin": "测试新增客户自动化",
                "customerType": "1",
                "customerTypeText": "连锁药店",
                "customerStatus": "3",
                "customerStatusText": "有意向未签约",
                "grade": "0",
                "gradeText": "未知",
                "mobile": "",
                "level": "2",
                "levelText": "省级分公司",
                "longitude": "118.779335",
                "latitude": "31.971964",
                "distance": "0",
                "address": "江苏省南京市雨花台区凤信路6号金证南京科技园2号楼中梁地产集团财务共享服务中心",
                "houseNumber": "",
                "zipCode": "",
                "fax": "",
                "remark": "",
                "organizationName": "",
                "cooperationCode": "",
                "organizationId": "0",
                "partnerId": "0",
                "gmtCreated": "2020-11-06 15:27:42",
                "gmtUpdated": "2020-11-06 15:27:42",
                "poolPartnerId": "0",
                "applyId": "0",
                "applyStoreId": "0",
                "insuranceApplyId": "0",
                "topStatus": "0",
                "visitStatus": "0",
                "visitStatusText": ""
            },
            "subCustomer": {
                "contacts": [],
                "images": [],
                "tags": [],
                "pbmInfo": {
                    "pbmNum": "0",
                    "notPbmNum": "0"
                },
                "chainInfo": {
                    "store_count_of_partner": "0",
                    "assistant_count_of_partner": "0",
                    "fund_pool": "0"
                },
                "report": [],
                "statusText": "",
                "customerId": "0",
                "userId": "0",
                "type": "0",
                "customerName": "",
                "pinyin": "",
                "customerType": "0",
                "customerTypeText": "",
                "customerStatus": "0",
                "customerStatusText": "",
                "grade": "0",
                "gradeText": "",
                "mobile": "",
                "level": "0",
                "levelText": "",
                "longitude": "",
                "latitude": "",
                "distance": "0",
                "address": "",
                "houseNumber": "",
                "zipCode": "",
                "fax": "",
                "remark": "",
                "organizationName": "",
                "cooperationCode": "",
                "organizationId": "0",
                "partnerId": "0",
                "gmtCreated": "",
                "gmtUpdated": "",
                "poolPartnerId": "0",
                "applyId": "0",
                "applyStoreId": "0",
                "insuranceApplyId": "0",
                "topStatus": "0",
                "visitStatus": "0",
                "visitStatusText": ""
            },
            "images": [{
                "imgUrl": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/v3063oba4f3m9r4idtbbrni1us.jpg",
                "visitId": "1331"
            }],
            "users": {
                "v4Role": "",
                "id": "306",
                "account": "18099990000",
                "member_id": "15961232",
                "full_name": "张大仙",
                "role": "0",
                "status": "1",
                "created_at": "2020-03-11 01:09:59",
                "updated_at": "2020-11-06 15:26:20",
                "last_login_at": "2020-11-06 15:26:20",
                "head_img": "",
                "app_version": "",
                "superuser": "0",
                "superior": "0",
                "role_id": "0"
            },
            "name": "",
            "userName": "张大仙",
            "isDataComplete": "1",
            "partnerId": "0",
            "visitId": "1331",
            "customerId": "7159",
            "userId": "306",
            "content": "添加计划拜访",
            "visitType": "1",
            "visitTypeText": "常规拜访",
            "visitDate": "2020-11-06",
            "visitStatus": "2",
            "visitStatusText": "已到达",
            "arrivalTime": "2020-11-06 15:40:37",
            "departureTime": "",
            "summary": "测试拜访自动化",
            "description": "",
            "address": "",
            "longitude": "0.000000",
            "latitude": "0.000000",
            "overDistance": "0",
            "gmtCreated": "2020-11-06 15:33:26",
            "gmtUpdated": "2020-11-06 15:40:37",
            "isTempCustomerVisit": "0",
            "comment": "",
            "subCustomerId": "0",
            "customerName": "测试新增客户自动化",
            "customerStatus": "3",
            "customerStatusText": "有意向未签约"
        }

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	客户拜访完成")
        return self.response



class VisitAddInterimVisit(httpHandler):
	def __init__(self):
		super(VisitAddInterimVisit, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/visit/addInterimVisit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "userId": "306",
 "visitId": "",
 "userName": "张大仙",
 "customerId": "7159",
 "customerName": "测试新增客户自动化（勿动）",
 "subCustomerName": "",
 "subCustomerAddress": "",
 "customerLongitude": "",
 "customerLatitude": "",
 "visitType": "2",
 "content": "",
 "visitDate": "2020-11-18",
 "overDistance": 0,
 "longitude": "118.779335",
 "latitude": "31.971964"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	临时拜访已到达")
		return self.response


class VisitPaging(httpHandler):
	def __init__(self):
		super(VisitPaging, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/visit/paging"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "visitStatus": [3, 5],
 "fromDate": "2020-11-18",
 "endDate": "2020-11-18",
 "manageId": "",
 "manageName": "",
 "customerName": "",
 "page": 1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	拜访记录列表")
		return self.response


class VisitInfo(httpHandler):
	def __init__(self):
		super(VisitInfo, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/visit/info"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "visitId": "1359",
 "userId": "306"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	拜访记录详情")
		return self.response


class InspectStart(httpHandler):
	def __init__(self):
		super(InspectStart, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/inspect/start"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "mapLon": "118.779305",
 "storeId": "105981",
 "remark": "距离过远自动化测试",
 "mapLat": "31.971830",
 "address": "江苏省南京市雨花台区凤信路靠近泽天能源东楼"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	新建巡店")
		return self.response


class MerchantStoreUpdate(httpHandler):
	def __init__(self):
		super(MerchantStoreUpdate, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/storeUpdate"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "storeId": "105981",
 "shortName": "益丰江栀大药房",
 "businessEndTime": "21:30",
 "mapLat": "31.971812",
 "storePhone": "",
 "subAddress": "",
 "address": "江苏省南京市雨花台区凤信路靠近泽天能源东楼",
 "image": "",
 "mapLon": "118.779324",
 "isDirect": "1",
 "isAllDay": "0",
 "businessStartTime": "07:30"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	修改门店地址信息")
		return self.response


class InspectUpdate(httpHandler):
	def __init__(self):
		super(InspectUpdate, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/inspect/update"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "mapLat": "31.971813",
 "mapLon": "118.779312",
 "address": "江苏省南京市雨花台区凤信路靠近泽天能源东楼",
 "remark": "巡店完成距离过远",
 "inspectId": "50511",
 "images": [{
  "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/nsopafbo6figaj2mu6l2gne46t.jpg",
  "type": "1"
 }, {
  "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/7s95odu3nohegk8d037m0o1epp.jpg",
  "type": "2"
 }, {
  "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/tprv5gunukq6p2k17rcrsvm293.jpg",
  "type": "2"
 }, {
  "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/vblt3ij77k9ead5t4fk68qckig.jpg",
  "type": "3"
 }, {
  "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/v2asl3v9f7i10ja63voik1g43q.jpg",
  "type": "3"
 }, {
  "url": "http:\/\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\/backend.assistant\/6c11db6u1dca13o6qjpc657aaq.jpg",
  "type": "4"
 }],
 "trains": []
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	完成巡店")
		return self.response


class InspectList(httpHandler):
	def __init__(self):
		super(InspectList, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/inspect/list"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "endTime": "2020-11-18 23:59:59",
 "partnerId": "",
 "limit": "10",
 "storeName": "",
 "storeId": "",
 "startTime": "2020-11-18 00:00:00",
 "page": "1"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	巡店记录列表")
		return self.response


class InspectDetail(httpHandler):
	def __init__(self):
		super(InspectDetail, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/inspect/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "id": "50511"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	巡店记录详情")
		return self.response


class MerchantList(httpHandler):
	def __init__(self):
		super(MerchantList, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/list"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "limit": 10,
 "page": 1,
 "common_name": "",
 "userId": "306"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	商户管理列表")
		return self.response


class MerchantInfo(httpHandler):
	def __init__(self):
		super(MerchantInfo, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/info"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "partnerId": "3"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	商户管理详情")
		return self.response


class MerchantStoreList(httpHandler):
	def __init__(self):
		super(MerchantStoreList, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/storeList"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "page": 1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	门店管理列表")
		return self.response


class MerchantStoreDetail(httpHandler):
	def __init__(self):
		super(MerchantStoreDetail, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/storeDetail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "storeId": "125756"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	门店管理详情")
		return self.response


class AssistantRegister(httpHandler):
	def __init__(self):
		super(AssistantRegister, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/assistant/register"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {
 "partnerId": "125610",
 "storeId": "125756",
 "fullName": "香香2",
 "account": "15899663122",
 "code": "8026",
 "role": 2,
 "jobNumber": "",
 "userId": "323",
 "partnerName": "吉林信康",
 "storeName": "金门分店",
 "autoLogin": 0,
 "newAide": "1"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	门店管理添加店员")
		return self.response


class V4CodeSend(httpHandler):
	def __init__(self):
		super(V4CodeSend, self).__init__()
		self.host = "http://app.turboradio.cn"
		self.path = "/v4/code/send"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e4"}
		self.params = None
		self.data = {"mobile":"15122222223","sendMethod":"sms","usage":"register"}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	添加店员获取验证码")
		return self.response


class MerchantStoreIsCanAdd(httpHandler):
	def __init__(self):
		super(MerchantStoreIsCanAdd, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/storeIsCanAdd"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {
    "internal_id": "1127",
    "cooperation": "fengchengyiyao"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	门店管理查询门店是否存在")
		return self.response


class MerchantStorePush(httpHandler):
	def __init__(self):
		super(MerchantStorePush, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/storePush"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {"address":"高密市阚家镇驻地","common_name":"第一百二十七连锁店","cooperation":"fengchengyiyao","created_at":"2020-12-21 14:43:53","id":"93","internal_id":"1127","number":"1127","out_id":"0","partners_name":"凤城医药","phone":"18706560495","status":"1","updated_at":"2020-12-21 14:43:53","user_id":"287"}


	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	门店管理推送门店")
		return self.response


class AssistantLists(httpHandler):
	def __init__(self):
		super(AssistantLists, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/assistant/lists"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {
 "page": 1
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	店员管理列表")
		return self.response


class AssistantDetail(httpHandler):
	def __init__(self):
		super(AssistantDetail, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/assistant/detail"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {
 "id": "200268"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	店员管理详情")
		return self.response


class AssistantStoreTransfer(httpHandler):
	def __init__(self):
		super(AssistantStoreTransfer, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/assistant/storeTransfer"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {
 "assistantId": "200268",
 "storeId": "125755"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	店员管理调店")
		return self.response


class AssistantUpdate(httpHandler):
	def __init__(self):
		super(AssistantUpdate, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/assistant/update"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {
    "chainIdBefore":"125610",
    "chainNameBefore":"梨树县信康大药房连锁有限公司",
    "storeIdBefore":"125755",
    "storeNameBefore":"恒升分店",
	"assistantId": "200268",
    "chainIdAfter":"125610",
    "chainNameAfter":"梨树县信康大药房连锁有限公司",
	"storeIdAfter": "125755",
    "storeNameAfter":"恒升分店",
    "submitReason":"cecece"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	店员管理调岗/编辑工号")
		return self.response


class WorkList(httpHandler):
	def __init__(self):
		super(WorkList, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/work/list"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer 0b388249-0c35-4e54-bc2e-2d66408df0e5"}
		self.params = None
		self.data = {
 "assistantId": "200268",
 "storeId": "125755"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"done" + "	店员管理调岗/编辑工号")
		return self.response
		

class WorkJob(httpHandler):
	def __init__(self):
		super(WorkJob, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/work/job"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	执行门店任务脚本")
		return self.response


class WorkCancel(httpHandler):
	def __init__(self):
		super(WorkCancel, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/work/cancel"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "id": "8962",
    "remark": "取消门店任务自动化20210513",
    "type": 1,
    "userId": "306"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	取消门店任务")
		return self.response


class WorkAccept(httpHandler):
	def __init__(self):
		super(WorkAccept, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/work/accept"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "workId": "8964"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	领取门店任务")
		return self.response


class WorkRecordCreate(httpHandler):
	def __init__(self):
		super(WorkRecordCreate, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/workRecord/create"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "communicateImages": [
        "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/qalrl3lteu3ngf7hoks22qqvc6.jpg"
    ],
    "communicateType": 2,
    "remark": "线上拜访自动化测试结束",
    "summary": [
        "5",
        "6"
    ],
    "workId": "78"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	完成线上门店任务")
		return self.response


class WorkRecordComplete(httpHandler):
	def __init__(self):
		super(WorkRecordComplete, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/workRecord/complete"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
    "communicateImages": [
        "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant/qalrl3lteu3ngf7hoks22qqvc6.jpg"
    ],
    "communicateType": 2,
    "remark": "线上拜访自动化测试结束",
    "summary": [
        "5",
        "6"
    ],
    "workId": "78"
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	完成线上门店任务")
		return self.response


class MerchantAllList(httpHandler):
	def __init__(self):
		super(MerchantAllList, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/merchant/allList"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "userId": "323",
 "page": 1,
 "limit": 10,
 "businessTypeArr": [1, 4],
 "common_name": ""
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	已合作连锁列表")
		return self.response


class ApprovalAddApprovalVisit(httpHandler):
	def __init__(self):
		super(ApprovalAddApprovalVisit, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/approvalAdd/approvalVisit"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "businessType": "1",
 "isCooperation": "1",
 "merchantId": "240329",
 "merchantName": "成大方圆医药连锁有限公司抚顺地区",
 "merchantAddress": "",
 "merchantSigning": "",
 "isReserved": "1",
 "visitDate": "2021-07-8",
 "visitTimes": "0",
 "visitTarget": [{
  "name": "秘密",
  "mobile": "88993744",
  "positionType": "2",
  "positionTypeText": "运营负责人",
  "positionOther": ""
 }],
 "visitContent": [{
  "goalId": "2",
  "departmentId": "1",
  "typeId": "1",
  "cooperationStatus": "1",
  "cooperationStatusText": "已合作",
  "signStatus": "0",
  "signStatusText": "未知",
  "display": "1",
  "displayText": "显示",
  "goal": "超级会员日活动业务上线沟通",
  "summary": "完成超级会员日活动政策上线沟通及确定连锁已充分了解政策并确定上线节点",
  "guideTitle": "",
  "guideContent": "",
  "gmtCreated": "2021-01-19 15:54:59",
  "gmtUpdated": "2021-01-19 15:54:59"
 }],
 "approval": {
  "approveType": "18",
  "applyName": "连锁拜访",
  "approveSettingId": "18",
  "processList": [{
   "taskSetting": [],
   "processSettingId": "1507",
   "approveSettingId": "18",
   "processType": "2",
   "customDuplicater": "0",
   "processName": "抄送人",
   "approverType": "1",
   "operateType": "1",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "1506",
   "gmtCreated": "2021-04-12 18:31:11",
   "gmtUpdated": "2021-04-12 18:31:11",
   "processUserList": [{
    "approverSettingId": "4491",
    "processSettingId": "1507",
    "approverGenre": "1",
    "relatedId": "323",
    "relatedName": "张俊超02",
    "avatar": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2834285391,2876082627&fm=26&gp=0.jpg",
    "mobile": "15380905486",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "323",
    "userName": "张俊超02"
   }]
  }, {
   "taskSetting": [],
   "processSettingId": "1506",
   "approveSettingId": "18",
   "processType": "1",
   "customDuplicater": "0",
   "processName": "运营审批",
   "approverType": "1",
   "operateType": "2",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "1505",
   "gmtCreated": "2021-04-12 18:31:11",
   "gmtUpdated": "2021-04-12 18:31:11",
   "processUserList": [{
    "approverSettingId": "4487",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "238",
    "userName": "康小强"
   }, {
    "approverSettingId": "4488",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "4129",
    "relatedName": "陈斌",
    "avatar": "",
    "mobile": "15905147519",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "4129",
    "userName": "陈斌"
   }, {
    "approverSettingId": "4489",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "287",
    "relatedName": "张俊超",
    "avatar": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2834285391,2876082627&fm=26&gp=0.jpg",
    "mobile": "15150578643",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "287",
    "userName": "张俊超"
   }, {
    "approverSettingId": "4490",
    "processSettingId": "1506",
    "approverGenre": "1",
    "relatedId": "4186",
    "relatedName": "肖文瑶",
    "avatar": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
    "mobile": "15651711729",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "4186",
    "userName": "肖文瑶"
   }]
  }, {
   "taskSetting": [],
   "processSettingId": "1505",
   "approveSettingId": "18",
   "processType": "2",
   "customDuplicater": "0",
   "processName": "抄送人",
   "approverType": "1",
   "operateType": "1",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "0",
   "gmtCreated": "2021-04-12 18:31:11",
   "gmtUpdated": "2021-04-12 18:31:11",
   "processUserList": [{
    "approverSettingId": "4486",
    "processSettingId": "1505",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-12 18:31:11",
    "gmtUpdated": "2021-04-12 18:31:11",
    "userId": "238",
    "userName": "康小强"
   }]
  }]
 }
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	申请连锁拜访")
		return self.response


class ApprovalAddApprovalSign(httpHandler):
	def __init__(self):
		super(ApprovalAddApprovalSign, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/approvalAdd/approvalSign"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "businessType": "1",
 "isCooperation": "1",
 "merchantId": "239911",
 "merchantName": "江西黄庆仁栈",
 "isReserved": "1",
 "merchantAddress": "",
 "merchantSigning": "",
 "visitDate": "2021-07-8",
 "visitTarget": [{
  "name": "测试",
  "mobile": "15933364445",
  "positionType": 2,
  "positionTypeText": "运营负责人"
 }],
 "visitContent": [{
  "goalId": "47",
  "departmentId": "2",
  "typeId": "2",
  "cooperationStatus": "0",
  "cooperationStatusText": "未知",
  "signStatus": "1",
  "signStatusText": "已签约",
  "display": "1",
  "displayText": "显示",
  "goal": "标准补充协议-药联增值服务＆药品直付补充协议",
  "summary": "完成非标补充协议-药联增值服务＆药品直付补充协议盖章签订",
  "guideTitle": "",
  "guideContent": "",
  "gmtCreated": "2021-01-20 11:49:59",
  "gmtUpdated": "2021-01-20 11:49:59"
 }],
 "approval": {
  "approveType": "19",
  "applyName": "连锁签约",
  "approveSettingId": "19",
  "processList": [{
   "taskSetting": [],
   "processSettingId": "1512",
   "approveSettingId": "19",
   "processType": "2",
   "customDuplicater": "0",
   "processName": "抄送人",
   "approverType": "1",
   "operateType": "1",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "1511",
   "gmtCreated": "2021-04-13 15:11:08",
   "gmtUpdated": "2021-04-13 15:11:08",
   "processUserList": [{
    "approverSettingId": "4497",
    "processSettingId": "1512",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-13 15:11:08",
    "gmtUpdated": "2021-04-13 15:11:08",
    "userId": "238",
    "userName": "康小强"
   }]
  }, {
   "taskSetting": [],
   "processSettingId": "1511",
   "approveSettingId": "19",
   "processType": "1",
   "customDuplicater": "0",
   "processName": "部门审批负责人",
   "approverType": "1",
   "operateType": "2",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "0",
   "gmtCreated": "2021-04-13 15:11:08",
   "gmtUpdated": "2021-04-13 15:11:08",
   "processUserList": [{
    "approverSettingId": "4495",
    "processSettingId": "1511",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-13 15:11:08",
    "gmtUpdated": "2021-04-13 15:11:08",
    "userId": "238",
    "userName": "康小强"
   }, {
    "approverSettingId": "4496",
    "processSettingId": "1511",
    "approverGenre": "1",
    "relatedId": "4186",
    "relatedName": "肖文瑶",
    "avatar": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
    "mobile": "15651711729",
    "gmtCreated": "2021-04-13 15:11:08",
    "gmtUpdated": "2021-04-13 15:11:08",
    "userId": "4186",
    "userName": "肖文瑶"
   }]
  }]
 }
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	申请连锁签约")
		return self.response


class ApprovalAddApprovalTrain(httpHandler):
	def __init__(self):
		super(ApprovalAddApprovalTrain, self).__init__()
		self.host = "http://assistant.backend.turboradio.cn"
		self.path = "/approvalAdd/approvalTrain"
		self.headers = {"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer"}
		self.params = None
		self.data = {
 "businessType": "1",
 "merchantId": "240320",
 "merchantName": "扬州市百信缘医药连锁有限公司DTP",
 "merchantAddress": "",
 "visitDate": "2021-07-8",
 "trainType": 2,
 "trainTypeText": "连锁全员培训",
 "trainNumber": "33",
 "isReserved": "1",
 "visitContent": [{
  "goalId": "64",
  "departmentId": "2",
  "typeId": "3",
  "cooperationStatus": "0",
  "cooperationStatusText": "未知",
  "signStatus": "0",
  "signStatusText": "未知",
  "display": "1",
  "displayText": "显示",
  "goal": "增值服务产品及销售流程培训",
  "summary": "完成增值服务产品及销售流程培训出单销售技巧培训以及参与培训人员已充分了解，熟悉操作",
  "guideTitle": "",
  "guideContent": "",
  "gmtCreated": "2021-01-20 11:49:59",
  "gmtUpdated": "2021-01-20 11:49:59"
 }, {
  "goalId": "65",
  "departmentId": "2",
  "typeId": "3",
  "cooperationStatus": "0",
  "cooperationStatusText": "未知",
  "signStatus": "0",
  "signStatusText": "未知",
  "display": "1",
  "displayText": "显示",
  "goal": "增值服务产品活动政策培训",
  "summary": "完成增值服务产品活动政策培训及确认，参与培训人员已充分了解，熟悉操作",
  "guideTitle": "",
  "guideContent": "",
  "gmtCreated": "2021-01-20 11:49:59",
  "gmtUpdated": "2021-01-20 11:49:59"
 }],
 "approval": {
  "approveType": "20",
  "applyName": "连锁培训",
  "approveSettingId": "20",
  "processList": [{
   "taskSetting": [],
   "processSettingId": "1496",
   "approveSettingId": "20",
   "processType": "2",
   "customDuplicater": "0",
   "processName": "抄送人",
   "approverType": "1",
   "operateType": "1",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "1495",
   "gmtCreated": "2021-04-12 16:48:53",
   "gmtUpdated": "2021-04-12 16:48:53",
   "processUserList": [{
    "approverSettingId": "4475",
    "processSettingId": "1496",
    "approverGenre": "1",
    "relatedId": "4129",
    "relatedName": "陈斌",
    "avatar": "",
    "mobile": "15905147519",
    "gmtCreated": "2021-04-12 16:48:53",
    "gmtUpdated": "2021-04-12 16:48:53",
    "userId": "4129",
    "userName": "陈斌"
   }]
  }, {
   "taskSetting": [],
   "processSettingId": "1495",
   "approveSettingId": "20",
   "processType": "1",
   "customDuplicater": "0",
   "processName": "部门负责人",
   "approverType": "1",
   "operateType": "3",
   "optionalType": "1",
   "approverArea": "1",
   "nextId": "0",
   "gmtCreated": "2021-04-12 16:48:53",
   "gmtUpdated": "2021-04-12 16:48:53",
   "processUserList": [{
    "approverSettingId": "4473",
    "processSettingId": "1495",
    "approverGenre": "1",
    "relatedId": "238",
    "relatedName": "康小强",
    "avatar": "http://uniondrug-release.oss-cn-shanghai.aliyuncs.com/backend.assistant.manage/gvlj45t2rdnksfgidnt2pnmoj4.jpeg",
    "mobile": "15150533368",
    "gmtCreated": "2021-04-12 16:48:53",
    "gmtUpdated": "2021-04-12 16:48:53",
    "userId": "238",
    "userName": "康小强"
   }, {
    "approverSettingId": "4474",
    "processSettingId": "1495",
    "approverGenre": "1",
    "relatedId": "4186",
    "relatedName": "肖文瑶",
    "avatar": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20200507%2F611083a06f4b486186df0558bb7a5925.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1628154553",
    "mobile": "15651711729",
    "gmtCreated": "2021-04-12 16:48:53",
    "gmtUpdated": "2021-04-12 16:48:53",
    "userId": "4186",
    "userName": "肖文瑶"
   }]
  }]
 }
}

	def changeEnv(self,env):
		self.host = self.host.replace("turboradio.cn",env)

	def excute(self):
		if self.params != None:
			for k in self.params.keys():
				self.path = self.path+self.params[k]
		self.response = self.run(1)
		self.logger.info(self.path +"	done" + "	申请连锁培训")
		return self.response