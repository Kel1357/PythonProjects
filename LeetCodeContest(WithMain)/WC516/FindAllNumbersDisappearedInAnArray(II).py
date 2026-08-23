class Solution(object):
    def findDisappearedNumbers(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        present=set(nums)
        res=[]
        start=None
        for x in range(lower,upper+1):
            if x not in present:
                if start is None:
                    start=x
            else:
                if start is not None:
                    res.append([start,x-1])
                    start=None
        if start is not None:
            res.append([start,upper])
        return res
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Comma-Separated):").split(',')))
    lower,upper=map(int,input("Enter lower and Upper Bounds (Comma-Separated):").split(','))
    res=sol.findDisappearedNumbers(nums,lower,upper)
    print("Missing ranges:",res)

