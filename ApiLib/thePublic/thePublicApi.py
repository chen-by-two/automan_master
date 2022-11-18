# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class ThePublicLoginSendCaptcha(httpHandler):
    def __init__(self):
        super(ThePublicLoginSendCaptcha, self).__init__()
        self.host = "https://auth-backend.turboradio.cn"
        self.path = "/login/sendCaptcha"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"mobile": "18923425589"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	公众号验证码发送接口")
        return self.response


class ThePublicLoginLogin(httpHandler):
    def __init__(self):
        super(ThePublicLoginLogin, self).__init__()
        self.host = "https://auth-backend.turboradio.cn"
        self.path = "/login/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"mobile": "18923425589", "code": "919136", "channel": {"type": "wechat",
                                                                            "openid": "jTcu+kAfgxtzPrgVMgGtilKR5tIahkXZpdpWnMXuCbVf1rS/9EGU7NB0puGdD+6JXNRRumvOPi1z4PwGivZG8vLoJ+1sKDgWzDmL9XQ1WU1qQVWpJj+vaTlXqEIgPq3Q/KSbW2jv7LbimexGOuY2BDJHZkylL/NamkCnsUByCKOcowijm6On3H17b6+mwAquRrGfffqNh7HHb91EHRId+tO04eOtlZWfNpR9VTFVeLhD2Kl8Dzx8zSR7Po9Ogh93oDSsLN+1xgZXxJC0CClIspS3MAo2WfQPVICRXDpls/ZaCmSpeD5PKP+bz2/Udn/HTa4MAcHHaqR43ixm8IFrJQ==",
                                                                            "encryptOpenid": "jTcu+kAfgxtzPrgVMgGtilKR5tIahkXZpdpWnMXuCbVf1rS/9EGU7NB0puGdD+6JXNRRumvOPi1z4PwGivZG8vLoJ+1sKDgWzDmL9XQ1WU1qQVWpJj+vaTlXqEIgPq3Q/KSbW2jv7LbimexGOuY2BDJHZkylL/NamkCnsUByCKOcowijm6On3H17b6+mwAquRrGfffqNh7HHb91EHRId+tO04eOtlZWfNpR9VTFVeLhD2Kl8Dzx8zSR7Po9Ogh93oDSsLN+1xgZXxJC0CClIspS3MAo2WfQPVICRXDpls/ZaCmSpeD5PKP+bz2/Udn/HTa4MAcHHaqR43ixm8IFrJQ==",
                                                                            "img": "http://thirdwx.qlogo.cn/mmopen/vwLEibamy4gOCUR45zJIqN3ycggsGwZ3ZpIDHqPDwyGdSjictldZfYjztlXDo47ThEYEpoESqGBRtCTmvtJK5ly80m3YnTOJKV/132",
                                                                            "nickname": "Regret", "sex": "1"}}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	公众号登录")
        return self.response


class VMemberDetail(httpHandler):
    def __init__(self):
        super(VMemberDetail, self).__init__()
        self.host = "https://wxapi.turboradio.cn"
        self.path = "/v/member/detail"
        self.headers = {"Content-Type": "application/json;charset=UTF-9",
                        "Authorization": "Token eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	公众号个人信息")
        return self.response


