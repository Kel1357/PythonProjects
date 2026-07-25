# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def countDominantNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        v=[]
        q=[root]
        while q:
            node=q.pop(0)
            v.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        n = len(v)
        s = [0] * (2 * n + 2)
        c = 0
        for i in range(n-1,-1,-1):
            l=2*i+1
            r=2*i+2
            m=max(v[i],s[l],s[r])
            s[i]=m
            if v[i]==m:
                c=c+1
        return c
def buildTree(values):
    if not values:
        return None
    nodes=[TreeNode(v) for v in values]
    n=len(nodes)
    for i in range(n):
        l=2*i+1
        r=2*i+2
        if l<n:
            nodes[i].left=nodes[l]
        if r<n:
            nodes[i].right=nodes[r]
    return nodes[0]
if __name__=="__main__":
    sol=Solution()
    root1=buildTree([5,3,8,2,4,7,1])
    print(sol.countDominantNodes(root1))
    root2=buildTree([1,2,3,1,2])
    print(sol.countDominantNodes(root2))
