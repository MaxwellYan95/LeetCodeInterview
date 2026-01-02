from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = [];
        temp = head;
        leftCounter = False;
        counter = 1;
        if left == right:
            return head;
        while True:
            if temp.next == None:
                lst.append(temp);
                break;
            if counter == left:
                leftCounter = True;
            if counter == right and leftCounter == True:
                lst.append(temp);
                break;
            if leftCounter == True:
                lst.append(temp);
            temp = temp.next;
            counter = counter + 1;
        if leftCounter == False:
            return head;
        for index in range(0, int(len(lst)/2)):
            lowerIndexVal = lst[index].val;
            highIndexVal = lst[len(lst)-index-1].val;
            lst[index].val = highIndexVal;
            lst[len(lst)-index-1].val = lowerIndexVal;
        return head;
