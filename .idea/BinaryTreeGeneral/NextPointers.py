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
                return None;
            rightTree = None;
            leftTree = None;
            if root.right == None and root.left == None:
                return root;
            elif root.right == None:
                leftTree = recur(root.left);
                stack.append(leftTree);
            elif root.left == None:
                rightTree = recur(root.right);
                stack.append(rightTree);
            else:
                rightTree = recur(root.right);
                leftTree = recur(root.left);
                leftTree.next = rightTree;
                useStack(rightTree);
            return Node(root.val, leftTree, rightTree);

        def useStack(cur: Node):
            if len(stack) != 0:
                nextTree = stack.popleft();
                cur.next = nextTree;
            else:
                cur.next = None;
        newRoot = recur(root);
        if newRoot != None:
            newRoot.next = None;
        return newRoot;

sol = Solution();
seven = Node(7);
three = Node(3, None, seven);
four = Node(4);
five = Node(5);
two = Node(2, four, five)
one = Node(1, two, three);
newOne = sol.connect(one);
print();
