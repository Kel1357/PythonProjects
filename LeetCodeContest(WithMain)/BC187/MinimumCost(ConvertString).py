import re
class Solution(object):
    def minCost(self, source, target, rules, costs):
        """
        :type source: str
        :type target: str
        :type rules: List[List[str]]
        :type costs: List[int]
        :rtype: int
        """
        n=len(source)
        d=[None]*(n+1)
        d[0]=0
        c=[]
        r=len(rules)
        for i in range(r):
            p=rules[i][0]
            rep=rules[i][1]
            cs=costs[i]
            l=len(p)
            ct=cs+p.count('*')
            regex = re.compile(p.replace('*', '.'))
            c.append((l, regex, rep, ct))
        for j in range(1, n + 1):
            best = None
            if d[j - 1] is not None and source[j - 1] == target[j - 1]:
                best = d[j - 1]
            for L, regex, replacement, cost_total in c:
                if j >= L and d[j - L] is not None:
                    if target[j - L:j] == replacement and regex.match(source[j - L:j]):
                        cand = d[j - L] + cost_total
                        if best is None or cand < best:
                            best = cand

            d[j] = best

        return d[n] if d[n] is not None else -1
if __name__ == "__main__":
    sol = Solution()
    test=[
        ("hello","world",[["he","wo"],["llo","rld"]],[3,4],7),
        ("cat","dog",[["c*t","dog"]],[2],3),
        ("test","next",[["*e*t","next"]],[4],6),
        ("ab","bc",[["a*","bd"]],[9],-1),
    ]
    for t in test:
        source=t[0]
        target=t[1]
        rules=t[2]
        costs=t[3]
        expected=t[4]
        result = sol.minCost(source, target, rules, costs)
        if result == expected:
            status="Pass"
        else:
            status="Fail"
        print(status,"\nsource:",source,"\ntarget:",target,"\nResult:",result,"\nExpected:",expected)



