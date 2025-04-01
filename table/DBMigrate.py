import sqlite3
class DBMigrate:
    __db_name: str
    cursor: any
 
    def __init__(self):
        self.__db_name = "db.db"
        self.__connection = sqlite3.connect(self.__db_name)
        cursor = self.__connection.cursor()
        self.users(cursor)
        self.products(cursor)
        self.__connection.commit()
 
    def users(self, cursor):
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL
                    )
                 ''')
 
    """
    this method wrote by Mr. Benedikt Brenk
    thanx
    """
    def products(self, cursor):
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    category TEXT NOT NULL,
                    price FLOAT NOT NULL
                    )
                 ''')