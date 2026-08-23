class Solution(object):
    def isPalindromic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        binary=""
        for ch in s:
            c=ord(ch)
            #format() function converts value into string following a format specification.
            re=format(c,'08b')
            binary=binary+re
        return binary==binary[::-1]
if __name__ =='__main__':
    s=input("Enter A String:")
    sol=Solution()
    res=sol.isPalindromic(s)
    if res:
        print("true")
    else:
        print("false")