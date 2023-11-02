
from math import sqrt

def isPrime(n:float) -> bool:
    """Returns `True` if `n` is prime, `False` otherwise"""
    assert n > 0, "n must be positive"
    if n == 1: return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primes(n:int) -> list[int]:
    """Returns a list of primes up to `n`"""
    assert n > 0, "n must be positive"
    primes = {2}
    for i in range(3,n+1,2):
        if any(i % p == 0 for p in primes): continue
        primes.add(i)
    return primes

def factorize(n:int) -> list[int]:
    """Returns a list of prime factors of `n`"""
    assert n > 0, "n must be positive"
    factors = []
    for p in primes(int(sqrt(n))+1):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1: factors.append(n)
    return factors
