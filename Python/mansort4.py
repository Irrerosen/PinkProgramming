unsorted=input("please input an unsorted list ")
if ' ' in unsorted:
    numbers=list(map(int, unsorted.split()))
    print("INPUT: {}".format(numbers))

else:
    data=(", ".join(unsorted))
    numbers=[]
    numbers= list(map(int, (list(data.split(', ')))))
    print("INPUT: {}".format(numbers))

new_list=[]
while numbers != []:
    minimum = min(numbers)
    new_list.append(minimum)
    numbers.remove(minimum)

    print(new_list)