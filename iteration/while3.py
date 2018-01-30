while True:
    a=input(">>Please enter a string, I will echo whatever to write, if you start with #, I will ignore it, press done to exit: ")
    if a[0] == "#":
        continue
    if a=="done":
        break
    print(a)
print(">>All done, I see you stopped playing games")