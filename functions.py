from data import accounts

def create_account():
    print("Thanks for creating an account")
    account_name = input("Enter your name: ")
    account_password = input("Enter your password: ")
    account_balance = float(input("Enter your balance: "))

    new_account = {
        "name": account_name,
        "password": account_password,
        "balance": account_balance
    }

    accounts.append(new_account)

if __name__ == "__main__":
    create_account()



