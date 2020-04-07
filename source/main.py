# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from block_init import Tango_block
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import widget_screen
import widget_QnA

class Ui_editor(object):
    def setupUi(self, editor):
        editor.setObjectName("editor")
        editor.resize(247, 267)
        editor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(editor)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_screen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_screen.setGeometry(QtCore.QRect(50, 40, 151, 71))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(14)
        self.btn_screen.setFont(font)
        self.btn_screen.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_screen.setObjectName("btn_screen")
        self.btn_card = QtWidgets.QPushButton(self.centralwidget)
        self.btn_card.setGeometry(QtCore.QRect(50, 150, 151, 71))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(14)
        self.btn_card.setFont(font)
        self.btn_card.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_card.setObjectName("btn_card")
        editor.setCentralWidget(self.centralwidget)

        self.retranslateUi(editor)
        self.btn_screen.clicked.connect(self.btn_open_screen)
        self.btn_card.clicked.connect(self.btn_open_QnA)
        QtCore.QMetaObject.connectSlotsByName(editor)

    def retranslateUi(self, editor):
        _translate = QtCore.QCoreApplication.translate
        editor.setWindowTitle(_translate("editor", "MainWindow"))
        self.btn_screen.setText(_translate("editor", "놀이판"))
        self.btn_card.setText(_translate("editor", "낱말카드"))


    def btn_open_screen(self):
        Form_s.show()

    def btn_open_QnA(self):
        # print('open QnA')
        # QnA.loadScreenData()
        # print('open QnA show')
        Form_QnA.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    editor = QtWidgets.QMainWindow()
    ui = Ui_editor()
    ui.setupUi(editor)
    editor.show()

    Form_s = QtWidgets.QWidget()
    screen = widget_screen.Ui_Form_Screen()
    screen.setupUi(Form_s)

    Form_QnA = QtWidgets.QWidget()
    QnA = widget_QnA.Ui_widget_QnA()
    QnA.setupUi(Form_QnA)

    sys.exit(app.exec_())
