class Solution(object):
    def canReach(self, start, target):
        """
        :type start: List[int]
        :type target: List[int]
        :rtype: bool
        """
        s1=start[0]+start[1]
        t1=target[0]+target[1]
        s2=s1%2
        t2=t1%2
        if s2==t2:
            return True
        return False
if __name__=="__main__":
    sol=Solution()
    r1=sol.canReach([1,1],[2,2])
    print(r1)
    r2=sol.canReach([4,5],[6,6])
    print(r2)