def main():
    t=int(input())
    b=[]
    for _ in range(t):
        n,c=map(int,input().split())
        d=list(map(int,input().split()))
        d.sort()
        s=0
        for x in d:
            if x<c:
                s=s+1
            else:
                break
        k=min(s,n//2)
        t=sum(d)
        l=sum(d[:k])
        ans=t-(c*n)+(k*c)-l
        print(ans)
if __name__=='__main__':
    main()