#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range, print an error message. If the score is between 0.0 and 1.0,
#print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

score=input("Please insert you agregate score(should be between 0.0 and 1.0): ")
try:
    score=float(score)
    if score < 0 or score > 1.0:
        print("I thought I told you to enter a score between 0.0 and 1.0, now look what you made me do")
    elif score >= 0.9:
        print("You have an A grade, congrats, you're certified clever")
    elif score >= 0.8:
        print("You have a B grade, not bad")
    elif score >= 0.7:
        print("You have a C grade, mediocre")
    elif score >= 0.6:
        print("You have a D grade, maybe its time to evaluate your life choices")
    elif score < 0.6:
        print("You have an F grade, books are not for you, have you ever tried plying a career in matress testing?")
except:
    print("Why are you inputing characters inspite of the clear instructions to the contrary? tusisumbuane")
    