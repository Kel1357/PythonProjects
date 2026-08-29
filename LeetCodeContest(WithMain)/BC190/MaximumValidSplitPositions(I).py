class Solution(object):
    def gcd(self, a, b):
        while b:
            a,b=b,a%b
        return a
    def maxValidSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=1:
            return 0
        gcd=self.gcd
        LOG=max(1,n.bit_length())
        st=[nums[:]]
        for _ in range(LOG-1):
            row=[0]*n
            st.append(row)
        for j in range(1,LOG):
            half=1<<(j-1)
            length=1<<j
            for i in range(n-length+1):
                st[j][i]=gcd(st[j-1][i],st[j-1][i+half])
        log_table=[0]*(n+1)
        for i in range(2,n+1):
            log_table[i]=log_table[i//2]+1
        def rank(l,r):
            if l>r:
                return 0
            j=log_table[r-l+1]
            return gcd(st[j][l],st[j][r-(1<<j)+1])
        P=[rank(0,i) for i in range(n)]
        S=[rank(i,n-1) for i in range(n)]
        best=0
        for b in range(1,n):
            if P[b-1]==S[b]:
                best=best+1
        if n<=2:
            return best
        for k in range(n):
            cnt=0
            A=rank(0,k-1)      
            B=rank(k+1,n-1)  
            acc=0
            for b in range(k-1,0,-1):
                acc=gcd(acc,nums[b]) 
                right1=gcd(acc,B)
                left1=P[b-1]
                if b>=1 and (n-b-1)>=1 and left1==right1:
                    cnt=cnt+1
            acc=0
            for b in range(k+1,n):
                left1=gcd(A,acc)
                right1=S[b]
                if (b-1)>=1 and (n-b)>=1 and left1==right1:
                    cnt=cnt+1
                acc=gcd(acc,nums[b]) 
            best=max(best,cnt)
        return best
if __name__=='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements:").split(',')))
    res=sol.maxValidSplits(nums)
    print("Maximum Valid Split Positions:",res)
