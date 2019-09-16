class BankAccount:
    def __init__(self, owner):
        self._owner = owner
        self._balance = 0.

    def deposit(self, amount):
        if not isinstance(amount, (float, int)):
            raise TypeError('Please enter a number')
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if not isinstance(amount, (float, int)):
            raise TypeError('Please enter a number')
        if self._balance - amount < 0:
            return "Insufficient balance"
        self._balance -= amount
        return self._balance

    def get_balance(self):
        return self._balance


my_fat_account = BankAccount('Paul')
balance = my_fat_account.deposit(20)
print(my_fat_account)
balance = my_fat_account.withdraw(30)
print(balance)
print(my_fat_account.get_balance())
balance = my_fat_account.withdraw(3)
print(my_fat_account.get_balance())
