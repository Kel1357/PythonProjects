class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        saw=set()
        count=0
        i=0
        n=len(nums)
        while i<n:
            val=nums[i]
            if val in saw:
                i=i+1
                continue
            j=i
            while j<n and nums[j]==val:
                j=j+1
            if val not in nums[j:]:
                count=count+1
            saw.add(val)            #.add() puts a new number into the set
            i=j
        return count
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Numbers (Separated By Commas):").split(',')))
    res=sol.countSpecialIntegers(nums)
    print("Number Of Special Integers:",res)
