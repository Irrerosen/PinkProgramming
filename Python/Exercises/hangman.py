import random
wordlong=["hippopotamus", "simulation", "compilator", "programming", "excitement", "daredevil"]
wordshort=["half", "happy", "life", "query", "input", "break"]
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
choicelength=len(choice)
my_word = random.randint(0, choicelength-1)
word=choice[my_word]
blank=""
#word=input("Enter a word for hangman ")
wordlength=len(word)
for y in range(wordlength):
    blank+="_ "
blank=blank[:-1]
word=" ".join(word)
word+=" "
#print(word)
#print(blank)
wordref=word
#word="p i n k "
#blank="_ _ _ _"


#print('\n'*20)


print("Time to play hangman!")
print("")
print(blank)
print("")

count=3
incorrect_guess=""
priorguess=""
game=True
while game==True:
    print("You have {} incorrect guesses left".format(count))
    guess=input("Take a guess! ")
    guessswap=guess.swapcase()
    if guess in priorguess:
        print("You already guessed that! Try again")
    elif guess in word:
        for letter in range(word.count(guess)):
            guessindex=word.find(guess)
            print((guessindex/2)+1)
            #guessspot=int(guessindex)
            blank=blank[:word.index(guess)]+word[word.index(guess)]+" "+blank[word.index(guess)+2:]
            word=word[:word.index(guess)]+"_"+word[word.index(guess)+1:]
            print(blank)
            #print(word)
            if blank == wordref:
                print("You got it!!!")
                game=False

            print("incorrect:{}".format(incorrect_guess))
        priorguess+=guess+" "
        print("prior guesses: {}".format(priorguess))
    elif guessswap in wordref:
        guess=guessswap
        for letter in range(word.count(guess)):
            guessindex = word.find(guess)
            print((guessindex / 2) + 1)
            # guessspot=int(guessindex)
            blank = blank[:word.index(guess)] + word[word.index(guess)] + " " + blank[word.index(guess) + 2:]
            word = word[:word.index(guess)] + "_" + word[word.index(guess) + 1:]
            print(blank)
            #print(word)
            if blank == wordref:
                print("You got it!!!")
                game = False

            print("incorrect:{}".format(incorrect_guess))
        priorguess += guess + " "
        print("prior guesses: {}".format(priorguess))
    elif count>=0:
        print("That's incorrect, try again:")
        count-=1
        incorrect_guess+=guess+", "
        priorguess+=guess+" "
        print(blank)
        print("incorrect:{}".format(incorrect_guess))
    else:
        print("Sorry you're out of guesses!")
        break
