
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None;
        lst = self.listToArray(head)
        midInd = (len(lst)) // 2;
        tree = TreeNode(lst[midInd]);
        for ind in range(midInd-1, -1, -1):
            self.insertIntoBST(tree, lst[ind]);
        for num in lst[midInd+1:]:
            self.insertIntoBST(tree, num);
        return tree;

    def listToArray(self, head: ListNode) -> list[int]:
        lst = [head.val]
        current = head;
        current = current.next;
        while current != None:
            lst.append(current.val);
            current = current.next;
        return lst

    def insertIntoBST(self, tree: TreeNode, value: int):
        front = tree;
        if (value < front.val):
            if (front.left == None):
                front.left = TreeNode(value)
            else:
                self.insertIntoBST(front.left, value)
        else:
            if (front.right == None):
                front.right = TreeNode(value)
            else:
                self.insertIntoBST(front.right, value)

sol = Solution();
last = ListNode(3)
middle = ListNode(2, last)
front = ListNode(1, middle)
tree = sol.sortedListToBST(front)
print();