
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node):
        if not node:
            return None;

        oldNodes = {}

        def dfs(node: Node):
            if (len(oldNodes) != 0):
                if (node in oldNodes):
                    return oldNodes[node];
            oldNodes[node] = Node(node.val);
            for n in node.neighbors:
                copy = oldNodes[node];
                newN = dfs(n);
                copy.neighbors.append(newN);
            return oldNodes[node];
        return dfs(node);

nodeList = [Node(0), Node(1), Node(2), Node(3)];
nodeList[0].neighbors.append(nodeList[1]);
nodeList[0].neighbors.append(nodeList[3]);

nodeList[1].neighbors.append(nodeList[0]);
nodeList[1].neighbors.append(nodeList[2]);

nodeList[2].neighbors.append(nodeList[1]);
nodeList[2].neighbors.append(nodeList[3]);

nodeList[3].neighbors.append(nodeList[0]);
nodeList[3].neighbors.append(nodeList[2]);

sol = Solution();
copyNode = sol.cloneGraph(nodeList[0]);
print();