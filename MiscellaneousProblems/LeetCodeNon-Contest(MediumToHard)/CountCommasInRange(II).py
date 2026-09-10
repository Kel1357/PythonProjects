class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        t=1000
        while n>=t:
            total=total+(n-t+1)
            t=t*1000 
        return total
if __name__=='__main__':
    sol=Solution()
    n=int(input().strip())
    res=sol.countCommas(n)
    print("Count Commas In Range:",res)
