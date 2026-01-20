class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        result = [];
        for i1 in range(len(transactions)):
            t1 = transactions[t1]
            for t2 in transactions[:i1]+transactions[i1+1:]:
                if self.greaterThan1000(t1):
                    result.append(t1)
                    break;
                elif self.lessThanHour(t1, t2):
                    result.append(t1)
                    break;
        return result;

    def greaterThan1000(self, transaction: str):
        format = self.transactionFormat(transaction);
        if format[2] > 1000:
            return True;
        return False;

    def lessThanHour(self, one: str, two: str):
        format1 = self.transactionFormat(one);
        format2 = self.transactionFormat(two);
        if abs(format1[1]-format2[1]) <= 60 and format1[0] == format2[0] and format1[3] != format2[3]:
            return True;
        return False;

    def transactionFormat(self, transaction: str):
        lst = transaction.split(",")
        lst[1] = int(lst[1])
        lst[2] = int(lst[2])
        return lst;

sol = Solution();
transact = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"];
print(sol.invalidTransactions(transact))
