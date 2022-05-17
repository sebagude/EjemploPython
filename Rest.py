from flask import Flask, request
import mysql.connector
import json
from flask_cors import CORS

from models.Customer import Customer

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="cnxcakeshop",
    password="cakeshop123",
    database="reposteriabd",
)

mycursor = mydb.cursor()


def jsonDefault(object):
    return object.__dict__


@app.route('/addCustomer', methods=['POST'])
def addCustomer():
    response = request.json

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (response['name'], response['address'])
    mycursor.execute(sql, val)
    mydb.commit()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/getCustomer', methods=['GET'])
def getCustomer():
    customerId = request.args.get('customerId')
    sql = "select * from customers where id = " + customerId
    cursor = mydb.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    return json.dumps(Customer(result[0], result[1], result[2]), default=jsonDefault)


@app.route('/getCustomers', methods=['GET'])
def getAllCustomers():
    sql = "select * from customers;"
    cursor = mydb.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    customers = []

    for row in result:
        customers.append(Customer(row[0], row[1], row[2]))

    return json.dumps(customers, default=jsonDefault)


@app.route("/deleteCustomer/<id>", methods=["DELETE"])
def deleteCustomers(id):

    sql = "DELETE FROM customers WHERE id = " + id

    mycursor.execute(sql)

    mydb.commit()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/updateCustomer/<id>", methods=["PATCH"])
def updateCustomer(id):
    response = request.json

    sql = "UPDATE customers SET address = '" + response['address'] + "', name = '" + response[
        'name'] + "' WHERE id = " + id

    mycursor.execute(sql)

    mydb.commit()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


app.run(debug=True)
