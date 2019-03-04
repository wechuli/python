
answer = [number for number in range(1, 101) if number % 12 == 0]
print(answer)

mystring = "amazing"

consonants = [cons for cons in mystring if cons not in [
    'a', 'e', 'i', 'o', 'u']]
print(consonants)