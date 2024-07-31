
from user import User
class Admin(User):
    def __init__(self, bank):
        super().__init__(bank)

    def delete_account(self, account_number):
        return self.bank.delete_account(account_number)

    def user_accounts(self):
        return self.bank.user_accounts()

    def total_balance(self):
        return self.bank.total_balance()

    def total_loan_amount(self):
        return self.bank.total_loan_amount()

    def set_loan_feature(self,status):
        return self.bank.set_loan_feature(status)
