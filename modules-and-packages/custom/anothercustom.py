class Customer:
    def __init__(self, customer, balance):
        self._customer = customer
        self._balance = balance

    def get_balance(self):
        return self._balance

    def get_customer(self):
        return self._customer


class Girl(Customer):
    def private_method(self):
        return "Fake method"
