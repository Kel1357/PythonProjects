class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        """
        :type n: int
        :type grid: List[List[int]]
        :type rowShift: List[int]
        :type colShift: List[int]
        :rtype: List[List[int]]
        """
        sh=[]                    
        for i in range(n):              
            row=[0]*n             
            sh.append(row)
        for i in range(n):
             k=rowShift[i]%n
             for j in range(n):
                    sh[i][j]=grid[i][(j+k)%n]
        bst=[]
        for i in range(n):
            col=[0]*n
            bst.append(col)
        for j in range(n):
            k=colShift[j]%n
            for i in range(n):
                bst[i][j]=sh[(i+k)%n][j]
        return bst
if __name__=='__main__':
    sol=Solution()
    n=int(input("Enter the Size Of Grid:"))
    grid=[]
    for i in range(n):
        row=list(map(int,input(f"Enter Row {i+1} (Separated By Commas):").split(',')))
        grid.append(row)
    rowShift=list(map(int,input("Cyclically Left Shift(Separated By Commas):").split(',')))
    colShift=list(map(int,input("Cyclically Upward Shift (Separated By Commas):").split(',')))
    res=sol.cyclicShift(n,grid,rowShift,colShift)
    print("Cyclically Shift Rows & Columns:",res)
