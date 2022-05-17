import json

from flask import Blueprint, request

from src.models.Tamano import Tamano
from src.services.TamanoService import TamanoService

tamano_controller = Blueprint('tamano_controller', __name__)

@tamano_controller.route('/getTamanos', methods=['GET'])
def get_all_tamanos():
    __tamano_service = TamanoService()
    print("Respondiendo desde el tamano controller")
    return json.dumps(__tamano_service.get_tamanos())


@tamano_controller.route('/addTamano', methods=['POST'])
def add_tamano():
    data_in = request.json
    __tamano_service = TamanoService()
    my_tamano = Tamano(0, data_in['tamano'], data_in['porcion'])
    answer = __tamano_service.add_tamano(my_tamano)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
