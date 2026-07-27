def solve(n,k):
    total=n-k
    x=(total+1)//2
    y=total//2
    c1=(n+1)//2
    c2=n//2
    if y==0:
        if c2!=0:
            return "-1"
    else:
        if c2<y or c1<x:
            return "-1"
    base=c1//x
    rem=c1%x
    if y>0:
        b=c2//y
        r=c2%y
    s=""
    for i in range(x):
        if i<rem:
            size=base+1
        else:
            size=base
        s=s+'1' * size
        if i<y:
            if i<r:
                si=b+1
            else:
                si=b
            s=s+'0' * si
    return s
if __name__=='__main__':
    t=int(input())
    out=""
    for _ in range(t):
        n,k=map(int,input().split())
        out=out+solve(n,k)+"\n"
    print(out,end="")
    
