class Solution(object):
    def validSubarrays(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n=len(nums)
        q=len(queries)
        block=1
        while block*block<=n:
            block=block+1
        block=block-1
        queries=[(l,r,idx) for idx,(l,r) in enumerate(queries)]
        queries.sort(key=lambda x:(x[0]//block,x[1]))
        freq={}
        state={"distinct":0,"odd_count":0}   
        ans=[False]*q
        def add(x):
            freq[x]=freq.get(x,0)+1
            if freq[x]==1:
                state["distinct"]+=1
            if freq[x]%2==1:
                state["odd_count"]+=1
            else:
                state["odd_count"]-=1
        def remove(x):
            if freq[x]%2==1:
                state["odd_count"]-=1
            else:
                state["odd_count"]+=1
            freq[x]=freq[x]-1
            if freq[x]==0:
                state["distinct"]-=1
        L,R=0,-1
        for l,r,idx in queries:
            while L>l:
                L=L-1
                add(nums[L])
            while R<r:
                R=R+1
                add(nums[R])
            while L<l:
                remove(nums[L])
                L=L+1
            while R>r:
                remove(nums[R])
                R=R-1
            ans[idx]=(state["distinct"]==k and state["odd_count"]==0)
        return ans
if __name__=='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Elements Of 'nums' Array:").split(',')))
    queries=[]
    k=int(input("Enter Number Of Distinct Elements Required:"))
    q=int(input("Enter Number Of queries:"))
    for i in range(q):
        li,ri=map(int,input(f"Query {i+1}:").split(','))
        queries.append([li,ri])
    res=sol.validSubarrays(nums,k,queries)
    out="["
    for idx,x in enumerate(res):
        if x:
            out=out+"true"
        else:
            out=out+"false"
        if idx!=len(res)-1:
            out=out+","
    out=out+"]"
    print(out)