class Solution(object):
    def weightedSum(self, parent, nums):
        """
        :type parent: List[int]
        :type nums: List[int]
        :rtype: int
        """
        n=len(parent)
        t=[]
        for i in range(n):
            t.append([])
        for i in range(1,n):
            t[parent[i]].append(i)
        d=[0]*n
        d[0]=1
        q=[0]
        f=0
        while f<len(q):
            node=q[f]
            f=f+1
            for ck in t[node]:
                d[ck]=d[node]+1
                q.append(ck)
        h = max(d)
        total=0
        for i in range(n):
            total=total+nums[i]*(h-d[i]+1)
        return total
if __name__ == "__main__":
    s=Solution()
    parent=list(map(int, input().strip().split(',')))
    nums=list(map(int, input().strip().split(',')))
    res=s.weightedSum(parent,nums)
    print("Weighted Sum Of A Tree:",res)
