days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def week():
    for day in days:
        yield day


myDays = week()
print(next(myDays))
print(next(myDays))
print(next(myDays))
print(next(myDays))
print(next(myDays))
print(next(myDays))
print(next(myDays))