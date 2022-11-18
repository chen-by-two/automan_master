import requests
import KeyWordDriver.CommonKeyWord as ckw

class CommonInterface():

    def __init__(self):
        pass
    #获取药店宝最新token
    def getToken(self):
        sqlToken = "SELECT token FROM `cn_uniondrug_backend_app`.`token` WHERE `assistantId` = '20083722' ORDER BY `gmtCreated` DESC LIMIT 1 "
        print(sqlToken)
        newToken = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data", sqlToken)
        print(newToken)
        return newToken

    #获取微信最新token
    def getWeChat(self):
        sqlToken = "SELECT token FROM `cn_uniondrug_backend_auth`.`member_token` WHERE `memberId` = '16236586' AND `channel` = 'wechat' LIMIT 0,1000 "
        print(sqlToken)
        wechatToken = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data", sqlToken)
        print(wechatToken)
        return wechatToken

    # 药店宝关键字搜药
    def searchDrug(self,  data1,header1):
        url = "https://app.uniondrug.net/v4/drugs/search"
        header = {"Content-Type": "application/json", "authorization": "Bearer cdcf5f86-7981-48ae-9933-e6a735417448","Content-Length":"","Host":"app.uniondrug.net"}
        res = requests.post(url=url, headers=header1, json=data1)
        return res

    # 药店宝推药
    def pushDrug(self,data2,header2):
        url = "https://app.uniondrug.net/v4/drugs/pushDrug"
        res = requests.post(url=url, headers=header2, data=data2)
        return res

    # 加购物车
    def checkCounselorAddCart(self,data3,header3):
        url = "https://eshop.uniondrug.net/api/cart/checkCounselorAddCart"
        res = requests.post(url=url, headers=header3, data=data3)
        return res

    # 清空购物车
    def clearUpCart(self,data4,header3):
        url = "https://eshop.uniondrug.net/api/cart/clearUpCart"
        res = requests.post(url=url, headers=header3, data=data4)
        return res

    # 创建预订单，拿到requestNo
    def createPreviewOrder(self, data5, header3):
        url = "https://eshop.uniondrug.net/api/order/createPreviewOrder"
        res = requests.post(url=url, headers=header3, data=data5)
        return res

    #提交订单
    def orderCreateOrder(self,data5, header3):
        url = "https://pm-dpsp-tc-order.uniondrug.net/order/createOrder"
        res = requests.post(url=url, headers=header3, data=data5)
        return res

    #支付
    def payment(self,data6):
        url = "http://java.pmc.cashier.uniondrug.net/notify/payment"
        header4 = {"Content-Type": "application/json"}
        res = requests.post(url=url,  data=data6,headers=header4)
        return res

    #查询线上门店列表
    def storeO2OGetShopList(self,data7):
        url = "https://eshop.uniondrug.net/admin/api/storeO2O/getShopList"
        header4 = {"Content-Type": "application/json","authorization":"Bearer 3c6aa4cf-c692-415c-bb16-f7d6e18811d0"}
        res = requests.post(url=url,  data=data7,headers=header4)
        return res

    #停用线上门店
    def updateStoreOnline1(self,data8):
        url = "https://eshop.uniondrug.net/admin/api/storeO2O/updateStoreOnline"
        header4 = {"Content-Type": "application/json","authorization":"Bearer 3c6aa4cf-c692-415c-bb16-f7d6e18811d0"}
        res = requests.post(url=url,  data=data8,headers=header4)
        return res

    #开启线上门店
    def updateStoreOnline2(self,data9):
        url = "https://eshop.uniondrug.net/admin/api/storeO2O/updateStoreOnline"
        header4 = {"Content-Type": "application/json","authorization":"Bearer 3c6aa4cf-c692-415c-bb16-f7d6e18811d0"}
        res = requests.post(url=url,  data=data9,headers=header4)
        return res
    
    #完善用药人信息
    def updatePreOrder(self,data10,header3):
        url = "https://pm-dpsp-tc-order.uniondrug.net/order/updatePreOrder"
        res = requests.post(url=url, headers=header3, data=data10)
        return res

    # 重置下单信息11
    def orderInit(self,data11,header3):
        url = "https://pm-dpsp-tc-order.uniondrug.net/order/init"
        res = requests.post(url=url, headers=header3, data=data11)
        return res

