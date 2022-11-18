import requests
import  json

class TestPartner(object):

    def testPartnerDetail(self):
        self.url="http://ps-finance-data.turboradio.cn/partner/detail"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"organizationId": "578"}
        res = requests.post(self.url,json=self.data)
        print("请求头：", res.request.headers)
        print("状态码：", res.status_code)
        print("响应正文：", res.text)

        assert res.status_code == 200

    def testMerchantInfo(self):
        self.url="http://ps-finance-data.turboradio.cn/merchant/info"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"organizationId": "578"}
        res = requests.post(self.url,json=self.data)
        print("请求头：", res.request.headers)
        print("状态码：", res.status_code)
        print("响应正文：", res.text)

        assert res.status_code == 200

    def testPartnerBillDetail(self):
        self.url = "http://ps-finance-data.turboradio.cn/partner/bill/info/detail"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.params = None
        self.data = {"unitId": "578"}
        res = requests.post(self.url, json=self.data)
        print("请求头：", res.request.headers)
        print("状态码：", res.status_code)
        print("响应正文：", res.text)

        assert res.status_code == 200
