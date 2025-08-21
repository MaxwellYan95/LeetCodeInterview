import collections


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        q = collections.deque([startGene]);
        bankSet = set(bank);
        if endGene not in bankSet:
            return -1
        letters = 'ACGT';
        step = 1;
        while q:
            # included this loop to account for multiple possibilities
            for _ in range(len(q)):
                newList = list(q.popleft());
                for index, c in enumerate(newList):
                    for l in letters:
                        newList[index] = l;
                        newGene = "".join(newList);
                        if newGene == endGene:
                            return step;
                        if newGene in bankSet:
                            bankSet.remove(newGene);
                            q.append(newGene);
                    newList[index] = c;
            step += 1;
        return -1;

sol = Solution();
print(sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))




