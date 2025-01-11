import datetime

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.add_transaction(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")
        return self.balance

    def add_transaction(self, description):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {description}")

    def print_statement(self):
        print(f"Transaction Statement for Account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)

# Step 2: Define the Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_holder):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, account_holder)
        self.accounts[account_number] = new_account
        print(f"Account created successfully! Account Number: {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred ${amount} from Account {sender_account_number} to Account {receiver_account_number}.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Invalid account number(s).")

    def admin_check_total_deposit(self):
        total_deposit = sum(account.balance for account in self.accounts.values())
        print(f"Total Deposits in the Bank: ${total_deposit}")
        return total_deposit

    def admin_check_total_accounts(self):
        total_accounts = len(self.accounts)
        print(f"Total Number of Accounts: {total_accounts}")
        return total_accounts

# Step 3: Create a Menu-Driven Interface
def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Open a New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. View Transaction Statement")
        print("7. Admin: View Total Deposits")
        print("8. Admin: View Total Accounts")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter the account holder's name: ")
            bank.open_account(account_holder)
        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = int(input("Enter your account number: "))
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found.")
        elif choice == "5":
            sender_account_number = int(input("Enter your account number: "))
            receiver_account_number = int(input("Enter the receiver's account number: "))
            amount = float(input("Enter the amount to transfer: "))
            bank.transfer(sender_account_number, receiver_account_number, amount)
        elif choice == "6":
            account_number = int(input("Enter your account number: "))
            account = bank.get_account(account_number)
            if account:
                account.print_statement()
            else:
                print("Account not found.")
        elif choice == "7":
            bank.admin_check_total_deposit()
        elif choice == "8":
            bank.admin_check_total_accounts()
        elif choice == "9":
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
