def datacollect(mathmode):
    modus=mathmode
    value1 = input("Please enter the first number of your {} ".format(modus))
    value2 = input("Please enter the second number of the calculation ")
    return value1, value2
def addition(value1,value2):
    added = int(value1) + int(value2)
    return added
def subtraction(value1,value2):
    subtracted = int(value1)-int(value2)
    return subtracted
def multiplication(value1,value2):
    multiplied = int(value1)*int(value2)
    return multiplied
def division(value1,value2):
    divided = int(value1)/int(value2)
    return divided
def printresult(value):
    print("The result of the calculation is {}".format(value))

print("Welcomme to the basic calculator,")
counting = True
while counting == True:
    modus=input("Please input mode of calculation, pick between 'add'(+), 'sub'(-), 'mult'(*), or 'div'(/). To quit input quit ")
    if modus == "add":
        firstvalue,secondvalue = datacollect("addition")
        result=addition(firstvalue,secondvalue)
        printresult(result)
    elif modus == "sub":
        firstvalue,secondvalue = datacollect("subtraction")
        result=subtraction(firstvalue,secondvalue)
        printresult(result)
    elif modus == "mult":
        firstvalue,secondvalue = datacollect("multiplication")
        result=multiplication(firstvalue,secondvalue)
        printresult(result)
    elif modus == "div":
        firstvalue,secondvalue = datacollect("division")
        result=division(firstvalue,secondvalue)
        printresult(result)
    elif modus == "quit":
        counting = False
    else:
        print("You've entered the mode incorrectly, please try again")

print("Thank you for using basic calculator by Hanna Johansson")
quit()