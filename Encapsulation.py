class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance or invalid amount.")
    
    def get_balance(self):
        return self.__balance

# Demonstration
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print("Balance:", account.get_balance())