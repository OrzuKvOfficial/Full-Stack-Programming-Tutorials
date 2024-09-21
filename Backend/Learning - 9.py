class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")

# Foydalanuvchi uchun hisob yaratish
account_1 = BankAccount("123456789", "Orzubek Kamariddinov", 500)

# Hisobga pul qo'shish
account_1.deposit(200)

# Hisobdan pul yechish
account_1.withdraw(100)

# Balansni tekshirish
account_1.check_balance()
