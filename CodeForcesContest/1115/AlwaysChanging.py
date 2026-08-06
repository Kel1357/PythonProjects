try:
    t1=input().strip()
    while not t1:
        t1=input().strip()
    t2= int(t1)
except EOFError:
    t2=0
for _ in range(t2):
    n1= input().strip()
    while not n1:
        n1=input().strip()
    n2=int(n1)
    s=input().strip()
    while not s:
        s=input().strip()
    total1=s.count('0')
    total2=n2-total1
    dp1=0
    dp2=0
    for c in s:
        if c=='0':
            dp1=dp2+1
        else:
            dp2=dp1+1
    maxi=max((dp1//2)*2,(dp2//2)*2)
    if dp1%2==1:
        maxi1=dp1
    else:
        maxi1=dp1-1
    if dp2%2==1:
        maxi2=dp2
    else:
        maxi2=dp2-1
    mini=-1
    for k in range((maxi//2),-1,-1):
        rem1=k
        rem2=k
        d1=total1-rem1
        d2=total2-rem2
        if d1>=0 and d2>=0 and abs(d1-d2)<=1:
            delete=d1+d2
            if mini==-1 or delete<mini:
                mini=delete
    if maxi1>0:
        for k in range(((maxi1-1)//2),-1,-1):
            rem1=k+1
            rem2=k
            d1=total1-rem1
            d2=total2-rem2
            if d1>=0 and d2>=0 and abs(d1-d2)<=1:
                delete=d1+d2
                if mini==-1 or delete<mini:
                    mini=delete
    if maxi2>0:
        for k in range(((maxi2-1)//2),-1,-1):
            rem1=k
            rem2=k+1
            d1=total1-rem1
            d2=total2-rem2
            if d1>=0 and d2>=0 and abs(d1-d2)<=1:
                delete=d1+d2
                if mini==-1 or delete<mini:
                    mini=delete
    print(mini)