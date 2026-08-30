class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        mini=nums.index(min(nums))
        maxi=nums.index(max(nums))
        if mini>maxi:
            mini,maxi=maxi,mini
        op1=maxi+1
        op2=n-mini
        op3=(mini+1)+(n-maxi)
        return min(op1,op2,op3)
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Separated By Commas):").split(',')))
    res=sol.minimumDeletions(nums)
    print("Minimum Deletions:",res)
