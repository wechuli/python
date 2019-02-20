numbers = [1, 2, 3, 4, 5, 6]
grocery = ['vegetable', 'carrot', 'tomato', 'beans', 'sauce']

for i in numbers:
    print(f'Number {i}')

i = 0
while i < len(grocery):
    print(f'{i+1}.{grocery[i]}') #We use a while loop if we need the index for something
    i+=1
