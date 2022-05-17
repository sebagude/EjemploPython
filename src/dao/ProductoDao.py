from src.conf.DbConnection import DbConnection


class ProductoDao:
    __db = None

    def __init__(self):
        self.__db = DbConnection()

    def get_productos(self):
        print('respondiendo desde producto dao')
        return self.__db.query("SELECT * FROM productos", None).fetchall()

    def add_producto(self, producto):
        sql = "INSERT INTO productos (nombre, descripcion) VALUES (%s, %s);"
        params = (producto.nombre, producto.descripcion)
        return self.__db.query(sql, params)