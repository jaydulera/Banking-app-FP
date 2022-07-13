
import Bank

class Account:

    _accountNumber = -1
    listOfAccounts = []

    def __init__(self , accountNumber , bank , balance):
        self.accountNumber = accountNumber
        self.bank = bank
        self.balance = balance

    @staticmethod
    def createAccount(fullName , bankAbbreviation):
        """Returns newly created account object"""
        isBankExist , bank = Bank.findBank(fullName , bankAbbreviation)
        if not isBankExist:
            print("Bank does not Exist")
            return None
        Account._accountNumber += 1
        account = Account(Account._accountNumber , bank , 1000)
        Account.listOfAccounts.append(account)
        return account

    @staticmethod
    """Returns required account object"""
    def findAccount(accountNumber):
        for account in Account.listOfAccounts:
            if account.accountNumber == accountNumber:
                return True , account
        return False , None

    @staticmethod
    def getBalance(accountNumber):
        """Returns most recently updated balance of required account"""
        isAccountExist , account = findAccount(accountNumber)
        if not isAccountExist:
            print("Account does not exist.")
        else:
            return account.balance

    @staticmethod
    def credit(amount , accountNumber):
        """Credits required amount to said account"""
        isAccountExist , account = findAccount(accountNumber)
        if not isAccountExist:
            print("Account does not exist")
            return False
        else:
            account.balance += amount
            return True
            
    @staticmethod
    def debit(amount , accountNumber):
        """Debits required amount from said account"""
        isAccountExist , account = findAccount(accountNumber)
        if not isAccountExist:
            print("Account does not exist")
            return False
        else:
            if account.balance < amount:
                print("Insufficient funds")
                return False
            else:
                account.balance -= amount
                return True
            
