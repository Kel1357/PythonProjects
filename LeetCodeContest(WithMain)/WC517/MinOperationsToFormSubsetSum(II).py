class Solution(object):
    def minOperations(self, nums, sum):
        """
        :type nums: List[int]
        :type sum: int
        :rtype: int
        """
        inf=float('inf')
        max_num=0
        for num in nums:
            if num>max_num:
                max_num=num
        candidate1=sum*2+2
        if max_num>candidate1:
            bound=max_num
        else:
            bound=candidate1
        cache={}
        def reach(num):
            if num in cache:
                return cache[num]
            dist=[-1]*(bound+1)
            start=num
            dist[start]=0
            queue=[start]
            head=0
            while head<len(queue):
                x=queue[head]
                head=head+1
                d=dist[x]+1
                nxt1=x*2
                if nxt1<=bound and dist[nxt1]==-1:
                    dist[nxt1]=d
                    queue.append(nxt1)
                nxt2=x//2
                if dist[nxt2]==-1:
                    dist[nxt2]=d
                    queue.append(nxt2)
            res=[]
            for v, c in enumerate(dist[:sum+1]):
                if c!=-1:
                    res.append((v,c))
            cache[num]=res
            return res
        dp=[inf]*(sum+1)
        dp[0]=0
        for num in nums:
            possible=reach(num)
            new_dp=dp[:]
            for val,cost in possible:
                for s in range(sum,val-1,-1):
                    if dp[s-val]!=inf:
                        new_dp[s]=min(new_dp[s],dp[s-val]+cost)
            dp=new_dp
        if dp[sum]!=inf:
            return dp[sum]
        else:
            return -1
if __name__ == '__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Numbers (Separated By Commas):").split(',')))
    target=int(input("Enter Target Sum:"))
    res=sol.minOperations(nums,target)
    print("Minimum Operations:",res)
