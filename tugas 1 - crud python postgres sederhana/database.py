import psycopg2
from psycopg2 import Error

'''
TUGAS PBO LANJUT 1

AUTHOR  : ADITYA BAYU AJI
NIM     : 200511140
R2 - TEKNIK INFORMATIKA
'''

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = '5432'
        self.database = 'myDB'
        self.user = 'adit'
        self.password = '123'
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0