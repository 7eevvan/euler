from collections import defaultdict, deque
import sys
import heapq
import math
MOD = 67
def gcd(x,y):
    if x == 0:
        return y
    return gcd(y % x, x)
def lcm(x,y):
    return x * y / gcd(x,y)
def sieve(n): # primes up and including n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [p for p in range(2, n + 1) if is_prime[p]]

n = 100

primes = sieve(n)
dp = [0 for _ in range(n+1)]
dp[0] = 1

for p in primes:
    for x in range(p, n+1):
        dp[x] += dp[x-p]

for i in range(n+1):
    if dp[i] > 5000:
        print(i)
        break

