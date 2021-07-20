class Customer:

    next_accountNumber = 87956423

    def __init__(self, forename, surname, ppsn, accountType, overdraft):

        self._accountNumber = Customer.next_accountNumber
        Customer.next_accountNumber = Customer.next_accountNumber + 1

        self._forename = forename
        self._surname = surname
        self._ppsn = ppsn
        self._accountType = accountType
        self._overdraft = overdraft
        if accountType == 'Deposit':
            self._balance = 50.0
        else:
            self._balance = 20.0
        self._interestRate = "2%"

    def __repr__(self):
        repr = f"{str(self.accountNumber).ljust(10)} {self.forename.ljust(11)} {self.surname.ljust(20)} "
        repr = repr + \
            f"{self.ppsn.ljust(11)} {self.accountType.ljust(15)} "
        repr = repr + \
            f"{self.overdraft.ljust(12)} {str(self.balance).ljust(10)} {self.interestRate}"

        return repr

    def file_text(self):
        return f"{self.forename}|{self.surname}|{self.ppsn}|{self.accountType}|{self.overdraft}|{self.balance}|{self.interestRate}"

    def _check_interest_rate(self):
        if self._balance >= 10000:
            self._interestRate = "5%"
        else:
            self._interestRate = "2%"

    def withdraw(self, amount):
        if self._balance <= 0 and self._overdraft == "No":
            print(
                "\n=========================================================================")
            print("Withdrawal Unsuccessful.")
            print("Insufficient funds in account and overdraft is not possible.")
            print(
                "=========================================================================\n")
            return False
        else:
            self._balance -= amount
            print(
                "\n=========================================================================")
            print("Withdrawal Successful!")
            print("The updated balance for account", self._accountNumber, "-", self._forename,
                  self._surname, "is", self._balance, "euro.")
            print(
                "=========================================================================\n")
            self._check_interest_rate()
            return True

    def deposit(self, amount):
        self._balance += amount
        print("\n=========================================================================")
        print("Deposit Successful!")
        print("The updated balance for account", self._accountNumber, "-", self._forename,
              self._surname, "is", self._balance, "euro.")
        print("=========================================================================\n")
        self._check_interest_rate()

    @property
    def accountNumber(self):
        return self._accountNumber

    @property
    def forename(self):
        return self._forename

    @forename.setter
    def forename(self, new_forename):
        self._forename = new_forename

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname

    @property
    def ppsn(self):
        return self._ppsn

    @ppsn.setter
    def ppsn(self, new_ppsn):
        self._ppsn = new_ppsn

    @property
    def accountType(self):
        return self._accountType

    @accountType.setter
    def accountType(self, accountType):
        self.accountType = accountType

    @property
    def overdraft(self):
        return self._overdraft

    @overdraft.setter
    def overdraft(self, new_overdraft):
        self._overdraft = new_overdraft

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance
        self._check_interest_rate()

    @property
    def interestRate(self):
        return self._interestRate

    @interestRate.setter
    def interestRate(self, new_interestRate):
        self._interestRate = new_interestRate
