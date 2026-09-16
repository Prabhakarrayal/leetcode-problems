class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        r = 2 * k

        fact = 1
        for i in range(2, n + k):
            fact = fact * i % MOD

        fact_r = 1
        for i in range(2, r + 1):
            fact_r = fact_r * i % MOD

        fact_nr = 1
        for i in range(2, n + k - 1 - r + 1):
            fact_nr = fact_nr * i % MOD

        return fact * pow(fact_r * fact_nr % MOD, MOD - 2, MOD) % MOD