# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


# 药店宝创建普通药品订单购物车
class OrdersCart(httpHandler):
    def __init__(self):
        super(OrdersCart, self).__init__()
        self.host = "https://app.turboradio.cn"
        self.path = "/v4/orders/cart"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "version": "4.44",
                        "Authorization": "Bearer dbdfaf52-5391-4619-a308-4bc71eb40717"}
        self.params = None
        self.data = {"gmtScanAt": "2020-12-03 10:52:57", "cartRecordId": "0", "waterNo": "", "cartDrugs": [
            {"approvalNumber": "国药准字H13024082", "commonAliasPinyiin": "ffafwap",
             "commonFullPinyin": "{\"commonFullPinyin\":\"fufanganfenwananpian\",\"memberPrice\":\"297.00\",\"isRule\":false,\"productPoint\":0,\"originalPrice\":\"297.00\",\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}",
             "commonName": "复方氨酚烷胺片", "count": 1, "form": "14片/盒", "hasAdd": "false", "id": "69485",
             "internalId": "3254", "isChange": "true", "isDrug": "true", "isDtp": "0", "isLast": "false", "isRule": "0",
             "isRx": "0", "isSelected": "false", "isSuper": "0", "manufacturer": "", "memberPrice": "297.00",
             "money": "297.00", "originalPrice": "0", "pack": "", "partnerId": "45", "pointMsg": "", "quantity": "1",
             "tradeCode": "6934366601288", "unitPrice": "297.00"}], "orderMethod": 3, "isShow": "0", "promotions": [],
                     "cartProducts": [{"productId": "50"}], "erpSn": "", "equityId": "28811617",
                     "entrance": "{\"code\":\"105268421130060953\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811617\",\"orderChannel\":\"wechat\"}",
                     "prescriptions": [], "items": [{"internalId": "3254", "quantity": "1"}], "memberId": "15961482"}

    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "药店宝购物车")
        return self.response


# 药店宝创建普通药品订单购物车
class DtpOrdersCart(httpHandler):
    def __init__(self):
        super(DtpOrdersCart, self).__init__()
        self.host = "https://app.turboradio.cn"
        self.path = "/v4/orders/cart"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "version": "4.44",
                        "Authorization": "Bearer 5535f1c2-f754-4010-93bb-c54eb420c123"}
        self.params = None
        self.data = {"gmtScanAt": "2020-12-03 10:52:57", "cartRecordId": "0", "waterNo": "", "cartDrugs": [
            {"approvalNumber": "国药准字H13024082", "commonAliasPinyiin": "ffafwap",
             "commonFullPinyin": "{\"commonFullPinyin\":\"fufanganfenwananpian\",\"memberPrice\":\"297.00\",\"isRule\":false,\"productPoint\":0,\"originalPrice\":\"297.00\",\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}",
             "commonName": "复方氨酚烷胺片", "count": 1, "form": "14片/盒", "hasAdd": "false", "id": "69485",
             "internalId": "3254", "isChange": "true", "isDrug": "true", "isDtp": "1", "isLast": "false", "isRule": "0",
             "isRx": "0", "isSelected": "false", "isSuper": "0", "manufacturer": "", "memberPrice": "297.00",
             "money": "297.00", "originalPrice": "0", "pack": "", "partnerId": "45", "pointMsg": "", "quantity": "1",
             "tradeCode": "6934366601288", "unitPrice": "297.00"}], "orderMethod": 3, "isShow": "0", "promotions": [],
                     "cartProducts": [{"productId": "50"}], "erpSn": "", "equityId": "28811617",
                     "entrance": "{\"code\":\"105268421130060953\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811617\",\"orderChannel\":\"wechat\"}",
                     "prescriptions": [], "items": [{"internalId": "3254", "quantity": "1"}], "memberId": "15961482"}

    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "药店宝DTP药品购物车")
        return self.response


