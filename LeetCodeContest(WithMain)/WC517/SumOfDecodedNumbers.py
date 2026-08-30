class Solution(object):
    def sumDecoded(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD=10**9+7
        t=0
        for n in nums:
            width=n%10
            d1=n//10
            d2=str(d1)
            x=int(d2[:width])
            y=int(d2[width:])
            decoded=pow(x,y,MOD)
            t=(t+decoded)%MOD
        return t
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Numbers:").split(',')))
    res=sol.sumDecoded(nums)
    print("Sum Of Decoded Values:",res)

