class Solution(object):
    def minAdjacentSwaps(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        c=0
        h=0
        s=0
        mod=10**9+7
        for x in nums:
            if x<a:
                s=s+(c+h)
            elif x<=b:
                s=s+h
                c=c+1
            else:
                h=h+1
        return s%mod
if __name__ == "__main__":
    s=Solution()
    m1=s.minAdjacentSwaps([1,3,2,4,5,6],3,4)
    print(m1)
    m2=s.minAdjacentSwaps([9,7,5,3],4,8)
    print(m2)
    m3=s.minAdjacentSwaps([3,7,5,9],4,8)
    print(m3)