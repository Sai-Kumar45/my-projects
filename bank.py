import random

print("*********** Welcome to Local Bank ***********")

class CreateAccount():
    def __init__(self, name, age, mobile_number, address, balance, pin):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.address = address
        self.balance = balance
        self.pin = pin

    def check_balance(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def mini_statement(self):
        return f"Name: {self.name}, Balance: {self.balance}"

# List to store accounts
accounts = []

while True:
    print("1. Create Account \n2. Check Balance \n3. Deposit \n4. Withdrawal\n5. Mini Statement\n6. Exit")

    choice = int(input("Enter your option: "))

    if choice == 1:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        mobile_number = input("Enter your mobile number: ")
        address = input("Enter your address: ")
        balance = 500

        # Generate a unique PIN
        while True:
            pin = random.randint(1000, 9999)
            pin_exists = any(account.pin == pin for account in accounts)
            if not pin_exists:
                break

        accounts.append(CreateAccount(name, age, mobile_number, address, balance, pin))
        print("************************ <o o> *******************")
        print(f"Hello {name}, your account has been created successfully!")
        print(f"Your security pin is {pin} \nUse the same pin for further transactions")

    elif choice == 2:
        entered_pin = int(input("Enter your pin: "))
        found = False

        for account in accounts:
            if account.check_balance(entered_pin):
                print(f"Your balance is: {account.balance}")
                found = True
                break

        if not found:
            print("Invalid pin or account not found.")

    elif choice == 3:
        entered_pin = int(input("Enter your pin: "))
        found = False

        for account in accounts:
            if account.check_balance(entered_pin):
                amount = float(input("Enter your deposit amount: "))
                account.deposit(amount)
                print(f"Your current balance is: {account.balance}")
                found = True
                break

        if not found:
            print("Invalid pin or account not found.")

    elif choice == 4:
        entered_pin = int(input("Enter your pin: "))
        found = False

        for account in accounts:
            if account.check_balance(entered_pin):
                amount = float(input("Enter your withdrawal amount: "))
                if account.withdraw(amount):
                    print(f"Withdrawal of {amount} successful. Your current balance is: {account.balance}")
                else:
                    print("Insufficient balance for withdrawal.")
                found = True
                break

        if not found:
            print("Invalid pin or account not found.")

    elif choice == 5:
        entered_pin = int(input("Enter your pin: "))
        found = False

        for account in accounts:
            if account.check_balance(entered_pin):
                print(account.mini_statement())
                found = True
                break

        if not found:
            print("Invalid pin or account not found.")

    elif choice == 6:
        print("Thank you for using Local Bank. Visit again")
        break

    else:
        print("Invalid choice. Please select a valid option.")
