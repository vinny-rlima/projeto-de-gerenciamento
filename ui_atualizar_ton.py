# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_atualizar_ton.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Atualizar_ton(object):
    def setupUi(self, Atualizar_ton):
        if not Atualizar_ton.objectName():
            Atualizar_ton.setObjectName(u"Atualizar_ton")
        Atualizar_ton.resize(614, 429)
        Atualizar_ton.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.horizontalLayout_2 = QHBoxLayout(Atualizar_ton)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(Atualizar_ton)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.tab_atualizar = QTableWidget(self.widget)
        if (self.tab_atualizar.columnCount() < 3):
            self.tab_atualizar.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_atualizar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_atualizar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_atualizar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tab_atualizar.setObjectName(u"tab_atualizar")

        self.verticalLayout_2.addWidget(self.tab_atualizar)

        self.btn_atualizar_pc = QPushButton(self.widget)
        self.btn_atualizar_pc.setObjectName(u"btn_atualizar_pc")
        self.btn_atualizar_pc.setMinimumSize(QSize(400, 30))
        font = QFont()
        self.btn_atualizar_pc.setFont(font)
        self.btn_atualizar_pc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atualizar_pc.setStyleSheet(u"QPushButton{\n"
"padding: 5px 25px;\n"
"font-size: 16px;\n"
"text-align: center;\n"
"color: #fff;\n"
"background-color: #4CAF50;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"}")
        icon = QIcon()
        icon.addFile(u"D:/Users/vinnylima/Desktop/Projeto de programa/img/Icons/updateicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_atualizar_pc.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_atualizar_pc)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bnt_voltar_atualizar = QPushButton(self.widget)
        self.bnt_voltar_atualizar.setObjectName(u"bnt_voltar_atualizar")
        self.bnt_voltar_atualizar.setMinimumSize(QSize(200, 30))
        self.bnt_voltar_atualizar.setFont(font)
        self.bnt_voltar_atualizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_voltar_atualizar.setStyleSheet(u"QPushButton{\n"
"padding: 5px 25px;\n"
"font-size: 16px;\n"
"text-align: center;\n"
"color: #fff;\n"
"background-color: #4CAF50;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"D:/Users/vinnylima/Desktop/Projeto de programa/img/Icons/Setapratras-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_voltar_atualizar.setIcon(icon1)

        self.horizontalLayout.addWidget(self.bnt_voltar_atualizar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(Atualizar_ton)

        QMetaObject.connectSlotsByName(Atualizar_ton)
    # setupUi

    def retranslateUi(self, Atualizar_ton):
        Atualizar_ton.setWindowTitle(QCoreApplication.translate("Atualizar_ton", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Atualizar_ton", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">ATUALIZAR TONNERS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tab_atualizar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Atualizar_ton", u"ID", None));
        ___qtablewidgetitem1 = self.tab_atualizar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Atualizar_ton", u"TONNER", None));
        ___qtablewidgetitem2 = self.tab_atualizar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Atualizar_ton", u"QUANTIDADE", None));
        self.btn_atualizar_pc.setText(QCoreApplication.translate("Atualizar_ton", u"ATUALIZAR", None))
        self.bnt_voltar_atualizar.setText(QCoreApplication.translate("Atualizar_ton", u"VOLTAR", None))
    # retranslateUi

