class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = [False for i in range(len(isConnected[0]))];
        def dfs(num: int):
            self.visited[num] = True;
            stack = [];
            row = isConnected[num];
            for index in range(len(row)):
                cond = self.visited[index] == False and row[index] == 1 and index != num;
                if cond:
                    dfs(index);
        provinces = 0;
        for index in range(len(isConnected[0])):
            if self.visited[index] == False:
                dfs(index);
                provinces += 1;
        return provinces;