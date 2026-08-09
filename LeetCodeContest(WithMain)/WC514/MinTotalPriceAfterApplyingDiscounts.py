class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        pri=sorted(prices,reverse=True)
        dis=sorted(discounts,reverse=True)
        t=0.0
        p1=len(pri)
        d1=len(dis)
        n=min(p1,d1)
        for i in range(n):
            p2=pri[i]
            d2=dis[i]
            t=t+(p2*(100-d2)/100.0)
        for i in range(n,p1):
            t=t+pri[i]
        return t
if __name__=='__main__':
    sol=Solution()
    prices=list(map(int,input("Enter Prices (Separated By Commas):").split(',')))
    discounts=list(map(int,input("Enter Discounts (Separated By Commas):").split(',')))
    res=sol.minPrice(prices,discounts)
    print("Minimum Total Price After Applying Discounts:",res)
