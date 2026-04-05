class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        minLst = []; # min[n] stands for (n-1)th smallest
        update = False; # Is a min updated?
        for n in nums: # using if, elif, and else
            for index in range(len(minLst)):
                minimum = minLst[index]
                if minimum >= n:
                    minLst[index] = n
                    update = True;
                    break;
            if not update:
                minLst.append(n)
            if len(minLst) == 3:
                return True;
            update = False;
        return False;