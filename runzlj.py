# -*- coding: UTF-8 -*
import pytest, os, sys
from datetime import datetime


def run():
    alluredir = "report/" + os.getenv("BUILD_NUMBER")
    pytest.main(["-s", r"C:\Users\zz\PycharmProjects\automan\TestFile\zljOnly\ApiTestCasezlj.xlsx" + sys.argv[1], "-q",
                 "--alluredir", alluredir])


if __name__ == '__main__':
    run()