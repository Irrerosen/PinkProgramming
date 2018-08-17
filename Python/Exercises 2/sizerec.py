Usersays=input("Say something ")

string=""
def swapper(string,Usersays):
    if Usersays=="":
        print(string.upper())
    else:
        string += Usersays[-1:]
        Usersays = Usersays[:-1]
        swapper(string,Usersays)
swapper(string,Usersays)


