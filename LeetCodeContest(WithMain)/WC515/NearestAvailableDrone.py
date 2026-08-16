class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        tx,ty=target
        b=-1
        distance=float('inf')
        for i,(x,y,r) in enumerate(drones):
            if x>=tx:
                dx=x-tx
            else:
                dx=tx-x
            if y>=ty:
                dy=y-ty
            else:
                dy=ty-y
            d=dx+dy
            if d<=r:
                if d<distance or (d==distance and i<b):
                    distance=d
                    b=i
        return b
if __name__=='__main__':
    sol=Solution()
    n=int(input("Enter Number Of Drones:"))
    drones=[]
    for i in range(n):
        x,y,r=map(int,input(f"Enter Drone {i} (x,y range):").split(','))
        drones.append([x,y,r])

    tx,ty=map(int,input("Enter Target Coordinates (tx,ty):").split(','))
    target=[tx,ty]
    res=sol.nearestDrone(drones,target)
    print("Nearest Drone Index:",res)