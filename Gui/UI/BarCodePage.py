# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BarCodePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BarCodePage(object):
    def setupUi(self, BarCodePage):
        BarCodePage.setObjectName("BarCodePage")
        BarCodePage.resize(422, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(BarCodePage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 381, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.codeInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.codeInput.setObjectName("codeInput")
        self.horizontalLayout.addWidget(self.codeInput)
        self.CreateBarCodeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CreateBarCodeButton.setObjectName("CreateBarCodeButton")
        self.horizontalLayout.addWidget(self.CreateBarCodeButton)
        self.BarCodeShow = QtWidgets.QLabel(BarCodePage)
        self.BarCodeShow.setGeometry(QtCore.QRect(20, 130, 381, 131))
        self.BarCodeShow.setObjectName("BarCodeShow")

        self.retranslateUi(BarCodePage)
        QtCore.QMetaObject.connectSlotsByName(BarCodePage)

    def retranslateUi(self, BarCodePage):
        _translate = QtCore.QCoreApplication.translate
        BarCodePage.setWindowTitle(_translate("BarCodePage", "Form"))
        self.label.setText(_translate("BarCodePage", "输入条形码"))
        self.CreateBarCodeButton.setText(_translate("BarCodePage", "生成"))
        self.BarCodeShow.setText(_translate("BarCodePage", "条形码"))
