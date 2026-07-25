n=int(input())
for _ in range(n): #We use underscore if we don't care about value in a loop
    m=int(input())
    a=[]
    for i in range(1,m+1,2):
        a.append(i+1)
        a.append(i)
    print(*a)
#(*a unpacks the list a into separate arguments instead of printing it as one list object)

