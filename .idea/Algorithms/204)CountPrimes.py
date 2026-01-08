class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0;
        isPrime = [True] * (n);
        isPrime[0] = isPrime[1] = False;
        for d in range(2, (n//2)+1):
            if isPrime[d] == True:
                for ind in range(d*d, n, d):
                    isPrime[ind] = False;
        return isPrime.count(True);





