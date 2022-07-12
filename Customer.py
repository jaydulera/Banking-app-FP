import Bank
import Account

class Customer:

    _customerID = -1
    listOfCustomers = []

    def __init__(self , customerID , firstName , lastName , accounts , totalBalance):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.accounts = accounts
        self.totalBalance = totalBalance

    def getTotalBalance(self):
        if len(self.accounts) == 0:
            return 0
        balance = 0
        for account in self.accounts:
            balance += account.balance
        return balance

    @staticmethod
    def createCustomer(firstName , lastName):
        Customer._customerID += 1
        customer = Customer(Customer._customerID , firstName , lastName , [] , getTotalBalance())
        Customer.listOfCustomers.append(customer)
        return customer
    
    def createAccount(self , fullName , bankAbbreviation):
        account = Account.createAccount(fullName , bankAbbreviation)
        if account:
            print("Account successfully created")
            self.accounts.append(account)

    def findAccount(self , accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                return account

    def deposit(self , amount , accountNumber):
        Account.credit(amount , accountNumber)
    
    def withraw(self , amount , accountNumber):
        Account.debit(amount , accountNumber)

    @staticmethod
    def transfer(amount , recepientNumber , benefactorNumber):
        if Account.findAccount(recepientNumber):
            if Account.debit(amount , benefactorNumber):
                Account.credit(amount , recepientNumber)

    def getBalance(self , accountNumber):
        account = findAccount(accountNumber)
        if not account:
            print("Account does not exist")
        else:
            return account.balance




    



