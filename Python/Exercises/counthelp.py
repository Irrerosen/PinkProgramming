list = []
def countbetween(start,end,step):
    for i in range(start,(end+step),step):
        list.append(i)
    return list

print("This program will help you count!")
num1=int(input("Where should we start? "))
numn=int(input("When should we stop? "))
print("Ok!")
if num1<numn:
    counting=countbetween(num1,numn,1)
elif num1>numn:
    counting=countbetween(num1,numn,-1)
else:
    counting=[num1]

print(*counting, sep=', ')