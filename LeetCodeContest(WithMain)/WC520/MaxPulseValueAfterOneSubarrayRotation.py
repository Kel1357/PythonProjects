class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        op=[0]*(n+1)
        for i in range(n):
            if i%2==0:
                sign=1
            else:
                sign=-1
            op[i+1]=op[i]+sign*nums[i]
        INF=float('-inf')
        even=INF     
        odd=INF
        best=float('inf')
        for k in range(2,n+1):
            l=k-2
            if l%2==0:
                if op[l]>even:
                    even=op[l]
            else:
                if op[l]>odd:
                    odd=op[l]
            if k%2==0:
                if even!=INF:
                    cd=op[k]-even
                    if cd<best:
                        best=cd
            else:
                if odd!=INF:
                    cd=op[k]-odd
                    if cd<best:
                        best=cd
        if best==float('inf'): 
            gain=0  
        else: 
            gain=max(0,-2*best)
        return op[n]+gain
if __name__=='__main__':
    sol=Solution()
    nums=list(map(int,input().split(',')))
    res=sol.maxValue(nums)
    print("Maximum Pulse Value After One Subarray Rotation:",res)
