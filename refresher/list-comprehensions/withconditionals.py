numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]


print(f'Odd numbers were {odds}')
print(f'Even numbers were {evens}')

# if we want the conditional to have an if

multiply = [num*2 if num % 2 == 0 else num/2 for num in numbers]
multiply.sort()
print(multiply)


#

with_vowels = 'This is so much fun'

without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)
