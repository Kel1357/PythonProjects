class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos={}
        for idx,x in enumerate(nums):
            if x in pos:
                pos[x].append(idx)
            else:
                pos[x]=[idx]
        c=0
        for x,it in pos.items():
            if len(it)==3:
                i1,i2,i3=it
                if i2-i1==i3-i2:
                    c=c+1
        return c
if __name__=='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Separated By Commas):").split(',')))
    res=sol.countSpecialIntegers(nums)
    print(res)
