class Solution(object):
    def largestString(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[]
        for x in nums:
            f={0:x}
            rank=0
            while rank in f and rank<25:
                if f[rank]>=2:
                    carry=f[rank]//2
                    f[rank]%=2
                    f[rank+1]=f.get(rank+1,0)+carry
                rank=rank+1
            res=""
            for r in sorted(f.keys(),reverse=True):
                if f[r]>0:
                    res=res+chr(ord('a')+r)*f[r]
            ans.append(res)
        return ans
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Separated By Commas):").split(',')))
    res=sol.largestString(nums)
    print("Result:",res)

