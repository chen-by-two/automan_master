# -*- coding: utf-8 -*-

from datetime import datetime

import os,shutil
import pytest

import Common.ImportApiFromExcel as importApi
import Common.ImportTestCaseFromExcel as importCase
import Common.Api2Bkw as importBkwApi

if __name__ == '__main__':

    # #更新接口
    importApi.impotApi().readExcel()
    #
    # #更新业务关键字接口
    # importBkwApi.impotBKWApi().do()

    #更新用例
    # importCase.impotTestCase("/Users/zoudw/PycharmProjects/automan/TestFile/ZhangJunChao/AssistantKeyword1.xlsx","assistantapp").readExcel()
    # importCase.impotTestCase("/Users/zoudw/PycharmProjects/automan/TestFile/O2OPlaceTheOrder/O2Oorderkeyword.xls","O2OFreightActivity").kwReadExcel()

    #执行用例
    repName = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    alluredir = "report/" + repName
    pytest.main(["-s", "testCase/O2OAddSignNameCard", "-q", "--alluredir", alluredir])

    #生成可视化报告
    if os.path.exists(os.path.join(os.path.dirname(__file__),"allure-report")):
        shutil.rmtree(os.path.join(os.path.dirname(__file__),"allure-report"))
    os.system("allure generate "+alluredir+ " -o allure-report")