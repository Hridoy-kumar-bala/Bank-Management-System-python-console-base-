from user import User
from admin import Admin
from account import Account,Bank

bank =Bank()
admin =Admin(bank)
user = User(bank)


def user_operation():
    print("USER OPERATION:\n")
    print("1. CREATE ACCOUNT.")
    print("2. Deposit Balance")
    print("3.Withdraw Balance")
    print("4. Check balance")
    print("5. Take loan")
    print("6. Transaction history\n")
    # print("7. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("CREATE AN ACCOUNT:\n")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter account type (savings/checking): ")
        account_number = user.create_account(name,email,address,account_type)
        print("\nAccount create: ",account_number)
    elif choice ==2:
        print("Deposit Balance:\n")
        account_number = input("Enter your account number:")
        amount =float(input("Enter your amount:"))
        print(user.deposit(account_number, amount))

    elif choice ==3:
        print("Withdraw Balance:\n")
        account_number = input("Enter your account number:")
        amount =float(input("Enter your amount:"))
        print(user.withdraw(account_number, amount))
    elif choice ==4:
        print("Check balance:\n")
        account_number = input("Enter your account number:")
        print(user.available_balance(account_number))
    elif choice ==5:
        print("Take loan:\n")
        account_number = input("Enter your account number:")
        amount =float(input("Enter your amount:"))
        print(user.take_loan(account_number,amount))
    
    elif choice == 6:
        print("Transaction history:\n")
        account_number = input("Enter your account number:")
        print(user.transaction_history(account_number))
    else:
        print("Invalid choice")

def admin_panel():
    print("Admin Panel:")
    print("1.User accounts")
    print("2.Total balance")
    print("3.Total loan amount")
    print("4.Enable/disable loan feature")
    print("5.Delete account\n")


    choice = input("Choose an operation: ")

    if choice == '1':
        print(admin.user_accounts())
    elif choice == '2':
        print(admin.total_balance())
    elif choice == '3':
        print(admin.total_loan_amount())
    elif choice == '4':
        status = input("Enable loan feature(True/False): ")
        print(admin.set_loan_feature(status))
    elif choice == '5':
        account_number = input("Enter account number to delete: ")
        print(admin.delete_account(account_number))
    else:
        print("Invalid choice")

while(True):
    print("Main Menu:")
    print("1. User Operation")
    print("2. Admin panel")
    print("3. Exit\n")
    main_choice = input("Choose option: ")

    if main_choice == '1':
        user_operation()
    elif main_choice == '2':
        admin_panel()
    elif main_choice == '3':
        break
    else:
        print("Invalid choice")



# account_number = user.create_account("Hridoy", "hridoykumarbala@gmail.com", "Khulna", "savings")
# print("Account created:", account_number)
# print(user.available_balance(account_number))
# print(user.deposit(account_number, 1000))
# print(user.available_balance(account_number))
# print(user.withdraw(account_number, 500))
# print(user.available_balance(account_number))
# print(user.take_loan(account_number, 400))
# print(user.available_balance(account_number))
# print(user.transaction_history(account_number))


# print("NOW SHOW ADMIN PANEL\n")
# print(admin.user_accounts())
# print(admin.total_balance())
# print(admin.total_loan_amount())
# print(admin.set_loan_feature(False))
# print(admin.delete_account(account_number))
# print(admin.user_accounts())
# print(admin.set_loan_feature(True))
