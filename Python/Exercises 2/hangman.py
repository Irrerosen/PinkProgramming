#working
#CLEAN THIS SHIT UP!!!


#
# Needed package - random, to choose randomly from words. Could also import lists of words (csv-files)
# IDEA - enable players to write word to a file after completing a game, adding a new word for next play!
#

import random
#
# Start with a While True to enable playing again - could possible be under the lists of words, as they are not related!
#
while True:
    #
    # List of words, currently long and short - could be changed to different difficulties, and also have categories - such as
    # code, animals, etc.
    #

    wordlong=["hippopotamus", "simulation", "compilator", "programming", "excitement", "daredevil",]
    wordshort=["lucky", "happy", "life", "query", "input", "sing", "html", "code", "python", "java", "coffee"]
    #
    # While for selection of word length. If user does not manage to select will be prompted again until inputing "short" or "long"
    #
    while True:
        select=input("Do you want a long or short word? ")
        if select == "long":
            choice=wordlong
            break
        elif select =="short":
            choice=wordshort
            break
        else:
            print("That is not an option, please select")

    #
    # Time to choose a word from the list, take length of list (-1)<- uncertain, and create a random integer.
    # TODO: use random.choice instead to skip steps
    #

    choicelength=len(choice)
    my_word = random.randint(0, choicelength-1)
    word=choice[my_word]

    #
    # Creating the guessing board, blank is made into a string
    #

    blank=""

    #
    # Possibility remains for user to enter word for a game if uncommented
    #

    #word=input("Enter a word for hangman ")

    #
    # Game generates blank "_ _ _ _" gameboard
    #

    wordlength=len(word)
    for y in range(wordlength):
        blank+="_ "
    blank=blank[:-1]
    word=" ".join(word)
    word+=" "

    #
    # wordref is a containter, towards which blank is checked - it contains the original word
    #

    wordref=word

    #
    # Game begins
    # TODO look into using command for newline instead of *3 print
    #

    print("Time to play hangman!")
    print("")
    print(blank)
    print("")

    #
    # Amount of incorrect guesses is set through count
    # Strings are created to hold incorrect guesses and prior guesses
    #

    count=10
    incorrect_guess=""
    priorguess=""

    #
    # Variable game enables game to stop mid-loop in case user gets word right, or runs out of guesses
    #

    game=True
    while game==True:
        print("You have {} incorrect guesses left".format(count))
        guess=input("Take a guess! ")

        #
        # function to ensure that both .lower and .upper both count
        # TODO swap this to guess=guess.lower() to only need one if-statement
        #

        #guessswap=guess.swapcase()

        #
        # To stop user from losing guesses if guessing already guessed letter
        #

        if guess in priorguess:
            print("You already guessed that! Try again")

        #
        # if the string guess exists in the longer string word:
        #

        elif guess in word:

            #
            # Identifies how many of that character that exists in the word and looping that a mount of times.
            #

            for letter in range(word.count(guess)):

                #
                # TODO consider uses of enumerate here
                # Finding index of letter in the word, and then recreating the blank string, replacing the "_" containing that letter with the letter
                #

                guessindex=word.find(guess)
                blank=blank[:word.index(guess)]+word[word.index(guess)]+" "+blank[word.index(guess)+2:]

                #
                # Swapping the same letter to a "_" in the word string
                #

                word=word[:word.index(guess)]+"_"+word[word.index(guess)+1:]

                #
                # Printing the new gamefield for the user to see.
                #

                print(blank)

                #
                # Wincheck towards wordref - which contains the original word. If match with blank, win and break game loop.
                #

                if blank == wordref:
                    print("You got it!!!")
                    game=False

                #
                # part of field showing incorrect guesses at every round.
                # TODO: Consider if this is at the right tab-level of code, could it be outside?
                #

                print("incorrect:{}".format(incorrect_guess))
            #
            # Add letter to prior guesses, for easier reference by user!
            #


            priorguess+=guess+" "
            print("prior guesses: {}".format(priorguess))

        #
        # While count is larger than 0, user still has more incorrect guesses left, the game goes on, reprint the game board
        #

        elif count>0:
            print("That's incorrect, try again:")
            count-=1
            incorrect_guess+=guess+", "
            priorguess+=guess+" "
            print(blank)
            print("incorrect:{}".format(incorrect_guess))

        #
        # If count reaches 0, game is over, user gets to see word before next option
        #

        else:
            print("Sorry you're out of guesses!")
            print(wordref)
            game = False


    #
    # Replay section
    # reply is set to False, and will change once user gives valid reply.
    #

    reply = False
    while reply == False:
        continueq=input("Do you want to continue?(y/n) ")
        if continueq == "y":
            reply = True
        elif continueq == "n":
            reply = True
            break
        else:
            print("that is not correct input")
            reply = False