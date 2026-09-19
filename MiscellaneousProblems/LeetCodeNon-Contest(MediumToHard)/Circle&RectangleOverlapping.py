class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        x=min(max(xCenter,x1),x2)
        y=min(max(yCenter,y1),y2)
        dx=xCenter-x
        dy=yCenter-y
        r=radius*radius
        return dx*dx+dy*dy<=r
if __name__=='__main__':
    sol=Solution()
    radius,xCenter,yCenter,x1,y1,x2,y2=map(int,input().split(','))
    res=sol.checkOverlap(radius,xCenter,yCenter,x1,y1,x2,y2)
    if res:
        print("true")
    else:
        print("false")
    
