import random


fortune_list = ["Don't do tomorrow, what can be done today", "Stay positive, people much rather help a smile than a frown",
                "If you don't believe your words, neither will they", "Make your own fortune! Code!"]
missfortunes_list = ["You will regret this day", "Just because I offer fortune doesn't mean it's guaranteed!",
                   "Incorrect decisions can alter your life negatively", "You'll remember this day :(!"]

while True:
    do_you_want = input("This is a fortune generator, do you want fortune? (y/n) ")
    my_fortune = random.randint(0,3)
    if do_you_want == "y":
        print(fortune_list[my_fortune])
    else:
        print(missfortunes_list[my_fortune])
        break

quit()
