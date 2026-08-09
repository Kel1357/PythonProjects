class Solution(object):
    def maxArea(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m,n=len(mat),len(mat[0])
        dp=[]
        for _ in range(m):
            row=[0]*n       
            dp.append(row)
        maxi=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    if dp[i][j]>maxi:
                        maxi=dp[i][j]
        def feasible(k):
            min_x=min_y=float('inf')
            max_x=max_y=float('-inf')
            count=0
            for i in range(m):
                row=dp[i]
                for j in range(n):
                    if row[j]>=k:
                        x,y=i-k+1,j-k+1
                        if x<min_x:
                            min_x=x
                        if x>max_x:
                            max_x=x
                        if y<min_y:
                            min_y=y
                        if y>max_y:
                            max_y=y
                        count=count+1
            if count<2:
                return False
            return (max_x-min_x)>=k or (max_y-min_y)>=k
        lo,hi,ans=1,maxi,0
        while lo<=hi:
            mid=(lo+hi)//2
            if feasible(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans*ans
if __name__ == "__main__":
    sol=Solution()
    m=int(input("Enter Number Of Rows:"))
    mat=[]
    print("Enter each Row (Commas Separated 0/1):")
    for _ in range(m):
        row=list(map(int,input().split(',')))
        mat.append(row)
    res=sol.maxArea(mat)
    print("Maximum Area Of Two Non-Overlapping Square Submatrices:",res)
