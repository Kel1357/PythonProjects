def rank():
    n=int(input())
    element=[]
    for _ in range(n):
        l,r,u,v=map(int,input().split())
        element.append((l,r,u,v))
    for m in range(n,0,-1):
        c=0
        possible=True
        for j in range(1,m+1):
            f=-1
            y=m-j+1
            for i in range(c,n):
                l,r,u,v=element[i]
                if (j<l or j>r) and (y<u or y>v):
                    f=i+1
                    break
            if f==-1:
                possible=False
                break
            c=f
        if possible:
            print(m)
            return
    print(0)
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        rank()
                
