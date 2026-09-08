if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        c=a.count(0)
        if c<2:
            print(-1)
            continue
        if a[0]==0 and a[-1]==0:
            print(0)
        elif a[0]==0 or a[-1]==0:
            print(1)
        else:
            print(2)