class VProjectUserCheck(httpHandler):
    def __init__(self):
        super(VProjectUserCheck, self).__init__()
        self.host = "https://activate-equity-backend.turboradio.cn"
        self.path = "/v/project/user/check"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {"cdKey": "VATS6JBU", "channel": "cdKey"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	公众号领取电子权益码提交")
        return self.response


class VProjectUserDetail(httpHandler):
    def __init__(self):
        super(VProjectUserDetail, self).__init__()
        self.host = "https://activate-equity-backend.turboradio.cn"
        self.path = "/v/project/user/detail"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {"cdKey": "VATS6JBU", "channel": "cdKey"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	公众号权益次卡领取信息确认")
        return self.response


class VEquityNewActivate(httpHandler):
    def __init__(self):
        super(VEquityNewActivate, self).__init__()
        self.host = "https://activate-equity-backend.turboradio.cn"
        self.path = "/v/equity/newActivate"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {"projectId": "415989", "groupId": "2875", "equityName": "自动化次卡电子码1",
                     "orderNo": "PC8353454084EFBDC3E4DB0F7138", "equityStyle": "2", "isActived": "yes",
                     "equityType": "1", "availableFrom": "2020-09-07 00:00:00", "availableTo": "2025-10-31 23:59:59",
                     "memberId": "0", "merchantId": "7", "programId": "107", "nominalValue": "3.00",
                     "nominalTimes": "3", "oneTimeValue": "1.00", "customerId": "482", "equityGroupId": "2676",
                     "effectiveType": "3", "validityPeriod": "1880", "limitOfReceive": "0", "isUnlimitedQuantity": "2",
                     "mobile": "18923455589", "code": None, "openId": "of-FXw3E_XH6sjbqlvleX1u7rZYg",
                     "channel": "cdKey"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	公众号权益次卡激活信息确认提交")
        return self.response


class VWxUserinfo(httpHandler):
    def __init__(self):
        super(VWxUserinfo, self).__init__()
        self.host = "https://activate-equity-backend.turboradio.cn"
        self.path = "/v/wx/userinfo"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {"openId": "of-FXw3E_XH6sjbqlvleX1u7rZYg", "channel": "cdKey"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + "	权益激活回调")
        return self.response


class ExtTemplateOperate(httpHandler):
    def __init__(self):
        super(ExtTemplateOperate, self).__init__()
        self.host = "http://msg.backend.turboradio.cn"
        self.path = "/extTemplate/operate"
        self.headers = {"Content-Type": "application/json"}
        self.params = None
        self.data = {"operate": "set", "key": "verifyCode_valid_13262567360", "data": "123456"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + " 公众号写死登录验证码")
        return self.response


class VProjectUserCondition(httpHandler):
    def __init__(self):
        super(VProjectUserCondition, self).__init__()
        self.host = "https://activate-equity-backend.turboradio.cn"
        self.path = "/v/project/user/condition"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {
            "type": "odx_dWxZnpesie_kDj-hNvvP2YiJpzxlx3O4bc3FWE5mpfBnWZEggCwIqF1BsTNpZ7Ni2m8BmsAk4MQG86ITxRsTIK24GcZpkdELWpEzQTRzIMsq11PAINVUrc37dMpAkGpCpahqhVZNoqhBeMWKr-16sncBiyF-ed-dTnNNWpDGh0HhSWrQjXq2rdZEE0g27rf3ZZ4rjdriO46MRzr1cTo7SV-9Gzn8cfVYmVACk_B7oyc6lT2DfYKTp4tee1nYZbAShL-nK3g12iblFQNoeR9Kq6PMpwBKtUtKpM0volhGtWzBAiJ7d-tXbB6tv0ojeA==",
            "channel": "userInfo"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + " 雇主清单次卡获取当前用户认证信息")
        return self.response


class VProjectUserGroup(httpHandler):
    def __init__(self):
        super(VProjectUserGroup, self).__init__()
        self.host = "https://activate-equity-backend.turboradio.cn"
        self.path = "/v/project/user/group"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjQ3NDUsInd4T3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF93ZWNoYXRfMTU5NjQ3NDUiLCJ2YWx1ZSI6IjEzIn0sImluZm8iOnsibmFtZSI6IiIsIm1vYmlsZSI6IjE4OTIzNDU1NTg5In0sImNoYW5uZWwiOnsib3BlbmlkIjoib2YtRlh3M0VfWEg2c2picWx2bGVYMXU3clpZZyIsInR5cGUiOiJ3ZWNoYXQifX0.QkEidMGn23evF_Kh65psgF7BdYaC10cV82569poyHrvRIeb5JQkzGMrtQ-UQo0hIX9Us7bqDh48QxLi7BIfXwJl_sup7GcHcuK0eBMT-JGkEiQ2aO1JYgUY12DnDNM_8-SUj4sfQydyNZIna2fOHIFZP0UuDRBIFTeNujgP6LaQUII4RTKUYKsRaKNnwDQ1vk3VsqoCqSSHfpW69lea_wdX61KY9OXqU0QpevlfLjTeszD37pWjsoQckBPl68WAEI2X5hlJViud4P8FQiAJ_3elSugZ-cxb7Ty03SyVvctGpY_NQe6ll8XZtaF0x8cvP9LvOB5dSvVjO07clf72NGQ"}
        self.params = None
        self.data = {"groupId": "zLkkaAm7g5ouJCILiz2BJgjcxXY=", "channel": "qrCodeLink"}

    def changeEnv(self, env):
        self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "\tdone" + " 通用码获取权益详情")
        return self.response
