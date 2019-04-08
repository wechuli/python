
def speak_pg():
    return 'oink'

print(speak_pg())


def generate_evens(start, finish):
    try:
        start = int(start)
        finish = int(finish)
    except:
        print('You have entered an invalid choice')
        exit()

    evens = [number for number in range(start, finish) if number % 2 == 0]

    return evens


returned_evens = generate_evens(56, 100)
print(returned_evens)
