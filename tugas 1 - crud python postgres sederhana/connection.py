import psycopg2
from psycopg2 import Error
from database import Database

'''
TUGAS PBO LANJUT 1

AUTHOR  : ADITYA BAYU AJI
NIM     : 200511140
R2 - TEKNIK INFORMATIKA
'''

class Connection(Database):
    def __init__(self):
        super().__init__()
        
    @property
    def connection_status(self):
        return self.connected
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(host = self.host,
                                        port = self.port,
                                        database = self.database,
                                        user = self.user,
                                        password = self.password)
            self.connected = True
            self.cursor = self.conn.cursor()
            # self.cursor.execute('SELECT version();')
            # self.version = self.cursor.fetchone()
        except (Exception, Error) as error:
            self.connected = False
            print(f'Error while connecting to PostgreSQL {error}')
        return self.conn
    
    def disconnect(self):
        if(self.connected==True):
            self.conn.close
        else:
            self.conn = None

    def findOne(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    def findAll(self, sql):
        self.connect()
        self.result = self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def update(self, sql, val):
        self.connect()  
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def delete(self, sql):
        self.connect()  
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount
        return self.affected

    def show(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    @property
    def info(self):
        if(self.connected==True):
            return 'Server is running on ' + self.host + ' using port ' + str(self.port)
        else:
            return 'Server is offline.'