class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ans=float('inf')
        for k in range(n):
            rotated=s[k:]+s[:k]
            op=k
            for i in range(n//2):
                a,b=rotated[i],rotated[n-1-i]
                diff=abs(ord(a)-ord(b))
                if diff<=(26-diff):
                    op=op+diff
                else:
                    op=op+(26-diff)
            if op<ans:
                ans=op
        return ans
if __name__=='__main__':
   sol=Solution()
   s=input("Enter the String:")
   res=sol.minOperations(s)
   print("Minimum Operations Required:",res)