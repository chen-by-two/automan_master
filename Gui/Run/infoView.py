# -*- coding: utf-8 -*-
# @Time ：2020/8/27 4:34 PM
# @Author : Haoran
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Gui.UI.infoPage import Ui_Dialog
from pystrich.code128 import Code128Encoder
from PyQt5.QtGui import *
import os,shutil


class infoView(QWidget,Ui_Dialog):
    def __init__(self,parent=None):
        super(infoView,self).__init__(parent)
        self.setupUi(self)


