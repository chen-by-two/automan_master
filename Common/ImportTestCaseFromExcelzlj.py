# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : zhanglijun
import os,xlrd
from KeyWordDriver.AnalysisLogic import readLogic as readLogic
class impotTestCase:
    def __init__(self,caseFilePath,suitNmae):

        self.caseInfo = xlrd.open_workbook(caseFilePath)
        self.suitName = suitNmae

    def kwReadExcel(self):
        kwRead = readLogic(self.caseInfo)
        kwRead.read()

    def readExcel(self):
        #通过sheet页获取功能模块
        sheets = self.caseInfo.sheet_names()
        #按照sheet页遍历并且写入接口
        for suit in sheets:
            path = os.path.dirname(__file__)
            modulePath = os.path.join(path,"../testCase",suit)
            #如果模块目录已经存在就不创建，如果不存在就创建一个模块目录
            if os.path.exists(modulePath):
                pass
            else:
                os.makedirs(modulePath)
            self.caseInfo.sheet_by_name(suit)
            #如果测试套文件存在就追加写，不存在就创建新的写
            if os.path.exists(modulePath + "/" + "test_" + self.suitName + "Cases.py"):
                with open(modulePath + "/" + "test_" + self.suitName + "Cases.py",mode="a",encoding="UTF-8") as f:
                    codes = self.writeApiTestCase(suit)
                    for code in codes:
                        f.write(code)
                    f.close()
            else:

                # open(modulePath + "/" + module + "Api.py")
                with open(modulePath + "/" + "test_" + self.suitName + "Cases.py",mode="a",encoding="UTF-8") as f:
                    codes = self.writeApiTestCase(suit)
                    f.write("# -*- coding: utf-8 -*-\n")
                    f.write("import pytest,os,allure\n")

                    for code in codes:
                        f.write(code)
                    f.close()


    def writeApiTestCase(self,suit):
        testCases = self.caseInfo.sheet_by_name(suit)
        resule = []
        modules = []
        for i in range(testCases.nrows):
            if i == 0:
                continue
            tmpapi = testCases.row_values(i)
            modules.append(tmpapi[0])
        modules = list(set(modules))
        for module in modules:
            resule.append("import ApiLib."+module+"."+module+"Api as "+module+"\n\n\n")
        resule.append("class "+"Test_"+suit+":\n")
        #获取行数,根据行数循环
        for i in range(testCases.nrows):
            if i == 0:
                continue
            tmpapi = testCases.row_values(i)
            mod = tmpapi[0]
            tmpapiName = tmpapi[1]
            tmpapiCaseName = tmpapi[2]
            tmpapiEnv = tmpapi[3]
            tmpapiHeaders = tmpapi[4]
            tmpapiParams = tmpapi[5]
            tmpapiData = tmpapi[6]
            tmpapiSeverity = tmpapi[7]
            tmpapiRange = tmpapi[8]
            tmpapiMatchRules = tmpapi[9]
            tmpapiExcepted = str(tmpapi[10]).split(".")[0]
            tmpapiDesc = tmpapi[11]

            finStr = ""
            str0 = "\n\t@allure.feature("+"\""+suit+"\""+")\n"+\
                "\t@allure.severity("+"\""+tmpapiSeverity+"\""+")\n"+\
                "\tdef test_"+tmpapiName+"_"+tmpapiCaseName+"(self):\n"+\
                "\t\t\"\"\"\n"+\
                "\t\t"+tmpapiDesc+"\n"+ \
                "\t\t\"\"\"\n" + \
                "\t\t" + tmpapiName + "=" + mod + "."+tmpapiName+"()\n"+ \
                "\t\t" + tmpapiName + "." +"headers = "+tmpapiHeaders+"\n"
            str1 = "\t\t" + tmpapiName + "." + "params = " + tmpapiParams + "\n"
            str2 = "\t\t" + tmpapiName + "." + "data = " + tmpapiData + "\n"
            str3 = "\t\t" + tmpapiName + "Res" + " = " + tmpapiName + ".excute()\n"

            str9 = "\t\t" + tmpapiName + "." + "changeEnv(" + "\"" + tmpapiEnv + "\"" +")\n"
            str4 = "\t\t" +"assert " + tmpapiName + "Res.status_code" + " == " + tmpapiExcepted + "\n"
            str5 = "\t\t" +"assert " + tmpapiName + "Res.text" + " == " + "\"" + tmpapiExcepted + "\"" + "\n"
            str6 = "\t\t" +"assert " + tmpapiName + "Res.headers" + " == " + "\"" + tmpapiExcepted + "\""+ "\n"
            str7 = "\t\t" +"assert " + tmpapiName + "Res.text" + ".__contains__(\"" + tmpapiExcepted + "\")\n"
            str8 = "\t\t" +"assert " + tmpapiName + "Res.headers" + ".__contains__(\"" + tmpapiExcepted + "\")\n"

            finStr = str0

            finStr+=str9
            if tmpapiParams != "None":
                finStr+=str1
            if tmpapiData != "None":
                finStr+=str2
            finStr+=str3
            if tmpapiRange == "响应码" and tmpapiMatchRules == "等于":
                finStr+=str4
            elif tmpapiRange == "响应头部" and tmpapiMatchRules == "等于":
                finStr+=str6
            elif tmpapiRange == "响应头部" and tmpapiMatchRules == "包含":
                finStr+=str8
            elif tmpapiRange == "响应体" and tmpapiMatchRules == "等于":
                finStr+=str5
            elif tmpapiRange == "响应体" and tmpapiMatchRules == "包含":
                finStr+=str7
            elif tmpapiRange == "响应体" and tmpapiMatchRules == "JSON":
                # tmpapiExcepted=预期结果，先按照"-"分割数组arr
                arr = tmpapiExcepted.split("-")
                # 将接口返回值转成json格式， e.g: result = UserCardGetByIdRes.json()
                str100 = "\t\t" + "result = " + tmpapiName + "Res.json()\n" \
                         "\t\tprint(\"" + tmpapiName + "Res: {0} \".format(result))\n" \
                         "\t\tif \"OBJECT\" == result[\"dataType\"]:\n\t\t\tr_data = result[\"data\"]\n" \
                         "\t\telif \"LIST\" == result[\"dataType\"]:\n\t\t\tr_data = result[\"data\"][0]\n"
                # 遍历数组arr, 拼装多个assert
                for kv in arr:
                    str100 += "\t\tp = str(r_data[\"" + \
                             kv.split(":")[0].strip('''"''') + "\"])\n\t\tassert p ==" + \
                             str(kv.split(":")[1].strip('''"''')) + "\"""\n"

                finStr+=str100
            elif tmpapiRange == "响应体" and tmpapiMatchRules == "JSON2":
                # 预期结果全等比较
                str110 = "\t\t" + "result = " + tmpapiName + "Res.json()\n" \
                         "\t\tprint(\"" + tmpapiName + "Res: {0} \".format(result))\n" \
                         "\t\tif \"OBJECT\" == result[\"dataType\"]:\n\t\t\tr_data = result[\"data\"]\n" \
                         "\t\telif \"LIST\" == result[\"dataType\"]:\n\t\t\tr_data = result[\"data\"][0]\n" \
                         "\t\tdiff = deepdiff.DeepDiff(r_data, " + tmpapiExcepted + ")\n\t\tassert any(diff)"
                # 利用deepdiff 直接比较两个json, 样例如下：
                '''
                d1 = {"a":{"a1":"123","a2":"456"},"b":{"b1":"135","b2":"246"},"d":{"b1":"135","b2":"246"}}
                d2 = {"a":{"a1":"123","a2":"456"},"c":{"b1":"135","b2":"246"},"b":{"b1":"1357","b2":"246"}}
                d3 = {"a": {"a1": "123", "a2": "456"}, "d": {"b2": "246", "b1": "135"}, "b": {"b1": "135", "b2": "246"}}
                diff = deepdiff.DeepDiff(d1, d3)
                print('JSON比较结果如下：\n')
                if any(diff):
                    print('增加项：%s\n' % diff['dictionary_item_added'])
                    print('删除项：%s\n' % diff['dictionary_item_removed'])
                    print('修改项：%s\n' % diff['values_changed'])
                else:
                    print('两个JSON一毛一样：\n')
                '''


                finStr += str110


            resule.append(finStr)

        print(resule)
        return resule

if __name__ == '__main__':
    ss = impotTestCase("/Users/liuhaoran/PycharmProjects/automan/TestFile/HaoRanOnly/ApiTestCase.xlsx","ProConn").readExcel()
    # with open("/Users/liuhaoran/PycharmProjects/automan/ApiLib/goodsCenter/goodsCenterApi.py",mode = "a") as f:
    #     lines = f.readlines()
    #     print(lines)
