# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current node to dummy head of the returning list.
        dummy = ListNode()
        cur = dummy
        # Initialize carry
        carry = 0
        # Initialize p and q to head of l1 and l2
        p = l1
        q = l2
        
        # Loop through lists l1 and l2 until you reach both ends
        while p or q:
            # Set x to node p's value. If p has reached the end of l1, set to 0
            x = p.val if p else 0
            # Set y to node q's value. If q has reached the end of l2, set to 0
            y = q.val if q else 0
            
            # calculate sum
            summa = x + y + carry
            # update carry 
            carry = summa // 10
            
            # Create a new node with the digit value of (sum mod 10) and set it to current node's next, 
            # then advance current node to next.
            val = summa % 10
            cur.next = ListNode(val)
            cur = cur.next
            
            # advance both p and q
            p = p.next if p else None
            q = q.next if q else None
            
        # check if carry = 1, if so append a new node with digit 1 to the returning list.
        if carry > 0:
            cur.next = ListNode(carry)
        
        # Return dummy head's next node.
        return dummy.next