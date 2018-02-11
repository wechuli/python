my_fall="She is the most beatiful thing I have ever seen in this short life of mine"
words=my_fall.split()
my_one=list()
for word in words:
    my_one.append((len(word),word))

my_one.sort(reverse=True)
my_two=list()
for length,wordy in my_one:
    my_two.append(wordy)

print(my_two)


