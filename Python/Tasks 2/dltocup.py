print("This program converts deciliters to cups")
deci_amount=int(input("please input amount of dl: "))

def dl_cup(dl):
    cups=round(dl/2.37, 2)
    return cups

cup_amount=dl_cup(deci_amount)
print("Amount of cups: {}".format(cup_amount))
