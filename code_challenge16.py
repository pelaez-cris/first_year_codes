def breakdown_denomination(amount):
    print("Denomination Breakdown:")
    denominations = (1000, 500, 200, 100, 50, 20, 10, 5, 1)
    for denom in denominations:
        if amount >= denom:
            count = amount // denom
            print("PHP", denom, ":", count)
            amount = amount % denom


def create_account():
    account_name = input("Enter your name: ")
    initial_deposit = eval(input("Enter initial deposit: "))
    if initial_deposit >= 0:
        print("Account created for", account_name, "with balance PHP", initial_deposit)
        return account_name, initial_deposit
    else:
        print("Initial deposit must be 0 or more.")
        return None, 0


def deposit(account_name, account_balance):
    if account_name == None:  
        print("No account found. Please create an account first.")
    else:
        amount = eval(input("Enter amount to deposit: "))
        if amount > 0:
            account_balance += amount
            print("Deposited PHP", amount, ". Current balance: PHP", account_balance)
            breakdown_denomination(amount)
        else:
            print("Deposit amount must be greater than 0.")
    return account_balance


def withdraw(account_name, account_balance):
    if account_name == None:
        print("No account found. Please create an account first.")
    else:
        amount = eval(input("Enter amount to withdraw: "))
        if amount > account_balance:
            print("Insufficient balance!")
        elif amount > 0:
            account_balance -= amount
            print("Withdrew PHP", amount, ". Current balance: PHP", account_balance)
        else:
            print("Withdrawal amount must be greater than 0.")
    return account_balance


def check_balance(account_name, account_balance):
    if account_name == None:
        print("No account found. Please create an account first.")
    else:
        print("Your current balance is PHP", account_balance)


def main():
    account_name = None
    account_balance = 0

    while True:
        print("\n=== Welcome to J-Bank ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            account_name, account_balance = create_account()
        elif choice == "2":
            account_balance = deposit(account_name, account_balance)
        elif choice == "3":
            account_balance = withdraw(account_name, account_balance)
        elif choice == "4":
            check_balance(account_name, account_balance)
        elif choice == "5":
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid option. Please try again.")

main()
