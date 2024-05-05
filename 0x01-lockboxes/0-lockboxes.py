#!/usr/bin/python3
""" this module is for the canunlockAll question """


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    """

    if not boxes or not boxes[0]:
        return False
        
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key] and key < n:
                visited[key] = True
                stack.append(key)

    return all(visited)
