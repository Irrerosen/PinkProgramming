from typing import List

package=input("please input the human captcha ")

data=(" ".join(package))
numbers=[]
total=[]
numbers= list(map(int, (list(data.split(' ')))))


for i in range(0,len(numbers)):
    j=i+1
    print(len(numbers))
    print(j)
    if j >= len(numbers):
        j=0
    if (numbers[i]) == (numbers[j]):
        total.append(numbers[i])
        #print(i)
        #print(total)

    else:
        #total.append(0)
        #print(i)
        print(total)


#if numbers[-1] == numbers[0]:
#   total.append(numbers[0])

print(total)
result=sum(total)
print(result)