class Owner:
    def __init__(self, balance):
        self.balance = balance
        print(f"Текущий счет: {self.balance} тенге")
        
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть положительной.")
        else:
            self.balance += amount
            print(f"Поступило: {amount} тенге")
            self.display_balance()
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
        elif self.balance < amount:
            print("Недостаточно средств на карте.")
        else:
            self.balance -= amount
            print(f"Вы сняли: {amount} тенге")
            print(f"Текущий счет: {self.balance} тенге")
        
card = Owner(1000)

card.withdraw(900)
