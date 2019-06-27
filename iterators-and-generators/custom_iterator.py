

class Counter:
    def __init__(self, low, high):
        self._current = low
        self._high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._high:
            num = self._current
            self._current += 1
            return num
        raise StopIteration


new_counter = Counter(3, 10)
for x in new_counter:
    print(x)
# for x in Counter(50, 70):
#     print(x)
