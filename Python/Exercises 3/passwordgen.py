#
# Import needed modules
#

import csv
import random

#
# Open files with nouns and adjectives
#

noun_file = open('noun.csv', newline='')
adj_file = open('adjectives.csv', newline='')

#
# Create list of punctuations to pick from
#

punctuation = ['.','.',':','!','?',';','#','$','(',')','[',']','>','<','*']


#
# Read files with nouns and adjectives
#

nouns = csv.reader(open('noun.csv', 'r'))
adjective = csv.reader(open('adjectives.csv', 'r'))

#
# Flatten data, is csv with one column, want with one row
#

datan = sum([i for i in nouns],[]) #To flatten the list
dataa = sum([i for i in adjective],[]) #To flatten the list

password = False
while password == False:
    #
    # Use random.choice to pick a word from the lists
    #

    randomnoun=(random.choice(datan))
    randomadj=(random.choice(dataa))

    #
    # Use randint to pick index of punctuation and random number between 0 and 100
    #

    puncnumber=random.randint(0,len(punctuation)-1)
    number=random.randint(0,100)
    punctuate=(punctuation[puncnumber])

    #
    # Turn number into string, to enable it being combined with other parts
    #

    textnumber=str(number)

    #
    # Capitalize the noun, increasing safety of password
    #

    noun=randomnoun.upper()

    #
    # Create unmixed password
    #

    unmixed=randomadj+textnumber+noun+punctuate

    #
    # Transform the unmixed password into a list to make use of the random.shuffle function
    #

    pwlist = list(unmixed)
    random.shuffle(pwlist)

    #
    # Recreate a password from the mixed list
    #

    mixed="".join(pwlist)

    #
    # print password for user
    #

    print("\n"+mixed+"\n")

    answer = True
    while answer == True:
        question=input("Are you happy with this password? (y/n) ")
        if question == "y":
            print("Great, stay safe in the digital world!")
            password = True
        elif question == "n":
            print("Okay, we'll start over")
            answer = False
        else:
            print("We can only understand y/n answers!!")
            answer = True




