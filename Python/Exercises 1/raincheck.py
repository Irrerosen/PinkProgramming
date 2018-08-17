info=False
while info == False:
    raininfo=input("Is it raining (y/n)?")
    if raininfo=="y":
        raining=True
        print("Bring your umbrella!")
        info=True
    elif raininfo=="n":
        raining=False
        print("Fingers crossed for sun all day!")
        info=True
    else:
        print("please answer the question with y/n")
        info=False

print("Have a nice day")
print("Raining value is {}".format(raining))
quit()