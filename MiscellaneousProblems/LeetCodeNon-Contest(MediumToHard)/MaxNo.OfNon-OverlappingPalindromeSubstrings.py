class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        Pal=[]
        for i in range(n):
            row=[False]*n
            Pal.append(row)
        for i in range(n):
            Pal[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                Pal[i][i+1]=True
            else:
                Pal[i][i+1]=False
        for lh in range(3,n+1):
            for i in range(n-lh+1):
                j=i+lh-1
                if s[i]==s[j] and Pal[i+1][j-1]==True:
                    Pal[i][j]=True
                else:
                    Pal[i][j]=False
        dp=[]
        for i in range(n+1):
            dp.append(0)
        i=n-1
        while i>=0:
            dp[i]=dp[i+1]
            j=i+k-1
            while j<n:
                if Pal[i][j]==True:
                    cd=1+dp[j+1]
                    if cd>dp[i]:
                        dp[i]=cd
                    break
                j=j+1
            i=i-1
        return dp[0]
if __name__=='__main__':
    sol=Solution()
    s=input("Enter the string:")
    k=int(input("Enter the Minimum Length Of Palindrome Substring:"))
    res=sol.maxPalindromes(s,k)
    print("Maximum Number Of Non-Overlapping Palindrome Substrings:",res)