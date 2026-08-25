class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        st=[("",0,0)]
        while st:
            current,count1,count2=st.pop()
            if len(current)==2*n:
                res.append(current)
                continue
            if count1<n:
                st.append((current+"(",count1+1,count2))
            if count2<count1:
                st.append((current+")",count1,count2+1))
        return res
if __name__ =='__main__':
    n=int(input("Enter Number Of Pairs:"))
    sol=Solution()
    res=sol.generateParenthesis(n)
    print(res)