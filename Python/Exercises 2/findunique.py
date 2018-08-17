print("We will find the first unique letter in word inputed to this program!")
word=str(input("Input a word "))
print("word: {}".format(word))
if word!="":
    storage=word[0]
    #print("storage:{}".format(storage))
    wordtest = word[0:]
    condition=0
    while True:
        for letter in range(len(word)):
            print("New LOOP number:{}".format(letter))

            print("storage: {}".format(storage))
            if wordtest!="":
                break
            elif wordtest.find(storage)>= 0:
                wordtest.replace(str(storage),"")
                print("wordtest: {}".format(wordtest))
                wordtest = word[letter+1:]

                storage = wordtest[0]
            else:
                print("{} is the first unique letter of the word".format(storage))
                condition=1
                break

    if condition == 0:
        print("There are no unique letters in this word")
else:
    print("sorry that's not a word")
    print("terminating")