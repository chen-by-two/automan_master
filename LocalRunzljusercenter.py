from datetime import datetime

import os
import pytest
import shutil

import Common.ImportApiFromExcelzlj as importApi
import Common.ImportTestCaseFromExcelzlj as importCase



if __name__ == '__main__':
    #更新接口
    importApi.impotApi().readExcel()
    #更新用例
    importCase.impotTestCase("/Users/zhanglijun/PycharmProjects/automan4/TestFile/zlj/ApiTestCasezljusercenter.xlsx","userCenter").readExcel()
    #执行用例
    repName = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    alluredir = "report/" + repName
    pytest.main(["-s", "testCase/userCenter", "-q", "--alluredir", alluredir])
    #生成可视化报告
    if os.path.exists(os.path.join(os.path.dirname(__file__),"allure-report")):
        shutil.rmtree(os.path.join(os.path.dirname(__file__),"allure-report"))
    os.system("allure generate "+alluredir+ " -o allure-report")
