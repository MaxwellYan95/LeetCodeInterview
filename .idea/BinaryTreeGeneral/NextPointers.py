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
        def addNext(cur: Node):
            if len(stack) == 0:
                cur.next = None;
            else:
                nextTree = stack.popleft();
                cur.next = nextTree;
                stack.append(cur);
        def recur(root: Node):
            if root == None:
                return;
            if root.right == None and root.left == None:
                stack.append(root);
                return root;
            rightTree = None;
            leftTree = None;
            if root.right != None:
                rightTree = recur(root.right);
                addNext(rightTree);
                stack.append(rightTree);
            if root.left != None:
                leftTree = recur(root.left);
                addNext(leftTree);
                stack.append(leftTree);
            addNext(root);
            return root;
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
