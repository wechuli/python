#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range, print an error message. If the score is between 0.0 and 1.0,
#print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

error="Bad Score"

score=input("Please enter your score, should be between 0.0 and 1.0: ")
try:
    score=float(score)
except:
    print("Bad Score")
def calc_grade(a):
    if a>=0.0 and a <=1.0:
        if a >= 0.9:
            print("A")
        elif a >=0.8:
            print("B")
        elif a >=0.7:
            print("C")
        elif a >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Bad Score")

try:
    calc_grade(score)
except:
    pass