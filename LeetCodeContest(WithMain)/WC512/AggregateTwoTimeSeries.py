class Solution(object):
    def aggregateTimeSeries(self, series1, series2):
        """
        :type series1: List[List[int]]
        :type series2: List[List[int]]
        :rtype: List[List[int]]
        """
        ts1 = [t for t, v in series1]
        val1 = [v for t, v in series1]
        ts2 = [t for t, v in series2]
        val2 = [v for t, v in series2]
        merged = sorted(set(ts1) | set(ts2), reverse=True)
        m, n = len(ts1), len(ts2)
        result = []

        for t in merged:
            while m > 0 and ts1[m - 1] >= t:
                m =m- 1
            u =(
                val1[m]
                if m < len(ts1)
                else 0
            )
            while n > 0 and ts2[n - 1] >= t:
                n =n- 1
            v =(
                val2[n]
                if n < len(ts2)
                else 0
            )
            result.append([t, u + v])

        result.reverse()
        return result
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        {
            "series1": [[1, 3], [4, 1]],
            "series2": [[2, 2], [5, 2]],
            "expected": [[1, 5], [2, 3], [4, 3], [5, 2]],
        },
        {
            "series1": [[1, 5], [3, 1]],
            "series2": [[2, 2]],
            "expected": [[1, 7], [2, 3], [3, 1]],
        },
        {
            "series1": [[1, 5]],
            "series2": [[1000000000, 2]],
            "expected": [[1, 7], [1000000000, 2]],
        },
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.aggregateTimeSeries(case["series1"], case["series2"])
        status = "PASS" if result == case["expected"] else "FAIL"
        print(f"Example {i}: {status}")
        print(f"  series1:  {case['series1']}")
        print(f"  series2:  {case['series2']}")
        print(f"  expected: {case['expected']}")
        print(f"  got:      {result}")
        print()
