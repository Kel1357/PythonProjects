t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=input()
    p=[0]*n
    for i in range(n-1):
        p[i+1]=p[i]
        if s[i]==s[i+1]:
            p[i+1]+=1
    for _ in range(q):
        l,r,k=map(int,input().split())
        if l==r:
            b=0
        else:
            b=p[r-1]-p[l-1]
        c=(b+1)//2
        if c<=k:
            print("YES")
        else:
            print("NO")
