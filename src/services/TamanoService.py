from src.dao.TamanoDao import TamanoDao


class TamanoService:
    __tamano_dao = TamanoDao()

    def get_tamanos(self):
        print('respondiendo desde el tamano service')
        return self.__tamano_dao.get_tamanos()

    def add_tamano(self, tamano):
        return self.__tamano_dao.add_tamano(tamano)

