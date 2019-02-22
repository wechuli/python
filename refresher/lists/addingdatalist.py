skills = ['javascript','python','react','node/express','azure','aws','react-native']

#append method for addding item to the end of a list
print(skills)

skills.append('artificial intelligence') #you cannot append multiple items
print(skills)

#extend -add a list

skills.extend(['data science','elasticsearch','iot'])

print(skills)

#insert - add a specific position

skills.insert(0,'mathematics')
print(skills)