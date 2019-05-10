

def divide(num1, num2):
    try:
        return num1/num2
    except TypeError as error:
        print(error)
        print("Please provide two integers or floats")
    except ZeroDivisionError as error:
        print(error)
        print("Please do not divide by zero")


print(divide(4, 2))
print(divide([], "1"))
print(divide(1, 0))
