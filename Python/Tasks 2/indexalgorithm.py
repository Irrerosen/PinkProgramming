package=input("Please enter a line of numbers: ")

if ' ' in package:
    numbers=list(map(int, package.split()))
    print("INPUT: {}".format(numbers))

else:
    data=(", ".join(package))
    numbers=[]
    numbers= list(map(int, (list(data.split(', ')))))
    print("INPUT: {}".format(numbers))
    length=len(numbers)

Indexid=int(input("Which number do you want to find the index of? "))
indexlist = []
for datapoint in range(len(numbers)):
    if Indexid == numbers[datapoint]:
        indexlist.append(datapoint+1)
    else:
        pass

if indexlist == []:
    print("OUTPUT: there is no {} in the list".format(Indexid))
elif len(indexlist) > 1:
    indexprint=", ".join(map(str, indexlist))
    print("The number {} can be found at index {}".format(Indexid, indexprint))
else:
    print("The number {} can be found at index {}".format(Indexid, indexlist[0]))

