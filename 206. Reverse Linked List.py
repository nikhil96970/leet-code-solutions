class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        lst=lst[::-1]
        ans=ListNode(0)
        tmp=ans
        for i in lst:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return ans.next
