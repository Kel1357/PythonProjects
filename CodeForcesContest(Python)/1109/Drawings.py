t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    m=0
    c=0
    for char in s:
        if char=='#':
            c=c+1
            if c>m:
                m=c
        else:
            c=0
    if m==0:
        print(0)
    else:
        time=(m+1)//2
        print(time)