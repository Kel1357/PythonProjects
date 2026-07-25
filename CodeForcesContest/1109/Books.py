t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    #This expression is a Python one-liner that processes user input by splitting it into parts,
    #converting each part into a tuple, and then collecting the results into a list.
    p=True
    s=0
    for i in range(n):
        s=s+a[i]
        m=((i+1)*(i+2))//2
        if s<m:
            p=False
    if p:
        print("YES")
    else:
        print("NO")
