temp_f=input("Please enter the temprature in fahrenheigt")
try:
    temp_f=float(temp_f)
    temp_c=(temp_f-32)*5/9
    print("The temprature is",temp_c,"in degrees celcius")
except:
    print("Enter a number, now look what you caused to happen")
    