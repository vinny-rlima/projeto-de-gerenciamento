# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_cadastro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CADASTRO(object):
    def setupUi(self, CADASTRO):
        if not CADASTRO.objectName():
            CADASTRO.setObjectName(u"CADASTRO")
        CADASTRO.resize(1128, 521)
        CADASTRO.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.verticalLayout = QVBoxLayout(CADASTRO)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(CADASTRO)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.label_13)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_codigo = QLineEdit(self.frame_4)
        self.txt_codigo.setObjectName(u"txt_codigo")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_codigo.setFont(font)
        self.txt_codigo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_codigo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_codigo)

        self.txt_hostname = QLineEdit(self.frame_4)
        self.txt_hostname.setObjectName(u"txt_hostname")
        self.txt_hostname.setFont(font)
        self.txt_hostname.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_hostname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_hostname)

        self.txt_usuario_2 = QLineEdit(self.frame_4)
        self.txt_usuario_2.setObjectName(u"txt_usuario_2")
        self.txt_usuario_2.setFont(font)
        self.txt_usuario_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_usuario_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_usuario_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_ip = QLineEdit(self.frame_4)
        self.txt_ip.setObjectName(u"txt_ip")
        self.txt_ip.setFont(font)
        self.txt_ip.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_ip.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.txt_ip)

        self.txt_mac = QLineEdit(self.frame_4)
        self.txt_mac.setObjectName(u"txt_mac")
        self.txt_mac.setFont(font)
        self.txt_mac.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_mac.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.txt_mac)

        self.txt_placa_mae = QLineEdit(self.frame_4)
        self.txt_placa_mae.setObjectName(u"txt_placa_mae")
        self.txt_placa_mae.setFont(font)
        self.txt_placa_mae.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_placa_mae.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.txt_placa_mae)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txt_processador = QLineEdit(self.frame_4)
        self.txt_processador.setObjectName(u"txt_processador")
        self.txt_processador.setFont(font)
        self.txt_processador.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_processador.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.txt_processador)

        self.cb_ram = QComboBox(self.frame_4)
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.addItem("")
        self.cb_ram.setObjectName(u"cb_ram")
        self.cb_ram.setMinimumSize(QSize(250, 0))
        self.cb_ram.setFont(font)
        self.cb_ram.setLayoutDirection(Qt.LeftToRight)
        self.cb_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.cb_ram)

        self.txt_placa_video = QLineEdit(self.frame_4)
        self.txt_placa_video.setObjectName(u"txt_placa_video")
        self.txt_placa_video.setFont(font)
        self.txt_placa_video.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_placa_video.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.txt_placa_video)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.txt_fonte = QLineEdit(self.frame_4)
        self.txt_fonte.setObjectName(u"txt_fonte")
        self.txt_fonte.setFont(font)
        self.txt_fonte.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_fonte.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.txt_fonte)

        self.txt_ssd = QLineEdit(self.frame_4)
        self.txt_ssd.setObjectName(u"txt_ssd")
        self.txt_ssd.setFont(font)
        self.txt_ssd.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_ssd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.txt_ssd)

        self.cb_rede = QComboBox(self.frame_4)
        self.cb_rede.addItem("")
        self.cb_rede.addItem("")
        self.cb_rede.addItem("")
        self.cb_rede.setObjectName(u"cb_rede")
        self.cb_rede.setMinimumSize(QSize(120, 0))
        self.cb_rede.setFont(font)
        self.cb_rede.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.cb_rede)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.txt_win = QLineEdit(self.frame_4)
        self.txt_win.setObjectName(u"txt_win")
        self.txt_win.setFont(font)
        self.txt_win.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_win.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_win)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_monit = QLineEdit(self.frame_4)
        self.txt_monit.setObjectName(u"txt_monit")
        self.txt_monit.setFont(font)
        self.txt_monit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_monit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_monit)

        self.txt_monit2 = QLineEdit(self.frame_4)
        self.txt_monit2.setObjectName(u"txt_monit2")
        self.txt_monit2.setFont(font)
        self.txt_monit2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_monit2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_monit2)

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

        self.line_5 = QFrame(self.frame_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(CADASTRO)

        QMetaObject.connectSlotsByName(CADASTRO)
    # setupUi

    def retranslateUi(self, CADASTRO):
        CADASTRO.setWindowTitle(QCoreApplication.translate("CADASTRO", u"Dialog", None))
        self.label_13.setText(QCoreApplication.translate("CADASTRO", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">CADASTRO DE MAQUINAS</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_erro.setText(QCoreApplication.translate("CADASTRO", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">TODOS OS CAMPOS S\u00c3O OBRIGATORIOS*</span></p></body></html>", None))
        self.label_15.setText("")
        self.txt_codigo.setText("")
        self.txt_codigo.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"CODIGO", None))
        self.txt_hostname.setText("")
        self.txt_hostname.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"HOSTMANE", None))
        self.txt_usuario_2.setText("")
        self.txt_usuario_2.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"USUARIO", None))
        self.txt_ip.setText("")
        self.txt_ip.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"IP", None))
        self.txt_mac.setText("")
        self.txt_mac.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"ENDERE\u00c7O MAC", None))
        self.txt_placa_mae.setText("")
        self.txt_placa_mae.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"PLACA M\u00c3E", None))
        self.txt_processador.setText("")
        self.txt_processador.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"PROCESSADOR", None))
        self.cb_ram.setItemText(0, QCoreApplication.translate("CADASTRO", u"MEMORIA RAM", None))
        self.cb_ram.setItemText(1, QCoreApplication.translate("CADASTRO", u"4 GB", None))
        self.cb_ram.setItemText(2, QCoreApplication.translate("CADASTRO", u"8 GB", None))
        self.cb_ram.setItemText(3, QCoreApplication.translate("CADASTRO", u"12 GB", None))
        self.cb_ram.setItemText(4, QCoreApplication.translate("CADASTRO", u"16 GB", None))
        self.cb_ram.setItemText(5, QCoreApplication.translate("CADASTRO", u"24 GB", None))
        self.cb_ram.setItemText(6, QCoreApplication.translate("CADASTRO", u"32 GB", None))
        self.cb_ram.setItemText(7, QCoreApplication.translate("CADASTRO", u"64 GB", None))

        self.cb_ram.setCurrentText(QCoreApplication.translate("CADASTRO", u"MEMORIA RAM", None))
        self.txt_placa_video.setText("")
        self.txt_placa_video.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"PLACA DE VIDEO", None))
        self.txt_fonte.setText("")
        self.txt_fonte.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"FONTE", None))
        self.txt_ssd.setText("")
        self.txt_ssd.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"SSD/HD", None))
        self.cb_rede.setItemText(0, QCoreApplication.translate("CADASTRO", u"PLACA DE REDE", None))
        self.cb_rede.setItemText(1, QCoreApplication.translate("CADASTRO", u"SIM", None))
        self.cb_rede.setItemText(2, QCoreApplication.translate("CADASTRO", u"N\u00c3O", None))

        self.txt_win.setText("")
        self.txt_win.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"LICEN\u00c7A WIN", None))
        self.txt_monit.setText("")
        self.txt_monit.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"CODIGO MONITOR", None))
        self.txt_monit2.setText("")
        self.txt_monit2.setPlaceholderText(QCoreApplication.translate("CADASTRO", u"CODIGO MONITOR AUXILIAR", None))
        self.btn_cadastrar_pc.setText(QCoreApplication.translate("CADASTRO", u"SALVAR", None))
        self.bnt_voltar_cad.setText(QCoreApplication.translate("CADASTRO", u"VOLTAR", None))
    # retranslateUi

