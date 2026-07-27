t=int(input())
for _ in range (t):
    n=int(input())
    m=list(map(int,input().split()))
    if n%2==1:
        print("NO")
        continue
    odd=m[0::2]
    even=m[1::2]
    mini=min(odd)
    maxi=max(even)
    k=mini-maxi
    if k>=2:
        print("YES")
    else:
        print("NO")
            
