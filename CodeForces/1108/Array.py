n=int(input())
for _ in range (n):
    m=int(input())
    if m==1:
        print(1)
    elif m==2:
        print(-1)
    else:
        a=[1,2,3]
        s=6
        while len(a)<m:
            a.append(s)
            s=s*2
        print(*a)