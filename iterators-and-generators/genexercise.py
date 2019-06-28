# Write a function called make_song which takes a count and a beverage and returns a generator that yields verses from a popular song about the bevarage . The number of verses in the son is determined by the count. Each verse of the song should involve one fewer beverage, until there are no beverages remaining.


def make_song(count, beverage):
    iterations = count
    while iterations > 0:
        if(iterations == 0):
            yield f'No more {beverage}!'
        if(iterations == 1):
            yield f'Only 1 bottle of {beverage} left!'
        yield f'{iterations} bottles of {beverage} on the wall.'
        iterations -= 1


song = make_song(10, "Tusker")
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
