t=int(input())
for _ in range(t):
        x,y,k=map(int,input().split())
        ans=0
        d=y-x
        i=0
        while i<k:
            a=x+i
            q=d//a
            if q==0:
                ans=ans+d*(k-i)
                break
            j=d//q-x
            if j>=k:
                j=k-1
            cn=j-i+1
            res=cn*x+(i+j)*cn//2
            ans=ans+cn*d-q*res
            i=j+1
        print(ans)
