# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        list = [];
        temp = head;
        while temp:
            if temp in list:
                return True;
            else:
                list.append(temp)
                temp = temp.next;
        return False;
