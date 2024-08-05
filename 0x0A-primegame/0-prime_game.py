#!/usr/bin/python3
''' module 0 '''


def isWinner(x, nums):
    ''' function to check if winner '''
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
        primes = [p for p in range(n + 1) if is_prime[p]]
        return primes

    # Generate all primes up to the maximum possible value in nums
    max_n = max(nums)
    primes = sieve(max_n)

    def play_game(n):
        ''' game function '''
        available = [True] * (n + 1)
        move_count = 0
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                move_count += 1
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
        return move_count % 2 == 1

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
