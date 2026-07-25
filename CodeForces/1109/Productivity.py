t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort(reverse=True)
    t=0
    c=n
    for i in range(b[0],n):
        t=t+a[i]
    c=b[0]
    for j in range(1,len(b)):
        v=b[j]
        s=0
        for i in range(v,c):
            s=s+a[i]
        t=t+abs(s)
        c=v
    s=0
    for i in range(0,c):
        s=s+a[i]
    t=t+abs(s)
    print(t)