from os import access
from PySide2 import QtCore
from PySide2.QtWidgets import(QApplication, QMainWindow, QMessageBox, QWidget, QFileDialog, QTreeWidgetItem, QTableWidgetItem)
from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QIcon
from ui_main import Ui_MainWindow
from ui_login import Ui_Login
from ui_cadastro import Ui_CADASTRO
from ui_excluir import Ui_Excluir
from ui_atualizar import Ui_Atualizar
from ui_atualizar_ton import Ui_Atualizar_ton
from ui_atualizar_es import Ui_Atualizar_es
from ui_cadastro_es import Ui_CADASTRO_es
from ui_cadastro_ton import Ui_CADASTRO_ton
from ui_excluir_ton import Ui_Excluir_ton
from ui_excluir_es import Ui_Excluir_es
import sys
import sqlite3
from database import DataBase
import pandas as pd
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
import re
import matplotlib.pyplot as plt

#*************************Pagina de Login*****************************************

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon('img/icone.png')
        self.setWindowIcon(appIcon)

        self.btn_login.clicked.connect(self.checkLogin)
 
    #**********************Checar se o usuario esta cadastrado*********************************
    def checkLogin(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_user.text().upper(), self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
        else:

            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f' Login ou senha incorreta \n \n Tentativas: {self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas += 1
                
            if self.tentativas == 3:
                self.users.close_connecion()
                sys.exit(0)


    #-****************************Paginas do Sistema*****************************************

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        appIcon = QIcon('img/icone.png')
        self.setWindowIcon(appIcon)

        if user.lower() == "user":
            self.btn_pgcadastrar.setVisible(False)
            self.btn_excluir.setVisible(False)
            self.btn_alterar.setVisible(False)

        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_outo.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_pecas))
        self.btn_outo_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_tonners))
        self.btn_table.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_pgcadastrar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))
        self.btn_inserir.clicked.connect(self.abrir_janela_inserir)
        self.btn_excluir.clicked.connect(self.abrir_janela_excluir)
        self.btn_alterar.clicked.connect(self.abrir_janela_atualizar)
        self.btn_excel.clicked.connect(self.excel_file)

        self.btn_inserir_inserir.clicked.connect(self.abrir_janela_inserir_ton)
        self.btn_excluir_excluir.clicked.connect(self.abrir_janela_excluir_ton)
        self.btn_alterar_tonners.clicked.connect(self.abrir_janela_atualizar_ton)

        self.btn_excluir_pecas_2.clicked.connect(self.abrir_janela_excluir_es)
        self.btn_inserir_pecas.clicked.connect(self.abrir_janela_inserir_es)
        self.btn_alterar_pecas.clicked.connect(self.abrir_janela_atualizar_es)        

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

        self.txt_filtro.textChanged.connect(self.update_filter)

        self.atualiza_tabela()
        self.reset_table()
    
    def abrir_janela_excluir(self):
        self.w = Excluir()
        self.w.show()  

    def abrir_janela_atualizar(self):
        self.w = Atualizar()
        self.w.show() 
        self.close()

    def abrir_janela_inserir(self):
        self.w = Cadastro()
        self.w.show()

    def abrir_janela_excluir(self):
        self.w = Excluir()
        self.w.show()  

    def abrir_janela_excluir_es(self):
        self.w = Excluir_es()
        self.w.show()

    def abrir_janela_excluir_ton(self):
        self.w = Excluir_ton()
        self.w.show()

    def abrir_janela_atualizar(self):
        self.w = Atualizar()
        self.w.show() 
        self.close()

    def abrir_janela_atualizar_es(self):
        self.w = Atualizar_es()
        self.w.show() 
        self.close()

    def abrir_janela_atualizar_ton(self):
        self.w = Atualizar_ton()
        self.w.show() 
        self.close()

    def abrir_janela_inserir(self):
        self.w = Cadastro()
        self.w.show()

    def abrir_janela_inserir_es(self):
        self.w = Cadastro_es()
        self.w.show()

    def abrir_janela_inserir_ton(self):
        self.w = Cadastro_ton()
        self.w.show()


    #*********************Cadastrar novo usuario*********************
    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas divirgentes")
            msg.setText("As senhas estão difentes!")
            msg.exec_()
            return None
        
        if self.txt_nome.text() == None or self.txt_nome.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Nome não cadastrado")
            msg.setText("Campo nome não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_usuario.text() == None or self.txt_usuario.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("User não cadastrado")
            msg.setText("Campo user não pode estar vazio!")
            msg.exec_()
            return None

        
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()
        
        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha2.setText("")

    #*********************Colocando Dados na tabela****************** 
    def atualiza_tabela(self):
        
        db = DataBase()
        db.conecta()
        result = db.select_all_companies()

        self.table_computadores.clearContents()
        self.table_computadores.setRowCount(len(result))

        for row, text in enumerate(result):
            
            for column, data in enumerate(text):
                self.table_computadores.setItem(row, column, QTableWidgetItem(str(data)))
       
        db.close_connecion()

    #*********************Gerar planilhas Excel***********************
    def excel_file(self):

        cnx = sqlite3.connect("system.db")
        result = pd.read_sql_query("SELECT * FROM hosts", cnx)
        result.to_excel("Resumo de Maquinas.xlsx", sheet_name='hosts', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Gerar excel")
        msg.setText("Excel gerado com sucesso!")
        msg.exec_()

    #********************Colocando Dados na tablema viwer************
    def table_geral(self):

       db = QSqlDatabase("QSQLITE")
       db.setDatabaseName("system.db")
       db.open()

       self.model = QSqlTableModel(db=db)
       self.tab_estoque.setModel(self.model)
       self.model.setTable("hosts")
       self.model.select()

    def reset_table(self):

        self.table_geral()
        self.atualiza_tabela()

    #********************Filtro para selecionar empresas*************
    def update_filter(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'codigo LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

class Cadastro(QWidget, Ui_CADASTRO):
    def __init__(self):
        super(Cadastro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Caadastro")

        self.bnt_voltar_cad.clicked.connect(self.fechar_janela_cadastrar)

        self.btn_cadastrar_pc.clicked.connect(self.cad_maquinas)

    def fechar_janela_cadastrar(self):
        self.close()

    def cad_maquinas(self):


        if self.txt_codigo.text() == None or self.txt_codigo.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Codigo não pode estar vazio!")
            msg.exec_()
            return None
        
        if self.txt_hostname.text() == None or self.txt_hostname.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo hostname não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_usuario_2.text() == None or self.txt_usuario_2.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo usuario não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_ip.text() == None or self.txt_ip.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo IP não pode estar vazio!")
            msg.exec_()
            return None
        
        if self.txt_mac.text() == None or self.txt_mac.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo MAC não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_placa_mae.text() == None or self.txt_placa_mae.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Placa Mãe não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_processador.text() == None or self.txt_processador.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Processador não pode estar vazio!")
            msg.exec_()
            return None
        
        teste1 = self.cb_ram.currentText()
        if teste1 == "MEMORIA RAM":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Seleção Invalida!")
            msg.setText("Seleção Memoria RAM invalido!")
            msg.exec_()
            return None

        if self.txt_placa_video.text() == None or self.txt_placa_video.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Placa de Video não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_fonte.text() == None or self.txt_fonte.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo fonte não pode estar vazio!")
            msg.exec_()
            return None
        
        if self.txt_ssd.text() == None or self.txt_ssd.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo SSD não pode estar vazio!")
            msg.exec_()
            return None

        teste2 = self.cb_rede.currentText()
        if teste2 == "PLACA DE REDE":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Seleção Invalida!")
            msg.setText("Seleção Placa de Rede invalido!")
            msg.exec_()
            return None

        if self.txt_win.text() == None or self.txt_win.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo WIN não pode estar vazio!")
            msg.exec_()
            return None

        codigo = self.txt_codigo.text()
        hostname = self.txt_hostname.text()
        usuario = self.txt_usuario_2.text()
        ip = self.txt_ip.text()
        mac = self.txt_mac.text()
        pmae = self.txt_placa_mae.text()
        processador = self.txt_processador.text()
        ram = self.cb_ram.currentText()
        pvideo = self.txt_placa_video.text()
        fonte = self.txt_fonte.text()
        ssd = self.txt_ssd.text()
        prede = self.cb_rede.currentText()
        win = self.txt_win.text()
        
        db = DataBase()
        db.conecta()
        db.insert_hosts(codigo, hostname, usuario, ip, mac, pmae, processador, ram, pvideo, fonte, ssd, prede, win)
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de maquinas")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_codigo.setText("")
        self.txt_hostname.setText("")
        self.txt_usuario_2.setText("")
        self.txt_ip.setText("")
        self.txt_mac.setText("")
        self.txt_placa_mae.setText("")
        self.txt_processador.setText("")
        self.txt_placa_video.setText("")
        self.txt_fonte.setText("")
        self.txt_ssd.setText("")
        self.txt_win.setText("")

class Excluir(QWidget, Ui_Excluir):
    def __init__(self):
        super(Excluir, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Excluir")

        self.bnt_voltarx.clicked.connect(self.fechar_janela_excluir)
        self.bnt_excluirx.clicked.connect(self.excluir_pcs)

    def excluir_pcs(self):

        if self.txt_excluir.text() == None or self.txt_excluir.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Erro!! Digite o codigo da maquina que vc deseja excluir!")
            msg.exec_()
            return None
        
        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.txt_excluir.text()
            result = db.delete_hosts(codigo)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText("Deletada com sucesso")
            msg.exec()

        db.close_connecion()
    
    def fechar_janela_excluir(self):
        self.close()

class Atualizar(QWidget, Ui_Atualizar):
    def __init__(self):
        super(Atualizar, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Atualizar")

        self.bnt_voltar_atualizar.clicked.connect(self.fechar_janela_atualizar)
        self.btn_atualizar_pc.clicked.connect(self.atualizar_maquinas)
        self.atualizar_tab()

    def fechar_janela_atualizar(self):
            autenticado = "administrador"
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
     
    def atualizar_tab(self):
        db = DataBase()
        db.conecta()
        result = db.select_all_companies()

        self.tab_atualizar.clearContents()
        self.tab_atualizar.setRowCount(len(result))

        for row, text in enumerate(result):
            
            for column, data in enumerate(text):
                self.tab_atualizar.setItem(row, column, QTableWidgetItem(str(data)))
       
        db.close_connecion()
    
    def atualizar_maquinas(self):
        dados = []
        update_dados = []

        for row in range(self.tab_atualizar.rowCount()):
            for column in range(self.tab_atualizar.columnCount()):
                dados.append(self.tab_atualizar.item(row, column).text())
            update_dados.append(dados)
            dados = []
        
        db = DataBase()
        db.conecta()

        for com in update_dados:
            db.update_table(tuple(com))
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de maquinas")
        msg.setText("Cadastro Atualizado com sucesso!")
        msg.exec_()
    
        self.tab_atualizar.reset()
        self.atualizar_tab()

class Cadastro(QWidget, Ui_CADASTRO):
    def __init__(self):
        super(Cadastro, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Cadastro")

        self.bnt_voltar_cad.clicked.connect(self.fechar_janela_cadastrar)

        self.btn_cadastrar_pc.clicked.connect(self.cad_maquinas)

    def fechar_janela_cadastrar(self):
        self.close()

    def cad_maquinas(self):


        if self.txt_codigo.text() == None or self.txt_codigo.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Codigo não pode estar vazio!")
            msg.exec_()
            return None
        
        if self.txt_hostname.text() == None or self.txt_hostname.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo hostname não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_usuario_2.text() == None or self.txt_usuario_2.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo usuario não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_ip.text() == None or self.txt_ip.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo IP não pode estar vazio!")
            msg.exec_()
            return None
        
        if self.txt_mac.text() == None or self.txt_mac.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo MAC não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_placa_mae.text() == None or self.txt_placa_mae.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Placa Mãe não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_processador.text() == None or self.txt_processador.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Processador não pode estar vazio!")
            msg.exec_()
            return None
        
        teste1 = self.cb_ram.currentText()
        if teste1 == "MEMORIA RAM":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Seleção Invalida!")
            msg.setText("Seleção Memoria RAM invalido!")
            msg.exec_()
            return None

        if self.txt_placa_video.text() == None or self.txt_placa_video.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo Placa de Video não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_fonte.text() == None or self.txt_fonte.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo fonte não pode estar vazio!")
            msg.exec_()
            return None
        
        if self.txt_ssd.text() == None or self.txt_ssd.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo SSD não pode estar vazio!")
            msg.exec_()
            return None

        teste2 = self.cb_rede.currentText()
        if teste2 == "PLACA DE REDE":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Seleção Invalida!")
            msg.setText("Seleção Placa de Rede invalido!")
            msg.exec_()
            return None

        if self.txt_win.text() == None or self.txt_win.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo WIN não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_monit.text() == None or self.txt_monit.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo MONITOR não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_monit2.text() == None or self.txt_monit2.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo MONITOR AUX não pode estar vazio!")
            msg.exec_()
            return None

        codigo = self.txt_codigo.text()
        hostname = self.txt_hostname.text()
        usuario = self.txt_usuario_2.text()
        ip = self.txt_ip.text()
        mac = self.txt_mac.text()
        pmae = self.txt_placa_mae.text()
        processador = self.txt_processador.text()
        ram = self.cb_ram.currentText()
        pvideo = self.txt_placa_video.text()
        fonte = self.txt_fonte.text()
        ssd = self.txt_ssd.text()
        prede = self.cb_rede.currentText()
        monitor = self.txt_monit.text()
        monitor2 = self.txt_monit2.text()
        win = self.txt_win.text()
        
        db = DataBase()
        db.conecta()
        db.insert_hosts(codigo, hostname, usuario, ip, mac, pmae, processador, ram, pvideo, fonte, ssd, prede, monitor, monitor2, win)
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de maquinas")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_codigo.setText("")
        self.txt_hostname.setText("")
        self.txt_usuario_2.setText("")
        self.txt_ip.setText("")
        self.txt_mac.setText("")
        self.txt_placa_mae.setText("")
        self.txt_processador.setText("")
        self.txt_placa_video.setText("")
        self.txt_fonte.setText("")
        self.txt_ssd.setText("")
        self.txt_win.setText("")
        self.txt_monit.setText("")
        self.txt_monit2.setText("")

class Cadastro_es(QWidget, Ui_CADASTRO_es):
    def __init__(self):
        super(Cadastro_es, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Cadastro de estoque")

        self.bnt_voltar_cad.clicked.connect(self.fechar_janela_cadastrar)

        self.btn_cadastrar_pc.clicked.connect(self.cad_maquinas)

    def fechar_janela_cadastrar(self):
        self.close()

    def cad_maquinas(self):
        if self.txt_win.text() == None or self.txt_win.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo peça não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_hostname.text() == None or self.txt_hostname.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo quantidade não pode estar vazio!")
            msg.exec_()
            return None

        quant = self.txt_hostname.text()
        peca = self.txt_win.text()

        db = DataBase()
        db.conecta()
        db.insert_estoque(peca, quant)
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de estoque")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_hostname.setText("")
        self.txt_win.setText("")

class Cadastro_ton(QWidget, Ui_CADASTRO_ton):
    def __init__(self):
        super(Cadastro_ton, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela de Cadastro de tonners")

        self.bnt_voltar_cad.clicked.connect(self.fechar_janela_cadastrar)

        self.btn_cadastrar_pc.clicked.connect(self.cad_maquinas)

    def fechar_janela_cadastrar(self):
        self.close()

    def cad_maquinas(self):
        if self.txt_win.text() == None or self.txt_win.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo tonner não pode estar vazio!")
            msg.exec_()
            return None

        if self.txt_hostname.text() == None or self.txt_hostname.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Campo quantidade não pode estar vazio!")
            msg.exec_()
            return None

        quant = self.txt_hostname.text()
        tonner = self.txt_win.text()

        db = DataBase()
        db.conecta()
        db.insert_tonner(tonner, quant)
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de tonners")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_hostname.setText("")
        self.txt_win.setText("")

class Excluir(QWidget, Ui_Excluir):
    def __init__(self):
        super(Excluir, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Excluir")

        self.bnt_voltarx.clicked.connect(self.fechar_janela_excluir)
        self.bnt_excluirx.clicked.connect(self.excluir_pcs)

    def excluir_pcs(self):

        if self.txt_excluir.text() == None or self.txt_excluir.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Erro!! Digite o codigo da maquina que vc deseja excluir!")
            msg.exec_()
            return None
        
        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.txt_excluir.text()
            result = db.delete_hosts(codigo)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("MAQUIONAS")
            msg.setText("Deletada com sucesso")
            msg.exec()

        db.close_connecion()
    
    def fechar_janela_excluir(self):
        self.close()

class Excluir_es(QWidget, Ui_Excluir_es):
    def __init__(self):
        super(Excluir_es, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Excluir")

        self.bnt_voltarx.clicked.connect(self.fechar_janela_excluir)
        self.bnt_excluirx.clicked.connect(self.excluir_pcs)

    def excluir_pcs(self):

        if self.txt_excluir.text() == None or self.txt_excluir.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Erro!! Digite o codigo de estoque que vc deseja excluir!")
            msg.exec_()
            return None
        
        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.txt_excluir.text()
            result = db.delete_estoque(codigo)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("PEÇAS")
            msg.setText("Deletada com sucesso")
            msg.exec()

        db.close_connecion()
    
    def fechar_janela_excluir(self):
        self.close()

class Excluir_ton(QWidget, Ui_Excluir_ton):
    def __init__(self):
        super(Excluir_ton, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Excluir")

        self.bnt_voltarx.clicked.connect(self.fechar_janela_excluir)
        self.bnt_excluirx.clicked.connect(self.excluir_pcs)

    def excluir_pcs(self):

        if self.txt_excluir.text() == None or self.txt_excluir.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Campo Vazio!")
            msg.setText("Erro!! Digite o codigo do tonner que vc deseja excluir!")
            msg.exec_()
            return None
        
        db = DataBase()
        db.conecta()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            codigo = self.txt_excluir.text()
            result = db.delete_tonner(codigo)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("TONNER")
            msg.setText("Deletada com sucesso")
            msg.exec()

        db.close_connecion()
    
    def fechar_janela_excluir(self):
        self.close()

class Atualizar(QWidget, Ui_Atualizar):
    def __init__(self):
        super(Atualizar, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Atualizar")

        self.bnt_voltar_atualizar.clicked.connect(self.fechar_janela_atualizar)
        self.btn_atualizar_pc.clicked.connect(self.atualizar_maquinas)
        self.atualizar_tab()

    def fechar_janela_atualizar(self):
            autenticado = "administrador"
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
     
    def atualizar_tab(self):
        db = DataBase()
        db.conecta()
        result = db.select_all_companies()

        self.tab_atualizar.clearContents()
        self.tab_atualizar.setRowCount(len(result))

        for row, text in enumerate(result):
            
            for column, data in enumerate(text):
                self.tab_atualizar.setItem(row, column, QTableWidgetItem(str(data)))
       
        db.close_connecion()
    
    def atualizar_maquinas(self):
        dados = []
        update_dados = []

        for row in range(self.tab_atualizar.rowCount()):
            for column in range(self.tab_atualizar.columnCount()):
                dados.append(self.tab_atualizar.item(row, column).text())
            update_dados.append(dados)
            dados = []
        
        db = DataBase()
        db.conecta()

        for com in update_dados:
            db.update_table(tuple(com))
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de maquinas")
        msg.setText("Cadastro Atualizado com sucesso!")
        msg.exec_()
    
        self.tab_atualizar.reset()
        self.atualizar_tab()

class Atualizar_es(QWidget, Ui_Atualizar_es):
    def __init__(self):
        super(Atualizar_es, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Atualizar")

        self.bnt_voltar_atualizar.clicked.connect(self.fechar_janela_atualizar)
        self.btn_atualizar_pc.clicked.connect(self.atualizar_maquinas)
        self.atualizar_tab()

    def fechar_janela_atualizar(self):
            autenticado = "administrador"
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
     
    def atualizar_tab(self):
        db = DataBase()
        db.conecta()
        result = db.select_all_estoques()

        self.tab_atualizar.clearContents()
        self.tab_atualizar.setRowCount(len(result))

        for row, text in enumerate(result):
            
            for column, data in enumerate(text):
                self.tab_atualizar.setItem(row, column, QTableWidgetItem(str(data)))
       
        db.close_connecion()
    
    def atualizar_maquinas(self):
        dados = []
        update_dados = []

        for row in range(self.tab_atualizar.rowCount()):
            for column in range(self.tab_atualizar.columnCount()):
                dados.append(self.tab_atualizar.item(row, column).text())
            update_dados.append(dados)
            dados = []
        
        db = DataBase()
        db.conecta()

        for com in update_dados:
            db.update_estoque(tuple(com))
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de maquinas")
        msg.setText("Cadastro Atualizado com sucesso!")
        msg.exec_()
    
        self.tab_atualizar.reset()
        self.atualizar_tab()

class Atualizar_ton(QWidget, Ui_Atualizar_ton):
    def __init__(self):
        super(Atualizar_ton, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Atualizar")

        self.bnt_voltar_atualizar.clicked.connect(self.fechar_janela_atualizar)
        self.btn_atualizar_pc.clicked.connect(self.atualizar_maquinas)
        self.atualizar_tab()

    def fechar_janela_atualizar(self):
            autenticado = "administrador"
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()
     
    def atualizar_tab(self):
        db = DataBase()
        db.conecta()
        result = db.select_all_tonner()

        self.tab_atualizar.clearContents()
        self.tab_atualizar.setRowCount(len(result))

        for row, text in enumerate(result):
            
            for column, data in enumerate(text):
                self.tab_atualizar.setItem(row, column, QTableWidgetItem(str(data)))
       
        db.close_connecion()
    
    def atualizar_maquinas(self):
        dados = []
        update_dados = []

        for row in range(self.tab_atualizar.rowCount()):
            for column in range(self.tab_atualizar.columnCount()):
                dados.append(self.tab_atualizar.item(row, column).text())
            update_dados.append(dados)
            dados = []
        
        db = DataBase()
        db.conecta()

        for com in update_dados:
            db.update_tonner(tuple(com))
        db.close_connecion()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de maquinas")
        msg.setText("Cadastro Atualizado com sucesso!")
        msg.exec_()
    
        self.tab_atualizar.reset()
        self.atualizar_tab()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()