class Solution(object):
    def countValidSequences(self,n,k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        p,q = n - 1, k - 1
        total = 0
        if 0 <= q <= p:
            if q == 0 or q == p:
                total = 1
            else:
                if q > p - q:
                    q = p - q
                num, d = 1, 1
                for i in range(1, q + 1):
                    num = (num * (p - i + 1)) %(10**9 + 7)
                    d = (d * i) % (10**9 + 7)
                total= (num * pow(d, (10**9 + 7)- 2, (10**9 + 7))) % (10**9 + 7)
        old = 0
        if (n - k) % 2 == 0 and n >= k:
            m = (n - k) // 2
            r, s = m + k - 1, k - 1
            if 0 <= s <= r:
                if s == 0 or s == r:
                    old= 1
                else:
                    if s > r - s:
                        s = r - s
                    num, c = 1, 1
                    for i in range(1, s + 1):
                        num = (num * (r - i + 1)) % (10**9 + 7)
                        c = (c * i) % (10**9 + 7)
                    old = (num * pow(c, (10**9 + 7) - 2, (10**9 + 7))) % (10**9 + 7)
        return (total- old) % (10**9 + 7)
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter n: "))
    m = int(input("Enter k: "))
    result = sol.countValidSequences(n, m)
    print("Output:", result)
