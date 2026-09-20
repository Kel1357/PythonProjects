class Solution(object):
    def countIntersectingIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        c=0
        count=0
        j=0
        st=[]
        end=[]
        for val in intervals:
            s=val[0]
            e=val[1]
            st.append(s)
            end.append(e)
        st.sort()
        end.sort()
        for i in range(n):
            while j<n and end[j]<st[i]:
                count=count-1
                j=j+1
            c=c+count
            count=count+1
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
    
