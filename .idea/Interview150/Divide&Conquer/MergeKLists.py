from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        newLst = [];
        for lst in lists:
            if lst != None:
                newLst.append(lst)
        return self.createList(newLst)
    def createList(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None;
        lst = None;
        current = lst;
        while len(lists) != 0:
            minIndex = 0;
            minVal = lists[minIndex].val
            for index in range(1, len(lists)):
                val = lists[index].val
                if val < minVal:
                    minIndex = index;
                    minVal = lists[index].val
            if lst == None:
                lst = ListNode(lists[minIndex].val);
                current = lst;
            else:
                current.next = ListNode(lists[minIndex].val);
                current = current.next;
            if lists[minIndex].next == None:
                lists = lists[:minIndex] + lists[minIndex+1:]
            else:
                lists[minIndex] = lists[minIndex].next;
        return lst



sol = Solution()
lst1_3 = ListNode(5);
lst1_2 = ListNode(4, lst1_3);
lst1 = ListNode(1, lst1_2);
lst2_3 = ListNode(4);
lst2_2 = ListNode(3, lst2_3)
lst2 = ListNode(1, lst2_2)
lst3_2 = ListNode(6);
lst3 = ListNode(2, lst3_2);
answer = sol.mergeKLists([lst1, lst2, lst3]);
print()
