# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        oddLL = None;
        oddTraverse = oddLL;
        ptr = head;
        result = head;
        while ptr.next != None:
            odd = ptr.next.val
            if oddLL == None:
                oddLL = ListNode(odd, None)
                oddTraverse = oddLL;
            else:
                oddLL.next = ListNode(odd, None);
                oddLL = oddLL.next;
            ptr.next = ptr.next.next;
            if ptr.next == None:
                break;
            ptr = ptr.next
        ptr.next = oddTraverse;
        return result

sol = Solution()
four = ListNode(4, None)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
print(sol.oddEvenList(one))



