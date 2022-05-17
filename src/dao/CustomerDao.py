from src.conf.DbConnection import DbConnection


class CustomerDao:
    __db = None

    def __init__(self):
        self.__db = DbConnection()

    def get_customers(self):
        print('respondiendo desde el custumer dao')
        return self.__db.query("SELECT * FROM customers", None).fetchall()

    def add_customer(self, customer):
        sql = "INSERT INTO customers (name, address) VALUES(%s, %s);"
        params = (customer.name, customer.address)
        return self.__db.query(sql, params)

    def delete_customer(self, id):
        sql = "DELETE FROM customers WHERE id=%s"
        return self.__db.query(sql, (id,))

    def update_customer(self, customer):
        sql = "UPDATE customers SET name=%s, address=%s WHERE id=%s"
        params = (customer.name, customer.address, customer.id)
        return self.__db.query(sql, params)