# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int):
        h1 = l1 = ListNode(0); # l1 tracks values less than x
        h2 = l2 = ListNode(0); # l2 tracks values greater than or equal to x
        temp = head;
        while temp:
            if temp.val < x:
                l1.next = temp;
                l1 = l1.next;
            else:
                l2.next = temp;
                l2 = l2.next;
            temp = temp.next;
        # Link h2 and h1 together
        l2.next = None;
        l1.next = h2.next;
        return h1.next;

sol = Solution();
node1 = ListNode(1, None);
node2 = ListNode(4, node1);
node3 = ListNode(2, node2);
node4 = ListNode(5, node3);
node5 = ListNode(3, node4);
partNode = sol.partition(node5, 2);
print("Done");