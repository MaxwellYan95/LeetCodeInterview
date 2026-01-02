from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None;
        lst = self.nodeToList(head);
        newLst = [];
        index = 0;
        while (index < len(lst)):
            if index == len(lst)-1:
                newLst.append(lst[index]);
                index = index+1;
            elif (lst[index] == lst[index+1]):
                while lst[index] == lst[index+1]:
                    index = index + 1;
                    if index+1 == len(lst):
                        break;
                index = index+1;
            else:
                newLst.append(lst[index]);
                index = index + 1;
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
