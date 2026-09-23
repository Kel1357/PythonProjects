class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[0]*k
        dp=[0]*k  
        for num in nums:
            op=[0]*k
            val=num%k            
            op[val]=op[val]+1            
            for r in range(k):
                if dp[r]>0:
                    rs=(r*val)%k
                    op[rs]=op[rs]+dp[r]
            dp=op
            for r in range(k):
                ans[r]=ans[r]+dp[r] 
        return ans
if __name__=="__main__":
    sol=Solution()
    nums=list(map(int,input("Enter Numbers:").split(',')))
    k=int(input("Enter k:"))
    res=sol.resultArray(nums,k)
    print("X Value Of Array:",res)
