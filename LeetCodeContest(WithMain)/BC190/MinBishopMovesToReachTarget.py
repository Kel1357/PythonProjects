class Solution(object):
    def minBishopMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        s1,s2=source
        t1,t2=target
        if(s1+s2)%2!=(t1+t2)%2:
            return -1
        if s1-s2==t1-t2 or s1+s2==t1+t2:
            return 1
        return 2
if __name__=='__main__':
    sol=Solution()
    s1,s2=map(int,input("Enter Source (row,col):").split(','))
    t1,t2=map(int,input("Enter Target (row,col):").split(','))
    res=sol.minBishopMoves([s1,s2],[t1,t2])
    print("Minimum Moves:",res)
    
