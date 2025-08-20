class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sList = list(s);
        tList = list(t);
        isoDict = {};
        for index in range(len(sList)):
            sVal = sList[index];
            tVal = tList[index];
            if sVal not in isoDict.keys():
                if tVal in isoDict.values():
                    return False;
                isoDict[sVal] = tVal;
            elif isoDict[sVal] != tVal:
                return False;
        return True;

    