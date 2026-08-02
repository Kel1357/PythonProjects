class Solution(object):
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        d=0
        for i in range(n):
            a=nums[i]
            for j in range(i+1,n):
                b=nums[j]
                g=self.gcd(a,b)
                st=(a//g)*(b//g)
                if st>d:
                    d=st
        return d
    def gcd(self,e,f):
        while f:
            e,f=f,e%f
        return e
if __name__=="__main__":
    sol=Solution()
    raw=input("Enter Numbers Separated By Commas:")
    nums=[]
    for x in raw.split(','):
        nums.append(int(x))
    res=sol.maxPairStrength(nums)
    print(f"Max Pair Strength: {res}")