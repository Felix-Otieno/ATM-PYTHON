class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"KES {amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"KES {amount} withdrawn successfully.")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Your current balance is: KES {self.balance}")


def main_menu():
    account = None

    while True:
        print("\n==== Welcome to Usiogope ATM ====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Please enter your name: ")
            while True:
                try:
                    initial_balance = float(input("Please enter your initial balance: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the balance.")

            account = Account(name, initial_balance)
            print(f"Account created successfully for {name}!")

        elif choice == '2':
            if account:
                try:
                    deposit_amount = float(input("Enter deposit amount: "))
                    account.deposit(deposit_amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Please create an account first.")

        elif choice == '3':
            if account:
                try:
                    withdraw_amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(withdraw_amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Please create an account first.")

        elif choice == '4':
            if account:
                account.check_balance()
            else:
                print("Please create an account first.")

        elif choice == '5':
            print("Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
