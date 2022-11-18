# coding: utf-8

import os
import Common.ImportApiFromExcel as importApi
import Common.ImportTestCaseFromExcel as importCase
import shutil,pytest
from datetime import datetime


if __name__ == '__main__':

    # 更新接口
    #importApi.impotApi('phoneCenter',ifall=False).readExcel()
    #导入单接口
    # print(os.path.join(os.getcwd(), 'TestFile\ApiTestCase.xlsx'))
    # importCase.impotTestCase(os.path.join(os.getcwd(),'TestFile\ApiTestCase.xlsx'),'phoneCenter1').readExcel()

    # 执行用例
    repName = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    alluredir = "report/" + repName
    pytest.main(["-s", "testCase/phoneCenter", "-q", "--alluredir", alluredir])
    # 生成可视化报告
    if os.path.exists(os.path.join(os.path.dirname(__file__), "allure-report")):
        shutil.rmtree(os.path.join(os.path.dirname(__file__), "allure-report"))
    os.system("allure generate " + alluredir + " -o allure-report")

    print(alluredir)