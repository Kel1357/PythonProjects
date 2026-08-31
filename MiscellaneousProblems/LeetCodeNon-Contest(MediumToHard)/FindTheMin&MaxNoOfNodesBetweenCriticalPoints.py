#Definition for Singly-Linked List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        cri=[]
        prev=head
        curr=head.next
        pos=1
        while curr and curr.next:
            nxt=curr.next
            #Check Local Maxima or Local Minima
            if(curr.val>prev.val and curr.val>nxt.val) or (curr.val<prev.val and curr.val<nxt.val):
                cri.append(pos)
            prev=curr
            curr=nxt
            pos=pos+1        
        if len(cri)<2:
            return [-1,-1]
        dist=[]
        for i in range(len(cri)-1):
            diff=cri[i+1]-cri[i]
            dist.append(diff)
        mini=min(dist)        
        maxi=cri[-1]-cri[0]
        return [mini,maxi]
if __name__=='__main__':
    sol=Solution()
    arr=list(map(int,input("Enter Linked-List Values (Separated By Commas):").split(',')))
    if arr:
        head=ListNode(arr[0])
        curr=head
        for val in arr[1:]:
            curr.next=ListNode(val)
            curr=curr.next
    else:
        head=None
    res=sol.nodesBetweenCriticalPoints(head)
    print("Result:",res)
