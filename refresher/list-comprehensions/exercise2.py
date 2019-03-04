list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

answer = [inter for inter in list1 if inter in list2]
print(answer)

names = ['Elie','Tim','Matt']
answer2 = [rev.lower()[-1::-1] for rev in names]
print(answer2)
