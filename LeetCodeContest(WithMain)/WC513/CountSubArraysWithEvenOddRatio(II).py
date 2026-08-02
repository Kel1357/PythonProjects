class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        n = len(nums)
        ex = [0] * (n + 1) 
        od = [0] * (n + 1) 
        for i in range(1, n + 1):
            if nums[i - 1] % 2 == 0:
                ex[i] = ex[i - 1] + 1
                od[i] = od[i - 1]
            else:
                ex[i] = ex[i - 1]
                od[i] = od[i - 1] + 1
        f = [ex[i] * b - od[i] * a for i in range(n + 1)]
        vals = sorted(set(f))
        rank={}
        i=0
        for v in vals:
            rank[v]=i+1
            i=i+1
        m = len(vals)
        bit = [0] * (m + 1)
        def add(i):
            while i <= m:
                bit[i] += 1
                i += i & (-i)
        def sum_up(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
        def lower_bound(arr, x, lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        ans = 0
        p = 0
        for r in range(1, n + 1):
            k = lower_bound(od, od[r], 0, r)
            while p < k:
                add(rank[f[p]])
                p += 1
            t = f[r]
            lo = lower_bound(vals, t, 0, m) 
            lt = sum_up(lo)
            ans += p - lt  
        return ans
if __name__=='__main__':
    sol=Solution()
    raw=input("Enter Numbers Separated By Commas:")
    nums=[]
    for x in raw.split(','):
        nums.append(int(x))
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    res=sol.countRatioSubarrays(nums, a, b)
    print(f"Number Of Valid SubArrays: {res}")
    

