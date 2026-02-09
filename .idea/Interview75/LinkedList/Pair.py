# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        headLst = self.convertList(head)
        n = len(headLst)-1;
        maximum = 0;
        for i in range(len(headLst)//2):
            maximum = max(maximum, headLst[i]+headLst[n-i])
        return maximum

    def convertList(self, head: ListNode) -> list[int]:
        lst = [];
        while head != None:
            lst.append(head.val)
            head = head.next;
        return lst