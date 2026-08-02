class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        n=len(nums)
        c=0
        for i in range(n):
            x=0
            y=0
            for j in range(i,n):
                if nums[j]%2==0:
                    x=x+1
                else:
                    y=y+1
                l=x*b
                r=a*y
                if y>0 and l<=r:
                    c=c+1
        return c
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
            