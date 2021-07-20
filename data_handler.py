
from customer import Customer
from file_parser import FileParser


class DataHandler:

    def __init__(self):

        self._customers = []

        self.read_customers()

    def read_customers(self):

        file_parser = FileParser()
        self._customers = file_parser.read_customers("custs.txt")

    # def load_customers(self):

    #     self._customers.append(Customer(
    #         "yyyyyyyy", "Bbbbbb", "0987654321", "aaaaaa.bbbbbb@test.org", "A12 BC34", 123.50))
    #     self._customers.append(Customer(
    #         "zzzzzzzz", "Dddd", "1234567890", "cccc.dddd@test.org", "D56 EF78", 67.90))

    def add_customer(self, customer):

        self._customers.append(customer)

    @property
    def customers(self):
        return self._customers
