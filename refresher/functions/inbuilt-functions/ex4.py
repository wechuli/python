

def interleave(first, second):
    interstring = ''.join([''.join(inet) for inet in zip(first, second)])
    return interstring


print(interleave('hi', 'no'))
print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))
print(interleave('lzr', 'iad'))
