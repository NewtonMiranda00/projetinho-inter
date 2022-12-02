import pymysql
import os


class DataBase:
    def __init__(self):
        self.db = pymysql.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASS'),
            database=os.getenv('DATABASE_NAME')
        )

        self.cursor = self.db.cursor()

    def checar_versao(self):
        self.cursor.execute('SELECT VERSION()')

        data = self.cursor.fetchone()

        print('Versão do banco de dados:', data)

        self.db.close()

    def criar_tabela(self):
        sql = 'DROP TABLE IF EXISTS Historico'
        self.cursor.execute(sql)

        sql = '''CREATE TABLE Historico (
            mano CHAR(20)
        );'''
        self.cursor.execute(sql)

        self.db.close()

    def inserir_na_tabela(self, a):
        sql = f'''INSERT INTO Historico VALUES ("{a}")'''

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except BaseException:
            self.db.rollback()

        self.db.close()
