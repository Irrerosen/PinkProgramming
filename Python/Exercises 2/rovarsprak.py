def rovarsprak(string,newstring):
    if string == "":
        print(newstring)
    elif string[0] in ("a", "e", "i", "o", "u", "y", "å", "ä", "ö"):
        newstring+=string[0]
        string=string[1:]
        rovarsprak(string,newstring)
    else:
        newstring+=string[0]+"o"+string[0].lower()
        string=string[1:]
        rovarsprak(string,newstring)


string=""
newstring=""
string=input("Say a word ")
rovarsprak(string,newstring)