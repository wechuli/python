# divisible_by_7 = [num for num in range(1, 10001) if num % 7 == 0]
# print(divisible_by_7)

# have_a_3 = [num for num in range(1, 10001) if '3' in str(num)]
# print(have_a_3)


mystring = "I need to count the number of spaces in this string using list comprehensions, am adding more space jusr to make sure"


number_of_spaces = [1 for num in mystring if num == " "]
print(len(number_of_spaces))
remove_vowels = [letter for letter in mystring if letter not in [
    'a', 'e', 'i', 'o', 'u']]
print(remove_vowels)

less_than_four = [word for word in mystring.split(" ") if len(word) > 4]
print(less_than_four)