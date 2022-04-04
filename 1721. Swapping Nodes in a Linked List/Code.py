class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        n=len(l)
        # print(l)
        l[k-1],l[n-k]=l[n-k],l[k-1]
        head2=ListNode(0)
        temp2=head2
        for i in range(n):
            temp2.next=ListNode(l[i])
            temp2=temp2.next
        return head2.next
       