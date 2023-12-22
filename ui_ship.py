# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ship_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ShopWindow(object):
    def setupUi(self, ShopWindow):
        if not ShopWindow.objectName():
            ShopWindow.setObjectName(u"ShopWindow")
        ShopWindow.resize(280, 409)
        ShopWindow.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.centralwidget = QWidget(ShopWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.groupBox_4.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.materialCB = QComboBox(self.groupBox_4)
        self.materialCB.setObjectName(u"materialCB")
        self.materialCB.setEditable(True)

        self.verticalLayout_2.addWidget(self.materialCB)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
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

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.shopE = QLineEdit(self.groupBox_3)
        self.shopE.setObjectName(u"shopE")

        self.horizontalLayout_5.addWidget(self.shopE)

        self.addShopB = QPushButton(self.groupBox_3)
        self.addShopB.setObjectName(u"addShopB")

        self.horizontalLayout_5.addWidget(self.addShopB)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_3)

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


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.priceE = QLineEdit(self.centralwidget)
        self.priceE.setObjectName(u"priceE")
        sizePolicy.setHeightForWidth(self.priceE.sizePolicy().hasHeightForWidth())
        self.priceE.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.priceE)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.batchE = QLineEdit(self.centralwidget)
        self.batchE.setObjectName(u"batchE")
        sizePolicy.setHeightForWidth(self.batchE.sizePolicy().hasHeightForWidth())
        self.batchE.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.batchE)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.shipB = QPushButton(self.centralwidget)
        self.shipB.setObjectName(u"shipB")

        self.verticalLayout_3.addWidget(self.shipB)

        ShopWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ShopWindow)
        self.statusbar.setObjectName(u"statusbar")
        ShopWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShopWindow)

        QMetaObject.connectSlotsByName(ShopWindow)
    # setupUi

    def retranslateUi(self, ShopWindow):
        ShopWindow.setWindowTitle(QCoreApplication.translate("ShopWindow", u"\u041e\u0442\u0433\u0440\u0443\u0437\u043a\u0430 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ShopWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ShopWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0430\u0433\u0430\u0437\u0438\u043d", None))
        self.addShopB.setText(QCoreApplication.translate("ShopWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("ShopWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_2.setText(QCoreApplication.translate("ShopWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u0432\u0441\u0435", None))
        self.label_3.setText(QCoreApplication.translate("ShopWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f", None))
        self.shipB.setText(QCoreApplication.translate("ShopWindow", u"\u041e\u0442\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
    # retranslateUi

