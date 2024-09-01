class PaymentProcessor:
    def __init__(self, balance):
        self.balance = balance

    def make_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"To'lov muvaffaqiyatli amalga oshirildi. Qolgan balans: {self.balance} so'm.")
        else:
            print("Balansingiz yetarli emas!")

# Foydalanuvchi balansi
my_balance = 100000  # 100 000 so'm

# To'lov miqdori
payment_amount = 25000  # 25 000 so'm

# To'lov jarayoni
processor = PaymentProcessor(my_balance)
processor.make_payment(payment_amount)
