# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(498, 751)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 255, 0);")
        self.centralwidget = QWidget(MainWindow)
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
        self.stockT = QTableWidget(self.groupBox_3)
        if (self.stockT.columnCount() < 4):
            self.stockT.setColumnCount(4)
        if (self.stockT.rowCount() < 1):
            self.stockT.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.stockT.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stockT.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.stockT.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.stockT.setItem(0, 3, __qtablewidgetitem3)
        self.stockT.setObjectName(u"stockT")
        self.stockT.setAlternatingRowColors(False)
        self.stockT.setSelectionMode(QAbstractItemView.SingleSelection)
        self.stockT.setGridStyle(Qt.DashLine)
        self.stockT.setRowCount(1)
        self.stockT.setColumnCount(4)
        self.stockT.horizontalHeader().setVisible(False)
        self.stockT.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.stockT)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shipB = QPushButton(self.groupBox_3)
        self.shipB.setObjectName(u"shipB")

        self.horizontalLayout.addWidget(self.shipB)

        self.returnB = QPushButton(self.groupBox_3)
        self.returnB.setObjectName(u"returnB")

        self.horizontalLayout.addWidget(self.returnB)

        self.deliveryB = QPushButton(self.groupBox_3)
        self.deliveryB.setObjectName(u"deliveryB")

        self.horizontalLayout.addWidget(self.deliveryB)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.batchBox = QGroupBox(self.groupBox_3)
        self.batchBox.setObjectName(u"batchBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batchBox.sizePolicy().hasHeightForWidth())
        self.batchBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.batchBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.batchBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deliveryBatchCB = QComboBox(self.batchBox)
        self.deliveryBatchCB.setObjectName(u"deliveryBatchCB")

        self.horizontalLayout_2.addWidget(self.deliveryBatchCB)

        self.deliveryDocB = QPushButton(self.batchBox)
        self.deliveryDocB.setObjectName(u"deliveryDocB")

        self.horizontalLayout_2.addWidget(self.deliveryDocB)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.batchBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.shipBatchCB = QComboBox(self.batchBox)
        self.shipBatchCB.setObjectName(u"shipBatchCB")

        self.horizontalLayout_3.addWidget(self.shipBatchCB)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.shipDocB = QPushButton(self.batchBox)
        self.shipDocB.setObjectName(u"shipDocB")

        self.verticalLayout_3.addWidget(self.shipDocB)

        self.returnDocB = QPushButton(self.batchBox)
        self.returnDocB.setObjectName(u"returnDocB")

        self.verticalLayout_3.addWidget(self.returnDocB)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.batchBox)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \"\u0421\u043a\u043b\u0430\u0434\"", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0441\u043a\u043b\u0430\u0434\u0430", None))

        __sortingEnabled = self.stockT.isSortingEnabled()
        self.stockT.setSortingEnabled(False)
        ___qtablewidgetitem = self.stockT.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem1 = self.stockT.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None));
        ___qtablewidgetitem2 = self.stockT.item(0, 2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem3 = self.stockT.item(0, 3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0438", None));
        self.stockT.setSortingEnabled(__sortingEnabled)

        self.shipB.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.returnB.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0432\u043e\u0437\u0432\u0440\u0430\u0442", None))
        self.deliveryB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0443", None))
        self.batchBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u044b\u0435 \u043d\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.deliveryDocB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043d\u0430 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u044b\u0435 \u043d\u0430 \u043e\u0442\u0433\u0440\u0443\u0437\u043a\u0438 \u0438 \u0432\u043e\u0437\u0432\u0440\u0430\u0442\u044b", None))
        self.shipDocB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043d\u0430 \u043e\u0442\u0433\u0440\u0443\u0437\u043a\u0443", None))
        self.returnDocB.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043d\u0430 \u0432\u043e\u0437\u0432\u0440\u0430\u0442", None))
    # retranslateUi

