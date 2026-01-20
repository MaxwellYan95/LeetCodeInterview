class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minA = costs[0][0]
        minA_index = 0;
        minB = costs[0][1]
        minB_index = 0;
        for index in range(len(cost)):
            a = costs[index][0]
            b = costs[index][1]
            if a < minA:
                minA = a;
                minA_index = index;
            if b < minB:
                minB = b;
                minB_index = index;
        smallA = minA;
        smallA_count = 0; # b flights
        smallB = minB;
        smallB_count = 0; # a flights
        for flight in costs[:minA_index]+costs[minA_index+1:]:
            a = flight[0]
            b = flight[1]
            if b < a:
                smallA_count += 1;
            smallA += min(a, b);
        for flight in costs[:minB_index]+costs[minB_index+1:]:
            a = flight[0]
            b = flight[1]
            if a < b:
                smallB_count += 1;
            smallB += min(a, b);
        if smallA_count == 0:
            return smallB;
        if smallB_count == 0:
            return smallA;
        return min(smallA, smallB);