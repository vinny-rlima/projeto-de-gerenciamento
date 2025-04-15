import sqlite3

class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connecion(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
        
               CREATE TABLE IF NOT EXISTS users(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL

               );
        
        """)
        except AttributeError:
            print("faça a conexão")
    
    def insert_user(self, name, user, password, access):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)

            """,(name, user, password, access))
            self.connection.commit()

        except AttributeError:
            print("Faça a conexão")
    
    def check_user(self, user, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                
                SELECT * FROM users;
                
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "ADMINISTRADOR":
                    return "administrador"

                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "USUARIO":
                    return "user"
                else:
                    continue
            return "sem acesso"

        except:
            pass


        self.name = name

        try:
            self.connection.close()
        except:
            pass
   
    def create_table_hosts(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
        
               CREATE TABLE IF NOT EXISTS hosts(

                    codigo TEXT NOT NULL,
                    hostname TEXT NOT NULL,
                    usuario TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    mac TEXT NOT NULL,
                    pmae TEXT NOT NULL,
                    processador TEXT NOT NULL,
                    ram TEXT NOT NULL,
                    pvideo TEXT NOT NULL,
                    fonte TEXT NOT NULL,
                    ssd TEXT NOT NULL,
                    prede TEXT NOT NULL,
                    monitor TEXT,
                    monitor2 TEXT,
                    win TEXT NOT NULL,

                    PRIMARY KEY(codigo)

               );
        
        """)
        except AttributeError:
            print("faça a conexão")
    
    def insert_hosts(self, codigo, hostname, usuario, ip, mac, pmae, processador, ram, pvideo, fonte, ssd, prede, monitor, monitor2, win):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO hosts(codigo, hostname, usuario, ip, mac, pmae, processador, ram, pvideo, fonte, ssd, prede, monitor, monitor2, win) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

            """,(codigo, hostname, usuario, ip, mac, pmae, processador, ram, pvideo, fonte, ssd, prede, monitor, monitor2, win))
            self.connection.commit()

        except AttributeError:
            print ("Faça a conexão")

    def update_table(self, fullDataSet):
       
        cursor = self.connection.cursor()
        cursor.execute(f"""
        
               UPDATE hosts set

                    codigo  = '{fullDataSet[0]}',
                    hostname = '{fullDataSet[1]}',
                    usuario = '{fullDataSet[2]}',
                    ip = '{fullDataSet[3]}',
                    mac = '{fullDataSet[4]}',
                    pmae = '{fullDataSet[5]}',
                    processador = '{fullDataSet[6]}',
                    ram = '{fullDataSet[7]}',
                    pvideo = '{fullDataSet[8]}',
                    fonte = '{fullDataSet[9]}',
                    ssd = '{fullDataSet[10]}',
                    prede = '{fullDataSet[11]}',
                    monitor = '{fullDataSet[12]}',
                    monitor2 = '{fullDataSet[13]}',
                    win = '{fullDataSet[14]}'

                    WHERE codigo = '{fullDataSet[0]}'
        
        """)
        
        self.connection.commit()

    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM hosts ORDER BY hostname")
            computadores = cursor.fetchall()
            return computadores
        except:
            pass

    def delete_hosts(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM hosts WHERE codigo = '{id}' ")

            self.connection.commit()

            print("Cadastro de computador excluido com sucesso!") 

        except AttributeError:
            print("Erro ao Excluir registro!")

    def create_table_estoque(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
        
               CREATE TABLE IF NOT EXISTS estoque(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    peca TEXT NOT NULL,
                    quant TEXT NOT NULL

               );
        
        """)
        except AttributeError:
            print("faça a conexão")
    
    def insert_estoque(self, peca, quant):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO estoque(peca, quant) VALUES(?,?)

            """,(peca, quant))
            self.connection.commit()

        except AttributeError:
            print("Faça a conexão")

    def update_estoque(self, fullDataSet):
       
        cursor = self.connection.cursor()
        cursor.execute(f"""
        
               UPDATE estoque set

                    id  = '{fullDataSet[0]}',
                    peca = '{fullDataSet[1]}',
                    quant = '{fullDataSet[2]}',

                    WHERE id = '{fullDataSet[0]}'
        
        """)
        
        self.connection.commit()

    def delete_estoque(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM estoque WHERE id = '{id}' ")

            self.connection.commit()

            print("Cadastro de estoque excluido com sucesso!") 

        except AttributeError:
            print("Erro ao Excluir registro!") 

    def select_all_estoques(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM estoque ORDER BY peca")
            computadores = cursor.fetchall()
            return computadores
        except:
            pass

    def create_table_tonner(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
        
               CREATE TABLE IF NOT EXISTS tonners(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    tonner TEXT NOT NULL,
                    quant TEXT NOT NULL

               );
        
        """)
        except AttributeError:
            print("faça a conexão")
    
    def insert_tonner(self, tonner, quant):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO tonners(tonner, quant) VALUES(?,?)

            """,(tonner, quant))
            self.connection.commit()

        except AttributeError:
            print("Faça a conexão")

    def update_tonner(self, fullDataSet):
       
        cursor = self.connection.cursor()
        cursor.execute(f"""
        
               UPDATE tonners set

                    id  = '{fullDataSet[0]}',
                    tonner = '{fullDataSet[1]}',
                    quant = '{fullDataSet[2]}',

                    WHERE id = '{fullDataSet[0]}'
        
        """)
        
        self.connection.commit()

    def select_all_tonner(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM tonners ORDER BY tonner")
            computadores = cursor.fetchall()
            return computadores
        except:
            pass

    def delete_tonner(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM tonners WHERE id = '{id}' ")

            self.connection.commit()

            print("Cadastro de tonner excluido com sucesso!") 

        except AttributeError:
            print("Erro ao Excluir registro!") 

if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table_hosts()
    db.create_table_tonner()
    db.create_table_estoque()
    db.close_connecion()
