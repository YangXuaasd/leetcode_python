# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head==None or k==0:
            return head
        #get length
        l = 1
        p = head
        while p.next:
            l+=1
            p = p.next
        k = k%l
        if k==0:
            return head
    
        p.next = head
        for i in range (l-k):
          p = p.next 
        
        head = p.next
        p.next = None
        return head
