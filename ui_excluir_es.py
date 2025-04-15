# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_excluir_es.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Excluir_es(object):
    def setupUi(self, Excluir_es):
        if not Excluir_es.objectName():
            Excluir_es.setObjectName(u"Excluir_es")
        Excluir_es.resize(867, 585)
        Excluir_es.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.horizontalLayout = QHBoxLayout(Excluir_es)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Excluir_es)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.widget_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 165))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line_3 = QFrame(self.frame_8)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)


        self.verticalLayout.addWidget(self.frame_8)

        self.bnt_voltarx = QPushButton(self.frame)
        self.bnt_voltarx.setObjectName(u"bnt_voltarx")
        self.bnt_voltarx.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_voltarx.setStyleSheet(u"QPushButton{\n"
"padding: 5px 25px;\n"
"font-size: 24px;\n"
"text-align: center;\n"
"color: #fff;\n"
"background-color: #4CAF50;\n"
"border-radius: 15px;\n"
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
        icon.addFile(u"D:/Users/vinnylima/Desktop/Projeto_gerenciador/dist/Icons/Setapratras-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_voltarx.setIcon(icon)
        self.bnt_voltarx.setIconSize(QSize(25, 15))

        self.verticalLayout.addWidget(self.bnt_voltarx)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 77))

        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.frame)

        self.line_2 = QFrame(Excluir_es)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.widget = QWidget(Excluir_es)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 80, 121);\n"
"font-size:20px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_2)

        self.txt_excluir = QLineEdit(self.widget)
        self.txt_excluir.setObjectName(u"txt_excluir")
        self.txt_excluir.setMaximumSize(QSize(656566, 16777215))
        self.txt_excluir.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.txt_excluir)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.bnt_excluirx = QPushButton(self.widget)
        self.bnt_excluirx.setObjectName(u"bnt_excluirx")
        self.bnt_excluirx.setCursor(QCursor(Qt.PointingHandCursor))
        self.bnt_excluirx.setStyleSheet(u"QPushButton{\n"
"padding: 5px 25px;\n"
"font-size: 24px;\n"
"text-align: center;\n"
"color: #fff;\n"
"background-color: #4CAF50;\n"
"border-radius: 15px;\n"
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
        icon1.addFile(u"D:/Users/vinnylima/Desktop/Projeto_gerenciador/dist/Icons/deleteicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_excluirx.setIcon(icon1)
        self.bnt_excluirx.setIconSize(QSize(40, 25))

        self.verticalLayout_2.addWidget(self.bnt_excluirx)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Excluir_es)

        QMetaObject.connectSlotsByName(Excluir_es)
    # setupUi

    def retranslateUi(self, Excluir_es):
        Excluir_es.setWindowTitle(QCoreApplication.translate("Excluir_es", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Excluir_es", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Excluir</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">dados</span></p></body></html>", None))
        self.bnt_voltarx.setText(QCoreApplication.translate("Excluir_es", u"Voltar", None))
        self.label_2.setText(QCoreApplication.translate("Excluir_es", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Insira o ID da pe\u00e7a que ser\u00e1 excluida:</span></p></body></html>", None))
        self.bnt_excluirx.setText(QCoreApplication.translate("Excluir_es", u"Excluir", None))
    # retranslateUi

