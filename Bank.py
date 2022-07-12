
class Bank:

    _bankID = -1
    listOfBanks = []

    def __init__(self , bankID , fullName, bankAbbreviation):
        self.bankID = bankID
        self.fullName = fullName
        self.bankAbbreviation = bankAbbreviation
    
    @staticmethod
    def createBank(fullName , bankAbbreviation):
        Bank._BankID += 1
        bank = Bank(Bank._BankID , fullName , bankAbbreviation)
        Bank.listOfBanks.append(bank)
        return bank

    @staticmethod
    def findBank(fullName , bankAbbreviation):
        for bank in Bank.listOfBanks:
            if bank.fullName == fullName and bank.bankAbbreviation == bankAbbreviation:
                return True , bank
        return False , None

