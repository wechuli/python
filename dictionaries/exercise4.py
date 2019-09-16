inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = {}
stock_list.update(inventory)
stock_list["cookie"] = 18
print(stock_list)

stock_list.pop("cake")

print(stock_list)
