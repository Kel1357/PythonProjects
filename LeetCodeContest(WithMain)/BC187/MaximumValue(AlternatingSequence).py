class Solution(object):
    def maximumValue(self, n, s, m):
        """
        :type n: int
        :type s: int
        :type m: int
        :rtype: int
        """
        k = ((n-2)// 2) * (m - 1)
        if n == 1:
            return s
        return s + m + k
if __name__=="__main__":
    n=int(input("Enter n:="))
    s=int(input("Enter s:="))
    m=int(input("Enter m:="))
    sol=Solution()
    ans=sol.maximumValue(n,s,m)
    print(ans)
