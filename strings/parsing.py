mystr="Please email me at wechulipaul@outlook.com to find out more"
pos1=mystr.find('@')
pos2=mystr.find(' ',pos1)

print(pos1)
print(pos2)

web=mystr[pos1+1:pos2]
print(web)
