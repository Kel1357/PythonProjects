class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        INF=float('inf')
        t=[]
        k=1
        while k*(k+1)//2<=n:
            t.append(k*(k+1)//2)
            k=k+1
        dp=[INF]*(n+1)
        dp[0]=0
        for r in range(1,n+1):
            best=INF
            for idx,u in enumerate(t):
                if u>r:
                    break
                l=idx+1
                if u==r:
                    cd=l
                else:
                    if dp[r-u]==INF:
                        continue
                    cd=l+1+dp[r-u]
                if cd<best:
                    best=cd
            dp[r]=best
        return dp[n]
if __name__=='__main__':
    sol=Solution()
    n=int(input())
    res=sol.minDays(n)
    print("Minimum Days To Score Exactly 'N' Points:",res)
