import json

from flask import Blueprint, request

from src.models.Customer import Customer
from src.services.CustomerService import CustomerService

customer_controller = Blueprint('customer_controller', __name__)


@customer_controller.route('/getCustomers', methods=['GET'])
def get_all_customers():
    __customer_service = CustomerService()
    print("Respondiendo desde el customer controller")
    return json.dumps(__customer_service.get_customers())


@customer_controller.route('/addCustomer', methods=['POST'])
def add_customer():
    data_in = request.json
    __customer_service = CustomerService()
    my_customer = Customer(0, data_in['name'], data_in['address'])
    answer = __customer_service.add_customer(my_customer)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@customer_controller.route('/deleteCustomer', methods=['DELETE'])
def delete_customer():
    data_in = request.json
    __customer_service = CustomerService()
    answer = __customer_service.delete_customer(data_in['id'])
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@customer_controller.route('/updateCustomer', methods=['PUT'])
def update_customer():
    data_in = request.json
    __customer_service = CustomerService()
    my_customer = Customer(data_in['id'], data_in['name'], data_in['address'])
    answer = __customer_service.update_customer(my_customer)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}