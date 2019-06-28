# Write a function calles yes_or_no which return a generator that first yields yes, then no then yes then no and so on


def yes_or_no():
    answer = 'yes'
    while True:
        if answer == 'yes':
            answer = 'no'
            yield 'yes'
        else:
            answer = 'yes'
            yield 'no'


gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

