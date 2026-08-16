class Solution(object):
    def minPenalty(self, period, lights, arrivalTime):
        """
        :type period: int
        :type lights: List[int]
        :type arrivalTime: List[int]
        :rtype: int
        """
        l=sorted(lights)
        n=len(l)
        p=0
        for t in arrivalTime:
            r=t%period
            lo=0
            hi=n
            while lo<hi:
                mid=(lo+hi)//2
                if l[mid]>r:
                    hi=mid
                else:
                    lo=mid+1
            if lo<n:
                wait=0
            else:
                wait=period-r
            if wait>p:
                p=wait
        return p
if __name__=='__main__':
    sol=Solution()
    period=int(input("Enter Period:"))
    lights=list(map(int,input("Enter Lights Array:").split(',')))
    arrivalTime=list(map(int,input("Enter Arrival Times:").split(',')))
    res=sol.minPenalty(period,lights,arrivalTime)
    print("Minimum Penalty:",res)