# 调取商户中心接口开通指定连锁为村医模式
class MerhantVillageDoctor(httpHandler):
    def __init__(self):
        super(MerhantVillageDoctor, self).__init__()
        self.host = "http://merchant.module.turboradio.cn"
        self.path = "/organizebasebackend/editwholesale"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"organizationId": "132169", "isWholesale": "1"}

    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "商户中心开通村医模式")
        return self.response


# 药店宝创建村医模式药品订单购物车
class VillageDoctorOrdersCart(httpHandler):
    def __init__(self):
        super(VillageDoctorOrdersCart, self).__init__()
        self.host = "https://app.turboradio.cn"
        self.path = "/v4/orders/cart"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "version": "4.44",
                        "Authorization": "Bearer 5535f1c2-f754-4010-93bb-c54eb420c123"}
        self.params = None
        self.data = {"gmtScanAt": "2020-12-03 10:52:57", "cartRecordId": "0", "waterNo": "", "cartDrugs": [
            {"approvalNumber": "国药准字H13024082", "commonAliasPinyiin": "ffafwap",
             "commonFullPinyin": "{\"commonFullPinyin\":\"fufanganfenwananpian\",\"memberPrice\":\"297.00\",\"isRule\":false,\"productPoint\":0,\"originalPrice\":\"297.00\",\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}",
             "commonName": "复方氨酚烷胺片", "count": 1, "form": "14片/盒", "hasAdd": "false", "id": "69485",
             "internalId": "3254", "isChange": "true", "isDrug": "true", "isDtp": "0", "isLast": "false", "isRule": "0",
             "isRx": "0", "isSelected": "false", "isSuper": "0", "manufacturer": "", "memberPrice": "297.00",
             "money": "297.00", "originalPrice": "0", "pack": "", "partnerId": "45", "pointMsg": "", "quantity": "1",
             "tradeCode": "6934366601288", "unitPrice": "297.00"}], "orderMethod": 3, "isShow": "0", "promotions": [],
                     "cartProducts": [{"productId": "50"}], "erpSn": "", "equityId": "28811617",
                     "entrance": "{\"code\":\"105268421130060953\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811617\",\"orderChannel\":\"wechat\"}",
                     "prescriptions": [], "items": [{"internalId": "3254", "quantity": "1"}], "memberId": "15961482"}

    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "药店宝创建村医模式药品订单购物车")
        return self.response

# 调取商户中心接口开通指定连锁开启处方
class Recipe(httpHandler):
    def __init__(self):
        super(Recipe, self).__init__()
        self.host = "http://merchant.module.turboradio.cn"
        self.path = "/organizebase/editelectronic"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"organizationId": "578", "isElectronic": "1"}

    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "商户中心开通连锁村医")
        return self.response

