
days = {
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thurday": 5,
    "Friday": 6,
    "Saturday": 7
}


def return_day(day):
    for key, value in days.items():
        if day == value:
            return key
    return 'None'


print(return_day(0))
