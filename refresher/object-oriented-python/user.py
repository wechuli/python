class ShoppingCart:
    def __init__(self):
        self._total = 0
        self._cart = {}

    def add(self, product, quantity, price):
        if not self._cart.get(product):
            self._cart[product] = quantity
        else:
            for key in self._cart:
                if product == key:
                    self._cart[key] += quantity
                    break
                else:
                    self._cart[product] = quantity
        total = quantity * price
        self._total += total

    def view(self):
        return [self._total, self._cart]


my_cart = ShoppingCart()
my_cart.add('Mango', 45, 20)
my_cart.add('Mango', 45, 20)
my_cart.add('Avacado', 4, 20)
print(my_cart.view())
