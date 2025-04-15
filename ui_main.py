# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
        MainWindow.resize(1116, 548)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        icon = QIcon()
        icon.addFile(u"img/Icons/Icone-casa-Png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_table = QPushButton(self.frame)
        self.btn_table.setObjectName(u"btn_table")
        self.btn_table.setMinimumSize(QSize(0, 35))
        self.btn_table.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_table.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        icon1 = QIcon()
        icon1.addFile(u"img/Icons/computer-png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_table.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_table)

        self.btn_outo = QPushButton(self.frame)
        self.btn_outo.setObjectName(u"btn_outo")
        self.btn_outo.setMinimumSize(QSize(0, 35))
        self.btn_outo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_outo.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        icon2 = QIcon()
        icon2.addFile(u"img/Icons/Icone-ram-Png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_outo.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_outo)

        self.btn_outo_2 = QPushButton(self.frame)
        self.btn_outo_2.setObjectName(u"btn_outo_2")
        self.btn_outo_2.setMinimumSize(QSize(0, 35))
        self.btn_outo_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_outo_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        icon3 = QIcon()
        icon3.addFile(u"img/Icons/Icone-impressora-Png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_outo_2.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btn_outo_2)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 1px;\n"
"	font-size: 16px;\n"
"	background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        icon4 = QIcon()
        icon4.addFile(u"img/Icons/Icone-informacao-Png-1-1024x1024.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sobre.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_sobre)


        self.verticalLayout.addWidget(self.frame)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_2 = QVBoxLayout(self.pg_table)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tb_base = QTabWidget(self.pg_table)
        self.tb_base.setObjectName(u"tb_base")
        self.QW_COMPUTADORES = QWidget()
        self.QW_COMPUTADORES.setObjectName(u"QW_COMPUTADORES")
        self.verticalLayout_7 = QVBoxLayout(self.QW_COMPUTADORES)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.QW_COMPUTADORES)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_12.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_chart = QPushButton(self.frame_3)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setMinimumSize(QSize(0, 25))
        font = QFont()
        self.btn_chart.setFont(font)
        self.btn_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart.setToolTipDuration(1)
        self.btn_chart.setStyleSheet(u"QPushButton{\n"
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
        icon5 = QIcon()
        icon5.addFile(u"img/Icons/126425.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chart.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 25))
        self.btn_excel.setFont(font)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
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
        icon6 = QIcon()
        icon6.addFile(u"img/Icons/icone-excel-vert.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excel.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.btn_excel)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_filtro = QLineEdit(self.frame_3)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 29))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.txt_filtro.setFont(font1)
        self.txt_filtro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_filtro)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)

        self.tab_estoque = QTableView(self.frame_3)
        self.tab_estoque.setObjectName(u"tab_estoque")

        self.verticalLayout_12.addWidget(self.tab_estoque)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.tb_base.addTab(self.QW_COMPUTADORES, "")
        self.QW_ALTERAR = QWidget()
        self.QW_ALTERAR.setObjectName(u"QW_ALTERAR")
        self.verticalLayout_10 = QVBoxLayout(self.QW_ALTERAR)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.name_computadores = QLabel(self.QW_ALTERAR)
        self.name_computadores.setObjectName(u"name_computadores")

        self.verticalLayout_5.addWidget(self.name_computadores)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.table_computadores = QTableWidget(self.QW_ALTERAR)
        if (self.table_computadores.columnCount() < 15):
            self.table_computadores.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_computadores.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.table_computadores.setObjectName(u"table_computadores")

        self.verticalLayout_4.addWidget(self.table_computadores)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.line_2 = QFrame(self.QW_ALTERAR)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.frame_2 = QFrame(self.QW_ALTERAR)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_inserir = QPushButton(self.frame_2)
        self.btn_inserir.setObjectName(u"btn_inserir")
        self.btn_inserir.setMinimumSize(QSize(100, 27))
        self.btn_inserir.setFont(font)
        self.btn_inserir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inserir.setStyleSheet(u"QPushButton{\n"
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
        icon7 = QIcon()
        icon7.addFile(u"img/Icons/InserirIcon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inserir.setIcon(icon7)
        self.btn_inserir.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.btn_inserir)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(100, 27))
        self.btn_alterar.setFont(font)
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
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
        icon8 = QIcon()
        icon8.addFile(u"img/Icons/updateicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon8)

        self.verticalLayout_3.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(100, 27))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
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
        icon9 = QIcon()
        icon9.addFile(u"img/Icons/deleteicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon9)

        self.verticalLayout_3.addWidget(self.btn_excluir)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.tb_base.addTab(self.QW_ALTERAR, "")
        self.QW_MONITORES = QWidget()
        self.QW_MONITORES.setObjectName(u"QW_MONITORES")
        self.verticalLayout_23 = QVBoxLayout(self.QW_MONITORES)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.name_computadores_2 = QLabel(self.QW_MONITORES)
        self.name_computadores_2.setObjectName(u"name_computadores_2")

        self.verticalLayout_20.addWidget(self.name_computadores_2)

        self.table_computadores_2 = QTableWidget(self.QW_MONITORES)
        if (self.table_computadores_2.columnCount() < 4):
            self.table_computadores_2.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_computadores_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_computadores_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_computadores_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_computadores_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.table_computadores_2.setObjectName(u"table_computadores_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_computadores_2.sizePolicy().hasHeightForWidth())
        self.table_computadores_2.setSizePolicy(sizePolicy)
        self.table_computadores_2.setFrameShape(QFrame.Panel)
        self.table_computadores_2.setFrameShadow(QFrame.Raised)
        self.table_computadores_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_computadores_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_computadores_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_computadores_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_computadores_2.setTextElideMode(Qt.ElideLeft)
        self.table_computadores_2.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.verticalLayout_20.addWidget(self.table_computadores_2)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.verticalLayout_19.addLayout(self.verticalLayout_21)


        self.horizontalLayout_15.addLayout(self.verticalLayout_19)

        self.line_3 = QFrame(self.QW_MONITORES)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_3)

        self.frame_6 = QFrame(self.QW_MONITORES)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_inserir_2 = QPushButton(self.frame_6)
        self.btn_inserir_2.setObjectName(u"btn_inserir_2")
        self.btn_inserir_2.setMinimumSize(QSize(100, 27))
        self.btn_inserir_2.setFont(font)
        self.btn_inserir_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inserir_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_inserir_2.setIcon(icon7)
        self.btn_inserir_2.setIconSize(QSize(16, 16))

        self.verticalLayout_22.addWidget(self.btn_inserir_2)

        self.btn_alterar_2 = QPushButton(self.frame_6)
        self.btn_alterar_2.setObjectName(u"btn_alterar_2")
        self.btn_alterar_2.setMinimumSize(QSize(100, 27))
        self.btn_alterar_2.setFont(font)
        self.btn_alterar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_alterar_2.setIcon(icon8)

        self.verticalLayout_22.addWidget(self.btn_alterar_2)

        self.btn_excluir_2 = QPushButton(self.frame_6)
        self.btn_excluir_2.setObjectName(u"btn_excluir_2")
        self.btn_excluir_2.setMinimumSize(QSize(100, 27))
        self.btn_excluir_2.setFont(font)
        self.btn_excluir_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_excluir_2.setIcon(icon9)

        self.verticalLayout_22.addWidget(self.btn_excluir_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.frame_6)


        self.verticalLayout_23.addLayout(self.horizontalLayout_15)

        self.tb_base.addTab(self.QW_MONITORES, "")

        self.verticalLayout_2.addWidget(self.tb_base)

        self.pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_9 = QVBoxLayout(self.pg_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.evoex = QLabel(self.pg_home)
        self.evoex.setObjectName(u"evoex")
        self.evoex.setStyleSheet(u"background-color: rgb(0, 80, 121);")

        self.verticalLayout_9.addWidget(self.evoex)

        self.line_5 = QFrame(self.pg_home)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.btn_pgcadastrar = QPushButton(self.pg_home)
        self.btn_pgcadastrar.setObjectName(u"btn_pgcadastrar")
        self.btn_pgcadastrar.setMinimumSize(QSize(0, 27))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_pgcadastrar.setFont(font2)
        self.btn_pgcadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pgcadastrar.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        self.btn_pgcadastrar.setIcon(icon7)

        self.verticalLayout_9.addWidget(self.btn_pgcadastrar)

        self.pages.addWidget(self.pg_home)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.pg_sobre)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_12.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_12)

        self.label_2 = QLabel(self.pg_sobre)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.pages.addWidget(self.pg_sobre)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_3 = QLabel(self.pg_cadastro)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, -1, -1)
        self.label_4 = QLabel(self.pg_cadastro)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, -1, -1)
        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_usuario)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txt_senha2 = QLineEdit(self.pg_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha2)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color:rgba(211, 239, 251, 1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155, 0.1);\n"
"font-family:Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setFont(font2)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.line_6 = QFrame(self.pg_cadastro)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
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
        self.btn_cadastrar.setIcon(icon7)

        self.horizontalLayout_11.addWidget(self.btn_cadastrar)

        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_tonners = QWidget()
        self.pg_tonners.setObjectName(u"pg_tonners")
        self.verticalLayout_18 = QVBoxLayout(self.pg_tonners)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_2 = QWidget(self.pg_tonners)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_16 = QVBoxLayout(self.widget_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_17.addWidget(self.label_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_inserir_inserir = QPushButton(self.frame_5)
        self.btn_inserir_inserir.setObjectName(u"btn_inserir_inserir")
        self.btn_inserir_inserir.setMinimumSize(QSize(0, 25))
        self.btn_inserir_inserir.setFont(font)
        self.btn_inserir_inserir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inserir_inserir.setToolTipDuration(1)
        self.btn_inserir_inserir.setStyleSheet(u"QPushButton{\n"
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
        self.btn_inserir_inserir.setIcon(icon7)

        self.horizontalLayout_13.addWidget(self.btn_inserir_inserir)

        self.btn_alterar_tonners = QPushButton(self.frame_5)
        self.btn_alterar_tonners.setObjectName(u"btn_alterar_tonners")
        self.btn_alterar_tonners.setMinimumSize(QSize(0, 25))
        self.btn_alterar_tonners.setFont(font)
        self.btn_alterar_tonners.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_tonners.setStyleSheet(u"QPushButton{\n"
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
        self.btn_alterar_tonners.setIcon(icon8)

        self.horizontalLayout_13.addWidget(self.btn_alterar_tonners)


        self.verticalLayout_17.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.txt_filtro_tonners = QLineEdit(self.frame_5)
        self.txt_filtro_tonners.setObjectName(u"txt_filtro_tonners")
        self.txt_filtro_tonners.setMinimumSize(QSize(0, 29))
        self.txt_filtro_tonners.setFont(font1)
        self.txt_filtro_tonners.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filtro_tonners.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.txt_filtro_tonners)


        self.verticalLayout_17.addLayout(self.horizontalLayout_14)

        self.tab_tonners = QTableView(self.frame_5)
        self.tab_tonners.setObjectName(u"tab_tonners")

        self.verticalLayout_17.addWidget(self.tab_tonners)


        self.verticalLayout_16.addWidget(self.frame_5)

        self.btn_excluir_excluir = QPushButton(self.widget_2)
        self.btn_excluir_excluir.setObjectName(u"btn_excluir_excluir")
        self.btn_excluir_excluir.setMinimumSize(QSize(0, 25))
        self.btn_excluir_excluir.setFont(font)
        self.btn_excluir_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_excluir.setStyleSheet(u"QPushButton{\n"
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
        self.btn_excluir_excluir.setIcon(icon9)

        self.verticalLayout_16.addWidget(self.btn_excluir_excluir)


        self.verticalLayout_18.addWidget(self.widget_2)

        self.pages.addWidget(self.pg_tonners)
        self.pg_pecas = QWidget()
        self.pg_pecas.setObjectName(u"pg_pecas")
        self.verticalLayout_13 = QVBoxLayout(self.pg_pecas)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget = QWidget(self.pg_pecas)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_14 = QVBoxLayout(self.widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_15.addWidget(self.label_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_inserir_pecas = QPushButton(self.frame_4)
        self.btn_inserir_pecas.setObjectName(u"btn_inserir_pecas")
        self.btn_inserir_pecas.setMinimumSize(QSize(0, 25))
        self.btn_inserir_pecas.setFont(font)
        self.btn_inserir_pecas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inserir_pecas.setToolTipDuration(1)
        self.btn_inserir_pecas.setStyleSheet(u"QPushButton{\n"
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
        self.btn_inserir_pecas.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.btn_inserir_pecas)

        self.btn_alterar_pecas = QPushButton(self.frame_4)
        self.btn_alterar_pecas.setObjectName(u"btn_alterar_pecas")
        self.btn_alterar_pecas.setMinimumSize(QSize(0, 25))
        self.btn_alterar_pecas.setFont(font)
        self.btn_alterar_pecas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_pecas.setStyleSheet(u"QPushButton{\n"
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
        self.btn_alterar_pecas.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.btn_alterar_pecas)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txt_filtro_pecas = QLineEdit(self.frame_4)
        self.txt_filtro_pecas.setObjectName(u"txt_filtro_pecas")
        self.txt_filtro_pecas.setMinimumSize(QSize(0, 29))
        self.txt_filtro_pecas.setFont(font1)
        self.txt_filtro_pecas.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filtro_pecas.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.txt_filtro_pecas)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)

        self.tab_pecas = QTableView(self.frame_4)
        self.tab_pecas.setObjectName(u"tab_pecas")

        self.verticalLayout_15.addWidget(self.tab_pecas)


        self.verticalLayout_14.addWidget(self.frame_4)

        self.btn_excluir_pecas_2 = QPushButton(self.widget)
        self.btn_excluir_pecas_2.setObjectName(u"btn_excluir_pecas_2")
        self.btn_excluir_pecas_2.setMinimumSize(QSize(0, 25))
        self.btn_excluir_pecas_2.setFont(font)
        self.btn_excluir_pecas_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_pecas_2.setStyleSheet(u"QPushButton{\n"
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
        self.btn_excluir_pecas_2.setIcon(icon9)

        self.verticalLayout_14.addWidget(self.btn_excluir_pecas_2)


        self.verticalLayout_13.addWidget(self.widget)

        self.pages.addWidget(self.pg_pecas)

        self.verticalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.tb_base.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_table.setText(QCoreApplication.translate("MainWindow", u"COMPUTADORES", None))
        self.btn_outo.setText(QCoreApplication.translate("MainWindow", u"PE\u00c7AS EM ESTOQUE", None))
        self.btn_outo_2.setText(QCoreApplication.translate("MainWindow", u"TONNERS", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">COMPUTADORES</span></p></body></html>", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setText("")
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.QW_COMPUTADORES), QCoreApplication.translate("MainWindow", u"COMPUTADORES", None))
        self.name_computadores.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">COMPUTADORES</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_computadores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem1 = self.table_computadores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"HOSTNAME", None));
        ___qtablewidgetitem2 = self.table_computadores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None));
        ___qtablewidgetitem3 = self.table_computadores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem4 = self.table_computadores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"MAC", None));
        ___qtablewidgetitem5 = self.table_computadores.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PLACA M\u00c3E", None));
        ___qtablewidgetitem6 = self.table_computadores.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"PROCESSADOR", None));
        ___qtablewidgetitem7 = self.table_computadores.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"MEMORIA RAM", None));
        ___qtablewidgetitem8 = self.table_computadores.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PLACA DE VIDEO", None));
        ___qtablewidgetitem9 = self.table_computadores.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"FONTE", None));
        ___qtablewidgetitem10 = self.table_computadores.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"HD/SSD", None));
        ___qtablewidgetitem11 = self.table_computadores.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"PLACA DE REDE", None));
        ___qtablewidgetitem12 = self.table_computadores.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"MONITOR", None));
        ___qtablewidgetitem13 = self.table_computadores.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MONITOR AUX", None));
        ___qtablewidgetitem14 = self.table_computadores.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"WIN", None));
        self.btn_inserir.setText(QCoreApplication.translate("MainWindow", u"Inserir", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.QW_ALTERAR), QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.name_computadores_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">COMPUTADORES</span></p></body></html>", None))
        ___qtablewidgetitem15 = self.table_computadores_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"CODIGO", None));
        ___qtablewidgetitem16 = self.table_computadores_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"MARCA", None));
        ___qtablewidgetitem17 = self.table_computadores_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"MODELO", None));
        ___qtablewidgetitem18 = self.table_computadores_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"TAMANHO", None));
        self.btn_inserir_2.setText(QCoreApplication.translate("MainWindow", u"Inserir", None))
        self.btn_alterar_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.QW_MONITORES), QCoreApplication.translate("MainWindow", u"MONITORES", None))
        self.evoex.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">EVOEX</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Sistema de gerenciamento</span></p><p align=\"center\"><img src=\"img/logoB.png\"/></p></body></html>", None))
        self.btn_pgcadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USUARIO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">SOBRE</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SISTEMA PARA CONTROLE</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DE ESTOQUE DE TI</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"> E MANUTE\u00c7\u00c3O</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">DE PCS</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TELA DE CADASTRO</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"img/user.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NOME:    </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"> USU\u00c1RIO:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"> SENHA:    </span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\"> SENHA:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PERFIL</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"ADMINISTRADOR", None))

        self.label_9.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">ESTOQUE DE TONNERS</span></p></body></html>", None))
        self.btn_inserir_inserir.setText(QCoreApplication.translate("MainWindow", u"INSERIR", None))
        self.btn_alterar_tonners.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.txt_filtro_tonners.setText("")
        self.txt_filtro_tonners.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.btn_excluir_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">ESTOQUE DE PE\u00c7AS</span></p></body></html>", None))
        self.btn_inserir_pecas.setText(QCoreApplication.translate("MainWindow", u"INSERIR", None))
        self.btn_alterar_pecas.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.txt_filtro_pecas.setText("")
        self.txt_filtro_pecas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.btn_excluir_pecas_2.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
    # retranslateUi

