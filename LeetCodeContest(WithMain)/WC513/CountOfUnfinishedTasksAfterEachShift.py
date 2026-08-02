class Solution(object):
    def countTasks(self, tasks, shifts):
        """
        :type tasks: List[int]
        :type shifts: List[int]
        :rtype: List[int]
        """
        n = len(tasks)
        P = [0] * (n + 1)
        for k in range(n):
            P[k + 1] = P[k] + tasks[k]
        i = 0
        re = 0
        ans = []
        for t in shifts:
            if re > 0:
                if t >= re:
                    t = t - re
                    re = 0
                    i = i + 1
                else:
                    re = re - t
                    t = 0
            if t > 0 and i < n:
                target = P[i] + t
                lo, hi = i, n
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    if P[mid] <= target:
                        lo = mid
                    else:
                        hi = mid - 1
                k = lo
                t = t - (P[k] - P[i])
                i = k
                if t > 0 and i < n:
                    re = tasks[i] - t
                    t = 0
            if i == n:
                ans.append(0)
                i = 0
                re = 0
            else:
                ans.append(n - i)
        return ans
if __name__=='__main__':
    sol=Solution()
    raw1=input("Enter Tasks Separated By Commas:")
    tasks=[]
    for x in raw1.split(','):
        tasks.append(int(x))
    raw2=input("Enter Shifts Separated By Commas:")
    shifts=[]
    for x in raw2.split(','):
        shifts.append(int(x))
    res=sol.countTasks(tasks,shifts)
    print(f"Unfinished Tasks After Each Shift: {res}")
    