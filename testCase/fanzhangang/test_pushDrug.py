from TestFile.fanzhangang.CommonInterface import CommonInterface
import pytest, os, allure
import json, time, datetime
import KeyWordDriver.CommonKeyWord as ckw
import TestFile.fanzhangang.fzgTestFile as fzgTestFile

class Test_Pushdrug:

    #线上推药测试case
    @allure.feature("樊战岗线上推药场景")
    @allure.severity("blocker")
    def test_pushDrugCase1(self):
        # 药店宝token
        global drugAppToken
        drugAppToken = "cdcf5f86-7981-48ae-9933-e6a735417448"
        # drugAppToken = CommonInterface.getToken(self)[0]["token"]
        # O2Otoken
        global eshoptoken
        # eshoptoken = CommonInterface.getWeChat(self)[0]["token"]
        # print("----------------", drugAppToken, eshoptoken, "------------------")
        eshoptoken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-9FGzuShNsYwdwA"
        # 查询门店线上列表，判断门店是否开通线上门店，没有开通线上门店时，调开通接口进行开通
        data7 = fzgTestFile.parameters[7]
        res7 = CommonInterface().storeO2OGetShopList(data7)
        if res7.json()["data"]["body"][0]["organizationId"] == "7590":
            print("------这是线上推药流程-------")
        else:
            data9 = fzgTestFile.parameters[9]
            CommonInterface().updateStoreOnline2(data9)

        # 第一步：搜药
        header1 = {"Content-Type": "application/json", "authorization": "Bearer " + drugAppToken}
        fzgTestFile.parameters[0]["keywords"] = "感冒灵胶囊"
        data1 = fzgTestFile.parameters[0]
        res1 = CommonInterface().searchDrug(data1, header1)
        print(res1.json())
        # 第二步：推药
        fzgTestFile.parameters[1]["drugs"][0]["image"] = res1.json()["data"]["body"][0]["image"]
        fzgTestFile.parameters[1]["drugs"][0]["originalPrice"] = res1.json()["data"]["body"][0]["originalPrice"]
        fzgTestFile.parameters[1]["drugs"][0]["money"] = res1.json()["data"]["body"][0]["originalPrice"]
        # fzgTestFile.parameters[1]["drugs"][0]["commonFullPinyin"] = res1.json()["data"]["body"][0]["commonFullPinyin"]
        fzgTestFile.parameters[1]["drugs"][0]["approvalNumber"] = res1.json()["data"]["body"][0]["approvalNumber"]
        fzgTestFile.parameters[1]["drugs"][0]["tradeCode"] = res1.json()["data"]["body"][0]["tradeCode"]
        fzgTestFile.parameters[1]["drugs"][0]["internalId"] = res1.json()["data"]["body"][0]["internalId"]
        fzgTestFile.parameters[1]["drugs"][0]["commonName"] = res1.json()["data"]["body"][0]["commonName"]
        fzgTestFile.parameters[1]["drugs"][0]["memberPrice"] = res1.json()["data"]["body"][0]["memberPrice"]
        data2 = json.dumps(fzgTestFile.parameters[1])
        header2 = {"content-type": "application/json;charset=utf-8", "authorization": "Bearer " + drugAppToken,
                   "Host": "app.uniondrug.net"}
        res2 = CommonInterface().pushDrug(data2, header2)
        print(res2.text)
        # 第三步：加购物车
        fzgTestFile.parameters[2]["batchId"] = res2.json()["data"]["batchId"]
        data3 = json.dumps(fzgTestFile.parameters[2])
        header3 = {"content-type": "application/json;charset=utf-8", "authorization": "Bearer " + eshoptoken}
        res3 = CommonInterface().checkCounselorAddCart(data3, header3)
        print(res3.text)
        # 第四步：清空购物车
        fzgTestFile.parameters[3]["products"][0]["sourceTradeCode"] = \
            res3.json()["data"]["display"]["76655f30a1f15ae0e192fb59e4c09b67"]["sourceTradeCode"]
        fzgTestFile.parameters[3]["products"][0]["tradeCode"] = \
            res3.json()["data"]["display"]["76655f30a1f15ae0e192fb59e4c09b67"]["tradeCode"]
        fzgTestFile.parameters[3]["batchId"] = res2.json()["data"]["batchId"]
        data4 = json.dumps(fzgTestFile.parameters[3])
        res4 = CommonInterface().clearUpCart(data4, header3)
        print(res4.text)
        # 第五步： 创建预订单，拿到requestNo
        data5 = json.dumps(fzgTestFile.parameters[4])
        res5 = CommonInterface().createPreviewOrder(data5, header3)
        print(res5.text)
        # 第六步：完善用药人信息
        fzgTestFile.parameters[10]["requestNo"] = res5.json()["data"]["requestNo"]
        data10 = json.dumps(fzgTestFile.parameters[10])
        res10 = CommonInterface().updatePreOrder(data10, header3)
        # 第七步：重置订单数据
        fzgTestFile.parameters[11]["requestNo"] = res5.json()["data"]["requestNo"]
        data11 = json.dumps(fzgTestFile.parameters[11])
        res11 = CommonInterface().orderInit(data11,header3)
        # 第八步：创建订单
        fzgTestFile.parameters[5]["requestNo"] = res5.json()["data"]["requestNo"]
        data5 = json.dumps(fzgTestFile.parameters[5])
        res6 = CommonInterface().orderCreateOrder(data5, header3)
        print(res6.json())
        # 第七步：支付
        getPaymentNo = "select payment_no from `cn_uniondrug_middleend_paymentcenter`.`pmc_pay_cashier` WHERE `out_trade_no` = {}".format(
            res6.json()["data"]["mainOrderNo"])
        print(getPaymentNo)
        paymentNo = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data", getPaymentNo)
        print(paymentNo)
        fzgTestFile.parameters[6]["paymentNo"] = paymentNo[0]["payment_no"]
        fzgTestFile.parameters[6]["outTradeNo"] = res6.json()["data"]["mainOrderNo"]
        time = datetime.datetime.now()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        fzgTestFile.parameters[6]["timeEnd"] = now_time
        data6 = json.dumps(fzgTestFile.parameters[6])
        res7 = CommonInterface().payment(data6)
        print(res7.json())
        assert res7.json()["errno"] == 0

    # 线下推药测试case
    @pytest.mark.flaky(retun=1, runs_delay=2)  # 失败重跑一次，在每次重试前都会等2s
    @allure.feature("樊战岗线下推药场景")
    @allure.severity("blocker")
    def test_pushDrugCase2(self):
        # 药店宝token
        # 药店宝token
        global drugAppToken
        drugAppToken = "cdcf5f86-7981-48ae-9933-e6a735417448"
        # drugAppToken = CommonInterface.getToken(self)[0]["token"]
        # O2Otoken
        global eshoptoken
        # eshoptoken = CommonInterface.getWeChat(self)[0]["token"]
        # print("----------------", drugAppToken, eshoptoken, "------------------")
        eshoptoken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTYyMzY1ODYsInd4T3BlbmlkIjoib3lseWx1TlN2aVNVekpGbGlVWnVxaUFyYm5jVSIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTYyMzY1ODYiLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU2YTBhXHU2MjE4XHU1Yzk3IiwibW9iaWxlIjoiMTgzNTQyOTk2ODcifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.CWwiH6j_F9sKZruqsHwF7eFWjJoBEaSq3EXukCTS--eWXluRHQyKDfIsTO8WdW85nR3Aeo4zpnUdJSvepgRT0GzxRxnHEFP01heRM1fvsYdk7cJaa_AYHOBoFQ05AdzT2UhsEiUR8-vblWzpIUIA-0XRBh39QK57me64RdNhuUxp71K7xZdYLTvu--Vx8tyKIGR0-wNbQSsAmFSHRpYDGW440OIRSje9UoOyuXt0g5PyEtbYVaRUGn37PW0dJv7TM9p1FpQd0ZA08A8yCe2_U-ccod5u-OllaKyEwH-3y1j7pyenDgADwyQ9BHSSQYVMGAX7UVb-9FGzuShNsYwdwA"
        # 查询门店线上列表，判断门店是否开通线上门店，没有开通线上门店时，调开通接口进行开通
        data7 = fzgTestFile.parameters[7]
        res7 = CommonInterface().storeO2OGetShopList(data7)
        if res7.json()["data"]["body"][0]["organizationId"] == "7590":
            data8 = fzgTestFile.parameters[8]
            CommonInterface().updateStoreOnline1(data8)
            print("------这是线下推药流程-------")

        # 第一步：搜药
        header1 = {"Content-Type": "application/json", "authorization": "Bearer " + drugAppToken}
        fzgTestFile.parameters[0]["keywords"] = "感冒灵胶囊"
        data1 = fzgTestFile.parameters[0]
        res1 = CommonInterface().searchDrug(data1, header1)
        print(res1.json())
        # 第二步：推药
        fzgTestFile.parameters[1]["drugs"][0]["image"] = res1.json()["data"]["body"][0]["image"]
        fzgTestFile.parameters[1]["drugs"][0]["originalPrice"] = res1.json()["data"]["body"][0]["originalPrice"]
        fzgTestFile.parameters[1]["drugs"][0]["money"] = res1.json()["data"]["body"][0]["originalPrice"]
        # fzgTestFile.parameters[1]["drugs"][0]["commonFullPinyin"] = res1.json()["data"]["body"][0]["commonFullPinyin"]
        fzgTestFile.parameters[1]["drugs"][0]["approvalNumber"] = res1.json()["data"]["body"][0]["approvalNumber"]
        fzgTestFile.parameters[1]["drugs"][0]["tradeCode"] = res1.json()["data"]["body"][0]["tradeCode"]
        fzgTestFile.parameters[1]["drugs"][0]["internalId"] = res1.json()["data"]["body"][0]["internalId"]
        fzgTestFile.parameters[1]["drugs"][0]["commonName"] = res1.json()["data"]["body"][0]["commonName"]
        fzgTestFile.parameters[1]["drugs"][0]["memberPrice"] = res1.json()["data"]["body"][0]["memberPrice"]
        data2 = json.dumps(fzgTestFile.parameters[1])
        header2 = {"content-type": "application/json;charset=utf-8",
                   "authorization": "Bearer " + drugAppToken,
                   "Host": "app.uniondrug.net"}
        res2 = CommonInterface().pushDrug(data2, header2)
        print(res2.text)
        # 第三步：加购物车
        fzgTestFile.parameters[2]["batchId"] = res2.json()["data"]["batchId"]
        data3 = json.dumps(fzgTestFile.parameters[2])
        header3 = {"content-type": "application/json;charset=utf-8",
                   "authorization": "Bearer " + eshoptoken}
        res3 = CommonInterface().checkCounselorAddCart(data3, header3)
        print(res3.text)
        # 第四步：清空购物车
        fzgTestFile.parameters[3]["products"][0]["sourceTradeCode"] = \
            res3.json()["data"]["display"]["76655f30a1f15ae0e192fb59e4c09b67"]["sourceTradeCode"]
        fzgTestFile.parameters[3]["products"][0]["tradeCode"] = \
            res3.json()["data"]["display"]["76655f30a1f15ae0e192fb59e4c09b67"]["tradeCode"]
        fzgTestFile.parameters[3]["batchId"] = res2.json()["data"]["batchId"]
        data4 = json.dumps(fzgTestFile.parameters[3])
        res4 = CommonInterface().clearUpCart(data4, header3)
        print(res4.text)
        # 第五步： 创建预订单，拿到requestNo
        data5 = json.dumps(fzgTestFile.parameters[4])
        res5 = CommonInterface().createPreviewOrder(data5, header3)
        print(res5.text)
        # 第六步：完善用药人信息
        fzgTestFile.parameters[10]["requestNo"] = res5.json()["data"]["requestNo"]
        data10 = json.dumps(fzgTestFile.parameters[10])
        res10 = CommonInterface().updatePreOrder(data10, header3)
        # 第七步：重置订单数据
        fzgTestFile.parameters[11]["requestNo"] = res5.json()["data"]["requestNo"]
        data11 = json.dumps(fzgTestFile.parameters[11])
        res11 = CommonInterface().orderInit(data11, header3)
        # 第八步：创建订单
        fzgTestFile.parameters[5]["requestNo"] = res5.json()["data"]["requestNo"]
        data5 = json.dumps(fzgTestFile.parameters[5])
        res6 = CommonInterface().orderCreateOrder(data5, header3)
        print(res6.json())
        # 第七步：支付
        getPaymentNo = "select payment_no from `cn_uniondrug_middleend_paymentcenter`.`pmc_pay_cashier` WHERE `out_trade_no` = {}".format(
            res6.json()["data"]["mainOrderNo"])
        print(getPaymentNo)
        paymentNo = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data", getPaymentNo)
        print(paymentNo)
        fzgTestFile.parameters[6]["paymentNo"] = paymentNo[0]["payment_no"]
        fzgTestFile.parameters[6]["outTradeNo"] = res6.json()["data"]["mainOrderNo"]
        time = datetime.datetime.now()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        fzgTestFile.parameters[6]["timeEnd"] = now_time
        data6 = json.dumps(fzgTestFile.parameters[6])
        res7 = CommonInterface().payment(data6)
        print(res7.json())
        assert res7.json()["errno"] == 0
