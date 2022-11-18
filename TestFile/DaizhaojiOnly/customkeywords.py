import requests
import pymysql
import json


class BackstageManagementLogin():
    def __init__(self):
        self.url = "http://uncenter.backend.turboradio.cn"
        self.path1 = "/sms/send"
        self.path2 = "/dd/mobilelogin"
        self.path3 = "/dd/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        self.host = "udtest.uniondrug.com"
        self.port = 6033
        self.username = "test"
        self.password = "tset@321abc"

    def getcaptcha(self):
        try:
            data = {'mobile': self.loginmobile}
            response = requests.post(self.url + self.path1, headers=self.headers, json=data)
            # print(response.content.decode('unicode-escape'))
            res = response.content.decode()
            res = json.loads(res)
            try:
                assert res["errno"] == '0'
            except:
                print("=" * 30 + "/sms/send返回异常"+"=" * 30)
            conn = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password)
            cursor = conn.cursor()
            # print(cursor)
            sql = "SELECT captcha FROM cn_uniondrug_module_data.captcha WHERE mobile = " + str(
                self.loginmobile) + " order by id desc limit 1;"
            # print(sql)
            cursor.execute(sql)
            sqlres = cursor.fetchone()
            try:
                assert sqlres != None
            except:
                print("=" * 30 + "数据库查询异常"+"=" * 30)
            cursor.close()
            conn.close()
            # print("sqlRes", sqlres)
            # print(type(sqlres))
            # print("getcaptcha", sqlres[0])
            captcha = sqlres[0]
            self.captcha = captcha
            return self.captcha
        except:
            print("="*30+"getcaptcha异常"+"="*30)

    def gettoken(self):
        try:
            self.captcha = self.getcaptcha()
            # print("gettoken", self.captcha)
            data = {"mobile": self.loginmobile, "code": self.captcha}
            # print(data)
            response = requests.post(self.url + self.path2, headers=self.headers, json=data)
            # print(response.content.decode())
            res = response.content.decode()
            # print(type(res))
            res = json.loads(res)
            try:
                assert res["errno"] == '0'
            except:
                print("=" * 30 + "/dd/mobilelogin返回异常"+"=" * 30)
            # print(type(res))
            # print(res["data"]["token"])
            self.token = res["data"]["token"]
            return self.token
        except:
            print("=" * 30 + "gettoken异常"+"=" * 30)

    def getauthorization(self,loginmobile):
        try:
            self.loginmobile = loginmobile
            self.token = self.gettoken()
            # print(self.token)
            data = {"token": self.token}
            response = requests.post(self.url + self.path3, headers=self.headers, json=data)
            # print(response.content.decode())
            res = response.content.decode()
            res = json.loads(res)
            # print(res)
            try:
                assert res["errno"] == '0'
            except:
                print("=" * 30 + "/dd/login返回异常"+"=" * 30)
            self.authorization = res["data"]["token"]
            # print(self.authorization)
            self.authorization = "Bearer "+self.authorization
            print(self.authorization)
            return self.authorization
        except:
            print("=" * 30 + "getauthorization异常"+"=" * 30)

class OfficialAccountsLogin():
    def __init__(self):
        self.url = "http://uncenter.backend.turboradio.cn"
        self.path1 = "/sms/send"
        self.path2 = "/dd/mobilelogin"
        self.path3 = "/dd/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

if __name__ == '__main__':
    bmlogin = BackstageManagementLogin()
    # bmlogin.getcaptcha()
    # bmlogin.gettoken()
    bmlogin.getauthorization(13333333333)
