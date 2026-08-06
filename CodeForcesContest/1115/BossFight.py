t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    t=sum(a)
    f={}
    for x in a:
        if x in f:
            f[x]=f[x]+1
        else:
            f[x]=1
    m=0
    for x in f:
        if f[x]>m:
            m=f[x]
    r=n-m
    if m<=r+1:
        print(t)
    else:
        u=None
        for x in f:
            if f[x]==m:
                if u is None or x<u:
                    u=x
        v=2*m-n-2
        res=t-v*u
        print(res)
