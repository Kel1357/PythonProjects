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
            n=len(it)
            if n<3:
                continue
            p=it[1]-it[0]
            eq=True
            for i in range(2,n):
                if it[i]-it[i-1]!=p:
                    eq=False
                    break
            if eq:
                c=c+1
        return c
if __name__ == '__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Separated By Commas):").split(',')))
    res=sol.countSpecialIntegers(nums)
    print(res)
