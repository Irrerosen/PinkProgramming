# Pink Programming
## Python Summer Camp
Files in this directory is for learning python.

|Schedule| Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | After camp |
|---------|:-----:|:-----:|:-----:|:-----:|:-----:|------------|
|Topics  |Downloading|History|Loops|Markdown|Recap|
|||paradigms|recursion|machine learning||
|||git and cmd||||
Programs|none|exercises 1|exercises 2|exercises 3|||

*Some code from the program hangman*
```python
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
```
