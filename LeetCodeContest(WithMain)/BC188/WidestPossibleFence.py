class Solution(object):
    def maximumWidth(self, planks):
        """
        :type planks: List[int]
        :rtype: int
        """
        if not planks:
            return 0
        count={}
        for p in planks:
            if p in count:
                count[p]=count[p]+1
            else:
                count[p]=1
        u=[]
        for p in count:
            u.append(p)
        n=len(u)
        h={}
        for i in range(n):
            x=u[i]
            c1=count[x]
            if c1>=2:
                t1=2*x
                pair=c1//2
                if t1 in h:
                    h[t1]=h[t1]+pair
                else:
                    h[t1]=pair
            for j in range(i+1,n):
                y=u[j]
                c2=count[y]
                t2=x+y
                if c1<c2:
                    pairs=c1
                else:
                    pairs=c2
                if t2 in h:
                    h[t2]=h[t2]+pairs
                else:
                    h[t2]=pairs
        for x in u:
            if x in h:
                h[x]=h[x]+count[x]
            else:
                h[x]=count[x]
        max_width=0
        for height,width in h.items():
            if width>max_width:
                max_width=width
        return max_width
if __name__=='__main__':
    sol=Solution()
    r=input("Enter Plank Length:=")
    clean=r.replace('[',' ').replace(']',' ').replace(',',' ')
    planks=[]
    for x in clean.split():
        planks.append(int(x))
    res=sol.maximumWidth(planks)
    print(f"Maximum Possible Width:={res}")
