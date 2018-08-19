#
# Code to handle input, repeats on empty input
#

word=""
while word == "":
    word=input("Input your word ")

#
# Checker for unique letter
#

for i,l in enumerate(word):
    if word.count(l)==1:
        print("Index of first unique letter is {}".format(i))
        break
    elif i == len(word)-1:
        print("there are no unique letters in the word")