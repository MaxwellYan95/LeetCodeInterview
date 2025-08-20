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
        minVal = 0;
        returnList = None;
        traverse = None;
        empty = True;
        sortedLst = [];
        while True:
            for ind in range(len(tempLists)):
                if tempLists[ind] != None:
                    empty = False;
                    if tempLists[ind].val <= minVal or minIndex == -1:
                        minIndex = ind;
                        minVal = tempLists[ind].val;
            if empty == True:
                break;
            else:
                sortedLst.append(minVal);
            tempLists[minIndex] = tempLists[minIndex].next;
            minIndex = -1;
            empty = True;
        if len(sortedLst) == 0:
            return None;
        return self.listToNode(sortedLst);

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
lst1 = ListNode(1, ListNode(3, None));
lst2 = ListNode(2);
result = sol.mergeKLists([lst1, lst2]);
print();