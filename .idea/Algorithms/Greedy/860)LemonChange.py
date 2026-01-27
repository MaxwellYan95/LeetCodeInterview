import heapq

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = 0
        tens = 0
        for payment in bills:
            if payment == 5:
                fives += 1;
            elif payment == 10:
                if fives == 0:
                    return False;
                fives -= 1;
                tens += 1;
            elif payment == 20:
                if fives == 0: # Previously was "fives == 0 or tens == 0"
                    return False;
                elif tens == 0 and fives < 3:
                    return False;
                elif tens == 0:
                    fives -= 3;
                else:
                    fives -= 1;
                    tens -= 1;
        return True;

sol = Solution()
print(sol.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))



