# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA = []
        stackB = []
        while headA != None or headB != None:
            if headA != None:
                stackA.append(headA)
                headA = headA.next;
            if headB != None:
                stackB.append(headB)
                headB = headB.next;
        prev = None;
        while len(stackA) > 0 and len(stackB) > 0:
            nodeA = stackA.pop();
            nodeB = stackB.pop();
            if nodeA != nodeB:
                return prev;
            prev = nodeB;
        return prev;

sol = Solution();
lst2 = ListNode(2);
lst1 = ListNode(1);
lst1.next = lst2
oneLst = ListNode(1);
print(sol.getIntersectionNode(lst1, lst2))