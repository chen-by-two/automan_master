# -*- coding: utf-8 -*-
# @Time ：2020/8/27 4:34 PM
# @Author : Haoran
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Gui.UI.BarCodePage import Ui_BarCodePage
from pystrich.code128 import Code128Encoder
from PyQt5.QtGui import *
import os,shutil


class BarCodeView(QWidget,Ui_BarCodePage):
    def __init__(self,parent=None):
        super(BarCodeView,self).__init__(parent)
        self.setupUi(self)
        self.CreateBarCodeButton.clicked.connect(self.createBarCode)

    def createBarCode(self):
        self.BarCodeShow.setPixmap(QPixmap(""))
        tmpPath = os.path.dirname(__file__)
        code = self.codeInput.text()
        # codePath = os.path.join(tmpPath,"../Tmp/"+code+".png")
        codePath = os.path.join("./Tmp/",code+".png")
        encoder = Code128Encoder(code)
        try:
            encoder.save(codePath)
        except Exception as e:
            print("ooo",e)
        png = QtGui.QPixmap(codePath)
        self.BarCodeShow.setPixmap(png)
        self.BarCodeShow.setScaledContents(True)

