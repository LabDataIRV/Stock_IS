# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'return_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ReturnWindow(object):
    def setupUi(self, ReturnWindow):
        if not ReturnWindow.objectName():
            ReturnWindow.setObjectName(u"ReturnWindow")
        ReturnWindow.resize(460, 412)
        ReturnWindow.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.centralwidget = QWidget(ReturnWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shopsCB = QComboBox(self.groupBox_3)
        self.shopsCB.setObjectName(u"shopsCB")
        self.shopsCB.setEditable(True)

        self.verticalLayout.addWidget(self.shopsCB)

        self.batchT = QTableWidget(self.groupBox_3)
        if (self.batchT.columnCount() < 2):
            self.batchT.setColumnCount(2)
        if (self.batchT.rowCount() < 1):
            self.batchT.setRowCount(1)
        self.batchT.setObjectName(u"batchT")
        self.batchT.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.batchT.setAlternatingRowColors(False)
        self.batchT.setSelectionMode(QAbstractItemView.SingleSelection)
        self.batchT.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.batchT.setGridStyle(Qt.DashLine)
        self.batchT.setRowCount(1)
        self.batchT.setColumnCount(2)
        self.batchT.horizontalHeader().setVisible(False)
        self.batchT.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.batchT)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.quantityE = QLineEdit(self.centralwidget)
        self.quantityE.setObjectName(u"quantityE")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantityE.sizePolicy().hasHeightForWidth())
        self.quantityE.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.quantityE)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.returnB = QPushButton(self.centralwidget)
        self.returnB.setObjectName(u"returnB")

        self.verticalLayout_2.addWidget(self.returnB)

        ReturnWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ReturnWindow)
        self.statusbar.setObjectName(u"statusbar")
        ReturnWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ReturnWindow)

        QMetaObject.connectSlotsByName(ReturnWindow)
    # setupUi

    def retranslateUi(self, ReturnWindow):
        ReturnWindow.setWindowTitle(QCoreApplication.translate("ReturnWindow", u"\u0412\u043e\u0437\u0432\u0440\u0430\u0442 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ReturnWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.label.setText(QCoreApplication.translate("ReturnWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.returnB.setText(QCoreApplication.translate("ReturnWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
    # retranslateUi

