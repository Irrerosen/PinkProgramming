hobbies =[]
collecthobby = True
while collecthobby == True:
    hobbyinput=input("What do you like to do? Write stop to stop listing hobbies ")
    if hobbyinput == "stop":
        collecthobby = False
    else:
        hobbies.append(hobbyinput)
        collecthobby = True
output = ", ".join(hobbies)
print("Okay your hobbies are {}!".format(output))