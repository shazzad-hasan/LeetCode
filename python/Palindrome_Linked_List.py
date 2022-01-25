# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:  
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        stillEqual = True
        leftInd = 0
        rightInd = len(nums)-1
        
        while leftInd <= rightInd and stillEqual:
            if nums[leftInd] != nums[rightInd]:
                stillEqual = False
            
            leftInd += 1 
            rightInd -= 1 

        return stillEqual
