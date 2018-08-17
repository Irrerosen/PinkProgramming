def daystoseconds(days):
    seconds=days*60*60*24
    return seconds


inputdays=int(input("Please input amount of days: "))
outputseconds=daystoseconds(inputdays)
print("That is {} seconds.".format(outputseconds))