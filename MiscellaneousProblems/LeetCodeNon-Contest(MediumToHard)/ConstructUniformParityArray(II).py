class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n=min(nums1)
        if n%2==1:
            return True
        for x in nums1:
            if x%2==1:
                return False
        return True
if __name__=='__main__':
    sol=Solution()
    nums1=list(map(int,input("Enter Numbers (Separated By Commas):").split(',')))
    res=sol.uniformArray(nums1)
    print(res)
