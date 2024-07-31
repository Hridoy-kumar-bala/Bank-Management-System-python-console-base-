class Account:
    account_number =100
    account_Type = {
        'savings','current'
    }


    def __init__(self,name, email, address,account_Type) -> None:
        if account_Type not in Account.account_Type:
            raise ValueError(f"Invalid account type. Choose from {Account.account_Type}")
        self.account_number =Account.account_number+1
        self.name = name
        self.email =email
        self.address = address
        self.account_Type =account_Type
        self.balance =0
        # self.loans = 0
        self.loans=0
        self.transactions =[]
        

    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
            self.transactions.append(
                {
                    'type': 'Deposit',
                    'amount':amount,
                    'balance': self.balance
                }
            )
            return f"{amount} deposited successful. New balance: {self.balance}"
        else:
            return f"Deposit amount must be positive."

    def withdraw(self,amount):    
        if amount<=0:
            return f"Withdrawal amount must be positive"
        elif amount>self.balance:
            return f"Withdrawal amount exceeded"
        else:
            self.balance -=amount
            self.transactions.append({
                'type': 'Withdrawal',
                'amount': amount,
                'balance': self.balance
            })

            return f"{amount} withdraw successfully.new balance is {self.balance}"


    def available_balance(self):
        return self.balance
    def transaction_history(self):
        if self.transactions:
            history =""
            for transaction in self.transactions:
                history += f"{transaction['type']}: {transaction['amount']}, Balance after transaction: {transaction['balance']}\n"
            return history
        else:
            return f"No transactions recorded"
        # return self.transactions


    def take_loan(self, amount):
        if self.loans < 2:
            # self.loan += amount
            self.balance += amount
            self.transactions.append({
                'type': 'Loan',
                'amount': amount,
                'balance': self.balance
            })
            # self.transactions.append(f"Loan taken {amount}")
            self.loans += 1
            return f"Loan of {amount} taken successfully.New balance {self.balance}"
        else:
            return f"Loan limit reached"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts[account.account_number] = account
        return account.account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return f"Account {account_number} deleted."
        return f"Account does not exist."


    def user_accounts (self):
        return [account.account_number for account in self.accounts.values()]

    def total_balance(self):
        return sum(account.balance for account in self.accounts.values())


    # def total_loan_amount(self):
    #     if not self.loan_feature:
    #         return f"Loan feature is turned off."
    #     total_loan_amount = 0
    #     for account in self.accounts.values():
    #         for loans in account.loans:
    #             total_loan_amount += loans
    #     return f"your total loan amount is {total_loan_amount}"
    def total_loan_amount(self):
        if not self.loan_feature:
            return "Loan feature is turned off."
    
        total_loan_amount = 0
        for account in self.accounts.values():
            # total_loan_amount += sum(account.loans)
            total_loan_amount = sum(account.balance - account.transactions[0]['balance'] for account in self.accounts.values() if account.loans > 0)
    
        return f"Your total loan amount is {total_loan_amount}."


    def set_loan_feature(self, status):
        self.loan_feature = status
        if self.loan_feature:
            return "Loan enabled."
        else:
            return "Loan disabled."


    def transfer_amount(self, from_account, to_account, amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            return "Account does not exist."
        if self.accounts[from_account].balance < amount:
            return "Insufficient funds."
        self.accounts[from_account].balance -= amount
        self.accounts[to_account].balance += amount
        self.accounts[from_account].transactions.append(f"Transferred {amount} to {to_account}")
        self.accounts[to_account].transactions.append(f"Received {amount} from {from_account}")
        return f"Transferred {amount} from {from_account} to {to_account}."
