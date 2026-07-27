class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s==0:
            return 0
        if s>9*n:
            return -1
        r=0
        rem=s
        for _ in range(n):
            d=min(9,rem)
            r=(r*10)+d
            rem=rem-d
        return r
if __name__ == '__main__':
    sol = Solution()
    n=int(input("Enter n:"))
    s=int(input("Enter s:"))
    ans=sol.largestInteger(n,s)
    print(f"Largest Integer with at most {n} digits and digit sum {s}: {ans}")
