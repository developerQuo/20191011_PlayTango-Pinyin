# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_QnA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from block_init import Mp3Object
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QEasingCurve, QFileInfo, QLineF, QMimeData,
                          QParallelAnimationGroup, QPoint, QPointF, QPropertyAnimation, qrand,
                          QRectF, qsrand, Qt, QTime)
from PyQt5.QtGui import (QBrush, QColor, QDrag, QImage, QPainter, QPen,
                         QPixmap, QTransform)
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsObject,
                             QGraphicsScene, QGraphicsView)
import pickle
import traceback, sys
from functools import partial
import ast


class Ui_widget_QnA(object):
    def __init__(self):
        self.mp3_list = []
        self.mp3_line_edit_list = []
        self.mp3_block_list = []
        self.mp3_block_question = []
        self.mp3_block_answer = []
        self.punch = []

        self.target = None

        self._translate = QtCore.QCoreApplication.translate
        self.font_basic = self.fontsettings_basic()
        self.font_basic2 = self.fontsettings_basic2()
        self.font = self.fontsettings()

        global ui
        ui = self

    def setupUi(self, widget_QnA):
        widget_QnA.setObjectName("widget_QnA")
        widget_QnA.resize(1440, 620)
        # 그리드 레이아웃
        self.gridLayout = QtWidgets.QGridLayout(widget_QnA)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")

        # 상단 메뉴
        self.upper_side = QtWidgets.QGroupBox(widget_QnA)
        self.upper_side.setStyleSheet("border:none")
        self.upper_side.setMaximumHeight(40)
        self.upper_layout = QtWidgets.QHBoxLayout(self.upper_side)
        self.upper_layout.setContentsMargins(0, 0, 0, 0)
        # 출력버튼
        self.btn_text_output = QtWidgets.QPushButton(self.upper_side)
        self.btn_text_output.setGeometry(QtCore.QRect(23, 300, 101, 28))
        font = self.fontsettings()
        self.btn_text_output.setFont(font)
        self.btn_text_output.setObjectName("btn_text_output")
        self.btn_text_output.setMaximumWidth(120)
        self.btn_text_output.setStyleSheet("color : red")
        # 빈공간
        self.upeer_side_blank = QtWidgets.QLabel(widget_QnA)
        # 음원 추가버튼
        self.btn_new_mp3_line_edit = QtWidgets.QPushButton(self.upper_side)
        self.btn_new_mp3_line_edit.setGeometry(QtCore.QRect(23, 300, 101, 28))
        font = self.fontsettings()
        self.btn_new_mp3_line_edit.setFont(font)
        self.btn_new_mp3_line_edit.setObjectName("btn_new_mp3_line_edit")
        self.btn_new_mp3_line_edit.setMaximumWidth(120)
        # 음원 삭제버튼
        self.btn_del_mp3_line_edit = QtWidgets.QPushButton(self.upper_side)
        self.btn_del_mp3_line_edit.setGeometry(QtCore.QRect(145, 300, 101, 28))
        self.btn_del_mp3_line_edit.setFont(font)
        self.btn_del_mp3_line_edit.setObjectName("btn_del_mp3_line_edit")
        self.btn_del_mp3_line_edit.setMaximumWidth(120)
        # 문제, 정답 음원버튼
        self.btn_QnA = QtWidgets.QPushButton(self.upper_side)
        self.btn_QnA.setGeometry(QtCore.QRect(145, 300, 101, 28))
        self.btn_QnA.setFont(font)
        self.btn_QnA.setObjectName("btn_QnA")
        self.btn_QnA.setMaximumWidth(120)
        self.btn_new_mp3_line_edit.setStyleSheet("color : skyblue")
        self.btn_del_mp3_line_edit.setStyleSheet("color : skyblue")
        self.btn_QnA.setStyleSheet("color : skyblue")
        # 상단 레이아웃에 추가
        self.upper_layout.addWidget(self.btn_text_output)
        self.upper_layout.addWidget(self.upeer_side_blank)
        self.upper_layout.addWidget(self.btn_new_mp3_line_edit)
        self.upper_layout.addWidget(self.btn_del_mp3_line_edit)
        self.upper_layout.addWidget(self.btn_QnA)

        # 음원 위젯
        self.mp3_widget = QtWidgets.QWidget(widget_QnA)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mp3_widget.sizePolicy().hasHeightForWidth())
        self.mp3_widget.setSizePolicy(sizePolicy)
        self.mp3_widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.mp3_widget.setBaseSize(QtCore.QSize(0, 0))
        self.mp3_widget.setObjectName("mp3_widget")

        # 음원 컨트롤박스
        self.control_box = QtWidgets.QGroupBox(self.mp3_widget)
        self.control_box.setObjectName("control_box")
        self.control_box.setMaximumSize(QtCore.QSize(121, 16777215))
        self.control_box.setFont(self.font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.control_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # 음원 생성 버튼
        self.btn_init_mp3 = QtWidgets.QPushButton(self.control_box)
        self.btn_init_mp3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_init_mp3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_init_mp3.setFont(self.font)
        self.btn_init_mp3.setObjectName("btn_init_mp3")
        self.verticalLayout_3.addWidget(self.btn_init_mp3)
        # 음원 저장 버튼
        self.btn_save_mp3 = QtWidgets.QPushButton(self.control_box)
        self.btn_save_mp3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save_mp3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_save_mp3.setFont(self.font)
        self.btn_save_mp3.setObjectName("btn_save_mp3")
        self.verticalLayout_3.addWidget(self.btn_save_mp3)
        # 음원 삭제 버튼
        self.btn_delete_mp3 = QtWidgets.QPushButton(self.control_box)
        self.btn_delete_mp3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_delete_mp3.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_delete_mp3.setFont(self.font)
        self.btn_delete_mp3.setObjectName("btn_delete_mp3")
        self.verticalLayout_3.addWidget(self.btn_delete_mp3)

        # mp3 widget list
        self.widget_mp3_list = QtWidgets.QListWidget(self.mp3_widget)
        self.widget_mp3_list.setMaximumSize(QtCore.QSize(181, 16777215))
        self.widget_mp3_list.setObjectName("widget_mp3_list")
        font = self.fontsettings_basic()
        self.widget_mp3_list.setFont(self.font)

        # mp3 setting groupbox
        self.mp3_detailBox = QtWidgets.QGroupBox(self.mp3_widget)
        self.mp3_detailBox.setFont(self.font)
        self.mp3_detailBox.setObjectName("mp3_detailBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.mp3_detailBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        # mp3 groupbox
        self.mp3_groupbox = QtWidgets.QGroupBox(self.mp3_detailBox)
        self.mp3_groupbox.setStyleSheet("border:none")
        self.mp3_layout = QtWidgets.QHBoxLayout(self.mp3_groupbox)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        self.label_mp3_titles1 = QtWidgets.QLabel(self.mp3_detailBox)
        self.label_mp3_titles1.setGeometry(QtCore.QRect(3, 115, 81, 21))
        font = self.fontsettings_basic()
        self.label_mp3_titles1.setFont(font)
        self.label_mp3_titles1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_titles1.setObjectName("label_mp3_titles1")
        self.label_mp3_titles1.setMaximumWidth(130)
        self.label_mp3_titles2 = QtWidgets.QLabel(self.mp3_detailBox)
        self.label_mp3_titles2.setGeometry(QtCore.QRect(83, 115, 30, 21))
        self.label_mp3_titles2.setFont(font)
        self.label_mp3_titles2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_titles2.setObjectName("label_mp3_titles2")
        self.label_mp3_titles2.setMaximumWidth(130)
        self.label_mp3_address = QtWidgets.QLabel(self.mp3_detailBox)
        self.label_mp3_address.setGeometry(QtCore.QRect(105, 115, 141, 21))
        self.label_mp3_address.setFont(font)
        self.label_mp3_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_address.setObjectName("label_mp3_address")
        self.mp3_layout.addWidget(self.label_mp3_titles1)
        self.mp3_layout.addWidget(self.label_mp3_titles2)
        self.mp3_layout.addWidget(self.label_mp3_address)
        # mp3 scrollarea
        self.mp3_scroll_area = QtWidgets.QScrollArea(self.mp3_detailBox)
        self.mp3_scroll_area.setWidgetResizable(True)
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.mp3_groupbox, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.mp3_scroll_area, 1, 0, 1, 1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.loadMp3Box()

        # 음원 위젯 레이아웃
        self.gridLayout_6 = QtWidgets.QGridLayout(self.mp3_widget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.addWidget(self.control_box, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_mp3_list, 0, 1, 3, 1)
        self.gridLayout_6.addWidget(self.mp3_detailBox, 0, 2, 3, 1)
        # 음원위젯 -> gridlayout에 올리기
        self.gridLayout.addWidget(self.upper_side, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.mp3_widget, 1, 0, 1, 1)

        self.retranslateUi(widget_QnA)
        self.btn_init_mp3.clicked.connect(self.initMp3)
        self.btn_save_mp3.clicked.connect(self.saveMp3)
        self.btn_delete_mp3.clicked.connect(self.deleteMp3)
        self.btn_text_output.clicked.connect(self.output)
        self.btn_new_mp3_line_edit.clicked.connect(self.initMp3LineEdit)
        self.btn_del_mp3_line_edit.clicked.connect(self.delMp3LineEdit)
        self.btn_QnA.clicked.connect(self.QnA_dialog)
        self.widget_mp3_list.itemClicked['QListWidgetItem*'].connect(self.widgetSelectMp3)
        self.widget_mp3_list.itemChanged['QListWidgetItem*'].connect(self.modifyMp3Name)
        QtCore.QMetaObject.connectSlotsByName(widget_QnA)

        self.initSettings()

    def retranslateUi(self, widget_QnA):
        _translate = QtCore.QCoreApplication.translate
        widget_QnA.setWindowTitle(_translate("widget_QnA", "Form"))
        self.btn_text_output.setText(_translate("Form", " 텍스트 출력 "))
        self.upeer_side_blank.setText(_translate("widget_QnA", "         "))
        self.btn_new_mp3_line_edit.setText(_translate("Form", " 음원 목록 추가 "))
        self.btn_del_mp3_line_edit.setText(_translate("Form", " 음원 목록 삭제 "))
        self.btn_QnA.setText(_translate("Form", " 문제 정답 정보 "))
        self.control_box.setTitle(_translate("widget_QnA", "ControlBox"))
        self.btn_init_mp3.setText(_translate("widget_QnA", "생성"))
        self.btn_save_mp3.setText(_translate("widget_QnA", "저장"))
        self.btn_delete_mp3.setText(_translate("widget_QnA", "삭제"))
        self.mp3_detailBox.setTitle(_translate("widget_QnA", "설정"))
        self.label_mp3_titles1.setText(_translate("Form", "타이틀"))
        self.label_mp3_titles2.setText(_translate("Form", "언어"))
        self.label_mp3_address.setText(_translate("Form", "음원 주소"))

# 음원
    # 저장된 음원 불러오기
    def mp3Load(self):
        try:
            with open('mp3_info.p', 'rb') as file:
                self.mp3_list = pickle.load(file)[0]
        except:
            self.mp3_list = []
        self.widgetBlockList_reload(self.mp3_list, self.widget_mp3_list)
    # widget_mp3_list 선택 시 정보 불러오기
    def widgetSelectMp3(self):
        self.checkToSave()
        if self.widget_mp3_list.currentRow() != -1:
            self.target = self.widget_mp3_list.currentRow()
        else:
            pass
        self.selected_mp3 = self.mp3_list[self.target]
        self.mp3_block_list = self.selected_mp3.mp3_block_list
        self.mp3_block_question = self.selected_mp3.mp3_block_question
        self.mp3_block_answer = self.selected_mp3.mp3_block_answer
        self.punch = self.selected_mp3.punch
        self.loadMp3()

    # 음원 이름 변경
    def modifyMp3Name(self):
        try:
            self.selected_mp3.name = self.widget_mp3_list.item(self.target).text()
        except:
            pass

    # 음원 생성 버튼
    def initMp3(self):
        # 이름 생성 규칙
        count = 1
        widget_names = []
        for obj in self.mp3_list:
            widget_names.append(obj.name)
        while(True):
            name = '새로운 음원{}'.format(self.widget_mp3_list.count()+count)
            if name not in widget_names:
                break
            else:
                count += 1
        # mp3 데이터 추출
        mp3 = []
        for obj in self.mp3_line_edit_list:
            tmp = []
            for count in obj:
                tmp.append(count.text())
            mp3.append(tmp)
        mp3obj = Mp3Object(name=name, mp3=mp3, mp3_block_list=self.mp3_block_list, mp3_block_question=self.mp3_block_question, mp3_block_answer=self.mp3_block_answer, punch=self.punch)
        self.mp3_list.append(mp3obj)
        count = len(self.mp3_list) - 1
        self.widgetBlockList(self.mp3_list, self.widget_mp3_list, mp3obj, count)

        try:
            with open('mp3_info.p', 'wb') as file:
                pickle.dump([self.mp3_list], file)
        except:
            traceback.print_exc(file=sys.stdout)
    # 음원 저장 버튼
    def saveMp3(self):
        try:    # 문제 선택 안하고 저장할 때 에러 방지
            self.selected_mp3
        except:
            self.error_dialog('음원을 선택해주세요!')
        else:
            self.selected_mp3.name = self.widget_mp3_list.item(self.target).text()
            mp3 = []
            for obj in self.mp3_line_edit_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            self.selected_mp3.mp3 = mp3
            self.selected_mp3.mp3_block_list = self.mp3_block_list
            self.selected_mp3.mp3_block_question = self.mp3_block_question
            self.selected_mp3.mp3_block_answer = self.mp3_block_answer
            self.selected_mp3.punch = self.punch

            with open('mp3_info.p', 'wb') as file:
                pickle.dump([self.mp3_list], file)
    # 음원 삭제 버튼
    def deleteMp3(self):
        try:    # 문제 선택 안하고 저장할 때 에러 방지
            self.selected_mp3
        except:
            self.error_dialog('음원을 선택해주세요!')
        else:
            del self.mp3_list[self.target]
            self.widgetBlockList_reload(self.mp3_list, self.widget_mp3_list)

    # 음원항목 추가
    def initMp3LineEdit(self):
        self.loadMp3Box()

    # 음원박스 추가
    def loadMp3Box(self):
        mp3groupbox = QtWidgets.QGroupBox()
        mp3groupbox.setStyleSheet("border:none")
        layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
        layout_groupbox.setContentsMargins(5, 3, 5, 3)

        label_title1 = QtWidgets.QLineEdit(mp3groupbox)
        label_title1.setMinimumHeight(30)
        label_title1.setMaximumWidth(130)
        layout_groupbox.addWidget(label_title1)
        label_title2 = QtWidgets.QLineEdit(mp3groupbox)
        label_title2.setMinimumHeight(30)
        label_title2.setMaximumWidth(130)
        layout_groupbox.addWidget(label_title2)
        label_address = QtWidgets.QLineEdit(mp3groupbox)
        label_address.setMinimumHeight(30)
        layout_groupbox.addWidget(label_address)
        self.mp3_layout.addWidget(mp3groupbox)

        mp3box = [label_title1, label_title2, label_address]
        self.mp3_line_edit_list.append(mp3box)

    # 음원항목 불러오기
    def loadMp3(self):
        # mp3 scrollarea reset
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        # mp3 line edit에 정보 로드
        self.mp3_line_edit_list = []
        for obj in self.selected_mp3.mp3:
            self.loadMp3Box()
            for count in range(3):
                self.mp3_line_edit_list[-1][count].setText(self._translate("Form", "{}".format(obj[count])))

    # 음원항목 삭제
    def delMp3LineEdit(self):
        # mp3 정보 임시 저장
        mp3 = []
        for obj in self.mp3_line_edit_list:
            tmp = []
            for count in obj:
                tmp.append([count,count.text()])
            mp3.append(tmp)
        # mp3 scrollarea reset
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        # mp3 line edit에 정보 로드
        self.mp3_line_edit_list = []
        for obj in mp3:
            if mp3.index(obj) == len(mp3) - 1:
                break
            else:
                self.loadMp3Box()
                for count in range(3):
                    self.mp3_line_edit_list[-1][count].setText(self._translate("Form", "{}".format(obj[count][1])))

    # QnA로 이동
    def QnA_dialog(self):
        try:
            # print(self.punch)
            # print(self.mp3_block_question, self.mp3_block_answer)
            self.select_screen = SelectScreen(self.selected_mp3, self.mp3_block_list, self.punch, self.mp3_block_question, self.mp3_block_answer)
        except:
            # print('QnA_dialog err')
            pass
        else:
            self.select_screen.show()

    # 공통
    # 폰트 세팅
    def fontsettings_basic(self, size=10):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font
    def fontsettings_basic2(self):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        return font
    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

    # widgetList 새로고침
    def widgetBlockList_reload(self, list, widget_list):
        widget_list.clear()
        for count in range(len(list)):
            tmp_name = list[count].name
            self.widgetBlockList(list, widget_list, tmp_name, count)

    # widgetList 생성
    def widgetBlockList(self, list, widget_list, obj, count):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
        widget_list.addItem(item)
        item = widget_list.item(count)
        try:
            item.setText(self._translate("Form", "{}".format(obj.name)))
        except:
            item.setText(self._translate("Form", "{}".format(obj)))

    # 탭 변경
    def changedTab(self):
        self.mp3Load()
        self.loadData('mp3_info.p', self.mp3_list, self.widget_mp3_list)

    # 가져올 데이터 선택
    def loadData(self, filename, list, widget_list):
        try:
            with open(filename, 'rb') as file:
                list = pickle.load(file)[0]
        except:
            list = []
        self.widgetBlockList_reload(list, widget_list)

    # 콤보박스 로드
    def loadComboBox(self, list, widget):

        widget.clear()
        for n in list:
            widget.addItem(n.name)

    # 저장없이 다른 놀이판 눌렀을 때 확인
    def checkToSave(self):
        try:
            mp3 = []
            for obj in self.mp3_line_edit_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            if self.selected_mp3.name == self.widget_mp3_list.item(self.target).text() and self.selected_mp3.mp3 == mp3 and self.selected_mp3.mp3_block_list == self.mp3_block_list and self.selected_mp3.mp3_block_question == self.mp3_block_question and self.selected_mp3.mp3_block_answer == self.mp3_block_answer and self.selected_mp3.punch == self.punch:
                pass
            else:
                dlg = checkDialog(obj=self.selected_mp3, name=self.widget_mp3_list.item(self.target).text(), mp3=mp3, mp3_block_list=self.mp3_block_list, mp3_block_question=self.mp3_block_question, mp3_block_answer=self.mp3_block_answer, punch=self.punch)
                dlg.exec_()
                self.selected_mp3 = dlg.obj

            with open('mp3_info.p', 'wb') as file:
                pickle.dump([self.mp3_list], file)
        except:
            pass

    # txt 출력
    def output(self):
        try:
            self.selected_mp3
        except:
            pass
        else:
            name = self.selected_mp3.name
            # mp3
            mp3 = '{}.txt'.format(name)
            mp3_contents = self.output_mp3(self.selected_mp3.mp3)
            with open(mp3, 'wt') as f:
                f.write(mp3_contents)
            # question mp3
            mp3 = '{}_question_mp3.txt'.format(name)
            mp3_contents = self.output_blocks_mp3(self.selected_mp3.mp3_block_question)
            with open(mp3, 'wt') as f:
                f.write(mp3_contents)
            # answer
            mp3 = '{}_answer.txt'.format(name)
            mp3_contents = self.output_blocks_mp3_punch(self.selected_mp3.mp3_block_answer)
            with open(mp3, 'wt') as f:
                f.write(mp3_contents)
            # answer mp3
            mp3 = '{}_answer_mp3.txt'.format(name)
            mp3_contents = self.output_blocks_mp3(self.selected_mp3.mp3_block_answer)
            with open(mp3, 'wt') as f:
                f.write(mp3_contents)


    # 문제 정답 음원 출력 형식
    def output_blocks_mp3(self, blocks_mp3):
        mp3_contents = '{}\n'.format(len(blocks_mp3))
        mp3_info = '{},{},\n'
        for block in blocks_mp3:
            mp3_contents += mp3_info.format(block[3], block[2])
        mp3_contents = mp3_contents.rstrip("\n")
        # print(mp3_contents)
        return mp3_contents

    # 정답 타공 출력 형식
    def output_blocks_mp3_punch(self, blocks_mp3):
        mp3_contents = '{}\n'.format(len(blocks_mp3))
        mp3_info = '{},{},{},{},\n'
        for block in blocks_mp3:
            mp3_contents += mp3_info.format(block[3], block[1][0], block[1][1], block[0])
        mp3_contents = mp3_contents.rstrip("\n")
        # print(mp3_contents)
        return mp3_contents

    # 음원 출력 형식
    def output_mp3(self, mp3_tmp):
        # print(mp3_tmp)
        mp3_count = []
        for count in mp3_tmp:
            if len(count[-1]) > 2:
                mp3_count.append(count[-1].count(',') + 1)
            else:
                # 언어 변경
                if count[0] == 'en':
                    mp3_count.append('')
                else:
                    mp3_count.append(0)
        # print(mp3_count)
        mp3_contents = ''
        mp3_save_list = []
        mp3_info = '{},{},{},{},\n'
        mp3_save_list2 = []
        for count in range(len(mp3_tmp)):
            mp3_save_list2.append(mp3_info)
        mp3_save_list += mp3_save_list2

        count = 0
        for i in mp3_save_list:
            mp3_contents += i.format(mp3_tmp[count][0], mp3_tmp[count][1],
                                     mp3_count[count], mp3_tmp[count][2])
            count += 1
        return mp3_contents

    def error_dialog(self, str):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str)
        error_dialog.exec_()

    def initSettings(self):
        self.mp3Load()

# 스크린 선택 후 문제 정답으로 이동
class SelectScreen(QtWidgets.QDialog):
    def __init__(self, selected_mp3, checkbox, punch, question, answer):
        super().__init__()
        self.selected_info = punch
        self.selected_mp3 = selected_mp3
        self.selected_checkbox = checkbox
        self.selected_checkbox_tmp = checkbox
        self.selected_QnA = [question, answer]
        self.selected_QnA_tmp = [question, answer]
        # 스크린 파일 로드
        self.loadScreenData()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 400, 700, 200)

        # 메세지
        text = QtWidgets.QLabel("스크린 정보를 선택해주세요.")
        font = self.fontsettings()
        text.setFont(font)
        text.setAlignment(QtCore.Qt.AlignCenter)

        # 스크린 선택
        self.comboBox_select_screen = QtWidgets.QComboBox()
        self.comboBox_select_screen.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_select_screen.setObjectName("comboBox_select_screen")
        # 콤보박스 리스팅
        self.comboBox_select_screen.addItem(self.selected_mp3.name)
        for n in self.screen_list:
            self.comboBox_select_screen.addItem(n.name)

        # 스크린 정보
        self.screen_info = QtWidgets.QLabel()
        self.screen_info.setFont(font)
        self.screen_info.setAlignment(QtCore.Qt.AlignCenter)
        info = "펀치좌표: {}   >>>   {}개".format(self.selected_info, len(self.selected_info))
        self.screen_info.setText(info)

        # 버튼
        self.pushButton1 = QtWidgets.QPushButton("확인")
        font = self.fontsettings(10)
        self.pushButton1.setFont(font)
        self.pushButton1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton1.clicked.connect(self.pushSaveButtonClicked)
        self.pushButton2 = QtWidgets.QPushButton("취소")
        self.pushButton2.setFont(font)
        self.pushButton2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton2.clicked.connect(self.pushCancelButtonClicked)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(text, 0, 0)
        layout.addWidget(self.comboBox_select_screen, 0, 1)
        layout.addWidget(self.screen_info, 1, 0)
        layout.addWidget(self.pushButton1, 2, 1)
        layout.addWidget(self.pushButton2, 2, 2)

        self.setLayout(layout)


        self.comboBox_select_screen.activated.connect(self.selectScreen)

    # 스크린 정보 파일 읽기
    def loadScreenData(self):
        try:
            with open('screen_info.p', 'rb') as file:
                self.screen_list = pickle.load(file)[0]
        except:
            # print('failed to load data')
            self.screen_list = []
        # print(self.screen_list)

    # 콤보박스에서 펀치 정보 불러오기
    def selectScreen(self):
        if self.selected_mp3.name == self.comboBox_select_screen.currentText():
            self.selected_info = self.selected_mp3.punch
            self.selected_QnA_tmp = self.selected_QnA
            self.selected_checkbox_tmp = self.selected_checkbox
        else:
            for screen in self.screen_list:
                if screen.name == self.comboBox_select_screen.currentText():
                    self.selected_info = screen.punch
                    self.selected_checkbox_tmp = []
                    break
            self.selected_QnA_tmp = []
        info = "펀치좌표: {}   >>>   {}개".format(self.selected_info, len(self.selected_info))
        self.screen_info.setText(info)

    # 확인 누르면 QnA로 이동
    def pushSaveButtonClicked(self):
        # print("punch  >>> ", self.selected_info)
        # print("question > ", self.selected_QnA_tmp)
        # print("checkbox > ", self.selected_checkbox_tmp)
        # 펀치 인덱스, QnA 음원정보 같이 넘김
        self.window = Window(self.selected_info, self.selected_QnA_tmp, self.selected_checkbox_tmp)
        self.window.InitWindow()
        self.window.show()
        self.close()

    def pushCancelButtonClicked(self):
        self.close()

    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

# 데이터가 QnA에 맞게 변경되어야 함.
# 문제 정답 설정 창
class Window(QtWidgets.QMainWindow):
    def __init__(self, punch_index, selected_QnA, selected_checkbox):
        super().__init__()
        self.mp3_block_list = []
        # print(selected_checkbox)
        if len(selected_checkbox) > 0:
            self.mp3_block_list = selected_checkbox
        # print('selected_QnA >>> ', selected_QnA)
        if len(selected_QnA) > 0:
            self.mp3_block_question = selected_QnA[0]
            self.mp3_block_answer = selected_QnA[1]
        else:
            self.mp3_block_question = []
            self.mp3_block_answer = []
        self.punch_index = punch_index
        self.block_count = len(self.mp3_block_list)

        self.title = "문제 정답 정보"
        self.top = 150
        self.left = 150
        self.width = 1440
        self.height = 660

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self._translate = QtCore.QCoreApplication.translate

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(0, 0, 840, self.height)
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")

        # mp3 groupbox
        self.mp3_groupbox = QtWidgets.QGroupBox(self)
        self.mp3_groupbox.setStyleSheet("border:none; background-color : white")
        self.mp3_groupbox_layout = QtWidgets.QHBoxLayout(self.mp3_groupbox)
        self.mp3_groupbox_layout.setContentsMargins(0, 5, 0, 10)

        self.label_block = QtWidgets.QPushButton(self)
        font = self.fontsettings_basic()
        self.label_block.setFont(font)
        self.label_block.setObjectName("label_block")
        self.label_block.setMaximumWidth(60)
        self.label_block.setStyleSheet("color: skyblue")
        self.mp3_groupbox_layout.addWidget(self.label_block)
        self.setLabels(font)
        self.label_count = QtWidgets.QLabel(self)
        self.label_count.setFont(font)
        self.label_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_count.setObjectName("label_count")
        self.label_count.setMaximumWidth(60)
        self.mp3_groupbox_layout.addWidget(self.label_count)
        self.label_reset = QtWidgets.QPushButton(self)
        self.label_reset.setFont(font)
        self.label_reset.setObjectName("label_reset")
        self.label_reset.setMaximumWidth(60)
        self.label_reset.setStyleSheet("color: skyblue")
        self.mp3_groupbox_layout.addWidget(self.label_reset)
        self.label_block.setText(self._translate("Window", "블럭"))
        self.label_count.setText(self._translate("Window", "합계"))
        self.label_reset.setText(self._translate("Window", "모두 삭제"))
        self.setLayout(self.mp3_groupbox_layout)
        self.gridLayout.addWidget(self.mp3_groupbox, 0, 0, 1, 1)

        self.ScrollAreaSet()

        self.label_block.clicked.connect(self.btn_new_mp3_block)
        self.label_reset.clicked.connect(self.btn_reset_scrollarea)

        try:
            # print('mp3_block_list >>>', self.mp3_block_list)
            self.ConvertToObj()
        except:
            # print('err ConvertToObj')
            pass

        # question mp3 layout
        self.widget2 = QtWidgets.QWidget(self)
        # self.widget2.setStyleSheet("background-color : white")
        self.widget2.setGeometry(840, 0, 300, self.height)
        self.gridLayout2 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout2.setObjectName("gridLayout2")

        self.label_sum = QtWidgets.QLabel(self)
        self.label_sum.setFont(font)
        self.label_sum.setObjectName("label_sum")
        self.label_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum.setText(self._translate("Window", "문제 총 개수 : {}".format(len(self.mp3_block_question))))
        self.label_sum.setContentsMargins(0, 5, 0, 10)
        self.gridLayout2.addWidget(self.label_sum, 0, 0, 1, 1)

        # scroll area 틀 만들기
        self.ScrollArea2Set()

        # scroll area 내용
        try:
            # print('mp3_block_question >>> ', self.mp3_block_question)
            self.ConvertToObj_2_q(self.mp3_layout2, self.label_sum)
            # self.loadBlocksInfo()
        except:
            # print('err ConvertToObj_2')
            pass

        # answer mp3 layout
        self.widget3 = QtWidgets.QWidget(self)
        # self.widget3.setStyleSheet("background-color : white")
        self.widget3.setGeometry(1140, 0, 300, self.height)
        self.gridLayout3 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout3.setObjectName("gridLayout3")

        self.label_sum2 = QtWidgets.QLabel(self)
        self.label_sum2.setFont(font)
        self.label_sum2.setObjectName("label_sum2")
        self.label_sum2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum2.setText(self._translate("Window", "정답 총 개수 : {}".format(len(self.mp3_block_answer))))
        self.label_sum2.setContentsMargins(0, 5, 0, 10)
        self.gridLayout3.addWidget(self.label_sum2, 0, 0, 1, 1)

        self.ScrollArea3Set()

        try:
            # print('mp3_block_answer >>> ', self.mp3_block_answer)
            self.ConvertToObj_2_a(self.mp3_layout3, self.label_sum2)
            # self.loadBlocksInfo()
        except:
            # print('err ConvertToObj_2')
            pass

    def setLabels(self, font):
        # label 이름 뿌리기
        for count in range(len(self.punch_index)):
            self.label = QtWidgets.QLabel(self)
            self.label.setFont(font)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.label.setMaximumWidth(130)
            self.mp3_groupbox_layout.addWidget(self.label)
            self.label.setText(self._translate("Window", str(self.punch_index[count])))

    # 블럭 추가 버튼
    def btn_new_mp3_block(self):
        mp3groupbox = QtWidgets.QGroupBox()
        mp3groupbox.setStyleSheet("border:none")
        layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
        layout_groupbox.setContentsMargins(5, 3, 5, 3)
        font = self.fontsettings_basic()
        mp3box = []

        # 블럭 이름
        block_name = QtWidgets.QLineEdit(mp3groupbox)
        block_name.setMaximumWidth(60)
        block_name.setFrame(False)
        block_name.setStyleSheet("background-color : rgb(250,250,250)")
        block_name.setFont(font)
        self.block_count = len(self.mp3_block_list)
        block_name.setText("블럭{}".format(self.block_count))
        block_name.editingFinished.connect(partial(self.changedBlockName, block_name))
        layout_groupbox.addWidget(block_name)
        mp3box.append(block_name)
        self.block_count += 1

        # 체크박스
        for count in range(len(self.punch_index)):
            check_box = QtWidgets.QCheckBox("{}좌표".format(count+1), mp3groupbox)
            check_box.setFont(font)
            check_box.setMaximumWidth(130)
            check_box.stateChanged.connect(partial(self.checkStateChanged, check_box, mp3box))
            layout_groupbox.addWidget(check_box)
            mp3box.append(check_box)

        # 합계 라벨
        label_count = QtWidgets.QLabel(mp3groupbox)
        label_count.setFont(font)
        label_count.setAlignment(QtCore.Qt.AlignCenter)
        label_count.setMaximumWidth(60)
        label_count.setText(str(0))
        label_count.setStyleSheet("color : green")
        layout_groupbox.addWidget(label_count)
        mp3box.append(label_count)

        # 삭제 버튼
        delete_button = QtWidgets.QPushButton(mp3groupbox)
        delete_button.setFont(font)
        delete_button.setMaximumWidth(30)
        delete_button.setStyleSheet("color: skyblue")
        delete_button.clicked.connect(partial(self.btn_delete, delete_button))
        delete_button.setText(self._translate("Window", "삭제"))
        layout_groupbox.addWidget(delete_button)
        mp3box.append(delete_button)

        self.mp3_layout.addWidget(mp3groupbox)
        self.mp3_block_list.append(mp3box)
    # 모두 삭제 버튼
    def btn_reset_scrollarea(self):
        self.mp3_block_list = []
        self.mp3_block_question = []
        self.mp3_block_answer = []
        self.ScrollAreaSet()
        self.Arrangement()
        self.ScrollArea2Set()
        self.ScrollArea3Set()
        self.label_sum.setText(self._translate("Window", "문제 총 개수 : {}".format(len(self.mp3_block_question))))
        self.label_sum2.setText(self._translate("Window", "정답 총 개수 : {}".format(len(self.mp3_block_answer))))

    # 체크박스 체크시 변화
    def checkStateChanged(self, check_box, mp3box):
        group_name = ""
        index_checkbox = 0
        self.updateSum()
        self.ScrollArea2Set()
        self.ScrollArea3Set()
        if mp3box in self.mp3_block_list:
            group_name = mp3box[0].text()
        if check_box in mp3box:
            index_checkbox = mp3box.index(check_box) - 1
        # print('target_mp3box = ', target_mp3box)
        # 체크박스 해제시 음원 넣는칸 제거
        if check_box.checkState() == 0:
            self.releasedCheckBox(self.mp3_block_question, group_name, index_checkbox)
            self.releasedCheckBox(self.mp3_block_answer, group_name, index_checkbox)

        # 체크박스 적용시 음원 넣는칸 추가
        else:
            new_block = True
            block_order = []
            # print("블럭 리스트 >>> ",self.mp3_block_list)
            # 해당 블럭 인덱스 출력
            for block in self.mp3_block_list:
                block_order.append(block[0].text())
            # 이미 같은 이름의 블럭이 있을 때
            for group in self.mp3_block_question:
                # print('group_name >>> ', group_name, group[0].text())
                # 블럭이름 같은거 있는지 확인.
                if group[0].text() == group_name:
                    # print('=========', group_name, group[0].text(), '============')
                    pos = ast.literal_eval(group[1].text())
                    # print("pos >>> ", pos, self.punch_index[index_checkbox])

                    # 첫번째 위치가 같을 때
                    if pos[0] == self.punch_index[index_checkbox][0]:
                        if pos[1] > self.punch_index[index_checkbox][1]:
                            # print("[1]에서 기준보다 위치가 앞인 경우")
                            index = self.mp3_block_question.index(group)
                            # print("index >>> ", index)
                            mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                            self.mp3_block_question.insert(index, mp3box)
                            mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                            self.mp3_block_answer.insert(index, mp3box2)
                            new_block = False
                            break
                        elif pos[1] < self.punch_index[index_checkbox][1]:
                            # print("[1]에서 기준보다 위치가 뒤인 경우")
                            for block in self.mp3_block_question:
                                if block[0].text() == group[0].text():
                                    checker = ast.literal_eval(block[1].text())
                                    # print(self.punch_index[-1][1],  pos[1])
                                    if self.punch_index[-1][1] == checker[1]:
                                        # print(">>>>>>>>>>>>>>>>>>>continued<<<<<<<<<<<<<<<<<<")
                                        continue
                                    last_block = block
                                    # print(last_block[1].text())
                            index = self.mp3_block_question.index(last_block) + 1
                            # print("index >>> ", index)
                            mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                            self.mp3_block_question.insert(index, mp3box)
                            mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                            self.mp3_block_answer.insert(index, mp3box2)
                            new_block = False
                            break
                    # 첫번째 위치가 더 작을 때
                    elif pos[0] > self.punch_index[index_checkbox][0]:
                        # print("[0]에서 기준보다 위치가 앞인 경우")
                        index = self.mp3_block_question.index(group)
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_question.insert(index, mp3box)
                        mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_answer.insert(index, mp3box2)
                        new_block = False
                        break
                    # 첫번째 위치가 더 클 때때
                    elif pos[0] < self.punch_index[index_checkbox][0]:
                        # print("[0]에서 기준보다 위치가 뒤인 경우")
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_question.append(mp3box)
                        mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_answer.append(mp3box2)
                        new_block = False
                        break
            # 새블럭의 블럭인포 - 블럭 간 순서 정렬
            if new_block == True:
                # print('=====================새로운 블럭==========================')
                # 앞순서 객체 있는지 확인.
                # 이미 한번이상 사용된 블럭 리스트
                already_used_block = []
                for i in self.mp3_block_question:
                    already_used_block.append(i[0].text())
                already_used_block = list(set(already_used_block))

                # 기준보다 앞에 배치해야 한다면
                if len(self.mp3_block_question) > 0:
                    # print(block_order.index(group_name))
                    # 생성한 블럭이 위치가 어딘지 확인
                    target_index = block_order.index(group_name)
                    # 앞단에 있는 블럭 리스트 뽑기
                    formal_blocks = []
                    for i in range(target_index):
                        # print('블럭 이름 >>>>>>>>>>>> ', self.mp3_block_list[i][0].text())
                        formal_blocks.append(self.mp3_block_list[i][0].text())

                    last_block_name = ''
                    # 가장 뒤에 있는 앞쪽 블럭
                    for block in formal_blocks:
                        if block in already_used_block:
                            last_block_name = block
                    # 앞쪽에 블럭 이름을 이미 추가했으면
                    if len(last_block_name) > 0:
                        for mp3_block in self.mp3_block_question:
                            if mp3_block[0].text() == last_block_name:
                                last_mp3_block = mp3_block
                        index_mp3_block = self.mp3_block_question.index(last_mp3_block)
                        # 마지막 앞 블럭 뒤에 배치
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_question.insert(index_mp3_block+1, mp3box)
                        mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_answer.insert(index_mp3_block+1, mp3box2)
                    # 아니면 가장 앞으로 추가.
                    else:
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_question.insert(0, mp3box)
                        mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_answer.insert(0, mp3box2)
                else:
                    # 뒤쪽에 배치
                    mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                    self.mp3_block_question.append(mp3box)
                    mp3box2 = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                    self.mp3_block_answer.append(mp3box2)
        for group in self.mp3_block_question:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout2.addWidget(mp3groupbox)
        self.label_sum.setText(self._translate("Window", "문제 총 개수 : {}".format(len(self.mp3_block_question))))

        for group in self.mp3_block_answer:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout3.addWidget(mp3groupbox)
        self.label_sum2.setText(self._translate("Window", "정답 총 개수 : {}".format(len(self.mp3_block_answer))))
    # 블럭 체크박스 해제
    def releasedCheckBox(self, mp3_block, group_name, index_checkbox):
        count = 0
        for group in mp3_block:
            if group[0].text() == group_name:
                if str(group[1].text()) == str(self.punch_index[index_checkbox]):
                    mp3_block.remove(group)
                    break
                count += 1

    # 합계 계산
    def updateSum(self):
        for group in self.mp3_block_list:
            count = 0
            for item in group:
                # print(item)
                try:
                    if item.isChecked():
                        count += 1
                except:
                    # 체크박스가 아니면 에러발생하도록
                    # print('err updateSum')
                    pass
            # print(count)
            group[-2].setText(str(count))

    # 삭제 버튼
    def btn_delete(self, button):
        for group in self.mp3_block_list:
            if group[-1] == button:
                group_name = group[0].text()
                check_box = group[1:-2]
                self.mp3_block_list.remove(group)
        self.ScrollAreaSet()
        self.Arrangement()
        self.ScrollArea2Set()
        self.ScrollArea3Set()

        delete_tmp = []
        for group in self.mp3_block_question:
            if group[0].text() == group_name:
                delete_tmp.append(group)
        for group in delete_tmp:
            if group in self.mp3_block_question:
                self.mp3_block_question.remove(group)
        delete_tmp = []
        for group in self.mp3_block_answer:
            if group[0].text() == group_name:
                delete_tmp.append(group)
        for group in delete_tmp:
            if group in self.mp3_block_answer:
                self.mp3_block_answer.remove(group)
        for group in self.mp3_block_question:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout2.addWidget(mp3groupbox)
        self.label_sum.setText(self._translate("Window", "문제 총 개수 : {}".format(len(self.mp3_block_question))))

        for group in self.mp3_block_answer:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout3.addWidget(mp3groupbox)
        self.label_sum2.setText(self._translate("Window", "정답 총 개수 : {}".format(len(self.mp3_block_answer))))

    # scroll area 초기 세팅
    def ScrollAreaSet(self):
        self.mp3_scroll_area = QtWidgets.QScrollArea(self)
        self.mp3_scroll_area.setWidgetResizable(True)
        self.widget1 = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget1)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget1)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.mp3_scroll_area, 1, 0, 1, 1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mp3_layout)

    # question scroll area2 초기 세팅
    def ScrollArea2Set(self):
        self.mp3_scroll_area2 = QtWidgets.QScrollArea(self)
        self.mp3_scroll_area2.setWidgetResizable(True)
        # self.mp3_scroll_area2.setStyleSheet("background-color : white")
        self.widget2 = QtWidgets.QWidget()
        self.mp3_scroll_area2.setWidget(self.widget2)
        self.mp3_scroll_area2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout2 = QtWidgets.QVBoxLayout(self.widget2)
        self.mp3_layout2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout2.addWidget(self.mp3_scroll_area2, 1, 0, 1, 1)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mp3_layout2)

    # answer scroll area3 초기 세팅
    def ScrollArea3Set(self):
        self.mp3_scroll_area3 = QtWidgets.QScrollArea(self)
        self.mp3_scroll_area3.setWidgetResizable(True)
        # self.mp3_scroll_area3.setStyleSheet("background-color : white")
        self.widget3 = QtWidgets.QWidget()
        self.mp3_scroll_area3.setWidget(self.widget3)
        self.mp3_scroll_area3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout3 = QtWidgets.QVBoxLayout(self.widget3)
        self.mp3_layout3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout3.addWidget(self.mp3_scroll_area3, 1, 0, 1, 1)
        self.gridLayout3.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mp3_layout3)

    # scroll area contents 다시 뿌리기
    def ConvertToObj(self):
        tmp_mp3_block_list = []
        for group in self.mp3_block_list:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            font = self.fontsettings_basic()
            count = 0
            mp3box = []
            for item in group:
                if item == group[0]:
                    # 블럭 이름
                    block_name = QtWidgets.QLineEdit(mp3groupbox)
                    block_name.setMaximumWidth(60)
                    block_name.setFrame(False)
                    block_name.setStyleSheet("background-color : rgb(250,250,250)")
                    block_name.setFont(font)
                    block_name.setText(item)
                    block_name.editingFinished.connect(partial(self.changedBlockName, block_name))
                    layout_groupbox.addWidget(block_name)
                    mp3box.append(block_name)
                elif item in group[1:-1]:
                    # 체크박스
                    check_box = QtWidgets.QCheckBox("{}좌표".format(count+1), mp3groupbox)
                    check_box.setFont(font)
                    check_box.setMaximumWidth(130)
                    check_box.setTristate(False)
                    if item == 0:
                        check_box.setCheckState(False)
                    else:
                        check_box.setCheckState(2)
                    check_box.stateChanged.connect(partial(self.checkStateChanged, check_box, mp3box))
                    layout_groupbox.addWidget(check_box)
                    mp3box.append(check_box)
                    count += 1
                elif item == group[-1]:
                    # 합계 라벨
                    label_count = QtWidgets.QLabel(mp3groupbox)
                    label_count.setFont(font)
                    label_count.setAlignment(QtCore.Qt.AlignCenter)
                    label_count.setMaximumWidth(60)
                    label_count.setText(item)
                    label_count.setStyleSheet("color : green")
                    layout_groupbox.addWidget(label_count)
                    mp3box.append(label_count)
            # 삭제 버튼
            delete_button = QtWidgets.QPushButton(mp3groupbox)
            delete_button.setFont(font)
            delete_button.setMaximumWidth(30)
            delete_button.setStyleSheet("color: skyblue")
            delete_button.clicked.connect(partial(self.btn_delete, delete_button))
            delete_button.setText(self._translate("Window", "삭제"))
            layout_groupbox.addWidget(delete_button)
            mp3box.append(delete_button)
            self.mp3_layout.addWidget(mp3groupbox)
            tmp_mp3_block_list.append(mp3box)
        self.mp3_block_list = tmp_mp3_block_list

    # scroll area2 다시뿌리기
    def ConvertToObj_2_q(self, mp3_layout, label_sum):
        tmp_mp3_block_info = []

        for group in self.mp3_block_question:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            font = self.fontsettings_basic()
            mp3box = []

            # 이름 라벨
            label_name = QtWidgets.QLabel()
            font.setWeight(40)
            label_name.setFont(font)
            label_name.setAlignment(QtCore.Qt.AlignCenter)
            label_name.setMaximumWidth(60)
            label_name.setText(group[0])
            layout_groupbox.addWidget(label_name)
            mp3box.append(label_name)

            # block 좌표
            label_pos = QtWidgets.QLabel()
            font = self.fontsettings_basic()
            label_pos.setFont(font)
            label_pos.setAlignment(QtCore.Qt.AlignCenter)
            label_pos.setMaximumWidth(60)
            label_pos.setText(str(group[1]))
            layout_groupbox.addWidget(label_pos)
            mp3box.append(label_pos)

            # mp3 입력 칸
            mp3_address = QtWidgets.QLineEdit()
            mp3_address.setFrame(False)
            mp3_address.setFont(font)
            mp3_address.setText(group[2])
            layout_groupbox.addWidget(mp3_address)
            mp3box.append(mp3_address)

            # mp3 개수 라벨
            label_count = QtWidgets.QLabel()
            label_count.setFont(font)
            label_count.setAlignment(QtCore.Qt.AlignCenter)
            label_count.setMaximumWidth(60)
            label_count.setText(group[3])
            label_count.setStyleSheet("color : green")
            mp3box[-1].textChanged.connect(partial(self.mp3Count, mp3box[-1], label_count))
            layout_groupbox.addWidget(label_count)
            mp3box.append(label_count)

            mp3_layout.addWidget(mp3groupbox)
            tmp_mp3_block_info.append(mp3box)
        self.mp3_block_question = tmp_mp3_block_info

        label_sum.setText(self._translate("Window", "문제 총 개수 : {}".format(len(self.mp3_block_question))))

    # scroll area3 다시뿌리기
    def ConvertToObj_2_a(self, mp3_layout, label_sum2):
        tmp_mp3_block_info = []

        for group in self.mp3_block_answer:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            font = self.fontsettings_basic()
            mp3box = []

            # 이름 라벨
            label_name = QtWidgets.QLabel()
            font.setWeight(40)
            label_name.setFont(font)
            label_name.setAlignment(QtCore.Qt.AlignCenter)
            label_name.setMaximumWidth(60)
            label_name.setText(group[0])
            layout_groupbox.addWidget(label_name)
            mp3box.append(label_name)

            # block 좌표
            label_pos = QtWidgets.QLabel()
            font = self.fontsettings_basic()
            label_pos.setFont(font)
            label_pos.setAlignment(QtCore.Qt.AlignCenter)
            label_pos.setMaximumWidth(60)
            label_pos.setText(str(group[1]))
            layout_groupbox.addWidget(label_pos)
            mp3box.append(label_pos)

            # mp3 입력 칸
            mp3_address = QtWidgets.QLineEdit()
            mp3_address.setFrame(False)
            mp3_address.setFont(font)
            mp3_address.setText(group[2])
            layout_groupbox.addWidget(mp3_address)
            mp3box.append(mp3_address)

            # mp3 개수 라벨
            label_count = QtWidgets.QLabel()
            label_count.setFont(font)
            label_count.setAlignment(QtCore.Qt.AlignCenter)
            label_count.setMaximumWidth(60)
            label_count.setText(group[3])
            label_count.setStyleSheet("color : green")
            mp3box[-1].textChanged.connect(partial(self.mp3Count, mp3box[-1], label_count))
            layout_groupbox.addWidget(label_count)
            mp3box.append(label_count)

            mp3_layout.addWidget(mp3groupbox)
            tmp_mp3_block_info.append(mp3box)
        self.mp3_block_answer = tmp_mp3_block_info

        label_sum2.setText(self._translate("Window", "정답 총 개수 : {}".format(len(self.mp3_block_answer))))

    # scroll area contents 다시 뿌리기
    def Arrangement(self):
        for group in self.mp3_block_list:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout.addWidget(mp3groupbox)

    # 블럭 이름 바뀔 때
    def changedBlockName(self, block_name):
        # 음원 정보의 블럭이름 바뀌도록
        blocks_name = []
        for block in self.mp3_block_list:
            blocks_name.append(block[0].text())
        blocks_name.remove(block_name.text())
        for mp3_block in self.mp3_block_question:
            if mp3_block[0].text() not in blocks_name:
                old_name = mp3_block[0].text()
                break
        if block_name.text() in blocks_name:
            self.error_dialog()
            block_name.setText(old_name)
        else:
            for mp3_block in self.mp3_block_question:
                if mp3_block[0].text() not in blocks_name:
                    mp3_block[0].setText(block_name.text())
            for mp3_block in self.mp3_block_answer:
                if mp3_block[0].text() not in blocks_name:
                    mp3_block[0].setText(block_name.text())

    # 블럭 음원 정보
    def loadBlocksInfo(self):
        block_list = self.blocksContents()
        self.mp3_block_question = []
        if len(self.mp3_block_question) == 0:
            for block in block_list:
                checkbox = block[1:-1]
                pos = [index for index, value in enumerate(checkbox) if value == 2]
                count = 0
                item_name = block[0]
                for item in checkbox:
                    if item == 2:
                        mp3groupbox = QtWidgets.QGroupBox()
                        mp3groupbox.setStyleSheet("border:none")
                        layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
                        layout_groupbox.setContentsMargins(5, 3, 5, 3)
                        font = self.fontsettings_basic()
                        mp3box = []
                        # 이름 라벨
                        label_name = QtWidgets.QLabel()
                        font.setWeight(40)
                        label_name.setFont(font)
                        label_name.setAlignment(QtCore.Qt.AlignCenter)
                        label_name.setMaximumWidth(60)
                        label_name.setText(item_name)
                        layout_groupbox.addWidget(label_name)
                        mp3box.append(label_name)
                        # 좌표 라벨
                        label_pos = QtWidgets.QLabel()
                        font = self.fontsettings_basic()
                        label_pos.setFont(font)
                        label_pos.setAlignment(QtCore.Qt.AlignCenter)
                        label_pos.setMaximumWidth(60)
                        label_pos.setText(str(self.punch_index[pos[count]]))
                        layout_groupbox.addWidget(label_pos)
                        mp3box.append(label_pos)
                        count += 1
                        # mp3 개수 라벨
                        label_count = QtWidgets.QLabel()
                        label_count.setFont(font)
                        label_count.setAlignment(QtCore.Qt.AlignCenter)
                        label_count.setMaximumWidth(60)
                        label_count.setText(str(0))
                        label_count.setStyleSheet("color : green")
                        # mp3 입력 칸
                        mp3_address = QtWidgets.QLineEdit()
                        mp3_address.setFrame(False)
                        mp3_address.setFont(font)
                        mp3_address.setText("")
                        mp3_address.textChanged.connect(partial(self.mp3Count, mp3_address, label_count))
                        layout_groupbox.addWidget(mp3_address)
                        mp3box.append(mp3_address)

                        layout_groupbox.addWidget(label_count)
                        mp3box.append(label_count)

                        self.mp3_layout2.addWidget(mp3groupbox)
                        self.mp3_block_question.append(mp3box)

        self.label_sum.setText(self._translate("Window", "문제 총 개수 : {}".format(len(self.mp3_block_question))))

    # 체크박스 적용시 음원정보 추가
    def addMp3BlockInfo(self, item_name, punch_index):
        font = self.fontsettings_basic()
        mp3box = []
        # 이름 라벨
        label_name = QtWidgets.QLabel()
        font.setWeight(40)
        label_name.setFont(font)
        label_name.setAlignment(QtCore.Qt.AlignCenter)
        label_name.setMaximumWidth(60)
        label_name.setText(item_name)
        mp3box.append(label_name)
        # 좌표 라벨
        label_pos = QtWidgets.QLabel()
        font = self.fontsettings_basic()
        label_pos.setFont(font)
        label_pos.setAlignment(QtCore.Qt.AlignCenter)
        label_pos.setMaximumWidth(60)
        label_pos.setText(str(punch_index))
        mp3box.append(label_pos)
        # mp3 개수 라벨
        label_count = QtWidgets.QLabel()
        label_count.setFont(font)
        label_count.setAlignment(QtCore.Qt.AlignCenter)
        label_count.setMaximumWidth(60)
        label_count.setText(str(0))
        label_count.setStyleSheet("color : green")
        # mp3 입력 칸
        mp3_address = QtWidgets.QLineEdit()
        mp3_address.setFrame(False)
        mp3_address.setFont(font)
        mp3_address.setText("")
        mp3_address.textChanged.connect(partial(self.mp3Count, mp3_address, label_count))
        mp3box.append(mp3_address)
        mp3box.append(label_count)

        return mp3box

    # 음원 숫자세기
    def mp3Count(self, mp3_address, label_count):
        count = 0
        if mp3_address.text() != '':
            count += 1
            count += mp3_address.text().count(',')
        else:
            count = 0
        label_count.setText(str(count))

    # 블럭 내용 추출
    def blocksContents(self):
        blocks = []
        for group in self.mp3_block_list:
            tmp = []
            for item in group:
                if item == group[0]:
                    tmp.append(item.text())
                elif item in group[1:-2]:
                    tmp.append(item.checkState())
                elif item == group[-2]:
                    tmp.append(item.text())
            blocks.append(tmp)
        return blocks

    # 블럭 mp3 내용 추출
    def blocksMp3Contents(self, mp3_blocks):
        blocks_mp3 = []
        for group in mp3_blocks:
            tmp = []
            for item in group:
                if item == group[1]:
                    item = ast.literal_eval(item.text())
                    tmp.append(item)
                else:
                    # item.text().strip("''")
                    tmp.append(item.text())
            blocks_mp3.append(tmp)
        return blocks_mp3

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, e):
        ui.mp3_block_list = self.blocksContents()
        # print(self.blocksContents())
        # print(self.punch_index)
        ui.mp3_block_question = self.blocksMp3Contents(self.mp3_block_question)
        ui.mp3_block_answer = self.blocksMp3Contents(self.mp3_block_answer)
        ui.punch = self.punch_index
        # print('close event', self.blocksMp3Contents())
        # print('close event ', self.blocksMp3Contents(self.mp3_block_question))
        # print('close event ', self.blocksMp3Contents(self.mp3_block_answer))
        # 닫은 후 table widget 안변하는 것 방지
        global table_widget_id
        table_widget_id = []

    # 폰트 세팅
    def fontsettings_basic(self, size=10):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font

    # 에러 메세지
    def error_dialog(self):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage("중복된 이름의 블럭이 있습니다.")
        error_dialog.exec_()

