from connection import Connection as mydb

'''
TUGAS PBO LANJUT 1

AUTHOR  : ADITYA BAYU AJI
NIM     : 200511140
R2 - TEKNIK INFORMATIKA
'''

class Mahasiswa:
    def __init__(self):
        self.__nim = None
        self.__nama = None
        self.__jk = None
        self.__info = None
        self.db = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info == None):
            return f'NIM: {self.__nim}\nNama: {self.__nama}\nJenis Kelamin: {self.__jk}'
        else:
            return self.__info
    
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value
    
    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value
        
    def simpan(self):
        self.db = mydb()
        sql = F'INSERT INTO mahasiswa (nim,nama,jk) VALUES (\'{self.__nim}\',\'{self.__nama}\',\'{self.__jk}\')'
        self.affected = self.db.insert(sql)
        self.db.disconnect
        return self.affected
        
    def update(self, nim):
        self.db = mydb()
        val = (nim,self.__nama,self.__jk, nim)
        sql = 'UPDATE mahasiswa SET nim = %s, nama = %s, jk = %s WHERE nim = %s;'
        self.affected = self.db.update(sql, val)
        self.db.disconnect
        return self.affected
        
    def delete(self, nim):
        self.db = mydb()
        sql="DELETE FROM mahasiswa WHERE nim='" + str(nim) + "';"
        self.affected = self.db.delete(sql)
        self.db.disconnect
        return self.affected
        
    def getByNIM(self, nim):
        self.db = mydb()
        sql="SELECT * FROM mahasiswa WHERE nim='" + nim + "';"
        self.result = self.db.findOne(sql)
        if(self.result != None):
            self.__nim = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.affected = self.db.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__jk = ''
            self.affected = 0
            self.affected = 0
            self.db.disconnect
            return self.result

    def getAllData(self):
        self.db = mydb()
        sql = 'SELECT * FROM mahasiswa;'
        self.result = self.db.findAll(sql)
        if(self.result == 0):
            return self.result
        else:
            for res in self.result:
                print(f'ID Mahasiswa    : ' + str(res[0]))
                print(f'NIM             : ' + res[1])
                print(f'Nama Lengkap    : ' + res[2])
                print(f'Jenis Kelamin   : ' + res[3])
                print('\n')