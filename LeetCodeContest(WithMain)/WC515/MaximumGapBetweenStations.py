class Solution(object):
    def maximumGap(self, skill, station):
        """
        :type skill: str
        :type station: str
        :rtype: int
        """
        n=len(skill)
        m=len(station)
        l=[0]*n
        j=0
        for i in range(n):
            while station[j]!=skill[i]:
                j=j+1
            l[i]=j
            j=j+1
        r=[0]*n
        j=m-1
        for i in range(n-1,-1,-1):
            while station[j]!=skill[i]:
                j=j-1
            r[i]=j
            j=j-1
        gap=0
        for i in range(1,n):
            d=r[i]-l[i-1]
            if d>gap:
                gap=d
        return gap
if __name__=='__main__':
    sol=Solution()
    skill=input("Enter Skill String:").strip()
    station=input("Enter Station String:").strip()
    res=sol.maximumGap(skill,station)
    print("Maximum Gap Between Stations:",res)