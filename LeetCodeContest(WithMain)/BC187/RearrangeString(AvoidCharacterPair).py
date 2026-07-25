class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        if x not in s or y not in s:
            return s
        y1=s.count(y)
        x1=s.count(x)
        m=""
        for char in s:
            if char!=x and char!=y:
                m=m+char
        y2=y*y1
        x2=x*x1
        return y2+m+x2
if __name__ == "__main__":
    s=Solution()
    a1,b1,c1="aabc","a","c"
    res1=s.rearrangeString(a1,b1,c1)
    print(res1)
    a2,b2,c2="dcab","d","b"
    res2=s.rearrangeString(a2,b2,c2)
    print(res2)
    a3,b3,c3="axe","o","x"
    res3=s.rearrangeString(a3,b3,c3)
    print(res3)

