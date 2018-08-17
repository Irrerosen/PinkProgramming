score = 0
def addtn(value, addition):
    print("Correct! {} points added.".format(addition))
    sum = (value) + (addition)
    score = int(sum)
    print("Your new total score is: {}!".format(score))
    return score
def ohno(value):
    print("Sorry that is incorrect")
    score = (value) - 2
    print("Your total score is: {}!".format(value))
    return score
def Qrepeat(tries, answer):
    repeat = input("Do you want to try again? Please answer yes/no ")
    if repeat == "yes" or repeat.lower() == "yes":
        sum = (tries) + 1
        return False, sum, False
    else:
        sum = (tries)
        print("Ok, the answer to the question was: {}!".format(answer))
        return True, sum, True

print("THE GAME OF THE YEAR")
print("You will get 3 tries on each question, each extra try costs 2 points,")
print("If you get the answer correct on the first try you'll get 10 points, on the second try 8 points and on the third try 6 points")
Q1completion = False
Q2completion = False
Q3completion = False
Q1tries = 1
Q2tries = 1
Q3tries = 1
while Q1completion == False:
    answer = 12
    Q1=input("Q1: How many months are there in a year? ")
    if int(Q1) == 12:
        if Q1tries == 1:
            score = addtn(score, 10)
        elif Q1tries == 2:
            score = addtn(score, 8)
        else:
            score = addtn(score, 6)
        Q1completion = True
    else:
        score = ohno(score)
        Q1completion, Q1tries, Q1giveup = Qrepeat(Q1tries, answer)

while Q2completion == False:
    answer = "march"
    Q2=input("Q2: What is the third month of the year? ")
    if ((Q2 == "march") or (Q2.lower() == "march")):
        score = addone(score)
        Q2completion = True

    else:
        ohno(score)
        Q2completion, Q2tries, Q2giveup = Qrepeat(Q2tries, answer)

print("You completed THE GAME OF THE YEAR!")
print("Your total score was: {}".format(score))
print("For Q1 you tried {} times".format(Q1tries))
print("For Q2 you tried {} times".format(Q2tries))
if Q1giveup == True or Q2giveup == True:
    totalgiveup = sum([Q1giveup, Q2giveup])
    print("You gave up on {} question(s)".format(totalgiveup))