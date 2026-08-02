class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=0
        valid=0
        for ch in s:
            if ch=='0':
                d=d+1
            else:
                d=d-1
            if abs(d)<=1:
                valid=valid+1
        return valid
if __name__=='__main__':
    sol=Solution()
    m=input("Enter Binary String:").strip()
    possible=True
    n=len(m)
    if n==0:
        possible=False
    else:
        for ch in m:
            if ch!='0' and ch!='1':
                possible=False
                break
    if not possible:
        print("Invalid Input, Please Try Again")
    res=sol.countValidPrefixes(m)
    print(f"Number Of Valid Prefixes: {res}")

