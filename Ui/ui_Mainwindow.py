# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setMinimumSize(QtCore.QSize(650, 500))
        MainWindow.setMaximumSize(QtCore.QSize(650, 500))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnKonumSec = QtWidgets.QPushButton(self.centralwidget)
        self.btnKonumSec.setGeometry(QtCore.QRect(440, 70, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKonumSec.setFont(font)
        self.btnKonumSec.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKonumSec.setObjectName("btnKonumSec")
        self.txtKonum = QtWidgets.QLineEdit(self.centralwidget)
        self.txtKonum.setGeometry(QtCore.QRect(20, 70, 381, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtKonum.sizePolicy().hasHeightForWidth())
        self.txtKonum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtKonum.setFont(font)
        self.txtKonum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtKonum.setObjectName("txtKonum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 380, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 380, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(490, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart.setObjectName("btnStart")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 160, 611, 121))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab.setMouseTracking(False)
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_2.setObjectName("tab_2")
        self.txtKonum_2 = QtWidgets.QLineEdit(self.tab_2)
        self.txtKonum_2.setGeometry(QtCore.QRect(10, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtKonum_2.setFont(font)
        self.txtKonum_2.setObjectName("txtKonum_2")
        self.btnKonumSec_2 = QtWidgets.QPushButton(self.tab_2)
        self.btnKonumSec_2.setGeometry(QtCore.QRect(420, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKonumSec_2.setFont(font)
        self.btnKonumSec_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKonumSec_2.setObjectName("btnKonumSec_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 300, 191, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lbl1 = QtWidgets.QLabel(self.groupBox)
        self.lbl1.setGeometry(QtCore.QRect(30, 30, 16, 21))
        self.lbl1.setObjectName("lbl1")
        self.lbl1_2 = QtWidgets.QLabel(self.groupBox)
        self.lbl1_2.setGeometry(QtCore.QRect(70, 30, 16, 21))
        self.lbl1_2.setObjectName("lbl1_2")
        self.lbl1_3 = QtWidgets.QLabel(self.groupBox)
        self.lbl1_3.setGeometry(QtCore.QRect(110, 30, 16, 21))
        self.lbl1_3.setObjectName("lbl1_3")
        self.lbl1_4 = QtWidgets.QLabel(self.groupBox)
        self.lbl1_4.setGeometry(QtCore.QRect(150, 30, 16, 21))
        self.lbl1_4.setObjectName("lbl1_4")
        self.btnStart_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart_2.setGeometry(QtCore.QRect(370, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnStart_2.setFont(font)
        self.btnStart_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart_2.setObjectName("btnStart_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YeDe-K"))
        self.btnKonumSec.setText(_translate("MainWindow", "Konum seçin"))
        self.label.setText(_translate("MainWindow", "Kaydedilecek  Dosya-Klasor"))
        self.label_3.setText(_translate("MainWindow", "Kayıt tekrarı Suresi"))
        self.comboBox.setItemText(0, _translate("MainWindow", "5 saniye"))
        self.comboBox.setItemText(1, _translate("MainWindow", "5 dakika"))
        self.comboBox.setItemText(2, _translate("MainWindow", "30 dakika"))
        self.comboBox.setItemText(3, _translate("MainWindow", "1 saat"))
        self.comboBox.setItemText(4, _translate("MainWindow", "4 saat"))
        self.comboBox.setItemText(5, _translate("MainWindow", "12 saat"))
        self.comboBox.setItemText(6, _translate("MainWindow", "1 gün"))
        self.btnStart.setText(_translate("MainWindow", "Başlat"))
        self.label_4.setText(_translate("MainWindow", "/home/yusuf/yedeklemeKlasoru"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Standart"))
        self.btnKonumSec_2.setText(_translate("MainWindow", "Konum seçin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Custom"))
        self.label_2.setText(_translate("MainWindow", "Kayıt yapılacak klasor"))
        self.lbl1.setText(_translate("MainWindow", "O"))
        self.lbl1_2.setText(_translate("MainWindow", "O"))
        self.lbl1_3.setText(_translate("MainWindow", "O"))
        self.lbl1_4.setText(_translate("MainWindow", "O"))
        self.btnStart_2.setText(_translate("MainWindow", "Durdur"))
