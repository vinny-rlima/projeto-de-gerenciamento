# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cadastro_ton.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CADASTRO_ton(object):
    def setupUi(self, CADASTRO_ton):
        if not CADASTRO_ton.objectName():
            CADASTRO_ton.setObjectName(u"CADASTRO_ton")
        CADASTRO_ton.resize(956, 325)
        CADASTRO_ton.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.verticalLayout = QVBoxLayout(CADASTRO_ton)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(CADASTRO_ton)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_15.addWidget(self.label_14)

        self.label_erro = QLabel(self.frame_4)
        self.label_erro.setObjectName(u"label_erro")
        self.label_erro.setMaximumSize(QSize(400, 50))

        self.horizontalLayout_15.addWidget(self.label_erro)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_15.addWidget(self.label_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_win = QLineEdit(self.frame_4)
        self.txt_win.setObjectName(u"txt_win")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_win.setFont(font)
        self.txt_win.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_win.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_win)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_hostname = QLineEdit(self.frame_4)
        self.txt_hostname.setObjectName(u"txt_hostname")
        self.txt_hostname.setMaximumSize(QSize(150, 16777215))
        self.txt_hostname.setFont(font)
        self.txt_hostname.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_hostname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_hostname)

        self.btn_cadastrar_pc = QPushButton(self.frame_4)
        self.btn_cadastrar_pc.setObjectName(u"btn_cadastrar_pc")
        self.btn_cadastrar_pc.setMinimumSize(QSize(400, 30))
        font1 = QFont()
        self.btn_cadastrar_pc.setFont(font1)
        self.btn_cadastrar_pc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_pc.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"img/Icons/InserirIcon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar_pc.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_cadastrar_pc)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.line_5 = QFrame(self.frame_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bnt_voltar_cad = QPushButton(self.frame_4)
        self.bnt_voltar_cad.setObjectName(u"bnt_voltar_cad")
        self.bnt_voltar_cad.setMinimumSize(QSize(200, 30))
        self.bnt_voltar_cad.setFont(font1)
        self.bnt_voltar_cad.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_voltar_cad.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u"img/Icons/Setapratras-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_voltar_cad.setIcon(icon1)

        self.horizontalLayout.addWidget(self.bnt_voltar_cad)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(CADASTRO_ton)

        QMetaObject.connectSlotsByName(CADASTRO_ton)
    # setupUi

    def retranslateUi(self, CADASTRO_ton):
        CADASTRO_ton.setWindowTitle(QCoreApplication.translate("CADASTRO_ton", u"Dialog", None))
        self.label_13.setText(QCoreApplication.translate("CADASTRO_ton", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">CADASTRO DE TONNERS</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_erro.setText(QCoreApplication.translate("CADASTRO_ton", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">TODOS OS CAMPOS S\u00c3O OBRIGATORIOS*</span></p></body></html>", None))
        self.label_15.setText("")
        self.txt_win.setText("")
        self.txt_win.setPlaceholderText(QCoreApplication.translate("CADASTRO_ton", u"TONNER", None))
        self.txt_hostname.setText("")
        self.txt_hostname.setPlaceholderText(QCoreApplication.translate("CADASTRO_ton", u"QUANTIDADE", None))
        self.btn_cadastrar_pc.setText(QCoreApplication.translate("CADASTRO_ton", u"SALVAR", None))
        self.bnt_voltar_cad.setText(QCoreApplication.translate("CADASTRO_ton", u"VOLTAR", None))
    # retranslateUi

