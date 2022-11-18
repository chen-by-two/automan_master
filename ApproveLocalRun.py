# -*- coding: utf-8 -*-
from datetime import datetime

import os,shutil
import pytest

import Common.ImportApiFromExcel as importApi
import Common.ImportTestCaseFromExcel as importCase

if __name__ == '__main__':
    #更新接口
    importApi.impotApi().readExcel()
    #更新用例
    #importCase.impotTestCase("./TestFile/activity/activitykeyword.xlsx","activity_case").readExcel()
    # importCase.impotTestCase("./TestFile/activity/activitykeyword.xlsx","activity_case").kwReadExcel()
    #执行用例
    repName = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    alluredir = "report/" + repName
    pytest.main(["-s", "testCase/AssistantApprove", "-q", "--alluredir", alluredir])
    #生成可视化报告
    if os.path.exists(os.path.join(os.path.dirname(__file__),"allure-report")):
        shutil.rmtree(os.path.join(os.path.dirname(__file__),"allure-report"))
    os.system("allure generate "+alluredir+ " -o allure-report")