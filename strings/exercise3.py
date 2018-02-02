# Exercise 5: Take the following Python code that stores a string:‘
# str = ’X-DSPAM-Confidence:0.8475’
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.

word='X-DSPAM-Confidence:0.8475'
pos1=word.find(":")
decimal=word[pos1+1:]
decimal=float(decimal)
print(decimal)
print(type(decimal))
