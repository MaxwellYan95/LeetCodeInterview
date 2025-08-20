from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        lists = []
        list1Next = list1
        list2Next = list2
        while True:
            if list1Next == None and list2Next == None:
                break
            elif list1Next == None:
                nums.append(list2Next.val)
                list2Next = list2Next.next
            elif list2Next == None:
                nums.append(list1Next.val)
                list1Next = list1Next.next
            else:
                if list1Next.val < list2Next.val:
                    nums.append(list1Next.val)
                    list1Next = list1Next.next
                else:
                    nums.append(list2Next.val)
                    list2Next = list2Next.next

        for n in reversed(nums):
            if len(lists) == 0:
                obj = ListNode(n, None)
                lists.append(obj)
            else:
                obj = ListNode(n, lists[len(lists)-1])
                lists.append(obj)

        return lists[len(lists)-1]

firstList1 = ListNode(4, None)
firstList2 = ListNode(2, firstList1)
firstList3 = ListNode(1, firstList2)
secondList1 = ListNode(4, None)
secondList2 = ListNode(3, secondList1)
secondList3 = ListNode(1, secondList2)
sol = Solution()
sol.mergeTwoLists(firstList3, secondList3)