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
        if not root:
            return None;

        stack = collections.deque([root]);
        while stack:
            size = len(stack);
            for i in range(size):
                cur = stack.popleft();
                if i < size-1:
                    cur.next = stack[0]
                if cur.left != None:
                    stack.append(cur.left);
                if cur.right != None:
                    stack.append(cur.right);
        return root;




sol = Solution();
five = Node(5);
four = Node(4);
three = Node(3, None, five);
two = Node(2, four, None)
one = Node(1, two, three);
newOne = sol.connect(one);
print();
