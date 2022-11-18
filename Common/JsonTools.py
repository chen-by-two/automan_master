# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import json


# 传入json字典
def modifyJson(jsonDict, k, v):
    for key in jsonDict.keys():
        if k == key:
            jsonDict[k] = v
    return json.dumps(jsonDict)


# 取单个值
def getJsonValue(jsonDict, k):
    value = None
    if type(jsonDict) == str:
        jsonDict = eval(jsonDict)
    for key in k:
        if key.__len__() == 1:
            value = jsonDict[key[0]]
        if key.__len__() == 2:
            value = jsonDict[key[0]][key[1]]
        if key.__len__() == 3:
            value = jsonDict[key[0]][key[1]][key[2]]
        if key.__len__() == 4:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]]
        if key.__len__() == 5:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]]
        if key.__len__() == 6:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]][key[5]]
        if key.__len__() == 7:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]][key[5]][key[6]]
        if key.__len__() == 8:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]][key[5]][key[6]][key[7]]
    return value

# 批量取值，支持遍历四层
def getJsonValues(jsonDict, keyList):
    valueList = []
    if type(jsonDict) == str:
        jsonDict = eval(jsonDict)
    for key in keyList:

        if key.__len__() == 1:
            valueList.append(jsonDict[key[0]])
        if key.__len__() == 2:
            valueList.append(jsonDict[key[0]][key[1]])
        if key.__len__() == 3:
            valueList.append(jsonDict[key[0]][key[1]][key[2]])
        if key.__len__() == 4:
            valueList.append(jsonDict[key[0]][key[1]][key[2]][key[3]])
        if key.__len__() == 5:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]]
        if key.__len__() == 6:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]][key[5]]
        if key.__len__() == 7:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]][key[5]][key[6]]
        if key.__len__() == 8:
            value = jsonDict[key[0]][key[1]][key[2]][key[3]][key[4]][key[5]][key[6]][key[7]]
    return valueList


if __name__ == '__main__':
    # print(getValue({"asd": 1, "ww": 2}, "ss"))
    # print(getJsonValues({"errno":0, "error": "请求成功", "dataType": "OBJECT", "data":{"skuNo": "53219-5062011", "refNo": "5062011", "waterNo": "11270f74dbc14c0a90bf85d22bbb50e6", "serviceDetails":None, "originPrice":None, "salePrice":1.00, "channel":8, "saleState":0, "goodsType":1, "goodsSubType":19, "title": "洋槐蜂蜜", "subTitle":None, "isAgent":None, "totalAmount":None, "logoActivity":[], "highlights":[], "detailsImg":[], "packageIds":[], "packageExplainCos":None, "productServiceList":[{"name": "洋槐蜂蜜", "price":None, "icon":None, "description":None, "skuNo":"53219-5062011"}], "memberId":None}, "success":True, "fail":False}
    #                     , [["data","waterNo"]]))
    # print(modifyJson({"asd":1,"ww":2},"ww","asdad"))
    print(getJsonValue({"cardId": "24b8365e184d4c938186", "schemeId": "20200825102020675253", "memberId": "15961742", "cardLimit": "3", "cardBalance": "3", "status": "1", "statusText": "已激活", "gmtEffectedStart": "2020-10-22 00:00:00", "gmtEffectedEnd": "2023-07-17 23:59:59", "gmtLeadTime": "2020-10-22 11:16:11", "orderCount": "0", "cardSource": "00", "cardSourceText": "发放", "schemeInfo": {"cardName": "lhr满5-3营销卡", "payRule": {"payTypeText": "单次减免", "convertTypeText": "订单全额转权益", "payType": "1", "maxAmount": "0", "fullAmount": "5", "deductAmount": "3", "discount": "0", "convertType": "1", "convertAmount": "2", "serviceId": "20106"}, "partners": "915"}, "partnerLimit": "1"},[["sms","code"]]))
