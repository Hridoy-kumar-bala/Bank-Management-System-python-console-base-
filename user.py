
class User:
    def __init__(self, bank):
        self.bank = bank
        
    def create_account(self, name, email, address, account_type):
        return self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        if account_number in self.bank.accounts:
            return self.bank.accounts[account_number].deposit(amount)
        return "Account does not exist."


    def withdraw(self, account_number, amount):
        if account_number in self.bank.accounts:    
            return self.bank.accounts[account_number].withdraw(amount)
        return "Account does not exist."

    def available_balance(self, account_number):
        if account_number in self.bank.accounts:
            return self.bank.accounts[account_number].available_balance()
        return "Account does not exist."

    def transaction_history(self, account_number):
        if account_number in self.bank.accounts:
            return self.bank.accounts[account_number].transaction_history()
        return "Account does not exist."

    def take_loan(self, account_number,amount):
        if account_number in self.bank.accounts:
            # if amount>0 and amount<=self.bank.accounts[account_number].balance:
            #     self.bank.accounts[account_number].balance+=amount
            return self.bank.accounts[account_number].take_loan(amount)
        return "Account does not exist."

    def transfer_amount(self, from_account, to_account, amount):
        return self.bank.transfer_amount(from_account, to_account, amount)

    def __repr__(self) -> str:
        return f"Account Number: {self.account_number}\n Name:{self.name}\n Email: {self.email}\n Address: {self.address}\n Account Type Name: {self.account_Type} Balance:{self.balance}"
    
