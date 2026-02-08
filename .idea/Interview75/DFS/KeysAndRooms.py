class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.visited = [False for i in range(len(rooms))]
        def dfs(node: int):
            if self.visited[node]:
                return;
            self.visited[node] = True;
            for neighbor in rooms[node]:
                dfs(neighbor);
            return;
        # Only 0 is unlocked, initially
        dfs(0);
        if False not in self.visited:
            return True
        return False

sol = Solution()
print(sol.canVisitAllRooms([[2,3],[],[2],[1,3]]))
