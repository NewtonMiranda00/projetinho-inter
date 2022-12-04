import pymysql
import os


class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASS'),
            database=os.getenv('DATABASE_NAME')
        )

        self.cursor = self.db.cursor()

    def version(self):
        self.cursor.execute('SELECT VERSION()')

        data = self.cursor.fetchone()

        self.db.close()

        return data

    def setup_database(self):
        sql = 'DROP TABLE IF EXISTS Historico'
        self.cursor.execute(sql)

        sql = '''CREATE TABLE Historico (
            input CHAR(20)
        );'''
        self.cursor.execute(sql)

        self.db.close()

    def inserir_na_tabela(self, data):
        sql = f'INSERT INTO Historico VALUES (%s)'

        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except BaseException:
            self.db.rollback()

        self.db.close()
