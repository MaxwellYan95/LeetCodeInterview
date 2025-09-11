from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        tempLists = lists;
        minIndex = -1;
        minVal = float('inf');
        for index in range(len(tempLists)):
            if tempLists[index] == None:
                continue;
            value = tempLists[index].val;
            if minVal > value:
                minVal = value;
                minIndex = index;
        if minIndex == -1:
            return None;
        tempLists[minIndex] = tempLists[minIndex].next;
        nextList = self.mergeKLists(tempLists);
        return ListNode(minVal, nextList);

sol = Solution();
lst1 = ListNode(1, ListNode(3, None));
lst2 = ListNode(2);
result = sol.mergeKLists([lst1, lst2]);
print();