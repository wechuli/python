vowels = 'eauoi'

answer = {vowels[pos]: pos for pos in range(0, len(vowels))}
print(answer)

answer2 = {vowel: 0 for vowel in ''.join(sorted(vowels))}
print(answer2)
