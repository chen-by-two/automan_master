import pytest,os,allure
from datetime import datetime
import ApiLib.goodsCenter.goodsCenterApi as gc

"""
Feature: 标注主要功能模块
Story: 标注Features功能模块下的分支功能
Step: 标注测试用例的重要步骤
Severity: 标注测试用例的重要级别
    1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
    2、 Critical级别：临界缺陷（ 功能点缺失）
    3、 Normal级别：普通缺陷（数值计算错误）
    4、 Minor级别：次要缺陷（界面错误与UI需求不符）
    5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
"""

class TestShow:

    @allure.feature("商品中心")
    @allure.story("spu")
    @allure.severity("blocker")
    def test_demo1(self):
        """
            这是一个拉取接口的描述
        """
        spuQuery = gc.spuQuery()

        spuQuery.headers = {}

        spuQuery.params = {}

        spuQuery.data = {}
        spuQueryRes = spuQuery.excute()
        assert spuQueryRes.status_code == 200

    @allure.feature("商品中心")
    @allure.story("sku")
    @allure.severity("minor")
    def test_aaa2(self):
        spuQuery = gc.spuQuery()
        spuQuery.headers = {}
        spuQueryRes = spuQuery.excute()
        print(spuQueryRes)
        print(spuQueryRes.text.__contains__("error"))
        assert spuQueryRes.status_code == 200

if __name__ == '__main__':
    oo = "sss"
    print(oo.__contains__(2))
    # alluredir = "/Users/liuhaoran/PycharmProjects/apiTest/report/"+str(datetime.now().strftime("%Y%m%d%H%M%S"))
    # pytest.main(["-s","/Users/liuhaoran/PycharmProjects/apiTest/testCase/","-q","--alluredir",alluredir])
    # os.system("allure generate "+alluredir+" -o "+alluredir +"/allureReport")