from src.dao.CustomerDao import CustomerDao


class CustomerService:
    __customer_dao = CustomerDao()

    def get_customers(self):
        print('respondiendo desde el customer service')
        return self.__customer_dao.get_customers()

    def add_customer(self, customer):
        if customer.name.isalpha():
            return self.__customer_dao.add_customer(customer)
        else:
            return "Nombre solo debe ser alfábetico."

    def delete_customer(self, id):
        return self.__customer_dao.delete_customer(id)

    def update_customer(self, customer):
        return self.__customer_dao.update_customer(customer)

