#RECURSIVE CODE
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fib=int(input("Which position in the fibinacci-series do you want to find the number for? "))
output=fibonacci(fib)
print(output)

#ITERATIVE
def fibadd(list):
    variable= list[-2]+list[-1]
    list.append(variable)
    return list, variable


fibindex=int(input("Which position in the fibinacci-series do you want to find the number for? "))
fib=[0,1]

if fibindex == 1:
    print(fib[0])
elif fibindex == 2:
    print(fib[1])
else:
    while len(fib) <= fibindex:
     fib, value =fibadd(fib)

print(value)
