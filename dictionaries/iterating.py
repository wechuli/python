MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}

for value in MLB_team.values(): # looping through the values
    print(value)
for key in MLB_team.keys(): # looping through the keys
    print(key)

for key, value in MLB_team.items():  #two looping variables
    print(key, value)



# print(MLB_team)
