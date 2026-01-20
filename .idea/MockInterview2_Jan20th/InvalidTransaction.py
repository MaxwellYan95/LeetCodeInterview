class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        if len(transactions) == 1:
            if self.greaterThan1000(transactions[0]):
                return [transactions[0]]
            return [];
        recur = self.invalidTransactions(transactions[:len(transactions)-1])
        last = transactions[len(transactions)-1]
        if self.greaterThan1000(last):
            recur.append(last)
        else:
            for prev in transactions[:len(transactions)-1]:
                if self.lessThanHour(prev, last):
                    if prev not in recur:
                        recur.append(prev);
                    recur.append(last);
                    break;
        return recur;

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
