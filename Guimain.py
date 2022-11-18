# -*- coding: utf-8 -*-
# @Time ：2020/8/27 10:26 AM
# @Author : Haoran


import sys
import Gui.UI.FirstPage as FirstPage
from Gui.Run.BarCodeView import BarCodeView
from Gui.Run.infoView import infoView
from Gui.Run.SshTunnelView import SshTunnelView
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mainUi = FirstPage.Ui_MainWindow()
        self.mainUi.setupUi(self)


if __name__ == '__main__':
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    MainWindow = Main()
    BarCodeWindow = BarCodeView()
    infoWindow = infoView()
    SshTunnelWindow = SshTunnelView()

    # 跳转绑定
    btBarCode = MainWindow.mainUi.barCode
    btBarCode.clicked.connect(BarCodeWindow.show)
    btQrCode = MainWindow.mainUi.qrCode
    btQrCode.clicked.connect(infoWindow.show)
    btSshTunnel = MainWindow.mainUi.sshTunnel
    btSshTunnel.clicked.connect(SshTunnelWindow.show)
    btAutoCaseRun = MainWindow.mainUi.autoCaseRun
    btAutoCaseRun.clicked.connect(infoWindow.show)
    btAutoCaseMake = MainWindow.mainUi.autoCaseMake
    btAutoCaseMake.clicked.connect(infoWindow.show)
    btCheckUpdate = MainWindow.mainUi.checkUpdate
    btCheckUpdate.clicked.connect(infoWindow.show)

    MainWindow.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
