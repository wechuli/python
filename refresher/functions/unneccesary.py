def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count


print(count_dollar_signs('3d $ddd$$$ kdl'))
