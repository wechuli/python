#The following program counts the number of times the letter a appears in a string:
#Encapsulate this code in a function named count, and generalize it so that it
#accepts the string and the letter as arguments.

def count(whole="strinig",letter="i"):
    counter=0
    for a in whole:
        if letter==a:
            counter=counter+1
    print("The number of",letter,"in your string is",counter)

user_str=input("Please enter your string: ")
user_lett=input("Please enter the letter you want to get count of")
    
count(user_str,user_lett)


