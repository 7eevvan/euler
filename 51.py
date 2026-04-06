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
def generate_perms(n):
    if n == 1:
        return ["0", "1"]
    res = []
    for x in generate_perms(n-1):
        res.append("0" + x)
        res.append("1" + x)
    return res
def solve(n):
    primes = sieve(n)
    primes_set = set(primes)
    for p in primes[4:]:
        # generate permutations
        perms = generate_perms(len(str(p)))
        # for each perm
        for perm in perms[1:len(perms)-1]:
            unique = set()
            for i in range(len(str(p))):
                if perm[i] == "1":
                    unique.add(str(p)[i])
            if len(unique) > 1:
                continue
            if perm[0] == "1": # can't make the first digit 0
                res = 0
                for digit in range(1,10):
                    num = ""
                    for i in range(len(str(p))):
                        if perm[i] == "1":
                            num += str(digit)
                        else:
                            num += str(str(p)[i])
                    if int(num) in primes_set:
                        res += 1
                if res == 8:
                    return p
                    break
            else:
                res = 0
                for digit in range(10):
                    num = ""
                    for i in range(len(str(p))):
                        if perm[i] == "1":
                            num += str(digit)
                        else:
                            num += str(str(p)[i])
                    if int(num) in primes_set:
                        res += 1
                if res == 8:
                    return p
                    break

n = 1000000
print(solve(n))