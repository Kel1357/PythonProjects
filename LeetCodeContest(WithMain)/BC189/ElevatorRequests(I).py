class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        c=0
        t=0
        for r in requests:
            if r>=c:
                t=t+(r-c)
            else:
                t=t+(c-r)
            c=r
        return t
if __name__=='__main__':
    sol=Solution()
    n=int(input("Enter Number of Floors:"))
    requests=list(map(int, input("Enter the Requests (Floors Separated By Commas):").split(',')))
    res=sol.elevatorRequests(n,requests)
    print("Total Time Required:",res,"seconds")