from customer import Customer


class FileParser():

    def read_customers(self, filename):

        fo = open(filename, "r")

        # store the file contents as a list of strings
        lines = fo.readlines()
        fo.close()

        customers = []

        # parse each line of customers file and create a Customer object
        for line in lines:
            customer = self.parse_customer_text(line)
            customers.append(customer)

        return customers

    def parse_customer_text(self, cust_text):

        fields = cust_text.split("|")

        forename = fields[0]
        surname = fields[1]
        ppsn = fields[2]
        accountType = fields[3]
        overdraft = fields[4]
        balance = float(fields[5])
        # todo: add exception handler

        customer = Customer(forename, surname, ppsn, accountType, overdraft)
        customer.balance = balance
        return customer

    def write_customers(self, filename, customers):

        fo = open(filename, "w")

        # list to contain text versions of customers for writing
        lines = []
        first_customer = True

        # build a list of customer file strings
        for customer in customers:

            if first_customer == True:
                lines.append(customer.file_text())
                first_customer = False
            else:
                # if this isn't the first customer, add a newline before writing
                lines.append(f"\n{customer.file_text()}")

        fo.writelines(lines)
        fo.close()
