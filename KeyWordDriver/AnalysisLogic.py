# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import os, xlrd,re


class readLogic:
    def __init__(self,info):
        self.keyWordInfo = info

    def read(self):
        modules = self.keyWordInfo.sheet_names()
        for module in modules:
            path = os.path.dirname(__file__)
            modulePath = os.path.join(path, "../testCase", module)
            # 如果模块目录已经存在就不创建，如果不存在就创建一个模块目录
            if os.path.exists(modulePath):
                pass
            else:
                os.makedirs(modulePath)

            with open(modulePath + "/" + "test_" + module + "KwCases.py", mode="w") as f0:
                f0.truncate()
                f0.close()
            with open(modulePath + "/" + "test_" + module + "KwCases.py", mode="a",encoding="UTF-8") as f:
                codes = self.writeCase(self.analysisCase(module))
                f.write("# -*- coding: utf-8 -*-\n")
                f.write("import pytest,os,allure\n")
                f.write("import KeyWordDriver.CommonKeyWord as ckw\n\n")
                f.write("import KeyWordDriver.BusinesskeyWord as bkw\n\n")
                f.write("class Test_" + module + ":\n")
                for code in codes:
                    f.write(code)
                f.close()

            print(os.getcwd() + "/" + module)
            print(os.path.exists(os.getcwd() + "/" + module))

    def analysisCase(self, module):
        testCases = self.keyWordInfo.sheet_by_name(module)
        result = {}
        tmpoo = []
        tmpCaseId = ""
        # 获取行数,根据行数循环
        # 跳过表头
        for i in range(testCases.nrows):
            if i == 0:
                continue
            tmpKw = testCases.row_values(i)
            tmpCaseParam = []

            # 根据ID判断是否为同一用例，同一ID用例信息写到kv里面
            # 用例ID：用例信息list
            if not tmpCaseId == tmpKw[0]:
                tmpoo = []
                tmpCaseId = tmpKw[0]
                tmpCaseName = tmpKw[1]
                tmpCaseSeverity = tmpKw[2]
                tmpoo.append([tmpCaseName, tmpCaseSeverity])
            tmpCaseStepDesc = tmpKw[3]
            tmpCaseAssignment = tmpKw[4]
            tmpCaseKeyWord = tmpKw[5]
            tmpCaseAction = tmpKw[6]
            for p in tmpKw[7:tmpKw.__len__()]:
                if p != "":

                    tmpCaseParam.append(str(p))
            tmpoo.append([tmpCaseStepDesc, tmpCaseAssignment, tmpCaseKeyWord, tmpCaseAction, tmpCaseParam])
            result[tmpCaseId] = tmpoo

        # print(result)

        return result

    def writeCase(self, caseDict):
        commonKeyWordList = ["var","print","json","dict","db"]
        businessKeywordsList =["authApi","goodCenterApi","orderCenterApi","equityCenterApi"]
        result = []
        for key in caseDict.keys():

            case = caseDict[key]
            str0 = "\n\t@allure.feature(" + "\"" + case[0][0] + "\"" + ")\n" + \
                   "\t@allure.severity(" + "\"" + case[0][1] + "\"" + ")\n" + \
                   "\tdef test_" + key + "(self):\n"
            for kw in case[1:]:
                # 步骤描述写入到注释
                tmp = "\t\t# " + kw[0] + "\n"
                str0+=tmp
                tmp2 = "\t\t"
                tmp3 = "\t\t"
                tmp4 = "{"
                tmp5 = []
                #是对操作参数进行解析
                for p in kw[4]:
                    #如果包含了等于就会打包写成一个dict传入
                    if p.__contains__("="):
                        kk = p.split("=")
                        ke = None
                        va = ""
                        tmpva = ""

                        if len(kk)> 2:
                            for t in kk[1:]:

                                tmpva+=t
                        else:
                            tmpva = kk[1]

                        if kk[0].__contains__("${"):
                            ke = self.tuoke(kk[0])
                        else:
                            ke = "\"" + kk[0] + "\""

                        va = self.tuoke(tmpva)
                        tmp4 += ke + ":" + va + ","
                    else:
                        #这里是对参数里数字处理
                        if p.startswith("*") and p.endswith("*"):
                            tmp5.append(p.replace("*",""))
                        else:
                            #这里是对数组的打包,支持数组类型的传入，注意数组内部不支持参数化
                            if p.startswith("[") and p.endswith("]"):
                                tmp5.append(p)
                                continue

                            #这里是对参数化做处理
                            if p.__contains__("${"):
                                tmp5.append(self.tuoke(p))
                            else:
                                tmp5.append("\"" + p + "\"")
                tmp4 = tmp4[:-1]
                tmp4 += "}"


                # 判断是否需要赋值操作，不需要直接开始
                "".istitle()
                if kw[2].istitle():
                    # 这里是增加断言支持
                    if kw[2] == "Assert":
                        tmp2 += "assert ckw.CommonKeyWord()." + kw[2] + "_" + kw[3] + "("
                    else:
                        if kw[1] == "":
                            tmp2 += "ckw.CommonKeyWord()." + kw[2] + "_" + kw[3] + "("
                        else:
                            tmp2 += self.tuoke(kw[1]) + " = " + "ckw.CommonKeyWord()." + kw[2] + "_" + kw[3] + "("
                else:
                    if kw[1] == "":
                        tmp2 += "bkw." + kw[2] + "_" + kw[3] + "("
                    else:
                        tmp2 += self.tuoke(kw[1]) + " = " + "bkw." + kw[2] + "_" + kw[3] + "("

                # 如果没有字典参数，就正常传，有的话就先传字典参数，再传普通参数
                if tmp4.__len__() <= 3:
                    i = 0
                    for o in tmp5:
                        tmp2 += o
                        i += 1
                        if i > 0:
                            tmp2 += ","
                else:
                    tmp2 += str(tmp4) + ","
                    i = 0
                    for o in tmp5:
                        tmp2 += o
                        i += 1
                        if i > 0:
                            tmp2 += ","
                # 取出末尾多余的逗号

                if tmp2.endswith(","):
                    tmp2 = tmp2[:-1]
                tmp2 += ")\n"
                str0 += tmp2

            result.append(str0)
        return result



    def tuoke(self, s):
        tmp = s
        plist = re.findall(r'\${(.*?)}', s)
        for p in plist:
            print(p)
            tmp = re.sub(r'\${(.*?)}', p, tmp, 1)
        s = tmp
        return s

    def isNum(self,s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True


if __name__ == '__main__':
    a = readLogic("C:/Users/haoran/PycharmProjects/automan/TestFile/HaoRanOnly/keyword.xlsx")
    # b = a.tuoke2("{ss:${mobile},ww:${captcha}}")
    a.read()
    # print(b)
