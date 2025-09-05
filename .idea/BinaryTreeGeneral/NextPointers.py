import collections;

# Definition for a Node.
class Node:
    def __init__(self, val = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        stack = collections.deque();
        def recur(root: Node):
            if root == None:
                return;
            rightTree = None;
            leftTree = None;
            if root.right == None and root.left == None:
                return root;
            if root.right != None:
                rightTree = recur(root.right);
                if len(stack) != 0:
                    nextTree = stack.popleft();
                    rightTree.next = nextTree;
                else:
                    rightTree.next = None;
            if root.left != None:
                leftTree = recur(root.left);
            if rightTree == None:
                leftTree.next = None;
                stack.append(leftTree);
            else:
                leftTree.next = rightTree;
                rightTree.next = None;
                stack.append(leftTree);
            return Node(root.val, leftTree, rightTree);
        return recur(root);

sol = Solution();
seven = Node(7);
three = Node(3, None, seven);
four = Node(4);
five = Node(5);
two = Node(2, four, five)
one = Node(1, two, three);
newOne = sol.connect(one);
print();
