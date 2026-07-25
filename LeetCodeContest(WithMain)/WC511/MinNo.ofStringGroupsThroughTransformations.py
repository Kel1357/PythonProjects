class Solution(object):
    def minimumGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sn = set()
        for w in words:
            c = []
            for t in (w[0::2], w[1::2]):
                if not t:
                    c.append(t)
                    continue
                s = t + t
                n = len(s)
                f = [-1] * n
                k = 0
                for j in range(1, n):
                    s1 = s[j]
                    i = f[j - k - 1]
                    while i != -1 and s1 != s[k + i + 1]:
                        if s1 < s[k + i + 1]:
                            k = j - i - 1
                        i = f[i]
                    if s1 != s[k + i + 1]:
                        if s1 < s[k]:
                            k = j
                        f[j - k] = -1
                    else:
                        f[j - k] = i + 1
                c.append(t[k:] + t[:k])
            sn.add(tuple(c))
        return len(sn)
if __name__=='__main__':
    sol = Solution()
    w1=["ntgwz","zwntg"]
    print(sol.minimumGroups(w1))
    w2=["abc","cab","bac","acb","bca","cba"]
    print(sol.minimumGroups(w2))
    w3=["leet","abb","bab","deed","edde","code","bba"]
    print(sol.minimumGroups(w3))
