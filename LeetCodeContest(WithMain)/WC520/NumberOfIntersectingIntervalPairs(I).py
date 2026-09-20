class Solution(object):
    def countIntersectingIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                st1,end1=intervals[i]
                st2,end2=intervals[j]
                maxi=max(st1,st2)
                mini=min(end1,end2)
                if maxi<=mini:
                    c=c+1
        return c
if __name__=='__main__':
    sol=Solution()
    n=int(input("Enter Number Of Intervals:"))
    intervals=[]
    for i in range(n):
        st,end=map(int,input(f"Enter start & end For Interval {i+1}:").split(','))
        intervals.append([st,end])
    res=sol.countIntersectingIntervals(intervals)
    print("Number Of Intersecting Interval Pairs:",res)
