from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None;
        lst = self.nodeToList(head);
        newK = k % len(lst);
        newLst = lst[len(lst)-newK: len(lst)] + lst[0:len(lst)-newK];
        return self.listToNode(newLst);

    def nodeToList(self, head: Optional[ListNode]) -> list[int]:
        lst = [];
        temp = head;
        while temp != None:
            lst.append(temp.val);
            temp = temp.next;
        return lst;

    def listToNode(self, numLst: list[int]) -> Optional[ListNode]:
        lst = [];
        counter = 0;
        lst.append(ListNode(numLst[len(numLst)-1], None));
        counter = counter + 1;
        for index in range(len(numLst)-2, -1, -1):
            lst.append(ListNode(numLst[index], lst[counter-1]));
            counter = counter + 1;
        return lst[len(lst)-1];

sol = Solution();
lstHead5 = ListNode(5, None);
lstHead4 = ListNode(4, lstHead5);
lstHead3 = ListNode(3, lstHead4);
lstHead2 = ListNode(2, lstHead3);
lstHead1 = ListNode(1, lstHead2);
lst = sol.rotateRight(lstHead1, 2);
print();