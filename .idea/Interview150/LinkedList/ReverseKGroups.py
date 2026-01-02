from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = self.nodeToList(head);
        newLst = [];
        for index in range(0, len(lst)-(len(lst)%k), k):
            newLst.extend(reversed(lst[index:index+k]));
        newLst.extend(lst[len(lst)-(len(lst)%k): len(lst)]);
        return self.listToNode(newLst);

    def nodeToList(self, head: Optional[ListNode]) -> list[int]:
        lst = [];
        temp = head;
        while temp != None:
            lst.append(temp.val);
            temp = temp.next;
        return lst;

    def listToNode(self, numLst: list[int]) -> Optional[ListNode]:
        if len(numLst) == 0:
            return None;
        lst = [];
        counter = 0;
        lst.append(ListNode(numLst[len(numLst)-1], None));
        counter = counter + 1;
        for index in range(len(numLst)-2, -1, -1):
            lst.append(ListNode(numLst[index], lst[counter-1]));
            counter = counter + 1;
        return lst[len(lst)-1];

sol = Solution();
five = ListNode(5, None);
four = ListNode(4, five);
three = ListNode(3, four);
two = ListNode(2, three);
one = ListNode(1, two);

newList = sol.reverseKGroup(one, 2);
print();