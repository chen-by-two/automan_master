# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 16:04
# @Author  : Haoran
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Gui.UI.SshTunnelPage import Ui_Form
from Common.SshTunnel import sshTunnel
from pystrich.code128 import Code128Encoder
from PyQt5.QtGui import *
import os, shutil


class SshTunnelView(QWidget, Ui_Form):
    def __init__(self, parent=None):
        self.tunnel = None
        super(SshTunnelView, self).__init__(parent)
        self.setupUi(self)
        self.tunnelStartbtn.clicked.connect(self.tunnelStart)
        self.tunnelStopbtn.clicked.connect(self.tunnelStop)

    def tunnelStart(self):
        self.tunnel = sshTunnel()
        if self.sshHostInput.text() != "" and self.sshPortInput.text() != "":
            self.tunnel.sshHost = self.sshHostInput.text()
            self.tunnel.sshPort = int(self.sshPortInput.text())
            self.tunnel.sshPassword = self.sshPasswordInput.text()
            self.tunnel.sshPrivateKey = self.sshPrivateKeyInput.text()
            self.tunnel.remoteAddress = self.remoteAddressInput.text()
            self.tunnel.remotePort = int(self.remotPortInput)
            self.tunnel.localAddress = self.localAddressInput
            self.tunnel.localPort = int(self.localPortInput)
            if self.sshPasswordInput.text().__len__() > 0:
                self.tunnel.connWithPassword()
            else:
                self.tunnel.connWithPrivateKey()
        else:
            print("1213")

    def tunnelStop(self):
        self.tunnel.closeConn()