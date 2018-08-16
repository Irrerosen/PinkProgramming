Usersays=input("Say something ")

string=""
for i in range(len(Usersays),0,-1):
    string+=Usersays[-1:]
    #print(string)
    Usersays=Usersays[:-1]
    #print(Usersays)
print(string.upper())