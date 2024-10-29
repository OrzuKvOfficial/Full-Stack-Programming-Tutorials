class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} qo'shildi. Joriy balans: ${self.balance}")
        else:
            print("Miqdorni to'g'ri kiriting.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} yechildi. Joriy balans: ${self.balance}")
        else:
            print("Yetarli mablag' mavjud emas yoki noto'g'ri miqdor kiritildi.")

    def check_balance(self):
        print(f"{self.account_name} balansingiz: ${self.balance}")

# Misol
account1 = BankAccount("Orzubek", 100)  # Boshlang'ich balans $100
account1.check_balance()                 # Balansni tekshirish
account1.deposit(50)                     # Balansga $50 qo'shish
account1.withdraw(30)                    # Balansdan $30 yechish
account1.check_balance()                 # Yangi balansni tekshirish
