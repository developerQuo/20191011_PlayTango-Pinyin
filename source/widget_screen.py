# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from block_init import ScreenObject
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import pickle
import ast

table_widget_id = []
selected_screen = None
size_x = 14
size_y = 21

class Ui_Form_Screen(object):
    def __init__(self):
        self.mp3_list = []
        self.screen_list = []
        self.mp3_block_list = []
        self.mp3_block_info = []
        self.punch_pos = []
        self._translate = QtCore.QCoreApplication.translate

        global ui_screen
        ui_screen = self


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1197, 800)
        Form.setMinimumSize(QtCore.QSize(1024, 512))

        # 놀이판 설정 groupbox
        self.gb_screen_init = QtWidgets.QGroupBox(Form)
        self.gb_screen_init.setGeometry(QtCore.QRect(20, 20, 271, 341))
        font = self.fontsettings_basic()
        self.gb_screen_init.setFont(font)
        self.gb_screen_init.setObjectName("gb_screen_init")
        # 놀이판 이름 설정
        self.label_screen_name = QtWidgets.QLabel(self.gb_screen_init)
        self.label_screen_name.setGeometry(QtCore.QRect(10, 20, 81, 41))
        font = self.fontsettings_basic()
        self.label_screen_name.setFont(font)
        self.label_screen_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_screen_name.setObjectName("label_screen_name")
        self.set_screen_num = QtWidgets.QLineEdit(self.gb_screen_init)
        self.set_screen_num.setGeometry(QtCore.QRect(100, 30, 141, 21))
        self.set_screen_num.setObjectName("set_screen_num")
        # self.set_screen_num.setFrame(False)
        # self.set_screen_num.setStyleSheet("background-color : red")
        # 인식 범위
        self.label_minmax = QtWidgets.QLabel(self.gb_screen_init)
        self.label_minmax.setGeometry(QtCore.QRect(10, 60, 81, 41))
        font = self.fontsettings_basic()
        self.label_minmax.setFont(font)
        self.label_minmax.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minmax.setObjectName("label_minmax")
        self.spinBox_min = QtWidgets.QSpinBox(self.gb_screen_init)
        self.spinBox_min.setGeometry(QtCore.QRect(102, 70, 61, 22))
        self.spinBox_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_min.setMaximum(10000)
        self.spinBox_min.setObjectName("spinBox_min")
        self.label_minmax_x = QtWidgets.QLabel(self.gb_screen_init)
        self.label_minmax_x.setGeometry(QtCore.QRect(160, 70, 21, 21))
        font = self.fontsettings_basic()
        self.label_minmax_x.setFont(font)
        self.label_minmax_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minmax_x.setObjectName("label_minmax_x")
        self.spinBox_max = QtWidgets.QSpinBox(self.gb_screen_init)
        self.spinBox_max.setGeometry(QtCore.QRect(180, 70, 61, 22))
        self.spinBox_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_max.setMaximum(10000)
        self.spinBox_max.setObjectName("spinBox_max")

        self.label_mp3_title = QtWidgets.QLabel(self.gb_screen_init)
        self.label_mp3_title.setGeometry(QtCore.QRect(3, 115, 81, 21))
        font = self.fontsettings_basic()
        self.label_mp3_title.setFont(font)
        self.label_mp3_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_title.setObjectName("label_mp3_title")
        self.label_mp3_lang = QtWidgets.QLabel(self.gb_screen_init)
        self.label_mp3_lang.setGeometry(QtCore.QRect(83, 115, 30, 21))
        font = self.fontsettings_basic()
        self.label_mp3_lang.setFont(font)
        self.label_mp3_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_lang.setObjectName("label_mp3_lang")
        self.label_mp3_address = QtWidgets.QLabel(self.gb_screen_init)
        self.label_mp3_address.setGeometry(QtCore.QRect(105, 115, 141, 21))
        font = self.fontsettings_basic()
        self.label_mp3_address.setFont(font)
        self.label_mp3_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mp3_address.setObjectName("label_mp3_address")
        # 음원
        self.mp3_scroll_area = QtWidgets.QScrollArea(self.gb_screen_init)
        self.mp3_scroll_area.setGeometry(QtCore.QRect(5, 140, 261, 150))
        self.mp3_scroll_area.setWidgetResizable(True)
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        self.loadMp3Box()
        # 음원 추가버튼
        self.btn_new_mp3 = QtWidgets.QPushButton(self.gb_screen_init)
        self.btn_new_mp3.setGeometry(QtCore.QRect(23, 300, 101, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_new_mp3.setFont(font)
        self.btn_new_mp3.setObjectName("btn_new_mp3")
        # 음원 삭제버튼
        self.btn_del_mp3 = QtWidgets.QPushButton(self.gb_screen_init)
        self.btn_del_mp3.setGeometry(QtCore.QRect(145, 300, 101, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_del_mp3.setFont(font)
        self.btn_del_mp3.setObjectName("btn_del_mp3")

        # 생성버튼
        self.btn_new = QtWidgets.QPushButton(Form)
        self.btn_new.setGeometry(QtCore.QRect(30, 370, 101, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        # 저장 버튼
        self.btn_apply = QtWidgets.QPushButton(Form)
        self.btn_apply.setGeometry(QtCore.QRect(142, 370, 61, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_apply.setFont(font)
        self.btn_apply.setObjectName("btn_apply")
        # 삭제버튼
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setGeometry(QtCore.QRect(214, 370, 61, 28))
        font = self.fontsettings_basic()
        font.setPointSize(10)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")

        # 미리보기버튼
        self.btn_preview = QtWidgets.QPushButton(Form)
        self.btn_preview.setGeometry(QtCore.QRect(1070, 25, 117, 38))
        self.btn_preview.setMaximumSize(QtCore.QSize(93, 28))
        font = self.fontsettings_basic()
        self.btn_preview.setFont(font)
        self.btn_preview.setObjectName("btn_preview")

        # 타공위치 설정
        self.gb_block_size = QtWidgets.QGroupBox(Form)
        self.gb_block_size.setGeometry(QtCore.QRect(310, 60, 881, 631))
        font = self.fontsettings_basic()
        self.gb_block_size.setFont(font)
        self.gb_block_size.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.gb_block_size.setObjectName("gb_block_size")
        self.tableWidget = QtWidgets.QTableWidget(self.gb_block_size)
        self.tableWidget.setGeometry(QtCore.QRect(0, 25, 867, 586))
        font = self.fontsettings_basic()
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(21)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        stylesheet = "QHeaderView::section{Background-color:rgb(183, 140, 151); border - radius: 14px;}"
        self.tableWidget.setStyleSheet(stylesheet)
        self.tableWidget.setRowCount(size_x)
        self.tableWidget.setColumnCount(size_y)
        self.tableWidget.setCellWidget(40,40, QtWidgets.QTextEdit())
        self.tableWidget.resizeColumnsToContents()

        # 놀이판 목록
        self.gb_screen_init_2 = QtWidgets.QGroupBox(Form)
        self.gb_screen_init_2.setGeometry(QtCore.QRect(20, 410, 271, 381))
        font = self.fontsettings_basic()
        self.gb_screen_init_2.setFont(font)
        self.gb_screen_init_2.setObjectName("gb_screen_init_2")
        # 목록 칸 생성
        self.widget_screen_list = QtWidgets.QListWidget(self.gb_screen_init_2)
        self.widget_screen_list.setGeometry(QtCore.QRect(50, 30, 171, 325))
        font = self.fontsettings(10)
        self.widget_screen_list.setFont(font)
        self.widget_screen_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.widget_screen_list.setItemAlignment(QtCore.Qt.AlignCenter)
        self.widget_screen_list.setObjectName("widget_screen_list")

        # 닫기버튼
        self.btn_close = QtWidgets.QPushButton(Form)
        self.btn_close.setGeometry(QtCore.QRect(1060, 735, 111, 41))
        font = self.fontsettings()
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        # 타공버튼
        self.btn_punch = QtWidgets.QPushButton(Form)
        self.btn_punch.setGeometry(QtCore.QRect(480, 715, 151, 61))
        self.btn_punch.setFont(font)
        self.btn_punch.setObjectName("btn_punch")
        # 타공취소버튼
        self.btn_cancel_punch = QtWidgets.QPushButton(Form)
        self.btn_cancel_punch.setGeometry(QtCore.QRect(650, 715, 151, 61))
        self.btn_cancel_punch.setFont(font)
        self.btn_cancel_punch.setObjectName("btn_cancel_punch")
        # txt 출력 버튼
        self.btn_output = QtWidgets.QPushButton(Form)
        self.btn_output.setGeometry(QtCore.QRect(930, 735, 111, 41))
        self.btn_output.setFont(font)
        self.btn_output.setObjectName("btn_output")

        self.retranslateUi(Form)
        self.btn_new_mp3.clicked.connect(self.initMp3)
        self.btn_del_mp3.clicked.connect(self.delMp3)
        self.btn_new.clicked.connect(self.initScreen)
        self.btn_del.clicked.connect(self.deleteScreen)
        self.btn_punch.clicked.connect(self.punchScreen)
        self.btn_cancel_punch.clicked.connect(self.cancelPunchScreen)
        self.btn_output.clicked.connect(self.output)
        self.btn_close.clicked.connect(Form.close)
        self.btn_apply.clicked.connect(self.saveScreen)
        self.widget_screen_list.itemClicked['QListWidgetItem*'].connect(self.selectScreen)
        self.tableWidget.itemChanged['QTableWidgetItem*'].connect(self.tableItemChanged)
        self.btn_preview.clicked.connect(self.unconstrainedPlay)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.loadData()
        self.blocksizeLoad(self.tableWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_screen_init.setTitle(_translate("Form", "놀이판"))
        self.label_screen_name.setText(_translate("Form", "놀이판 \n식별번호"))
        self.label_minmax.setText(_translate("Form", "낱말카드 \n인식 범위"))
        self.label_minmax_x.setText(_translate("Form", "~"))
        self.label_mp3_title.setText(_translate("Form", "음원 항목"))
        self.label_mp3_lang.setText(_translate("Form", "언어"))
        self.label_mp3_address.setText(_translate("Form", "음원 주소"))
        self.btn_apply.setText(_translate("Form", "저장"))
        self.btn_preview.setText(_translate("Form", "자유놀이정보"))
        self.gb_block_size.setTitle(_translate("Form", "타공위치 (하양: 1,  검정: 0  입력)"))
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.gb_screen_init_2.setTitle(_translate("Form", "놀이판 목록"))
        self.btn_del.setText(_translate("Form", "제거"))
        self.btn_new.setText(_translate("Form", "새로만들기"))
        self.btn_new_mp3.setText(_translate("Form", "음원 목록 추가"))
        self.btn_del_mp3.setText(_translate("Form", "음원 목록 삭제"))
        __sortingEnabled = self.widget_screen_list.isSortingEnabled()
        self.widget_screen_list.setSortingEnabled(False)
        self.widget_screen_list.setSortingEnabled(__sortingEnabled)
        self.btn_close.setText(_translate("Form", "닫기"))
        self.btn_punch.setText(_translate("Form", "타공"))
        self.btn_cancel_punch.setText(_translate("Form", "타공취소"))
        self.btn_output.setText(_translate("Form", "txt출력"))


    # 가져올 데이터 선택
    def loadData(self):
        try:
            with open('screen_info.p', 'rb') as file:
                self.screen_list = pickle.load(file)[0]
        except:
            # print('failed to load data')
            self.screen_list = []
        self.widgetScreenList_reload()

    # widget_screen_list 선택 시 정보 불러오기
    def selectScreen(self, count=None):
        # self.target = self.widget_screen_list.currentRow()
        if type(count) == int:
            self.target = count
        else:
            self.checkToSave()
            self.target = self.widget_screen_list.currentRow()

        global selected_screen
        selected_screen = self.screen_list[self.target]

        self.set_screen_num.setText(self._translate("Form", "{}".format(selected_screen.name)))
        self.spinBox_min.setValue(selected_screen.minmax[0])
        self.spinBox_max.setValue(selected_screen.minmax[1])
        self.mp3_block_list = selected_screen.blocks
        self.mp3_block_info = selected_screen.blocks_mp3
        self.punch_pos = selected_screen.punch
        self.loadMp3()

        self.blocksizeLoad(selected_screen)

    # 저장된 블럭 값 가져오기
    def blocksizeLoad(self, tablewidget):
        self.tableWidget.setRowCount(size_x)
        self.tableWidget.setColumnCount(size_y)
        self.tableWidget.setCellWidget(40, 40, QtWidgets.QTextEdit())
        self.tableWidget.resizeColumnsToContents()
        input = str(0)
        count = 0
        for x in range(size_x):
            for y in range(size_y):
                item = QtWidgets.QTableWidgetItem()
                try:
                    item.setText(str(table_widget_id[count]))
                except:
                    try:
                        item.setText(str(tablewidget.id[count]))
                    except:
                        item.setText(input)
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(x, y, item)
                try:
                    if self.tableWidget.item(x, y).text() == '0':
                        self.tableWidget.item(x, y).setBackground(Qt.black)
                except:
                    pass
                count += 1


    # 타공시 색변경
    def tableItemChanged(self):
        for item in self.tableWidget.selectedItems():
            if item.text() == '0':
                item.setBackground(Qt.black)
            else:
                # print(self.tableWidget.row(item))
                if self.tableWidget.row(item) % 2 == 1:
                    item.setBackground(QtGui.QColor(244,244,244))
                else:
                    item.setBackground(Qt.white)

    # 놀이판 추가
    def initScreen(self):
        id = []
        for x in range(size_x):
            for y in range(size_y):
                try:
                    id.append(int(self.tableWidget.item(x, y).text()))
                except:
                    id.append(0)
        name = self.set_screen_num.text()
        size = [size_x, size_y]
        minmax = [self.spinBox_min.value(), self.spinBox_max.value()]
        mp3 = []
        for obj in self.mp3_list:
            tmp = []
            for count in obj:
                tmp.append(count.text())
            mp3.append(tmp)
        blocks = self.mp3_block_list
        blocks_mp3 = self.mp3_block_info
        punch = self.punch_pos
        screen = ScreenObject(name=name, x=size[0], y=size[1], id=id, minmax=minmax, mp3=mp3, blocks=blocks, blocks_mp3=blocks_mp3, punch = punch)
        self.screen_list.append(screen)
        count = len(self.screen_list)-1
        self.widgetBlockList(self.widget_screen_list, screen, count)
        self.selectScreen(-1)

        self.applyData()

    # 놀이판 삭제
    def deleteScreen(self):
        try:
            del self.screen_list[self.target]
            self.selectScreen()
        except:
            pass
        self.widgetScreenList_reload()

        self.applyData()

    # 놀이판 적용
    def saveScreen(self):
        id = []
        for x in range(size_x):
            for y in range(size_y):
                id.append(int(self.tableWidget.item(x, y).text()))
        # 같은 이름 중복 제거
        for n in self.screen_list:
            if self.target != self.screen_list.index(n) and self.set_screen_num.text() == n.name:
                self.check_error = 1
                break
            else:
                self.check_error = 0
        if self.check_error == 1:
            self.error_dialog('중복된 이름입니다!')
        elif self.check_error == 0:
            selected_screen.name = self.set_screen_num.text()
            selected_screen.size = [size_x, size_y]
            selected_screen.id = id
            selected_screen.minmax = [self.spinBox_min.value(), self.spinBox_max.value()]
            mp3 = []
            for obj in self.mp3_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            selected_screen.mp3 = mp3
            selected_screen.blocks = self.mp3_block_list
            selected_screen.blocks_mp3 = self.mp3_block_info
            selected_screen.punch = self.punch_pos
        count = self.widget_screen_list.currentRow()
        self.widgetScreenList_reload(count)
        self.selectScreen(count=count)

        self.applyData()

    # 저장없이 다른 놀이판 눌렀을 때 확인
    def checkToSave(self):
        global selected_screen
        try:
            table_id = []
            for x in range(14):
                for y in range(21):
                    table_id.append(int(self.tableWidget.item(x, y).text()))
            mp3 = []
            for obj in self.mp3_list:
                tmp = []
                for count in obj:
                    tmp.append(count.text())
                mp3.append(tmp)
            # print(selected_screen.blocks_mp3)
            # print(self.mp3_block_info)
            # print(selected_screen.punch)
            # print(self.punch_pos)
            if selected_screen.name == self.set_screen_num.text() and selected_screen.id == table_id and selected_screen.minmax == [self.spinBox_min.value(), self.spinBox_max.value()] and selected_screen.mp3 == mp3 and selected_screen.blocks == self.mp3_block_list and selected_screen.blocks_mp3 == self.mp3_block_info and selected_screen.punch == self.punch_pos:
                pass
            else:
                dlg = checkDialog(screen=selected_screen, name=self.set_screen_num.text(), id=table_id, minmax=[self.spinBox_min.value(), self.spinBox_max.value()], mp3=mp3, blocks=self.mp3_block_list, blocks_mp3=self.mp3_block_info, punch=self.punch_pos)
                dlg.exec_()
                selected_screen = dlg.screen
            self.applyData()
        except:
            pass

    # 파일에 정보 저장
    def applyData(self):
        with open('screen_info.p', 'wb') as file:
            pickle.dump([self.screen_list], file)

    def widgetScreenList_reload(self, o_count=-1):
        self.widget_screen_list.clear()
        for count in range(len(self.screen_list)):
            tmp_name = self.screen_list[count].name
            self.widgetBlockList(self.widget_screen_list, tmp_name, count)
        self.widget_screen_list.setCurrentRow = o_count

    def widgetBlockList(self, widget_list, obj, count):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.widget_screen_list.addItem(item)
        item = widget_list.item(count)
        try:
            item.setText(self._translate("Form", "{}".format(obj.name)))
        except:
            item.setText(self._translate("Form", "{}".format(obj)))

    # 놀이판에 타공
    def punchScreen(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        count = 0
        for item in selected_tablewidget_items:
            if count == 0:
                item.setText(str(5))
            else:
                item.setText(str(1))
            count += 1

    # 타공취소
    def cancelPunchScreen(self):
        selected_tablewidget_items = self.tableWidget.selectedItems()
        for item in selected_tablewidget_items:
            item.setText(str(0))

    def error_dialog(self, str):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str)
        error_dialog.exec_()

    # 자유놀이 버튼
    def unconstrainedPlay(self):
        id = []
        for x in range(14):
            for y in range(21):
                id.append(int(self.tableWidget.item(x, y).text()))
        global table_widget_id
        table_widget_id = id


        self.window = Window()
        self.window.InitWindow()
        self.window.show()

    # txt 출력
    def output(self):
        screen = 'screen.txt'
        screen_contents = self.output_id(selected_screen.id)
        with open(screen, 'wt') as f:
            f.write(screen_contents)

        ready = 'init.txt'
        ready_contents = self.output_mp3(selected_screen.mp3)
        with open(ready, 'wt') as f:
            f.write(ready_contents)

        block = 'block.txt'
        block_contents = self.output_blocks_mp3(selected_screen.blocks_mp3)
        with open(block, 'wt') as f:
            f.write(block_contents)

    # 음원항목 추가
    def initMp3(self):
        self.loadMp3Box()

    # 음원박스 추가
    def loadMp3Box(self):
        mp3groupbox = QtWidgets.QGroupBox()
        mp3groupbox.setStyleSheet("border:none")
        layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
        layout_groupbox.setContentsMargins(0,0,0,0)

        label_title = QtWidgets.QLineEdit(mp3groupbox)
        label_title.setMaximumWidth(90)
        layout_groupbox.addWidget(label_title)
        label_lang = QtWidgets.QLineEdit(mp3groupbox)
        label_lang.setMaximumWidth(40)
        layout_groupbox.addWidget(label_lang)
        label_address = QtWidgets.QLineEdit(mp3groupbox)
        layout_groupbox.addWidget(label_address)
        self.mp3_layout.addWidget(mp3groupbox)

        mp3box = [label_lang, label_title, label_address]
        self.mp3_list.append(mp3box)

    # 음원항목 불러오기
    def loadMp3(self):
        # mp3 scrollarea reset
        self.widget = QtWidgets.QWidget()
        self.mp3_scroll_area.setWidget(self.widget)
        self.mp3_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout = QtWidgets.QVBoxLayout(self.widget)
        self.mp3_layout.setContentsMargins(0, 0, 0, 0)
        # mp3 line edit에 정보 로드
        self.mp3_list = []
        for obj in selected_screen.mp3:
            self.loadMp3Box()
            for count in range(3):
                self.mp3_list[-1][count].setText(self._translate("Form", "{}".format(obj[count])))

    # 음원항목 삭제
    def delMp3(self):
        # mp3 정보 임시 저장
        mp3 = []
        for obj in self.mp3_list:
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
        self.mp3_list = []
        for obj in mp3:
            if mp3.index(obj) == len(mp3) - 1:
                break
            else:
                self.loadMp3Box()
                for count in range(3):
                    self.mp3_list[-1][count].setText(self._translate("Form", "{}".format(obj[count][1])))

    # 음원 출력 형식
    def output_mp3(self, mp3_tmp):
        mp3_count = []
        for count in mp3_tmp:
            if len(count[-1]) > 2:
                mp3_count.append(count[-1].count(',') + 1)
            else:
                mp3_count.append(0)
        mp3_contents = 'wordcard,none,1,,\n'
        mp3_save_list = ['wordcard,min,{},,\n',
                         'wordcard,max,{},,\n',]
        mp3_info = '{},{},{},{},\n'
        mp3_save_list2 = []
        for count in range(len(mp3_tmp)):
           mp3_save_list2.append(mp3_info)
        mp3_save_list += mp3_save_list2

        count = 0
        new_count = 0
        for i in mp3_save_list:
            if count == 0:
                mp3_contents += i.format(selected_screen.minmax[0])
            elif count == 1:
                mp3_contents += i.format(selected_screen.minmax[1])
            else:
                mp3_contents += i.format(mp3_tmp[new_count][1], mp3_tmp[new_count][0], mp3_count[new_count], mp3_tmp[new_count][2])
                new_count += 1
            count += 1

        return mp3_contents

    # 자유놀이 출력 형식
    def output_blocks_mp3(self, blocks_mp3):
        mp3_contents = '{},\n'.format(len(blocks_mp3))
        mp3_info = '{},{},{},{},{},\n'
        for block in blocks_mp3:
            mp3_contents += mp3_info.format(block[1][0], block[1][1], block[0], block[3], block[2])
        mp3_contents = mp3_contents.rstrip("\n")

        return mp3_contents

    # id 출력 형식
    def output_id(self, id):
        count = 0
        output = ''
        for ypos in range(size_x):
            output += '\n'
            for xpos in range(size_y):
                # 임시로 초록색 -> 검은색
                if id[count] == 5:
                    output += str(1) + ','
                else:
                    output += str(id[count]) + ','
                count += 1
        output = output.lstrip('\n')
        return output

    def fontsettings_basic(self):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        return font
    def fontsettings(self, size=12):
        font = QtGui.QFont()
        font.setFamily("1훈정글북 R")
        font.setPointSize(size)
        return font


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mp3_block_list = []
        self.mp3_block_info = []
        self.block_count = len(self.mp3_block_list)

        self.title = "자유놀이"
        self.top = 150
        self.left = 150
        self.width = 1140
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
            self.mp3_block_list = ui_screen.mp3_block_list
            self.mp3_block_info = ui_screen.mp3_block_info
            self.ConvertToObj()
        except:
            # print('err ConvertToObj')
            pass

        # right layout
        self.widget2 = QtWidgets.QWidget(self)
        # self.widget2.setStyleSheet("background-color : white")
        self.widget2.setGeometry(840, 0, 300, self.height)
        self.gridLayout2 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout2.setObjectName("gridLayout2")

        self.label_sum = QtWidgets.QLabel(self)
        self.label_sum.setFont(font)
        self.label_sum.setObjectName("label_sum")
        self.label_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sum.setText(self._translate("Window", "총 개수 : {}".format(len(self.mp3_block_info))))
        self.label_sum.setContentsMargins(0, 5, 0, 10)
        self.gridLayout2.addWidget(self.label_sum, 0, 0, 1, 1)

        self.ScrollArea2Set()

        try:
            self.ConvertToObj_2()
            # self.loadBlocksInfo()
        except:
            # print('err ConvertToObj_2')
            pass

    def setLabels(self, font):
        # 타공위치 좌표로 변환
        try:
            punch_index = [index for index, value in enumerate(table_widget_id) if value == 5]
        except:
            pass
        else:
            for index in punch_index:
                quotient = index//21
                remainder = index - quotient*21
                punch_index[punch_index.index(index)] = [quotient+1, remainder+1]
            self.punch_index = punch_index

            # label 이름 뿌리기
            for count in range(len(punch_index)):
                self.label = QtWidgets.QLabel(self)
                self.label.setFont(font)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label.setMaximumWidth(130)
                self.mp3_groupbox_layout.addWidget(self.label)
                self.label.setText(self._translate("Window", str(punch_index[count])))

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
        self.mp3_block_info = []
        self.ScrollAreaSet()
        self.Arrangement()
        self.ScrollArea2Set()
        self.label_sum.setText(self._translate("Window", "총 개수 : {}".format(len(self.mp3_block_info))))

    # 체크박스 체크시 변화
    def checkStateChanged(self, check_box, mp3box):
        self.updateSum()
        self.ScrollArea2Set()
        if mp3box in self.mp3_block_list:
            group_name = mp3box[0].text()
        if check_box in mp3box:
            index_checkbox = mp3box.index(check_box) - 1
        # print('target_mp3box = ', target_mp3box)
        # 체크박스 해제시 음원 넣는칸 제거
        if check_box.checkState() == 0:
            count = 0
            for group in self.mp3_block_info:
                if group[0].text() == group_name:
                    if str(group[1].text())==str(self.punch_index[index_checkbox]):
                        self.mp3_block_info.remove(group)
                        break
                    count += 1
        # 체크박스 적용시 음원 넣는칸 추가
        else:
            new_block = True
            block_order = []
            # 해당 블럭 인덱스 출력
            for block in self.mp3_block_list:
                block_order.append(block[0].text())
            for group in self.mp3_block_info:
                if group[0].text() == group_name:
                    pos = ast.literal_eval(group[1].text())
                    # 첫번째 위치가 같을 때
                    if pos[0] == self.punch_index[index_checkbox][0]:
                        if pos[1] > self.punch_index[index_checkbox][1]:
                            # print("[1]에서 기준보다 위치가 앞인 경우")
                            index = self.mp3_block_info.index(group)
                            # print("index >>> ", index)
                            mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                            self.mp3_block_info.insert(index, mp3box)
                            new_block = False
                            break
                        elif pos[1] < self.punch_index[index_checkbox][1]:
                            # print("[1]에서 기준보다 위치가 뒤인 경우")
                            for block in self.mp3_block_info:
                                if block[0].text() == group[0].text():
                                    checker = ast.literal_eval(block[1].text())
                                    # print(self.punch_index[-1][1],  pos[1])
                                    if self.punch_index[-1][1] == checker[1]:
                                        # print(">>>>>>>>>>>>>>>>>>>continued<<<<<<<<<<<<<<<<<<")
                                        continue
                                    last_block = block
                                    # print(last_block[1].text())
                            index = self.mp3_block_info.index(last_block) + 1
                            # print("index >>> ", index)
                            mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                            self.mp3_block_info.insert(index, mp3box)
                            new_block = False
                            break
                    # 첫번째 위치가 더 작을 때
                    elif pos[0] > self.punch_index[index_checkbox][0]:
                        # print("[0]에서 기준보다 위치가 앞인 경우")
                        index = self.mp3_block_info.index(group)
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_info.insert(index, mp3box)
                        new_block = False
                        break
                    # 첫번째 위치가 더 클 때때
                    elif pos[0] < self.punch_index[index_checkbox][0]:
                        # print("[0]에서 기준보다 위치가 뒤인 경우")
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_info.append(mp3box)
                        new_block = False
                        break
            # 새블럭의 블럭인포
            if new_block == True:

                # 이미 한번이상 사용된 블럭 리스트
                already_used_block = []
                for i in self.mp3_block_info:
                    already_used_block.append(i[0].text())
                already_used_block = list(set(already_used_block))

                # 기준보다 앞에 배치해야 한다면
                if len(self.mp3_block_info) > 0:
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
                        for mp3_block in self.mp3_block_info:
                            if mp3_block[0].text() == last_block_name:
                                last_mp3_block = mp3_block
                        index_mp3_block = self.mp3_block_info.index(last_mp3_block)
                        # 마지막 앞 블럭 뒤에 배치
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_info.insert(index_mp3_block + 1, mp3box)
                    # 아니면 가장 앞으로 추가.
                    else:
                        mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                        self.mp3_block_info.insert(0, mp3box)
                else:
                    # 뒤쪽에 배치
                    mp3box = self.addMp3BlockInfo(group_name, self.punch_index[index_checkbox])
                    self.mp3_block_info.append(mp3box)

        for group in self.mp3_block_info:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout2.addWidget(mp3groupbox)
        self.label_sum.setText(self._translate("Window", "총 개수 : {}".format(len(self.mp3_block_info))))

    # 합계 계산
    def updateSum(self):
        for group in self.mp3_block_list:
            count = 0
            for item in group:
                try:
                    if item.isChecked():
                        count += 1
                except:
                    pass
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

        delete_tmp = []
        for group in self.mp3_block_info:
            if group[0].text() == group_name:
                delete_tmp.append(group)
        for group in delete_tmp:
            if group in self.mp3_block_info:
                self.mp3_block_info.remove(group)
        for group in self.mp3_block_info:
            mp3groupbox = QtWidgets.QGroupBox()
            mp3groupbox.setStyleSheet("border:none")
            layout_groupbox = QtWidgets.QHBoxLayout(mp3groupbox)
            layout_groupbox.setContentsMargins(5, 3, 5, 3)
            mp3box = []
            for item in group:
                layout_groupbox.addWidget(item)
                mp3box.append(item)
            self.mp3_layout2.addWidget(mp3groupbox)
        self.label_sum.setText(self._translate("Window", "총 개수 : {}".format(len(self.mp3_block_info))))

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

    # scroll area2 초기 세팅
    def ScrollArea2Set(self):
        self.mp3_scroll_area2 = QtWidgets.QScrollArea(self)
        self.mp3_scroll_area2.setWidgetResizable(True)
        self.widget2 = QtWidgets.QWidget()
        self.mp3_scroll_area2.setWidget(self.widget2)
        self.mp3_scroll_area2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mp3_layout2 = QtWidgets.QVBoxLayout(self.widget2)
        self.mp3_layout2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout2.addWidget(self.mp3_scroll_area2, 1, 0, 1, 1)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mp3_layout2)

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
    def ConvertToObj_2(self):
        tmp_mp3_block_info = []
        # print(self.mp3_block_info)
        for group in self.mp3_block_info:
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
            mp3box[-1].textChanged.connect(partial(self.mp3Count, mp3box[-1], label_count))
            layout_groupbox.addWidget(label_count)
            mp3box.append(label_count)

            self.mp3_layout2.addWidget(mp3groupbox)
            tmp_mp3_block_info.append(mp3box)
        self.mp3_block_info = tmp_mp3_block_info

        self.label_sum.setText(self._translate("Window", "총 개수 : {}".format(len(self.mp3_block_info))))

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
        for mp3_block in self.mp3_block_info:
            if mp3_block[0].text() not in blocks_name:
                old_name = mp3_block[0].text()
                break
        if block_name.text() in blocks_name:
            self.error_dialog()
            block_name.setText(old_name)
        else:
            for mp3_block in self.mp3_block_info:
                if mp3_block[0].text() not in blocks_name:
                    mp3_block[0].setText(block_name.text())


    # 블럭 음원 정보
    def loadBlocksInfo(self):
        block_list = self.blocksContents()
        self.mp3_block_info = []
        if len(self.mp3_block_info) == 0:
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
                        self.mp3_block_info.append(mp3box)

        self.label_sum.setText(self._translate("Window", "총 개수 : {}".format(len(self.mp3_block_info))))

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
    def blocksMp3Contents(self):
        blocks_mp3 = []
        for group in self.mp3_block_info:
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
        ui_screen.mp3_block_list = self.blocksContents()
        # print(self.blocksContents())
        ui_screen.punch_pos = self.punch_index
        ui_screen.mp3_block_info = self.blocksMp3Contents()
        # print('close event', self.blocksMp3Contents())

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

# 저장 없이 스크린 변경 시 생성되는 다이얼로그
class checkDialog(QtWidgets.QDialog):
    def __init__(self, screen, name, id, minmax, mp3, blocks, blocks_mp3, punch):
        super().__init__()
        self.setupUI()
        self.screen = screen
        self.name = name
        self.id = id
        self.minmax = minmax
        self.mp3 = mp3
        self.blocks = blocks
        self.blocks_mp3 = blocks_mp3
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
        self.screen.name = self.name
        self.screen.id = self.id
        self.screen.minmax = self.minmax
        self.screen.mp3 = self.mp3
        self.screen.blocks = self.blocks
        self.screen.blocks_mp3 = self.blocks_mp3
        self.screen.punch_pos = self.punch
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
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Screen()
    ui.setupUi(Form)
    Form.show()

    w = QtWidgets.QWidget()
    window = Window()
    window.InitWindow()


    sys.exit(app.exec_())
