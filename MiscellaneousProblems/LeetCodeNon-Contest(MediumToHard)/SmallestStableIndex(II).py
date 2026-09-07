class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)        
        maxi=[0]*n
        maxi[0]=nums[0]
        for i in range(1,n):
            maxi[i]=max(maxi[i-1],nums[i])        
        mini=[0]*n
        mini[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            mini[i]=min(mini[i+1],nums[i])        
        for i in range(n):
            inst=maxi[i]-mini[i]
            if inst<=k:
                return i
        return -1
if __name__=='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Separated By Commas):").split(',')))
    k=int(input("Enter Index k:"))
    res=sol.firstStableIndex(nums,k)
    print("Smallest Stable Index:",res)
