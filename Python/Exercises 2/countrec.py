list=[]
def countrec(n,top):
    if n == top:
        list.append(n)
    elif n!=top:
        list.append(n)
        n=int(n)
        n += 1
        countrec(n,top)
    return list

def countrecdwn(bottom,n):
    if n == bottom:
        list.append(n)
    elif n!=bottom:
        list.append(n)
        n=int(n)
        n -= 1
        countrecdwn(bottom,n)
    return list

start=int(input("Name your start value "))
end=int(input("Name your end value "))
if start < end:
    counting=countrec(start,end)
    print(*counting, sep=', ')
elif end < start:
    counting=countrecdwn(end,start)
    print(*counting, sep=', ')
else:
    print(start)