# 변경없이 다른 정보 눌렀을 때 확인 다이얼로그
class checkDialog(QtWidgets.QDialog):
    def __init__(self, obj, name, mp3, mp3_block_list, mp3_block_question, mp3_block_answer, punch):
        super().__init__()
        self.setupUI()
        self.obj = obj
        self.name = name
        self.mp3 = mp3
        self.mp3_block_list = mp3_block_list
        self.mp3_block_question = mp3_block_question
        self.mp3_block_answer = mp3_block_answer
        self.punch = punch

    def setupUI(self):
        self.setGeometry(600, 400, 300, 100)
        self.setWindowTitle("변경된 정보 저장 확인")

        text = QtWidgets.QLabel("변경한 정보를 저장하시겠습니까?")
        font = self.fontsettings()
        text.setFont(font)
        text.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton1 = QtWidgets.QPushButton("저장")
        font = self.fontsettings(10)
        self.pushButton1.setFont(font)
        self.pushButton1.clicked.connect(self.pushSaveButtonClicked)
        self.pushButton2 = QtWidgets.QPushButton("취소")
        self.pushButton2.setFont(font)
        self.pushButton2.clicked.connect(self.pushCancelButtonClicked)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(text, 0, 0)
        layout.addWidget(self.pushButton1, 1, 1)
        layout.addWidget(self.pushButton2, 1, 2)

        self.setLayout(layout)

    def pushSaveButtonClicked(self):
        self.obj.name = self.name
        self.obj.mp3 = self.mp3
        self.obj.mp3_block_list = self.mp3_block_list
        self.obj.mp3_block_question = self.mp3_block_question
        self.obj.mp3_block_answer = self.mp3_block_answer
        self.obj.punch = self.punch
        self.close()

    def pushCancelButtonClicked(self):
        self.close()

    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget_QnA = QtWidgets.QWidget()
    ui = Ui_widget_QnA()
    ui.setupUi(widget_QnA)
    widget_QnA.show()


    sys.exit(app.exec_())
