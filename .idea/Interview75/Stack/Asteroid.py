class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [];
        for rock in asteroids:
            added = True;
            while rock < 0 and stack:
                ind = len(stack)-1
                last = stack[ind]
                if last < 0:
                    break;
                if -1*rock >= last:
                    stack.pop(ind)
                if -1*rock <= last:
                    added = False;
                    break;
            if added:
                stack.append(rock);
        return stack

sol = Solution()
print(sol.asteroidCollision([8, -8]))