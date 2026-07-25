class Solution(object):
    def transformStr(self, s, strs):
        """
        :type s: str
        :type strs: List[str]
        :rtype: List[bool]
        """
        ts = s.count('0')
        x = []
        d = 0
        for ch in s:
            if ch == '0':
                x.append(d)
            d = d + 1
        ans = []
        for t in strs:
            fs = t.count('0')
            w = t.count('?')
            n = ts - fs
            if n < 0 or n > w:
                ans.append(False)
                continue
            y = []
            z = 0
            tx = 0
            for ch in t:
                if ch == '0':
                    y.append(tx)
                elif ch == '?':
                    if z < n:
                        y.append(tx)
                        z = z + 1
                tx = tx + 1
            possible = True
            for k in range(ts):
                if y[k] > x[k]:
                    possible = False
                    break
            ans.append(possible)
        return ans
if __name__=='__main__':
    sol=Solution()
    s1="101"
    st1=["1?1","0?1","0?0"]
    op1=sol.transformStr(s1,st1)
    print(op1)
    s2="1100"
    st2=["0011","11?1","1?1?"]
    op2=sol.transformStr(s2,st2)
    print(op2)
    s3="1010"
    st3=["0011"]
    op3=sol.transformStr(s3,st3)
    print(op3)