# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headB == None or headA == None:
            return None;
        if headB.val == headA.val:
            return headA.val;
        else:
            aNode = self.getIntersectionNode(headA.next, headB);
            bNode = self.getIntersectionNode(headA, headB.next);
            if aNode == None and bNode == None:
                return None;
            elif aNode == None:
                return bNode;
            elif bNode == None:
                return aNode
            return aNode;

sol = Solution();
lst2 = ListNode(2);
lst1 = ListNode(1);
lst1.next = lst2
oneLst = ListNode(1);
print(sol.getIntersectionNode(lst1, lst2))