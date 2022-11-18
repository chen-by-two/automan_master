# coding: utf-8
# @author: chen
# @time: 2022/11/3 15:38
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
     importCase.impotTestCase(os.path.join(os.getcwd(),'TestFile\ApiTestCase.xlsx'),'phoneCenter1').readExcel()


