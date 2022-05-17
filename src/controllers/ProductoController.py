import json

from flask import Blueprint, request

from src.models.Producto import Producto
from src.services.ProductoService import ProductoService

producto_controller = Blueprint('producto_controller', __name__)

@producto_controller.route('/getProductos', methods=['GET'])
def get_all_productos():
    __producto_service = ProductoService()
    print("Respondiendo desde el controlador de producto")
    return json.dumps(__producto_service.get_productos())


@producto_controller.route('/addProducto', methods=['POST'])
def add_producto():
    data_in = request.json
    __producto_service = ProductoService()
    my_producto = Producto(0, data_in ['nombre'], data_in['descripcion'])
    answer = __producto_service.add_producto(my_producto)
    return json.dumps({'sucess': True}), 200, {'ContentType': 'application/json'}
