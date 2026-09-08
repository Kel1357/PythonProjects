if __name__=='__main__':
        t=int(input())
        for _ in range(t):
            x,y=map(int,input().split())
            s=x+y
            b=x&(~s)
            if b==0:
                a=x
            else:
                j=-1
                temp=b
                while temp:
                    temp>>=1
                    j=j+1
                hi=~((1<<(j+1))-1)
                lo=(1<<j)-1
                a=(x&hi)|(s&lo)
            k=x-a
            print(s,k,flush=True)                       
