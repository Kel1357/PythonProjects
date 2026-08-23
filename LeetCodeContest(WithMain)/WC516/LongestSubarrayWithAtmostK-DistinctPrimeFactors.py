class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        maxi=0
        f={}
        l=len(nums)
        for right in range(l):
            n=nums[right]
            temp=set()
            while n%2==0:
                temp.add(2)
                n=n//2
            i=3
            while i*i<=n:
                while n%i==0:
                    temp.add(i)
                    n=n//i
                i=i+2
            if n>2:
                temp.add(n)
            for p in temp:
                f[p]=f.get(p,0)+1
            while len(f)>k:
                n=nums[left]
                fact=set()
                while n%2==0:
                    fact.add(2)
                    n=n//2
                i=3
                while i*i<=n:
                    while n%i==0:
                        fact.add(i)
                        n=n//i
                    i=i+2
                if n>2:
                    fact.add(n)
                for p in fact:
                    f[p]=f[p]-1
                    if f[p]==0:
                        del f[p]
                left=left+1
            maxi=max(maxi,right-left+1)
        return maxi
if __name__ =='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Comma-separated):").split(',')))
    k=int(input("Enter k:"))
    res=sol.longestSubarray(nums,k)
    print("Longest Subarray length:",res)
