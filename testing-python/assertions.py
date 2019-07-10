
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y


print(add_positive_numbers(1, 2))
add_positive_numbers(1, -34)  # AssertionError: Both numbers must be positive!


def eat_junk(food):
    assert food in ["pizza", "ice cream", "candy",
                    "fried butter"], "food must be a junk food"
    return f'NOM NOM NOM, I am eating {food}'


print(eat_junk("pizza"))
print(eat_junk("ugali"))

