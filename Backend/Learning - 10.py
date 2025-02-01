class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.statements = []
        self.statements.append(f"Account created for {owner} with balance ${balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.statements.append(f"Deposited: ${amount}, New Balance: ${self.balance}")
            return f"${amount} deposited successfully."
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.statements.append(f"Withdrawn: ${amount}, New Balance: ${self.balance}")
            return f"${amount} withdrawn successfully."
        return "Insufficient funds or invalid amount."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_statements(self):
        return "\n".join(self.statements)


# Example usage
account = BankAccount("123456", "Orzubek Kamariddinov", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print("\nStatements:\n", account.get_statements())
