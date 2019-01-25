# ask for age
# 18-21 wristband
# 21+ drink, normal enrty
# too young,sorry

age_raw = input('How old are you: ')
try:
    age = int(age_raw)
except:
    print('Please provide a valid age')
    exit()

if age >= 18 and age < 21:
    print('You can enter, but need a wristband!')
elif age >= 21:
    print('You are good to enter and you can drink')
else:
    print("You can't come in little one")
