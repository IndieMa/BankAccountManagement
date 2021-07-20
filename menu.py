import os
from customer import Customer
from data_handler import DataHandler
from file_parser import FileParser
from user_input_processor import UserInputProcessor


class Menu():

    def clearscreen(self):
        os.system('cls')

    def main_menu(self, datahandler):
        inputProcessor = UserInputProcessor()
        menuExit = False
        while not menuExit:
            self.display_user_menu()
            choice = inputProcessor.readUserInputInteger(6, 1)
            if(choice == 1):
                self.view_customers_menu(datahandler)
            elif(choice == 2):
                self.add_customer(datahandler)
            elif(choice == 3):
                self.deposit_to_account(datahandler)
            elif(choice == 4):
                self.withdraw_from_account(datahandler)
            elif(choice == 5):
                self.transfer_to_another_account(datahandler)
            elif(choice == 6):
                menuExit = True
        print("Exiting application. Goodbye!")

        # application is now exiting - write customers list to file
        file_parser = FileParser()
        file_parser.write_customers("custs.txt", datahandler.customers)

    # Display the options for the main menu
    def display_user_menu(self):
        self.clearscreen()
        print("Welcome!")
        print("Main Menu - Menu options:")
        print("1. View Customers")
        print("2. Add Customer")
        print("3. Deposit to account")
        print("4. Withdraw funds from account")
        print("5. Transfer funds to another account")
        print("6. Exit\n")

    def view_customers_menu(self, datahandler):
        inputProcessor = UserInputProcessor()
        menuExit = False
        while not menuExit:
            self.display_view_customers_menu()
            choice = inputProcessor.readUserInputInteger(3, 1)
            if(choice == 1):
                self.view_all_customers(datahandler)
            elif(choice == 2):
                self.clearscreen()
                print("View account by PPSN")
                print("==================\n")
                ppsn = input("Enter the PPSN for the customer to be viewed: ")
                self.view_customer_by_ppsn(datahandler, ppsn)
            elif(choice == 3):
                menuExit = True

    def display_view_customers_menu(self):
        print("View Customers - Menu options:")
        print("1. View all customers")
        print("2. View customer by PPSN")
        print("3. Back to Main Menu")

    def view_all_customers(self, datahandler):
        self.clearscreen()
        print("ID         Forename    Surname              PPSN        Account Type    Overdraft    Balance    Interest Rate")
        print("============================================================================================================")

        for customer in datahandler.customers:
            print(customer)

        print("Return to continue...")
        input()

    def view_customer_by_ppsn(self, datahandler, ppsn):
        ppsnFound = False
        self.clearscreen()
        for customer in datahandler.customers:
            if customer.ppsn == ppsn:
                print(
                    "ID         Forename    Surname              PPSN        Account Type    Overdraft    Balance    Interest Rate")
                print(
                    "============================================================================================================")
                print(customer)
                ppsnFound = True
        if not ppsnFound:
            print("No customers with the PPSN", ppsn, "were found. ")

        print("Return to continue...")
        input()

    def add_customer(self, datahandler):
        accountTypeSet = False
        overdraftSet = False
        print("Add a new Customer")
        print("==================\n")
        forename = input("Forename: ")
        surname = input("Surname: ")
        ppsn = input("PPSN: ")
        while not accountTypeSet:
            accountType = input(
                "Account Type (Deposit/Current, case sensitive): ")
            if accountType == 'Deposit' or accountType == 'Current':
                accountTypeSet = True
            else:
                print(
                    "Invalid account type specified. Please choose from \'Deposit\' or \'Current\'")
        while not overdraftSet:
            overdraft = input("Overdraft (Yes/No, case sensitive): ")
            if overdraft == 'Yes' or overdraft == 'No':
                overdraftSet = True
            else:
                print(
                    "Invalid overdraft option specified. Please choose from \'Yes\' or \'No\'")

        customer = Customer(forename, surname, ppsn, accountType, overdraft)

        datahandler.add_customer(customer)

        print("Return to continue...")
        input()

    def deposit_to_account(self, datahandler):
        accountFound = False
        accountNumberValid = False
        amountValid = False
        self.clearscreen()
        print("Deposit money into account")
        print("==================\n")
        while not accountNumberValid:
            try:
                accountNumber = int(
                    input("Enter the Account Number for the customer account to deposit into: "))
                accountNumberValid = True
            except ValueError as e:
                print(
                    'Value Error - Account number must be an integer. Please try again.')

        for customer in datahandler.customers:
            if customer.accountNumber == accountNumber:
                print("Account,", customer.forename,
                      customer.surname, "found!")
                while not amountValid:
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                        amountValid = True
                    except ValueError as e:
                        print(
                            'Value Error - Deposit amount must be a whole number or decimal number. Please try again.')

                customer.deposit(amount)
                accountFound = True
        if not accountFound:
            print("Account with account number", accountNumber, "not found...")

        print("Return to continue...")
        input()

    def withdraw_from_account(self, datahandler):
        accountFound = False
        accountNumberValid = False
        amountValid = False
        self.clearscreen()
        print("Withdraw money from account")
        print("==================\n")
        while not accountNumberValid:
            try:
                accountNumber = int(
                    input("Enter the Account Number for the customer account to withdraw from: "))
                accountNumberValid = True
            except ValueError as e:
                print(
                    'Value Error - Account number must be an integer. Please try again.')

        for customer in datahandler.customers:
            if customer.accountNumber == accountNumber:
                print("Account,", customer.forename,
                      customer.surname, "found!")
                while not amountValid:
                    try:
                        amount = float(input("Enter the amount to withdraw: "))
                        amountValid = True
                    except ValueError as e:
                        print(
                            'Value Error - Withdraw amount must be a whole number or decimal number. Please try again.')

                customer.withdraw(amount)
                accountFound = True
        if not accountFound:
            print("Account with account number", accountNumber, "not found...")

        print("Return to continue...")
        input()

    def transfer_to_another_account(self, datahandler):
        senderAccountFound = False
        recipientAccountFound = False
        senderAccountNumberValid = False
        recipientAccountNumberValid = False
        self.clearscreen()
        print("Transfer money from one account to another")
        print("==================\n")
        while not senderAccountNumberValid:
            try:
                senderAccountNumber = int(
                    input("Enter the Account Number for the sender customer account: "))
                senderAccountNumberValid = True
            except ValueError as e:
                print(
                    'Value Error - Sender account number must be an integer. Please try again.')

        while not recipientAccountNumberValid:
            try:
                recipientAccountNumber = int(
                    input("Enter the Account Number for the recipient customer account: "))
                recipientAccountNumberValid = True
            except ValueError as e:
                print(
                    'Value Error - Recipient account number must be an integer. Please try again.')

        for customer in datahandler.customers:
            if customer.accountNumber == senderAccountNumber:
                senderAccount = customer
                senderAccountFound = True
                print("Sender account,", customer.forename,
                      customer.surname, "found!")
            elif customer.accountNumber == recipientAccountNumber:
                recipientAccount = customer
                recipientAccountFound = True
                print("Recipient account,", customer.forename,
                      customer.surname, "found!")

        if recipientAccountFound and senderAccountFound:
            self.execute_funds_transfer(senderAccount, recipientAccount)
        else:
            if not senderAccountFound:
                print("Sender account with account number",
                      senderAccountNumber, "not found...")

            if not recipientAccountFound:
                print("Recipient account with account number",
                      recipientAccountNumber, "not found...")

        print("Return to continue...")
        input()

    def execute_funds_transfer(self, sender, recipient):
        amountValid = False
        while not amountValid:
            try:
                amount = float(input("Enter the amount to transfer: "))
                amountValid = True
            except ValueError as e:
                print(
                    'Value Error - Withdraw amount must be a whole number or decimal number. Please try again.')

        if(sender.withdraw(amount) == True):
            recipient.deposit(amount)
            print("Transfer successful", sender.accountNumber, "-", sender.forename,
                  sender.surname, "sent", amount, "to", recipient.accountNumber, "-", recipient.forename,
                  recipient.surname)
        else:
            print("Transfer failed for", sender.accountNumber, "-", sender.forename,
                  sender.surname, "sending", amount, "to", recipient.accountNumber, "-", recipient.forename,
                  recipient.surname)
            print("For more information on the failed transfer, see the \'Withdrawal Unsuccessful\' print statement above.")
