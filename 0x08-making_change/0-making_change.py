#!/usr/bin/python3
''' Module 0 '''

from collections import deque
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    ''' Function to get the change using BFS '''
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        current_amount, num_coins = queue.popleft()

        # Explore all possible next steps
        for coin in coins:
            new_amount = current_amount + coin
            if new_amount == total:
                return num_coins + 1
            if new_amount < total and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    return -1
