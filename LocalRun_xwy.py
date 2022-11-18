# -*- coding: utf-8 -*-
from datetime import datetime

import os,shutil
import pytest

import Common.ImportApiFromExcel as importApi
import Common.ImportTestCaseFromExcel as importCase
import Common.Api2Bkw as importBkwApi


if __name__ == '__main__':
    #更新接口
    importApi.impotApi().readExcel()
    # 更新业务关键字接口
    importBkwApi.impotBKWApi().do()
    #更新用例
    importCase.impotTestCase("./TestFile/XiaoWenyao/SearchCenter.xlsx","SearchCenterAutoCaseRun").readExcel()
    #importCase.impotTestCase("./TestFile/XiaoWenyao/keyword_stagnation.xlsx","stagnation").kwReadExcel()
    #执行用例
    repName = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    alluredir = "report/" + repName
    pytest.main(["-s", "testCase/SearchCenterAutoCaseRun/test_apiConn.py", "-q", "--alluredir", alluredir])
    #pytest.main(["-s", "testCase/stagnation/test_stagnationCases.py", "-q", "--alluredir", alluredir])
    #生成可视化报告
    if os.path.exists(os.path.join(os.path.dirname(__file__),"allure-report")):
        shutil.rmtree(os.path.join(os.path.dirname(__file__),"allure-report"))
    os.system("allure generate "+alluredir+ " -o allure-report")