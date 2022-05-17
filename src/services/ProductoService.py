from src.dao.ProductoDao import ProductoDao


class ProductoService:
    __producto_dao = ProductoDao()

    def get_productos(self):
        print('respondiendo desde el servicio productos')
        return self.__producto_dao.get_productos()

    def add_producto(self, producto):
            return self.__producto_dao.add_producto(producto)