# 药店宝创建村医模式药品订单购物车
class RecipeCart(httpHandler):
    def __init__(self):
        super(RecipeCart, self).__init__()
        self.host = "https://app.turboradio.cn"
        self.path = "/v4/orders/cart"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "version": "4.44",
                        "Authorization": "Bearer 5535f1c2-f754-4010-93bb-c54eb420c123"}
        self.params = None
        self.data = {"gmtScanAt":"2021-01-08 11:39:55","cartRecordId":"0","waterNo":"c2507684b339232ada225a49852f4253","cartDrugs":[{"approvalNumber":"国药准字Z41020695","commonAliasPinyiin":"qzxfw","commonFullPinyin":"{\"commonFullPinyin\":\"qizhixiangfuwan\",\"memberPrice\":5,\"isRule\":false,\"productPoint\":0,\"originalPrice\":1000,\"image\":\"http:\\/\\/uniondrug.oss-cn-hangzhou.aliyuncs.com\\/Icon\\/drug_common.png\"}","commonName":"七制香附丸","count":1,"form":"6g*10袋","hasAdd":"false","id":"3","internalId":"01138","isChange":"true","isDrug":"true","isDtp":"0","isLast":"false","isRule":"false","isRx":"1","isSelected":"false","isSuper":0,"manufacturer":"","memberPrice":"5","money":"1000.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"","quantity":"1","tradeCode":"","unitPrice":"1000"},{"approvalNumber":"国药准字Z22020394","commonAliasPinyiin":"kgzsp","commonFullPinyin":"{\"commonFullPinyin\":\"kangguzengshengpian\",\"memberPrice\":0.01,\"isRule\":false,\"productPoint\":0,\"originalPrice\":288,\"image\":\"http:\\/\\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\\/oss\\/upload\\/file\\/goods\\/1567407661654.jpg\"}","commonName":"抗骨增生片","count":1,"form":"24s","hasAdd":"false","id":"","internalId":"01234","isChange":"true","isDrug":"true","isDtp":"0","isLast":"false","isRule":"false","isRx":"0","isSelected":"false","isSuper":0,"manufacturer":"","memberPrice":"0.01","money":"288.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"预计单件可得11.11积分","quantity":"1","tradeCode":"6943750066107","unitPrice":"288"}],"orderMethod":3,"isShow":"0","promotions":[],"cartProducts":[{"productId":"50"}],"erpSn":"","equityId":"28811598","entrance":"{\"code\":\"103947485544233857\",\"channel\":\"10\",\"memberId\":\"15961482\",\"accountId\":\"28811598\",\"orderChannel\":\"wechat\"}","prescriptions":[{"image":"","waterNo":"30c92b126e316446adcfb2ad327a05d9"}],"items":[{"internalId":"01138","quantity":"1"},{"internalId":"01234","quantity":"1"}],"memberId":"15961482"}

    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "药店宝创建处方药+处方单药品订单购物车")
        return self.response


# 药店宝创建换药理赔订单购物车
class RenewCart(httpHandler):
    def __init__(self):
        super(RenewCart, self).__init__()
        self.host = "https://app.turboradio.cn"
        self.path = "/v4/orders/cart"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "version": "4.44",
                        "Authorization": "Bearer 5535f1c2-f754-4010-93bb-c54eb420c123"}
        self.params = None
        self.data ={"gmtScanAt":"2021-01-08 15:51:17","cartRecordId":"0","waterNo":"9c0a48c8744dd1f59a1bea4d751aac3d","cartDrugs":[{"approvalNumber":"国药准字Z22020394","commonAliasPinyiin":"kgzsp","commonFullPinyin":"{\"commonFullPinyin\":\"kangguzengshengpian\",\"memberPrice\":0.01,\"isRule\":false,\"productPoint\":0,\"originalPrice\":288,\"image\":\"http:\\/\\/uniondrug-release.oss-cn-shanghai.aliyuncs.com\\/oss\\/upload\\/file\\/goods\\/1567407661654.jpg\"}","commonName":"抗骨增生片","count":1,"form":"24s","hasAdd":"false","id":"","internalId":"01234","isChange":"false","isDrug":"true","isDtp":"0","isLast":"false","isRule":"0","isRx":"0","isSelected":"false","isSuper":"0","manufacturer":"","memberPrice":"0.01","money":"288.00","originalPrice":"0","pack":"","partnerId":"45","pointMsg":"预计单件可得11.11积分","quantity":"1","tradeCode":"6943750066107","unitPrice":"288"}],"orderMethod":3,"isShow":"0","itemId":"200826470030","promotions":[],"cartProducts":[],"erpSn":"","equityId":"0","entrance":"{\"code\":\"104089288032103429\",\"channel\":\"10\",\"memberId\":\"1107820\",\"entrance\":\"5\",\"claimNo\":\"200826470030\",\"orderChannel\":\"wechat\"}","prescriptions":[],"items":[{"internalId":"01234","quantity":"1"}],"memberId":"1107820"}
    def changeEnv(self, envgs):
        self.host = self.host.replace("turboradio.cn", envgs)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "药店宝创建换药理赔订单购物车")
        return self.response






