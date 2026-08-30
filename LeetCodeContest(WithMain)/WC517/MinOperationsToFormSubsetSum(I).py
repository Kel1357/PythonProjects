class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        inf=float('inf')
        dp=[inf]*(target+1)
        dp[0]=0
        for num in nums:
            possible=[]
            d,cost=num,0
            while True:
                if d<=target:
                    possible.append((d,cost))
                if d==0:
                    break
                d=d//2
                cost=cost+1
            m,cost=num*2,1
            while m<=target:
                possible.append((m,cost))
                m=m*2
                cost=cost+1
            new_dp=dp[:]
            for val,cost in possible:
                for s in range(target,val-1,-1):
                    if dp[s-val]!=inf:
                        new_dp[s]=min(new_dp[s],dp[s-val]+cost)
            dp=new_dp
        if dp[target]!=inf:
            return dp[target]
        else:
            return -1
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Numbers (Separated By Commas):").split(',')))
    target=int(input("Enter Target Sum:"))
    res=sol.minOperations(nums,target)
    print("Minimum Operations:",res)

