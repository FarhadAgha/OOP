class Bank:
    def __init__(self, balance, bank_name, branch, ifsc_code, account_number, account_holder_name, account_type):
        self.balance = balance
        self.branch = branch
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"Balance: {self.balance}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Branch: {self.branch}")
        print(f"IFSC Code: {self.ifsc_code}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Type: {self.account_type}")

b = Bank(1000, "Askari Bank", "DHA Branch", "ABC12345678", "1234567890", "Farhad Agha", "Savings")
b.deposit(500)
b.show_balance()