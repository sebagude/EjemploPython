from src.conf.DbConnection import DbConnection

class TamanoDao:
    __db = None

    def __init__(self):
        self.__db = DbConnection()

    def get_tamanos(self):
        print('respondiendo desde el tamaños dao')
        return self.__db.query("SELECT * FROM tamano", None).fetchall()

    def add_tamano(self, tamano):
        sql = "INSERT INTO tamano (tamano, porcion) VALUES(%s, %s);"
        params = (tamano.tamano, tamano.porcion)
        return self.__db.query(sql, params)