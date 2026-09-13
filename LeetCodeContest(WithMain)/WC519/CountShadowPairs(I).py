class Solution(object):
    def shadowPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        st1=[0] * n
        st2=[0] * n
        tp=-1
        total=0
        c=0
        for x in nums:
            while tp>=0 and st1[tp] > x:
                total=total-st2[tp]
                tp=tp-1
            if tp>=0 and st1[tp]==x:
                c=c+total-st2[tp]
                st2[tp]=st2[tp]+1
            else:
                c=c+total
                tp=tp+1
                st1[tp]=x
                st2[tp]=1
            total=total+1
        return c
if __name__=='__main__':
    sol=Solution()
    nums=list(map(int,input("Enter Array Elements (Separated By Commas):").split(',')))
    res=sol.shadowPairs(nums)
    print("Total Shadow Pairs:",res)
