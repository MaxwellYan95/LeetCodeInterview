class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0;
        primes = [2]
        for i in range(3, n):
            isPrime = True
            for p in primes:
                if i % p == 0:
                    isPrime = False;
                    break;
            if isPrime:
                primes.append(i);
        return len(primes)




