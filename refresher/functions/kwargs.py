# **kwargs , gathers remaining keyword arguments as a dictionary


def fav_colors(number, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")


fav_colors(1, paul='beige', june='blue', christie='black', caro='orange')
