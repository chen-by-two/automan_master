# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import xlrd

class excel:
    def __init__(self,excelFilePath):
        self.excelFile = xlrd.open_workbook(excelFilePath)
        self.excelTable = None
    def getTables(self):
        return self.excelFile.sheet_names()

    def changeTable(self,tableName):
        self.excelTable = self.excelFile.sheet_by_name(tableName)

    def getRowNum(self):
        return self.excelTable.nrows

    def getRowValues(self,rowIndex):
        return self.excelTable.row_values(rowIndex)

if __name__ == '__main__':
    oo = excel("/Users/liuhaoran/PycharmProjects/automan/TestFile/ApiInfo.xlsx")
    oo.changeTable(oo.getTables()[0])
    print(oo.getRowNum())
    print(oo.getRowValues(1))